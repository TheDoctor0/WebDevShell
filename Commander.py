import os
import shlex
import subprocess
import sublime
import sublime_plugin
import webbrowser

class CommanderCommand(sublime_plugin.WindowCommand):
    def __init__(self, *args, **kwargs):
        super(CommanderCommand, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        self.settings = sublime.load_settings('Commander.sublime-settings')

        if self.settings.get('override_panel_settings', True) is True:
            self.preferences = sublime.load_settings('Preferences.sublime-settings')
            self.panel = self.preferences.get('show_panel_on_build', True)

            if self.panel is False:
                self.preferences.set('show_panel_on_build', True)

        try:
            self.path = kwargs.get('path', self.window.folders()[0])

            if 'changeable' not in self.path and self.path_exists(self.path) is False:
                return
        except IndexError:
            sublime.error_message('Please open a project.')
            return

        self.args = []
        command_type = kwargs.get('type', None)

        if command_type is not None:
            if command_type == 'url':
                url = kwargs.get('href', False)

                if url is not False:
                    if kwargs.get('additional', False) is True:
                        view = self.window.active_view()
                        selection = view.substr(view.sel()[0])
                        webbrowser.open_new_tab(url + (selection if selection else sublime.get_clipboard()))
                    else:
                        webbrowser.open_new_tab(url)
                else:
                    sublime.error_message('URL href is not specified.')

                return
            else:
                command_paths = shlex.split(command_type)

                for path in command_paths:
                    command_path = self.settings.get(path + '_path', None)

                    if self.path_exists(command_path, path):
                        self.args.append(command_path)
                    else:
                        return

        self.command = kwargs.get('command', None)
        self.additional = kwargs.get('additional', False)
        self.additional_label = kwargs.get('additional_label', 'Enter additional parameters (optional)')

        if 'changeable' in self.path:
            self.window.show_input_panel('Enter path for command:', '', self.on_path, None, None)
        else:
            self.on_path()

    def on_path(self, command = None):
        if command is not None:
            self.path = command

            if self.path_exists(self.path) is False:
                return

        if self.command is None:
            self.window.show_input_panel('Enter your command:', '', self.on_command, None, None)
        else:
            self.on_command(self.command)

    def on_command(self, command):
        self.args.extend(shlex.split(str(command if self.command is None else self.command)))

        if self.additional is True:
            self.window.show_input_panel(self.additional_label + ':', '', self.on_command_params, None, None)
        else:
            self.on_done()

    def on_command_params(self, params):
        self.args.extend(shlex.split(str(params)))
        self.on_done()

    def on_done(self):
        if os.name != 'posix':
            self.args = subprocess.list2cmdline(self.args)

        try:
            self.window.run_command('exec', {
                'cmd': self.args,
                'shell': os.name == 'nt',
                'working_dir': self.path,
                'syntax': 'Packages/Commander/Commander.sublime-syntax' if self.settings.get('colored_output', True) is True else ''
            })
        except IOError:
            sublime.error_message('IOError - command aborted.')

        sublime.status_message(self.args)

        if self.settings.get('override_panel_settings', True) is True:
            self.preferences.set('show_panel_on_build', self.panel)

    def path_exists(self, path, command = None):
        if path is None:
            sublime.error_message('Please specify ' + command + '_path in Commander Settings.')
            return False
        elif os.sep in path and os.path.exists(path) is False:
            sublime.error_message(('Command' if command is not None else 'Setting') + ' path "' + path + '" does not exists.')
            return False
        else:
            return True

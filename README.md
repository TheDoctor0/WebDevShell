# WebDevShell [![StyleCI](https://github.styleci.io/repos/127345708/shield?branch=master&style=flat)](https://github.styleci.io/repos/127345708) [![Downloads](https://img.shields.io/packagecontrol/dt/WebDevShell.svg?color=sucess)](https://img.shields.io/packagecontrol/dt/WebDevShell.svg?color=sucess&style=plastic) [![License](https://img.shields.io/github/license/TheDoctor0/WebDevShell.svg?color=sucess)](https://img.shields.io/github/license/TheDoctor0/WebDevShell.svg?color=sucess&style=plastic)

WebDevShell is a Sublime Text 3 plugin for executing shell commands related to web apps development.

I created it because constant switching between Sublime and terminal while working on my project was just frustrating.

Commands available out of the box are mostly related Laravel based project development, but custom commands can be easily added.

### Available commands:
- `Laravel Artisan` (all commands, documentation link)
- `Composer` (all commands, documentation link)
- `NPM` (all commands, dev/prod/watch, documentation link)
- `Yarn` (all commands, dev/prod/watch, documentation link)
- `PHP` (general command, version, documentation link)
- `StackOverflow Search` (text in search input or if empty from selected text)
- `Google Search` (text in search input or if empty from selected text)
- `Check Internet Connection` (ping 1.1.1.1)

Feel free to open pull request with additional commands.

### Custom commands
To add custom commands use `Preferences/Package Settings/WebDevShell/Commands – User` menu item.

#### Custom command structure:

```json
{
    "caption": "WebDevShell: Custom Artisan Command (with path and parameters)",
    "command": "webdevshell",
    "args": {
        "type": "php artisan",
        "path": "changeable",
        "command": "test",
        "additional": true,
        "additional_label": "Enter additional parameters"
    }
}
```

All `args` are optional and you can remove them.

- `command` a command that will be executed in shell.
If you don't define any command in `args` there will be an input to insert it every time when you use this custom command.

- `type` specify command prefixes - you can add one or more. In this example executed command will be `php artisan test`.
All of prefixes have to be defined in `Preferences/Package Settings/WebDevShell/Settings – User` as `prefixname_path` settings.
For example `"php_path": "php"`. You can define `path` as global command or full path to binary file.

- `additional` will trigger input for some parameters for you command, text from additional input will be command suffix.
To set message for this input set `additional_label`.

- `path` is a location where your command will be executed.
You can add any path here or set it to `changeable` so there will be option to insert path every time you execute that command.
If no path is defined, command will be executed in project root directory.

#### Custom url command structure:

```json
{
    "caption": "WebDevShell: Google Search",
    "command": "webdevshell",
    "args": {
        "type": "url",
        "href": "https://google.com/search?q=",
        "additional": true,
    }
}
```

If you want to define url command you have to set `"type": "url"` and specify link in `href`.

Argument `additional` is optional and you can remove it, it enables adding selected text or if empty from clipboard to the end of url.

### Installation:
Use Package Controller or create a the directory `WebDevShell` in your Sublime Text Packages directory with source code from this repository.

### Usage:
Press `Cmd + Shift + P` for the dropdown command list, search for `WebDevShell ` and pick your command. You can alternatively use `Tools/WebDevShell...` menu item.

### Notes:
You may need insert in Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.

By default `"override_panel_settings" : true` in WebDevShell settings enables a mechanism forcing to show panel, but I don't guarantee it works on all versions.

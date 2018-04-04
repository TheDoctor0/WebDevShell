Commander
===============

Commander is a plugin for executing shell commands in Sublime Text.

I created it because constant window changing while working on my project was just frustrating.

As you can see by default most commands are for Laravel project development, but you can add custom commands.

### Available commands:
- `Laravel Artisan` (all commands + documentation link)
- `Composer` (all commands + documentation link)
- `NPM` (run dev/production/watch + documentation link)
- `StackOverflow Search` (text in search input or if empty from selected text)
- `Google Search` (text in search input or if empty from selected text)
- `Check Internet Connection` (ping 1.1.1.1)

More will be added in the future. I am open to suggestions.

### Custom Commands
To add custom commands use `Preferences/Package Settings/Commander/Commands – User` menu item.

#### Custom command structure:

```json
    {
        "caption": "Commander: Custom Artisan Command (with path and parameters)",
        "command": "commander",
        "args": {
            "type": "php artisan",
            "path": "changeable",
            "command": "test",
            "additional": true,
            "additional_label": "Enter additional parameters"
        }
    },
```

All `args` are optional and you can remove them.

- `command` a command that will be executed in shell.
If you don't define any command in `args` there will be an input to insert it every time when you use this custom command.

- `type` specify command prefixes - you can add one or more. In this example executed command will be `php artisan test`.
All of prefixes have to be defined in `Preferences/Package Settings/Commander/Settings – User` as `prefixname_path` settings.
For example `"php_path": "php"`. You can define `path` as global command or full path to binary file.

- `additional` will trigger input for some parameters for you command, text from additional input will be command suffix.
To set message for this input set `additional_label`.

- `path` is a location where your command will be executed.
You can add any path here or set it to `changeable` so there will be option to insert path every time you execute that command.
If no path is defined, command will be executed in project root directory.

#### Custom url command structure:

```json
    {
        "caption": "Commander: Google Search",
        "command": "commander",
        "args": {
            "type": "url",
            "href": "https://google.com/search?q=",
            "additional": true,
        }
    },
```

If you want to define url command you have to set `"type": "url"` and specify link in `href`.

Argument `additional` is optional and you can remove it, it enables adding selected text or if empty from clipboard to the end of url.

### Installation:
Use Package Controller or create a the directory `Commander` in your Sublime Text Packages directory with source code from this repository.

### Usage:
Press `Cmd + Shift + P` for the dropdown command list, search for `Commander ` and pick your command. You can alternatively use `Tools/Commander...` menu item.

### Notes:
You may need insert in Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.

By default `"override_panel_settings" : true` in Commander settings enables a mechanism forcing to show panel, but I don't guarantee it works on all versions.

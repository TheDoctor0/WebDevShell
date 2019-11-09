# WebDevShell [![StyleCI](https://github.styleci.io/repos/127345708/shield?branch=master&style=flat)](https://github.styleci.io/repos/127345708) [![Downloads](https://img.shields.io/packagecontrol/dt/WebDevShell.svg?color=sucess)](https://img.shields.io/packagecontrol/dt/WebDevShell.svg?color=sucess&style=plastic) [![License](https://img.shields.io/github/license/TheDoctor0/WebDevShell.svg?color=sucess)](https://img.shields.io/github/license/TheDoctor0/WebDevShell.svg?color=sucess&style=plastic)

Sublime Text 3 plugin for executing shell commands related to web apps development: Laravel Artisan, Composer, NPM, Yarn, Python, PHP, PHPStan, Psalm, ESLint and more!

I created it because constant switching between Sublime and terminal while working on my project was just frustrating.

Commands available out of the box are mostly related Laravel based project development, but custom commands can be easily added.

### Available commands:
- `Laravel Artisan` (all commands, documentation link)
- `Composer` (all commands, documentation link)
- `NPM` (all commands, dev/prod/watch, documentation link)
- `Yarn` (all commands, dev/prod/watch, documentation link)
- `Python` (general and version command, documentation link)
- `PHP` (general and version command, documentation link)
- `PHPStan` (general and analysis command, documentation link)
- `Psalm` (general and analysis command, documentation link)
- `ESLint` (general and analysis command, documentation link)
- `StackOverflow Search` (text in search input or if empty from selected text)
- `Google Search` (text in search input or if empty from selected text)
- `Check Internet Connection` (ping 1.1.1.1)

Feel free to open pull request with additional commands.

### Installation:
Use Package Controller or create a the directory `WebDevShell` in your Sublime Text Packages directory with source code from this repository.

Update paths for types in `Preferences/Package Settings/WebDevShell/Settings – User` defined as `prefixname_path` settings.
For example `"php_path": "php"`. You need to define `path` as global command or full path to binary file.

```json
{
    // Settings
    "override_panel_settings": true,
    "colored_output": true,

    // Type paths
    "php_path": "php",
    "artisan_path": "artisan",
    "composer_path": "composer",
    "npm_path": "npm",
    "yarn_path": "yarn",
    "python_path": "python",
    "phpunit_path": "./vendor/bin/phpunit",
    "phpstan_path": "./vendor/bin/phpstan",
    "psalm_path": "./vendor/bin/psalm",
    "eslint_path": "./node_modules/.bin/eslint"
}
```

### Usage:
Press `Cmd + Shift + P` for the dropdown command list, search for `WebDevShell ` and pick your command. You can alternatively use `Tools/WebDevShell...` menu item.

### Notes:
You may need insert in Sublime Text user settings `"show_panel_on_build": true` or use `Tools/Build Results/Show Build Results` menu item for view results.

By default `"override_panel_settings" : true` in WebDevShell settings enables a mechanism forcing to show panel, but I don't guarantee it works on all versions.

### Custom commands
To add custom commands use `Preferences/Package Settings/WebDevShell/Commands – User` menu item.

#### Custom alias command:

```json
{
    "caption": "WebDevShell: Custom Alias",
    "command": "webdevshell",
    "args": {
        "command": "some_long_command_with_params --param value",
        "additional": true,
    }
}
```

All you have to do is set command that you want to execute.

Argument `additional` is optional and you can remove it, it enables input that will be added after the command.

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

#### Full custom command structure:

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

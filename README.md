#weechat

weechat_plugins. Not submitting to weechat as the director seems anally fixated and has created shitty scripting support.

##markup.py
Use a simple in-line markup language to decorate IRC posts with color/formatting/unicode characters.
Autocompletion of the marukup language is also supported to make it easier to use.

###Installation
To install this script copy it to ~/.weechat/python/autoload/
Use the weechat /load or /reload commands to activate the script, or simply restart your instance of weechat.

###Example
The script supports markup in user posts of the form [markup]. See the script itself for a full list of supported markup, but the following is a simple example that makes posted text bold.
```
[bold]hello
```
The text would then appear as follows when posted:

hello

Also note that the markup ``[bold]`` can be introduced via autocompletion. Merely typing ``[bo``+<kbd>tab</kbd> will autocomplete to ```[bold]```.

Markup tags accumulate. so using ``[bold]`` followed by ``[red]`` will result in bold, red text. Accumulated markup can be cleared by using the ``[normal]`` tag.

###Greentext

This script also supports 'greentext' posts via initial '>' operator. The operator remains after color introduced.



#weechat

weechat_plugins. Not submitting to weechat as the director seems anally fixated and has created shitty scripting support.

##markup.py
Use a simple in-line markup language to decorate IRC posts with color/formatting/unicode characters.
Autocompletion of the marukup language is also supported to make it easier to use.

###Installation
To install put this script in ~/.weechat/python/autoload/

###Example
For example the post (local view)
[red][bold]hello

Will be sent to channel with the IRC (red)(bold) color codes.

reset current markup tags with [normal]

Also supports 'greentext' via initial '>' operator. The operator remains after color introduced.



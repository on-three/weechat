#weechat

weechat_plugins. Not submitting to weechat as the director seems anally fixated and has created shitty scripting support.

##markup.py
Script to reinterpret markup in user posts to IRC color and decorator codes.
For example the post (local view)
[red][bold]hello

Will be sent to channel with the IRC (red)(bold) color codes.

reset current markup tags with [normal]

Also supports 'greentext' via initial '>' operator. The operator remains after color introduced.

To install put this script in ~/.weechat/python/autoload/

# -*- coding: utf-8 -*-

SCRIPT_NAME = "markup"
SCRIPT_AUTHOR = "on-three"
SCRIPT_VERSION = "0.0.1"
SCRIPT_LICENSE = "GPL"
SCRIPT_DESC = "use color and other markup in my IRC posts."
 
# make sure we're run under weechat.
import_ok = True
try:
  import weechat
except ImportError:
  print "This script must be run under WeeChat."
  print "Get WeeChat now at: http://www.weechat.org/"
  import_ok = False

import re
import string

colors = {
  'white': u'00',
  'black': u'01',
  'darkblue': u'02',
  'green': u'03',
  'red': u'04',
  'brown': u'05',
  'purple': u'06',
  'olive': u'07',
  'yellow': u'08',
  'green': u'09',
  'teal': u'10',
  'cyan': u'11',
  'blue': u'12',
  'magenta': u'13',
  'darkgray': u'14',
  'gray': u'15',
}

styles = {
  'bold' :  u'\u0002',
  'normal' : u'\u000f',
  'underline' : u'\u001f',
  'italic' : u'\u0009',
  'strikethrough' : u'\u0013',
  'reverse' : u'\u0016',
}

decorators = {
  'note' : u'♫',#♬,♪,♩
  'copyright' : u'©',
  'section' : u'§',
  'yen' : u'¥',
  'pound' : u'£',
  'registered' : u'®',
  'quarter' : u'¼',
  'half' : u'½',
  'threequarters' : u'¾',
  'times' : u'×',
  'divided' : u'÷',
  'cross' : u'†',
  'doubleexclaimation' : u'‼',
  'starofdavid' : u'✡',
  'heart' : u'❤',
  'arrow' : u'➔',
  'sun' : u'☀',
  'umbrella' : u'☂',
  'radioactive' : u'☢',
  'euro' : u'€',
  'telephone' : u'☎',
  'flag' : u'⚑',
  'cut' : u'✂',

}

def markup():
  '''Iterator to cycle through markup keys
  This supports autocompletion
  '''
  for s in styles.keys():
    yield '[{s}]'.format(s=s)
  for c in colors.keys():
    yield '[{c}]'.format(c=c)
  for d in decorators.keys():
    yield '[{d}]'.format(d=d)

def markup2code(m):
  ml = m.lower()
  if ml in styles:
    return styles[ml]
  elif ml in colors:
    return u'\u0003{0}'.format(colors[ml])
  elif ml in decorators:
    return decorators[ml]
  else:
    return m

def to_color(c):
  cl = c.lower()
  if cl in colors:
    return colors[cl]
  else:
    #default to original
    return c

#have to precompile these regexes 'cause i want them case insensitive
SINGLE_MARKUP_RE = re.compile(r'\[(?P<markup>\w+)\]', re.I)
DOUBLE_MARKUP_RE = re.compile(r'\[(?P<foreground>\w+) (?P<background>\w+)\]', re.I)

# Functions
def process_markup(data, msgtype, servername, args):
  '''filter outgoing messages before 512 line parsing
  so the results are visible locally.
  cmd results are of the form: PRIVMSG #bariety :this is a message [h]with markup[n]
  or<MESSAGE TYPE> <channel> :<msg>
  So i'll split it by colon for now.
  '''
  header,blurb = string.split(args, ':', maxsplit=1)

  #first let's tag on a "greentext" modifier for lines which start with '>'
  blurb = re.sub(r'^\>', u'[green][bold]>', blurb)
  
  blurb = re.sub(r'\[(?P<markup>\w+)\]', lambda match: u'{0}'.format(markup2code(match.group(1))), blurb)
  blurb = re.sub(r'\[(?P<foreground>\w+) (?P<background>\w+)\]', lambda match: u"\u0003{0},{1}".format(to_color(match.group(1)),to_color(match.group(2))), blurb)
  args = header  + ':' + blurb
  return args

def markup_autocomplete(data, buffer, command):
  str_input = weechat.buffer_get_string(weechat.current_buffer(), "input")
  if command == "/input complete_next":# and str_input == '':
    last_pos = str_input.rindex('[')#fails if not found.
    last = str_input[last_pos:]
    first = str_input[:last_pos]
    for m in markup():
      if m.startswith(last) and m != last and last != "":
        weechat.command(buffer, '/input delete_line')
        weechat.command(buffer, "/input insert "+ first + m)
        break 
  return weechat.WEECHAT_RC_OK

 
if __name__ == "__main__":
  if import_ok and weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
    weechat.hook_modifier("irc_out1_privmsg", "process_markup", "")
    weechat.hook_modifier("irc_out1_topic", "process_markup", "")
    #attempt to autocomplete markup text in input area
    weechat.hook_command_run('/input complete*', 'markup_autocomplete', '')


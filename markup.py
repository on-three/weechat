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

def to_color(c):
  if c in colors:
    return colors[c]
  else:
    #default to white for bad input
    return u'00'


# Functions
def process_markup(data, msgtype, servername, args):
  '''filter outgoing messages before 512 line parsing
  so the results are visible locally.
  cmd results are of the form: PRIVMSG #bariety :this is a message [h]with markup[n]
  or<MESSAGE TYPE> <channel> :<msg>
  So i'll split it by colon for now.
  '''
  header,blurb = args.split(':')

  #first let's tag on a "greentext" modifier for lines which start with '>'
  blurb = re.sub(r'^\>', u'[green][bold]>', blurb)

  blurb = re.sub(r'\[bold\]', u'\u0002', blurb)
  blurb = re.sub(r'\[reset\]', u'\u000f', blurb)
  blurb = re.sub(r'\[underline\]', u'\u001f', blurb)
  blurb = re.sub(r'\[italic\]', u'\u0009', blurb)
  blurb = re.sub(r'\[strikethrough\]', u'\u0013', blurb)
  blurb = re.sub(r'\[white\]', u'\u000300', blurb)
  blurb = re.sub(r'\[black\]', u'\u000301', blurb)
  blurb = re.sub(r'\[darkblue\]', u'\u000302', blurb)
  blurb = re.sub(r'\[reverse\]', u'\u0016', blurb)
  blurb = re.sub(r'\[green\]', u'\u000303', blurb)
  blurb = re.sub(r'\[red\]', u'\u000304', blurb)
  blurb = re.sub(r'\[brown\]', u'\u000305', blurb)
  blurb = re.sub(r'\[purple\]', u'\u000306', blurb)
  blurb = re.sub(r'\[olive\]', u'\u000307', blurb)
  blurb = re.sub(r'\[yellow\]', u'\u000308', blurb)
  blurb = re.sub(r'\[green\]', u'\u000309', blurb)
  blurb = re.sub(r'\[teal\]', u'\u000310', blurb)
  blurb = re.sub(r'\[cyan\]', u'\u000311', blurb)
  blurb = re.sub(r'\[blue\]', u'\u000312', blurb)
  blurb = re.sub(r'\[magenta\]', u'\u000313', blurb)
  blurb = re.sub(r'\[darkgray\]', u'\u000314', blurb)
  blurb = re.sub(r'\[gray\]', u'\u000315', blurb)
  blurb = re.sub(r'\[(?P<foreground>\w+) (?P<background>\w+)\]', lambda match: u"\u0003{0},{1}".format(to_color(match.group(1)),to_color(match.group(2))), blurb)
  args = header  + ':' + blurb
  return args

 
if __name__ == "__main__":
  if import_ok and weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", ""):
    weechat.hook_modifier("irc_out1_privmsg", "process_markup", "")
    weechat.hook_modifier("irc_out1_topic", "process_markup", "")


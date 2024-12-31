#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                        / /
#  /  | | |\ |  \   |  | / | | /   |   \                        (**)
#  \_ |_| | \| _/   |  | \ |_| \_  |  _/                        (____)o
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#  Copyright 2024, Rebecca Rashkin
#  -------------------------------
#  This code may be copied, redistributed, transformed, or built upon in
#  any format for educational, non-commercial purposes.
# 
#  Please give me appropriate credit should you choose to modify this
#  code. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#  //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
#_______________________________________________________________________

#_______________________________________________________________________
# Visual Studio Terminal color scheme
#_______________________________________________________________________

from classes.scheme_types.base_scheme import ColorScheme

from platform import system
from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class VsCodeTermScheme(ColorScheme):

  OUT_EXT: str = 'json'
  BACKGROUND_COLOR_INTENSE: str = 'background'
  FOREGROUND_COLOR_INTENSE: str = 'foreground'

  LINUX_SETTINGS_LOCATION: str =\
    r'~/.config/Code/User/settings.json'

  WIN_SETTINGS_LOCATION: str =\
    r'C:\Users\<your-username>\AppData\Roaming\Code\User\settings.json'

  if system() == 'Windows':
    settings_path = WIN_SETTINGS_LOCATION
    
  else:
    settings_path = LINUX_SETTINGS_LOCATION

  VSCODE_DESCR: str =\
    'Copy the following text to your settings.json file.'\
    '\nYour settings.json file is usually located: '\
    f'\n{settings_path}'\
    '\n'

  COLOR_NAMES: list[str] = ['ansiBlack'
    , 'ansiRed'
    , 'ansiGreen'
    , 'ansiYellow'
    , 'ansiBlue'
    , 'ansiMagenta'
    , 'ansiCyan'
    , 'ansiWhite'
    , 'ansiBrightBlack'
    , 'ansiBrightRed'
    , 'ansiBrightGreen'
    , 'ansiBrightYellow'
    , 'ansiBrightBlue'
    , 'ansiBrightMagenta'
    , 'ansiBrightCyan'
    , 'ansiBrightWhite'
  ]

  # Used to line up values in column form
  COLOR_FIELD_WIDTH: int =\
    2 + max(len(x) for x in COLOR_NAMES)

  #_____________________________________________________________________
  def __init__(self, *arg):
    """
    Constructor, takes additional argument to base class.

    Parameters
    intense_bold - set intense colors to appear bold, presence in json
                   file input takes precedence
    """
    super(VsCodeTermScheme, self).__init__(*arg)

    self.color_scheme_str_: str = self.create_color_scheme_str()


    return

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates color scheme string to be printed to a file.
    """

    out_str: str =\
      '\n  "workbench.colorCustomizations": {"terminal.background": '

    foreground: str = "foreground"

    space_length: int =\
      VsCodeTermScheme.COLOR_FIELD_WIDTH - len(foreground)

    out_str = f'{out_str}"#{self.background_color_:06x}"'

    out_str = f'{out_str}'\
      f'\n    , "terminal.{foreground}"{": ":>{space_length}}'\
      f'"#{self.foreground_color_:06x}"'

    #___________________________________________________________________
    # Iterate through palette and append to out_str
    # Assumption that normal_colors_ and intense_colors_ are same size
    #___________________________________________________________________
    colors: list[str] = VsCodeTermScheme.COLOR_NAMES
    for i in range(len(self.palette_)):

      # Used to align values in column
      space_length: int =\
        VsCodeTermScheme.COLOR_FIELD_WIDTH - len(colors[i])

      out_str = f'{out_str}'\
        f'\n    , "terminal.{colors[i]}"{": ":>{space_length}}'\
        f'"#{self.palette_[i]:06x}"'

    out_str = f'{out_str}\n'\
      r'}'
    #___________________________________________________________________

    return out_str

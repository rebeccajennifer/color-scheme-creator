#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                        / /
#  /  | | |\ |  \   |  | / | | /   |   \                        (^^)
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
# Mintty color scheme - used for Mintty and Cygwin
#_______________________________________________________________________

from classes.scheme_types.base_scheme import ColorScheme
from classes.rgb_color import RgbConst, RgbColor
from utilities.color_scheme_utils import GeneralUtils as Utils
from classes.color_scheme_strings import ColorSchemeStrings as Strings


#_______________________________________________________________________
class MinttyScheme(ColorScheme):
  """
  Used to generate a color scheme file for Mintty and Cygwin.
  """

  OUT_EXT: str = 'mintty'

  COMPLETION_TEXT: str =str (
    '\nFor your color scheme file to take effect in Mintty or Cygwin, '
    '\nsave your file as \'.minttyrc\' and save to your home '
    '\ndirectory,'
    '\n~/'
  )

  HEADER_COMMENT: str = (
    '\n#' +
    Strings.LINE +
    '\n#' +
    '\n# Mintty color scheme file created by Color Scheme Creator.'
    '\n# Script Author: Rebecca Jennifer'
    '\n#'
    '\n# Save as \'.minttyrc\' in your home directory to use.'
    '\n#' +
    Strings.LINE
  )

  # Color names mapped by position to the ANSI 16 color indices (0–15)
  COLOR_NAME_LIST: list =\
  [ "Black"
  , "Red"
  , "Green"
  , "Yellow"
  , "Blue"
  , "Magenta"
  , "Cyan"
  , "White"
  , "BoldBlack"
  , "BoldRed"
  , "BoldGreen"
  , "BoldYellow"
  , "BoldBlue"
  , "BoldMagenta"
  , "BoldCyan"
  , "BoldWhite"
  ]

  #_____________________________________________________________________
  def create_color_scheme_str(self) -> str:
    """
    Creates color scheme string to be printed to a file.
    """

    if (len(self.palette_) != len(self.COLOR_NAME_LIST)):
      print("Color palette created does not have the correct number of entries")

    out_str: str = self.HEADER_COMMENT + '\n\n'

    # Used to line up values in column form
    color_field_width: int =\
      2 + max(len(x) for x in self.COLOR_NAME_LIST)

    for i in range(0, len(self.palette_)):
      crnt_color: int = self.palette_[i]

      out_str = out_str + f'\n  {self.COLOR_NAME_LIST[i]:<{color_field_width}} = #{Utils.int_to_hex6(crnt_color)}'


    return out_str

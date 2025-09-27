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
# Driver for program
#_______________________________________________________________________

import argparse

from classes.color_scheme_parser import ColorSchemeParser
from classes.color_scheme_parser import ParserStrings

from classes.scheme_types.gnome_scheme import GnomeScheme
from classes.scheme_types.mintty_scheme import MinttyScheme
from classes.scheme_types.konsole_scheme import KonsoleScheme
from classes.scheme_types.vscode_term_scheme import VsCodeTermScheme

from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
def new_line (new_line_count: int = 1) -> None:
  for i in range(new_line_count):
    print()

#_______________________________________________________________________
if __name__ == '__main__':

  new_line(2)

  parser: argparse.ArgumentParser = argparse.ArgumentParser()
  ColorSchemeParser.init_parser(parser)

  args: argparse.Namespace = parser.parse_args()

  scheme_name : str = args.name
  out_dir     : str = args.out_dir

  scheme_types: list =\
  [ GnomeScheme
  #, KonsoleScheme
  , VsCodeTermScheme
  , MinttyScheme
  ]

  if (args.scheme_type == ParserStrings.GNOME_INPUT):
    SchemeType = GnomeScheme

  elif (args.scheme_type == ParserStrings.KONSOLE_INPUT):
    SchemeType = KonsoleScheme

  elif (args.scheme_type == ParserStrings.VSCODE_TERM_INPUT):
    SchemeType = VsCodeTermScheme

  elif (args.scheme_type == ParserStrings.MINTTY_INPUT):
    SchemeType = MinttyScheme

  if (args.default):
    color_scheme = SchemeType()

  if (args.scheme_type != 'all'):
    scheme_types = [SchemeType]

  for SchemeType in scheme_types:
    # Data in file overrides all other arguments
    if(args.file):
      color_scheme = SchemeType(
        args.name, args.out_dir, Utils.read_hex_color_json(args.file))

    else:
      color_scheme =\
        SchemeType(args.name, args.out_dir, args.background_color
          , args.foreground_color
          , args.rgb_list)

    color_scheme.write_file()

  color_scheme.on_completion()
  color_scheme.print_color_scheme()

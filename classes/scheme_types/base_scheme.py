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
# Base class for color schemes
#_______________________________________________________________________

from os import path

from classes.color_scheme_strings import ColorSchemeStrings
from classes.color_scheme_strings import ErrorStrings
from classes.rgb_color import RgbColor
from classes.rgb_color import RgbConst
from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class ColorScheme():

  BACKGROUND_COLOR: str = 'background-color'
  FOREGROUND_COLOR: str = 'foreground-color'
  PALETTE: str = 'palette'

  PREVIEW: str = str(
    '\n-------------------'
    '\n Your Color Scheme'
    '\n'
  )
  ALT_PREV: str = str(
    '\n-------------------------'
    '\n Alternative Backgrounds'
    '\n'
  )

  #_____________________________________________________________________
  def __init__(self, *arg):

    self.background_color_ = RgbConst.DEFAULT_BACKGROUND
    self.foreground_color_ = RgbConst.DEFAULT_FOREGROUND
    self.palette_ = RgbConst.DEFAULT_RGB_INT_LIST
    self.name_ = ColorSchemeStrings.DEFAULT_NAME

    #___________________________________________________________________
    # Default with no arguments
    #___________________________________________________________________
    if (not len(arg)):
      return

    #___________________________________________________________________
    if (isinstance(arg[0], dict)):
      self.construct_from_json(arg[0])

    #___________________________________________________________________
    if (isinstance(arg[0], int)):
        self.background_color_ = arg[0]

    #___________________________________________________________________
    if (len(arg) > 1):
      try:
        self.foreground_color_ = arg[1]
      except TypeError:
        pass

    #___________________________________________________________________
    # Third argument is assumed to be a string containing white space
    # separated hex int strings, used when command line input.
    #___________________________________________________________________
    if (len(arg) > 2):
      try:
        rgb_colors: str = arg[2]

        rgb_color_str_list: list[str] = rgb_colors.split()

        self.palette_ =\
          Utils.str_list_to_hex_list(rgb_color_str_list)

      except TypeError:
        pass

    return

  #_____________________________________________________________________
  def construct_from_json(self, input_dict: dict):
    """
    Constructs color scheme from dictionary created from json.
    """

    #___________________________________________________________________
    try:
      self.name_ = input_dict['name'].replace(' ', '-')
    except:
      pass

    #___________________________________________________________________
    try:
      self.background_color_ =\
        Utils.str_hex_to_int(input_dict[ColorScheme.BACKGROUND_COLOR])

    except TypeError:
      pass

    #___________________________________________________________________
    try:
      self.foreground_color_ =\
        Utils.str_hex_to_int(input_dict[ColorScheme.FOREGROUND_COLOR])

    except TypeError:
      pass

    #___________________________________________________________________
    try:
      color_palette: list = input_dict[ColorScheme.PALETTE]

      if (len(color_palette)):

        # Assumption that color palette is list of hex strings
        if (isinstance(color_palette[0], str)):
          self.palette_ =\
          Utils.str_list_to_hex_list(color_palette)

        #_______________________________________________________________
        # TODO modify function to take other types of dicts
        #      currently shouldn't ever enter this branch
        #_______________________________________________________________
        # Assumption that color palette is list of ints
        elif (isinstance(color_palette[0], int)):
          self.palette_ = color_palette

    except TypeError:
      pass

    return

  #_____________________________________________________________________
  def write_file(self, out_dir) -> None:
    """
    Writes color scheme string to file.

    Parameters
    out_dir - path to directory
    """

    if path.isdir(out_dir):

      out_file_path: str =\
        f'{self.name_}.{self.OUT_EXT}'

      if (not path.isdir(out_dir)):
        input(f'{ErrorStrings.INVALID_DIR}{ColorSchemeStrings.CONTINUE}')
      else:
          out_file_path = path.join(out_dir, out_file_path)

      f = open(out_file_path, 'w')
      f.write(self.color_scheme_str_)
      f.close()

  #_____________________________________________________________________
  def print_color_scheme(self) -> None:
    """
    Prints color scheme to console as colored text.
    """

    bg: int = self.background_color_

    bg_rgb: dict = RgbColor.get_rgb_from_hex(self.background_color_)

    # Flag to determine if background color is light or dark
    is_lite_bg: bool = self.background_color_ >= 0x808080

    if (is_lite_bg):
      greyscale_list: list = RgbConst.ANSI_256_LITE_GREYS
    else:
      greyscale_list: list = RgbConst.ANSI_256_DARK_GREYS

    print(self.PREVIEW)

    DOWN_ARROW: str =\
    '\u2193'

    RGHT_ARROW: str =\
    '\u2192'

    # Print table header
    header: str = ' Selected Background' +\
      '\n               ' + DOWN_ARROW + '\n Options ' + RGHT_ARROW + ' '

    header += RgbColor.construct_color_print_str\
      ( text=f' 0x{self.background_color_:06x} '
      , fg=self.foreground_color_
      , bg=bg
      )

    bg_color_list: list = [self.background_color_]

    # Make an abbreviated list
    for i in range(0, len(greyscale_list)):
      if (i % 3 == 0):
        bg_color_list.append(greyscale_list[i])


    for color in bg_color_list[1:len(bg_color_list)]:
      header += '|' + RgbColor.construct_color_print_str\
        ( text=f' 0x{color:06x} '
        , fg=self.foreground_color_
        , bg=color
        )


    header +='\n----------'

    for i in range(len(bg_color_list)):
      header += '|----------'
    print(header)

    colored_text: str = ''
    #___________________________________________________________________
    for i in range(0, len(self.palette_)):
      crnt_color: int = self.palette_[i]

      colored_text += RgbColor.construct_color_print_str\
        ( text=f' 0x{crnt_color:06x} '
        , fg=crnt_color
        )

      for grey in bg_color_list:
        colored_text += '|'

        colored_text += RgbColor.construct_color_print_str\
        ( text=f' Color {i:2d} '
        , fg=crnt_color
        , bg=grey
        )

      colored_text += '\n'

    print(colored_text)

    return

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

from classes.color_scheme_strings import ColorSchemeStrings as Strings
from classes.color_scheme_strings import ErrorStrings
from classes.rgb_color import RgbColor
from classes.rgb_color import RgbConst
from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class ColorScheme():
  """
  Contains base functionality to generate color schemes. This class
  cannot be used on its own - it must be inherited by a derived class.
  """

  BACKGROUND_COLOR: str = 'background-color'
  FOREGROUND_COLOR: str = 'foreground-color'
  PALETTE: str = 'palette'

  PREVIEW: str = str(
    f'\n{Strings.LINE}'
    f'\n{Strings.LINE}'
    '\n Your Color Scheme'
    '\n'
  )
  ALT_PREV: str = str(
    '\n-------------------------'
    '\n Alternative Backgrounds'
    '\n'
  )

  COMPLETION_TEXT: str = Strings.OUTPUT_STR

  #_____________________________________________________________________
  def __init__(self, name: str = Strings.DEFAULT_NAME, out_dir: str = '.', *arg):

    self.background_color_ = RgbConst.DEFAULT_BACKGROUND
    self.foreground_color_ = RgbConst.DEFAULT_FOREGROUND
    self.palette_ = RgbConst.DEFAULT_RGB_INT_LIST
    self.name_ = name

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
    # separated hex int strings, used when command line input. E.g.
    # TODO add example
    #___________________________________________________________________
    if (len(arg) > 2):
      try:
        rgb_colors: str = arg[2]

        rgb_color_str_list: list[str] = rgb_colors.split()

        self.palette_ =\
          Utils.str_list_to_hex_list(rgb_color_str_list)

      except TypeError:
        pass

    self.out_file_name_: str =\
      f'{self.name_}.{self.OUT_EXT}'


    if path.isdir(out_dir):

      # TODO raise exception instead
      if (not path.isdir(out_dir)):
        input(f'{ErrorStrings.INVALID_DIR}{Strings.CONTINUE}')
      else:
          self.out_file_path_ = path.join(out_dir, self.out_file_name_)

    return

  #_____________________________________________________________________
  def construct_from_json(self, input_dict: dict):
    """
    Constructs color scheme from dictionary created from json.
    """

    #___________________________________________________________________
    try:
      # Ensure file names have no spaces
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

    f = open(self.out_file_path_, 'w')
    f.write(self.color_scheme_str_)
    f.close()

    return

  #_____________________________________________________________________
  def print_color_scheme(self) -> None:
    """
    Prints color scheme to console as colored text.
    """

    bg: int = self.background_color_

    # Flag to determine if background color is light or dark
    is_lite_bg: bool = self.background_color_ >= 0x808080

    if (is_lite_bg):
      greyscale_list: list = RgbConst.ANSI_256_LITE_GREYS
    else:
      greyscale_list: list = RgbConst.ANSI_256_DARK_GREYS

    print(self.PREVIEW)

    TABLE_LINE: str = '\n' + (76 * '-')

    # Print table header
    header: str = str(
      TABLE_LINE +
      '\n Color    | Selected |              Color Scheme Preview with'
      '\n Scheme   | Backgrnd |               Alternative Backgrounds'
      + TABLE_LINE +
      '\n RGB Vals |'
    )

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
      header += '-----------'
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

  #_____________________________________________________________________
  def on_completion(self):
    """
    Prints upon completion.
    """

    completion_text: str = str (
      f'\n{Strings.LINE}'
      f'\n{Strings.OUTPUT_STR}'
      f'\n{self.out_file_path_}'
      f'\n{Strings.LINE}'
      f'\n'
      f'\n{self.color_scheme_str_}'
      f'\n{Strings.LINE}'
      f'\n{self.COMPLETION_TEXT}'
    )

    print(completion_text)

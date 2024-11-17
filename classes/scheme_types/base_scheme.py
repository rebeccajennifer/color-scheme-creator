#_______________________________________________________________________
# Base class for color schemes
#_______________________________________________________________________

from os import path

from classes.color_scheme_strings import ColorSchemeStrings
from classes.color_scheme_strings import ErrorStrings
from classes.rgb_color import RgbConst
from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class ColorScheme():

  BACKGROUND_COLOR: str = "background-color"
  FOREGROUND_COLOR: str = "foreground-color"
  PALETTE: str = "palette"

  PALETTE_COLOR_COUNT: int = 8

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


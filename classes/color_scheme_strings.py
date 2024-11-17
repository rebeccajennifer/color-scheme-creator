#_______________________________________________________________________
# Collection of strings used in color_scheme_designer.
#_______________________________________________________________________

from classes.rgb_color import RgbConst, RgbColor
from utilities.color_scheme_utils import GeneralUtils as Utils

class ColorSchemeStrings:

  LINE: str =\
    '\n________________________________________________________________'

  CONTINUE: str =\
    '\nPress enter to continue.'\
    f'{LINE}'\
    '\n'

  OUTPUT_STR: str =\
    'The following text will be printed to the output file: '\
    '\n'

  DEFAULT_NAME: str =\
    'color-scheme-name'


#_______________________________________________________________________
class ErrorStrings:
  ERROR_STR: str =\
    'ERROR:'

  INVALID_ENTRY: str =\
    f'{ERROR_STR} Invalid argument input.'\
    '\n'

  INVALID_DIR: str =\
    f'{ERROR_STR} Output directory does not exist. File will be '\
    'created in cwd.'\
    '\n'

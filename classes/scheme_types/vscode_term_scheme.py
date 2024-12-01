#_______________________________________________________________________
#   __                _
#  |__ |   | |  \/   |_\ | | |\ | |\ | | |
#  |   |__ |_|  /\   |_/ |_| | \| | \|  |
#   _   _    _    _         _                                    / /
#  | \ |_   \  | /   |\ |  \                                    (**)
#  |_/ |_  _/  | \_| | \| _/                                    (____)o
#_______________________________________________________________________
# Visual Studio Terminal color scheme
#_______________________________________________________________________

from classes.rgb_color import RgbColor, RgbConst
from classes.scheme_types.base_scheme import ColorScheme

from utilities.color_scheme_utils import GeneralUtils as Utils


#_______________________________________________________________________
class VsCodeTermScheme(ColorScheme):

  OUT_EXT: str = 'json'
  BACKGROUND_COLOR_INTENSE: str = 'background'
  FOREGROUND_COLOR_INTENSE: str = 'foreground'

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

    out_str: str = '{'\
      '\n  "workbench.colorCustomizations": {"terminal.background": '

    out_str = f'{out_str}"#{self.background_color_:06x}"'
    out_str = f'{out_str}'\
      f'\n    , "terminal.foreground": "#{self.foreground_color_:06x}"'

    #___________________________________________________________________
    # Iterate through palette and append to out_str
    # Assumption that normal_colors_ and intense_colors_ are same size
    #___________________________________________________________________
    for i in range(len(self.palette_)):

      out_str = f'{out_str}'\
        f'\n    , "terminal.{VsCodeTermScheme.COLOR_NAMES[i]}": '\
        f'"#{self.palette_[i]:06x}"'

    out_str = f'{out_str}\n'\
      r'}'
    #___________________________________________________________________

    return out_str

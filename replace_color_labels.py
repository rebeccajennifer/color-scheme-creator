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
#  Copyright 2025, Rebecca Rashkin
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
# DESCRIPTION
# Replaces color labels in a VSCode template file with actual color
# values.
#_______________________________________________________________________

from os import path

def get_color_label_map() -> dict:
  """
  Returns a mapping of color labels to their RGB integer values.
  """

  color_label_map: dict =\
  { 'FG__NORM': 'c6c6c6'
  , 'BG__NORM': '262626'
  , 'BLK_NORM': '1c1c1c'
  , 'RED_NORM': 'd787af'
  , 'GRN_NORM': 'afd787'
  , 'YEL_NORM': 'ffaf87'
  , 'BLU_NORM': '87afd7'
  , 'VIO_NORM': 'af87d7'
  , 'CYA_NORM': '87d7af'
  , 'WHT_NORM': 'd7d7d7'
  , 'FG__BOLD': 'd7d7d7'
  , 'BG__BOLD': '303030'
  , 'BLK_BOLD': '121212'
  , 'RED_BOLD': 'd75f87'
  , 'GRN_BOLD': '87af5f'
  , 'YEL_BOLD': 'ffd787'
  , 'BLU_BOLD': '00afd7'
  , 'VIO_BOLD': 'af87af'
  , 'CYA_BOLD': '5fafaf'
  , 'WHT_BOLD': 'd0d0d0'
  , 'FG__INVL': 'ff5f87'
  , 'BG__INVL': 'af5f87'

  , 'BLU_BGND': '005f87'
  , 'CYA_BGND': '005f5f'
  , 'VIO_BGND': '875faf'
  , 'GRN_BGND': '00875f'
  , 'ORN_BGND': 'ff875f'
  }

  return color_label_map

if __name__ == '__main__':

  color_label_map: dict = get_color_label_map()

  #_______________________________________________________________
  # File paths.
  #_______________________________________________________________

  script_dir: str = path.dirname(path.abspath(__file__))

  template_file: str = path.join(script_dir
    , 'templates'
    , 'flux-bunny-template.json'
  )

  output_fp: str = '.'

  #_______________________________________________________________
  # Load template file.
  #_______________________________________________________________
  with open(template_file, 'r') as file:
    text: str = file.read()

  #print(text)

  #_______________________________________________________________
  # Replace color labels.
  #_______________________________________________________________

  for key in color_label_map:
    value: str = color_label_map[key]

    label_str: str = f'#{key}'
    text = text.replace(label_str, f'#{value}')

  out_file: str = path.join('/home'
    , 'flux'
    , '.vscode'
    , 'extensions'
    , 'flux-bunny-color-themes'
    , 'flux-bunny-lite.json'
    )

  with open(out_file, 'w') as file:
    file.write(text)
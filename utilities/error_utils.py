#_______________________________________________________________________
#_______________________________________________________________________
#        _   __   _   _ _   _   _   _         _
#   |   |_| | _  | | | V | | | | / |_/ |_| | /
#   |__ | | |__| |_| |   | |_| | \ |   | | | \_
#    _  _         _ ___  _       _ ___   _                    / /
#   /  | | |\ |  \   |  | / | | /   |   \                    (^^)
#   \_ |_| | \| _/   |  | \ |_| \_  |  _/                    (____)o
#_______________________________________________________________________
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#   Copyright 2024, Rebecca Rashkin
#   -------------------------------
#   This code may be copied, redistributed, transformed, or built
#   upon in any format for educational, non-commercial purposes.
#
#   Please give me appropriate credit should you choose to use this
#   resource. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#   //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\  //\^.^/\\
#_______________________________________________________________________
#   DESCRIPTION
#   Error utility functions.
#_______________________________________________________________________

#_____________________________________________________________________
class ErrorUtils:
  """
  Utilities for error messages
  """

  LINE: str =\
    '\n________________________________________________________________'

  ERROR: str =\
    f'{LINE}'\
    '\nUH OH! The program has encountered an error!'\
    f'{LINE}'

  ERROR_TYPE: str =\
    f'{ERROR}'\
    '\nERROR TYPE:  '

  DESC_LABEL: str =\
    '\nDESCRIPTION: '

  MK_DIR_NO_PARENT_ERR: str =\
    'Parent directory not found: '

  FILE_WITH_DIR_NAME_ERR: str =\
    'File exists with the same name: '

  WRONG_FILE_TYPE: str =\
    'Wrong file type.'

  FILE_DNE: str =\
    'File does not exist: '


  #_____________________________________________________________________
  def raise_exception_with_desc(err: Exception, desc: str) -> None:
    """
    Raiese exception with descriptive message.

    Parameters:
      err   : Exception type.
      desc  : Error message.

    Side Effects:
      Raises exception

    Returns:
      None
    """

    err_type = type(err)

    err_msg: str = str(
      f'{ErrorUtils.ERROR_TYPE}{err_type.__name__}'
      f'{ErrorUtils.DESC_LABEL}{desc}'
      f'{ErrorUtils.LINE}'
    )

    raise err_type(err_msg)

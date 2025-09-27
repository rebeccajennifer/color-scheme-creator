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
#   File utility functions.
#_______________________________________________________________________

from os.path import isdir
from os.path import dirname
from os import mkdir
from os import remove

from pypdf import PdfReader
from pypdf import PdfWriter


from utilities.error_utils import ErrorUtils

#_____________________________________________________________________
class FileUtils:
  """
  Utilities related to file and directory operations.
  """

  #_____________________________________________________________________
  def verify_dir(dir_path: str) -> bool:
    """
    Creates a directory if it doesn't exist.

    Parameters:
      dir_path: Path to directory

    Side Effects:
      Creates directory.

    Returns:
      None
    """

    if (not isdir(dir_path)):
      try:
        mkdir(dir_path)
        print(
          '\n Directory created:'
          f'\n {dir_path}'
        )

      except Exception as error:

        err_type: Exception = type(error)
        desc: str = ''

        if (err_type == FileNotFoundError):
          desc: str =\
            f'{ErrorUtils.MK_DIR_NO_PARENT_ERR}{dirname(dir_path)}'

        if (err_type == FileExistsError):
          desc: str =\
            f'{ErrorUtils.FILE_WITH_DIR_NAME_ERR}{dir_path}'

        ErrorUtils.raise_exception_with_desc(error, desc)

    return True

  #_____________________________________________________________________
  def is_pdf(file_path: str) -> bool:
    """
    Determines if file is a pdf.

    Parameters:
      file_path: path to file

    Side Effects:
      None

    Returns:
      bool indicating if file is pdf
    """

    try:
      with open(file_path, 'rb') as f:
        header = f.read(4)
        return header == b'%PDF'

    except Exception as error:

      err_type: Exception = type(error)
      desc: str = ''

      if (err_type == FileNotFoundError):
        desc: str =\
          f'{ErrorUtils.FILE_DNE}{file_path}'

      ErrorUtils.raise_exception_with_desc(error, desc)

    return True

  #_____________________________________________________________________
  def combine_pdfs\
  ( pdf_paths: list
  , combined_pdf_path: str
  , remove_indv_pgs: bool = True
  ) -> None:
    """
    Combines pdfs into one pdf. Order of pages in combined pdf
    determined by order of pdf_paths.

    Parameters:
    pdf_paths         : List of paths of pdfs to combine.
    combined_pdf_path : Path of combined pdf.
    remove_indv_pgs   : True - remove individual pdfs after combining.

    Side Effects:
    Creates a new pdf.

    Returns:
    True  : No errors.
    False : Errors during creation.
    """

    pdf_writer = PdfWriter()

    for pdf in pdf_paths:

      with open (pdf, 'rb') as file:
        pdf_writer.append(file)

    with open\
      (combined_pdf_path, 'wb') as out:

      pdf_writer.write(out)

    # Clean up pdfs
    if(remove_indv_pgs):

      # Loop through all files in the directory
      for pdf in pdf_paths:
          remove(pdf)

    print(str(
      f'\n Combined pdf successfully created!'
      f'\n Output path: {combined_pdf_path}'
      )
    )

    return

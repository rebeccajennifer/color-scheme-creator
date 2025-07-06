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
# Test file for module
#_______________________________________________________________________

from utilities.color_scheme_utils import GeneralUtils as Utils

class TestConst:

  ALL_CAPS_2_CHAR_WITH_0X: str = '0xFF'
  MIX_CAPS_2_CHAR_WITH_0X: str = '0xFf'

  ALL_CAPS_2_CHAR_NO_PRFX: str = 'FF'
  MIX_CAPS_2_CHAR_NO_PRFX: str = 'Ff'

  INT_2_CHAR: int = 255

#_______________________________________________________________________
def test_str_hex2int_all_caps_with_0x():
  assert(
    Utils.str_hex_to_int(TestConst.ALL_CAPS_2_CHAR_WITH_0X) ==\
    TestConst.INT_2_CHAR
  )

def test_str_hex2int_mix_caps_with_0x():
  assert(
    Utils.str_hex_to_int(TestConst.MIX_CAPS_2_CHAR_WITH_0X) ==\
    TestConst.INT_2_CHAR
  )

def test_str_hex2int_all_caps_no_prfx():
  assert(
    Utils.str_hex_to_int(TestConst.ALL_CAPS_2_CHAR_NO_PRFX) ==\
    TestConst.INT_2_CHAR
  )

def test_str_hex2int_mix_caps_no_prfx():
  assert(
    Utils.str_hex_to_int(TestConst.MIX_CAPS_2_CHAR_NO_PRFX) ==\
    TestConst.INT_2_CHAR
  )



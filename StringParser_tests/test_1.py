
import pytest

from StringParser import utils

def test_parseString():
  """
  Tests the pareString function 
  """
  parser = utils.parseString("Hi This is just text to the parser")
  assert(parser)==["Hi","This", "is", "just", "text","to", "the", "parser"]
 

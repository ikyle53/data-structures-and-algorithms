import pytest
from linked_list import (
print_list
)

# TESTING-----------------------------------------------------------------------------
# Can successfully instantiate an empty linked list
# Can properly insert into the linked list
# The head property will properly point to the first node in the linked list
# Can properly insert multiple nodes into the linked list
# Will return true when finding a value within the linked list that exists
# Will return false when searching for a value in the linked list that does not exist
# Can properly return a collection of all the values that exist in the linked list
# TESTING-----------------------------------------------------------------------------

def test_instantiation():
    actual = print_list()
    expected = "None  -> None  -> None  -> "
    assert actual == expected


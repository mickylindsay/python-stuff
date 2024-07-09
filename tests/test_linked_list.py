import pytest

from python_stuff.linked_list import LinkedList


def test_linked_list() -> None:
    linked_list = LinkedList("value")
    assert linked_list.length() == 1
    assert linked_list.get(0) == "value"
    linked_list.add("new value")
    assert linked_list.length() == 2
    assert linked_list.get(1) == "new value"
    linked_list.insert(1, "insert value")
    assert linked_list.length() == 3
    assert linked_list.get(1) == "insert value"
    linked_list.insert(2, "insert value 2")
    assert linked_list.length() == 4
    assert linked_list.get(2) == "insert value 2"
    assert linked_list.remove(1) == "insert value"


def test_linked_list_construct() -> None:
    node = LinkedList(321, LinkedList(123))
    assert node.length() == 2
    assert node.get(0) == 321
    assert node.get(1) == 123


def test_linked_list_insert_negative() -> None:
    with pytest.raises(ValueError, match="index must be greater than 0"):
        LinkedList("value").insert(-1, "test")


def test_linked_list_insert_zero() -> None:
    with pytest.raises(ValueError, match="index must be greater than 0"):
        LinkedList("value").insert(0, "test")


def test_linked_list_insert_out_of_range() -> None:
    with pytest.raises(IndexError, match="index out of range"):
        LinkedList("value").insert(2, "test")


def test_linked_list_get_negative() -> None:
    with pytest.raises(ValueError, match="index must be greater than 0"):
        LinkedList("value").get(-1)


def test_linked_list_get_out_of_range() -> None:
    with pytest.raises(IndexError, match="index out of range"):
        LinkedList("value").get(2)


def test_linked_list_remove_negative() -> None:
    with pytest.raises(ValueError, match="index must be greater than 0"):
        LinkedList("value").remove(-1)


def test_linked_list_remove_zero() -> None:
    with pytest.raises(ValueError, match="index must be greater than 0"):
        LinkedList("value").remove(0)


def test_linked_list_remove_out_of_range() -> None:
    with pytest.raises(IndexError, match="index out of range"):
        LinkedList("value").remove(1)


def test_linked_list_remove_out_of_range_2() -> None:
    with pytest.raises(IndexError, match="index out of range"):
        LinkedList("value").remove(2)

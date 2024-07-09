from python_stuff.linked_list import LinkedList


def test_linked_list() -> None:
    linked_list = LinkedList[str]("value")
    assert linked_list.length() == 1
    linked_list.add("new value")
    assert linked_list.length() == 2

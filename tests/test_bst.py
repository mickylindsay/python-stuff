from python_stuff.bst import BST


def test_bst() -> None:
    bst = BST(10)
    bst.insert(15)
    assert bst.right
    assert bst.right.value == 15
    bst.insert(5)
    assert bst.left
    assert bst.left.value == 5
    bst.insert(12)
    assert bst.right.left
    assert bst.right.left.value == 12
    bst.insert(7)
    assert bst.left.right
    assert bst.left.right.value == 7
    found = bst.search(12)
    assert found
    assert found.value == 12
    assert bst.search(11) is None


def test_bst_insert_exists() -> None:
    bst = BST(10)
    assert bst.insert(10) == bst

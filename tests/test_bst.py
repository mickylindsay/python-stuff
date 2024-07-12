from python_stuff.bst import BST


def test_bst_insert() -> None:
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

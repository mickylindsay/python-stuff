from python_stuff.bst import BST, traverse_in_order


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


def test_bst_delete() -> None:
    bst = BST(10)
    for x in [15, 12, 7, 5, 4, 20, 17, 16]:
        bst.insert(x)
    assert bst.search(4)
    bst.delete(4)
    assert bst.search(4) is None
    assert bst.search(7)
    bst.delete(7)
    assert bst.search(7) is None
    assert bst.search(15)
    bst.delete(15)
    assert bst.search(15) is None
    assert bst.right
    assert bst.right.value == 16


def test_bst_in_order_traversal() -> None:
    bst = BST(10)
    for x in [15, 12, 7, 5, 4, 20, 17, 16]:
        bst.insert(x)
    collector = []

    def fn(node: BST) -> None:
        collector.append(node.value)

    traverse_in_order(bst, fn)
    assert collector == [4, 5, 7, 10, 12, 15, 16, 17, 20]

from python_stuff.hash_table import HashTable


def test_hash_table() -> None:
    table = HashTable[str, float]()
    table.put("test", 1.5)
    assert table.size() == 1
    assert table.get("test") == 1.5
    table.put("test2", 2.0)
    assert table.size() == 2
    assert table.get("test2") == 2.0
    table.put("test2", 2.5)
    assert table.size() == 2
    assert table.get("test2") == 2.5
    table.put("test", 0)
    assert table.size() == 2
    assert table.get("test") == 0
    table.put("test3", 1.0)
    assert table.size() == 3
    assert table.get("test3") == 1.0
    table.put("test3", 1.5)
    assert table.size() == 3
    assert table.get("test3") == 1.5


def test_hash_table_replacement() -> None:
    table = HashTable[int, str]()
    table.put(0, "string")
    table.put(16, "string2")
    table.put(24, "string3")
    table.put(32, "string4")
    assert table.size() == 4
    assert table.get(16) == "string2"
    table.put(32, "string_replacement")
    assert table.size() == 4
    assert table.get(32) == "string_replacement"


def test_hash_table_get_missing() -> None:
    table = HashTable[int, str]()
    assert table.get(0) is None
    table.put(0, "string")
    assert table.get(16) is None


def table_hash_table_remove_head() -> None:
    table = HashTable[int, str]()
    table.put(0, "string")
    assert table.remove(0) == "string"
    assert table.size() == 0


def test_hash_table_remove() -> None:
    table = HashTable[int, str]()
    table.put(0, "string")
    table.put(16, "string2")
    table.put(24, "string3")
    table.put(32, "string4")
    assert table.remove(24) == "string3"
    assert table.size() == 3
    assert table.remove(32) == "string4"
    assert table.size() == 2


def test_hash_table_remove_missing() -> None:
    table = HashTable[int, str]()
    assert table.remove(24) is None
    table.put(0, "string")
    assert table.remove(16) is None

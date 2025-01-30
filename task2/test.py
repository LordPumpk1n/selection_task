from main import HashTable


def test_insert():
    h = HashTable(8)
    h.insert("spoiler", 100)
    h.insert("porog", 200)
    count = h.table.count(None)

    assert len(h.table) - count == 2


def test_insert_collussion():
    h = HashTable(8)
    h.insert(3, 3)
    h.insert(11, 11)
    count = h.table.count(None)

    assert len(h.table) - count == 1


def test_get():
    h = HashTable()
    h.insert("a", 100)
    h.insert("b", 200)

    assert h.get("b") == 200


def test_get_collusion():
    h = HashTable()
    h.insert(11, "a")
    h.insert(3, "b")
    assert h.get(3) == "b"


def test_resize():
    h = HashTable()
    for i in range(7):
        h.insert(i,i)

    assert h.size == 16


def test_overwrite():
    h = HashTable()
    h.insert("a", 123)
    h.insert("a", 1)
    assert h.get("a") == 1


def test_delete():
    h = HashTable()
    h.insert(1,1)
    h.remove(1)
    assert h.get(1) is None


test_insert()
test_insert_collussion()
test_get()
test_get_collusion()
test_resize()
test_overwrite()
test_delete()
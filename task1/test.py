from main import Tree, merge


def test_insert_left_rotation():
    t = Tree()
    t.root = t.insert(9, t.root)
    t.root = t.insert(10, t.root)
    t.root = t.insert(11, t.root)
    assert t.root.val == 10


def test_insert_right_rotation():
    t = Tree()
    t.root = t.insert(3, t.root)
    t.root = t.insert(2, t.root)
    t.root = t.insert(1, t.root)

    assert t.root.val == 2
    assert t.root.left.val == 1
    assert t.root.right.val == 3


def test_delete_leaf_node():
    t = Tree()
    t.root = t.insert(10, t.root)
    t.root = t.insert(5, t.root)
    t.root = t.insert(15, t.root)
    t.root = t.delete_node(5, t.root)

    assert t.root.left is None


def test_delete_node_with_one_child():
    t = Tree()
    t.root = t.insert(10, t.root)
    t.root = t.insert(5, t.root)
    t.root = t.insert(15, t.root)
    t.root = t.insert(3, t.root)
    t.root = t.delete_node(5, t.root)

    assert t.root.left.val == 3


def test_delete_min_node():
    t = Tree()
    t.build_by_arr([15, 100, 20, 10])
    t.root = t.delete_min_node(t.root)

    assert 10 not in t.inorder(t.root)


def test_delete_max_node():
    t = Tree()
    t.build_by_arr([15, 10, 20, 100])
    t.root = t.delete_max_node(t.root)
    arr = t.inorder(t.root)

    assert 100 not in arr


def test_count_nodes():
    t = Tree()
    t.build_by_arr([x for x in range(100)])
    count = t.count_nodes(t.root)
    assert count == 100


def test_count_nodes_zero():
    t = Tree()
    assert t.count_nodes(t.root) == 0


def test_find_average():
    t = Tree()
    t.build_by_arr([10, 20, 30, 40, 50])

    assert t.find_average(t.root) == 30


def test_find_average_zero():
    t = Tree()
    assert t.find_average(t.root) == 0


def test_inorder():
    t = Tree()
    t.build_by_arr([60, 89, 34, 31, 22])
    assert t.inorder(t.root) == [22, 31, 34, 60, 89]


def test_inorder_zero():
    t = Tree()
    assert t.inorder(t.root) == []


def test_split():
    t = Tree()
    t.build_by_arr([10, 20, 25, 30, 40, 50, 60])
    l, r = t.split(26, t.root)

    assert r.check(r.root)
    assert l.check(l.root)
    assert l.inorder(l.root) == [10, 20, 25] and r.inorder(r.root) == [30, 40, 50, 60]


def test_split_empty():
    t = Tree()
    l, r = t.split(100, t.root)

    assert l is None and r is None


def merge_test():
    t1 = Tree()
    t2 = Tree()
    t1.build_by_arr([1, 10, 400])
    t2.build_by_arr([2, 3, 10, 50, 100, 500])
    merge(t1, t2)
    assert t1.inorder(t1.root) == [1, 2, 3, 10, 10, 50, 100, 400, 500]


test_insert_left_rotation()
test_delete_max_node()
test_count_nodes()
test_count_nodes_zero()
test_find_average()
test_inorder()
test_find_average_zero()
test_inorder_zero()
test_split()
test_split_empty()
merge_test()

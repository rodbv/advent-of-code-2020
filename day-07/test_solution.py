from solution import find_bag

MY_BAG = "golden bag"


def test_return_False_if_there_are_no_direct_ways_to_find_my_bag():
    input = ["red bags contain 2 blue bags."]
    assert len(find_bag(input, None, MY_BAG)) == 0


def test_return_one_if_there_is_direct_way_to_find_my_bag():
    input = ["red bags contain 1 golden bag."]
    assert find_bag(input, None, MY_BAG) == {"red bags"}


def test_return_one_if_there_is_direct_way_to_find_my_bags_plural():
    input = ["red bags contain 2 golden bags."]
    assert find_bag(input, None, MY_BAG) == {"red bags"}


def test_2_bags_if_there_is_one_direct_and_one_indirect_way_to_find_my_bag():
    input = ["red bags contain 1 blue bag.", "blue bags contain 1 golden bags."]
    assert find_bag(input, None, MY_BAG) == {"red bags", "blue bags"}


def test_2_bags_one_one_dead_end():
    input = [
        "black bags contain no bags.",
        "red bags contain 3 blue bags.",
        "blue bags contain 1 golden bags.",
    ]
    assert find_bag(input, None, MY_BAG) == {"red bags", "blue bags"}


def test_3_bags_one_dead_end():
    input = [
        "black bags contain no bags.",
        "red bags contain 3 blue bags.",
        "blue bags contain 1 white bags.",
        "white bags contain one golden bag.",
    ]
    assert find_bag(input, None, MY_BAG) == {"red bags", "blue bags", "white bags"}


def test_4_bags():
    input = [
        "black bags contain no bags.",
        "red bags contain 3 blue bags.",
        "blue bags contain 1 white bags.",
        "white bags contain one golden bags.",
        "charcoal bags contain golden bags.",
    ]
    assert find_bag(input, None, MY_BAG) == {
        "red bags",
        "blue bags",
        "white bags",
        "charcoal bags",
    }


def test_return_one_if_my_bag_is_alongside_another_bag():
    input = ["red bags contain 3 golden bags, 2 blue bags."]
    assert find_bag(input, None, MY_BAG) == {"red bags"}


def test_siblings():
    input = [
        "red bags contain 3 blue bags, 2 white bags.",
        "blue bags contain 1 golden bag.",
    ]
    assert find_bag(input, None, MY_BAG) == {"red bags", "blue bags"}


def test_complex():
    input = [
        "red bags contain 3 blue bags, 2 white bags.",
        "blue bags contain 1 golden bag.",
        "white bags contain 5 golden bags.",
    ]
    assert find_bag(input, None, MY_BAG) == {"white bags", "blue bags", "red bags"}


def test_disregard_outer_bag():
    input = ["golden bags contain 3 blue bags"]
    assert len(find_bag(input, None, MY_BAG)) == 0

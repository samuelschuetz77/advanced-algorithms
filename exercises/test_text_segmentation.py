from text_segmentation import all_segmentations, is_word, segmentations_as_lists, splittable


def test_is_word_true():
    assert is_word("earth")


def test_is_word_false():
    assert not is_word("xyz")


def test_splittable_full_string():
    assert splittable("bothearthandsaturnspin")


def test_splittable_single_word():
    assert splittable("earth")


def test_splittable_false():
    assert not splittable("xyzxyz")


def test_splittable_empty_string():
    assert splittable("")


def test_all_segmentations_returns_immutable_word_tuples():
    assert all_segmentations("bothearthandsaturnspin") == (
        ("bot", "heart", "hand", "saturn", "spin"),
        ("both", "earth", "and", "saturn", "spin"),
    )


def test_all_segmentations_false_case():
    assert all_segmentations("xyzxyz") == ()


def test_segmentations_as_lists():
    assert segmentations_as_lists("earth") == [["earth"]]

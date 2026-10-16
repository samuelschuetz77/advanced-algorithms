# Reproducing JEA 2.5 "Text Segmentation" (Splittable) from the reading.

WORDS = {
    "bot", "both", "heart", "earth", "hands", "hand", "and", "at", "saturn",
    "urns", "spin", "blue", "stem", "unit", "robot", "bluest", "emu", "nitro",
}


def is_word(w):
    return w in WORDS


def splittable(s):
    if s == "":
        return True
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        rest = s[i:]
        if is_word(prefix) and splittable(rest):
            return True
    return False


def all_segmentations(s):
    """Return every valid word segmentation of s as immutable tuples."""
    if s == "":
        return ((),)

    segmentations = ()
    for end_of_first_word in range(1, len(s) + 1):
        first_word = s[:end_of_first_word]
        remaining_letters = s[end_of_first_word:]

        if not is_word(first_word):
            continue

        for remaining_segmentation in all_segmentations(remaining_letters):
            full_segmentation = (first_word,) + remaining_segmentation
            segmentations = segmentations + (full_segmentation,)

    return segmentations


def all_splits(s):
    """Compatibility name for the in-class version."""
    return all_segmentations(s)


def segmentations_as_lists(s):
    return [list(segmentation) for segmentation in all_segmentations(s)]
        

if __name__ == "__main__":
    test_str = "bothearthandsaturnspin"
    print(test_str, "->", splittable(test_str))

    print("earth", "->", splittable("earth"))
    print("xyzxyz", "->", splittable("xyzxyz"))

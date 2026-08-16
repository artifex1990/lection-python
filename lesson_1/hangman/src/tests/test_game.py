from hangman.game import is_won, make_mask, validate_letter


def test_mask_hides_unknown_letters():
    assert make_mask("питон", set()) == "_ _ _ _ _"


def test_mask_shows_guessed_letters():
    assert make_mask("питон", {"п", "н"}) == "п _ _ _ н"


def test_win_detected():
    assert is_won("кот", {"к", "о", "т"}) is True
    assert is_won("кот", {"к", "о"}) is False


def test_validation():
    assert validate_letter("а", set()) is None
    assert validate_letter("аб", set()) is not None  # две буквы
    assert validate_letter("1", set()) is not None  # не буква
    assert validate_letter("а", {"а"}) is not None  # повтор

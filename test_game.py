import pytest

from game import Game


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)


@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "12s", "121"])
def test_exception_when_invalid(game, invalid_input):
    assert_illegal_argument(game, invalid_input)

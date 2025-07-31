from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        else:
            strikes = sum(1 for g, q in zip(guess_number, self._question) if g == q)
            balls = len(set(guess_number) & set(self._question)) - strikes
            return GameResult(False, strikes, balls)

    def _assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 입니다.")

        if len(guess_number) != 3:
            raise TypeError("입력은 3 자리 문자열이어야 합니다.")

        if not guess_number.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self._is_duplicated_number(guess_number):
            raise TypeError("중복된 숫자가 존재합니다.")

    def _is_duplicated_number(self, guess_number):
        return len(set(guess_number)) != 3

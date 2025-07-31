class GameResult:
    def __init__(self, solved, strikes, balls):
        self._solved = solved
        self._strikes = strikes
        self._balls = balls

    @property
    def solved(self):
        return self._solved

    @property
    def strikes(self):
        return self._strikes

    @property
    def balls(self):
        return self._balls


# статистика игры
class Stats():

    # инициализация статистики
    def __init__(self):
        self.update_stats()
        self.run_game = False
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    # статистика, изменяющаяся во время игры
    def update_stats(self):
        self.lifes = 1
        self.score = 0
        self.win = False
        self.lose = False
        self.lvl = 1
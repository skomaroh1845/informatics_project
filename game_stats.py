
# статистика игры
class Stats():

    # инициализация статистики
    def __init__(self):
        self.update_stats()
        self.run_game = True

    # статистика, изменяющаяся во время игры
    def update_stats(self):
        self.lifes = 1

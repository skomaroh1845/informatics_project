
# статистика игры
class Stats():

    # инициализация статистики
    def __init__(self):
        self.update_stats()

    # статистика, изменяющаяся во время игры
    def update_stats(self):
        self.lifes = 3

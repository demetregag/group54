def points(games):
    return sum(3 if x > y else 1 if x == y else 0 for game in games for x, y in [map(int, game.split(':'))])

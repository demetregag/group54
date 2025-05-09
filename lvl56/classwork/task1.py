def feast(beast, dish):
    first_matches = beast.startswith(dish[0])
    last_matches = beast.endswith(dish[-1])
    return first_matches and last_matches
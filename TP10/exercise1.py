
def square_odds(values):
    squares = [str(int(num) ** 2) for num in values.split(',') if int(num) % 2 != 0]
    return ','.join(squares)
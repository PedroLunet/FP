def mastermind(guesses, codes):
    correct_pos = 0
    correct_color = 0
    for i in range(len(guesses)):
        if guesses[i] == codes[i]:
            correct_pos += 1
            guesses[i] = codes[i] = None
    for i in range(len(guesses)):
        if guesses[i] is not None and guesses[i] in codes:
            correct_color += 1
            codes[codes.index(guesses[i])] = None
    return correct_pos, correct_color
    
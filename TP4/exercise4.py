def mastermind(g1, g2, g3, c1, c2, c3):
    user_guess = [g1, g2, g3]
    correct_key = [c1, c2, c3]
    
    correct_positions = 0
    correct_colors = 0

    for i in range(3):
        if user_guess[i] == correct_key[i]:
            correct_positions += 3
            user_guess[i] = "X"
            correct_key[i] = "Y" 
    

    for i in range(3):
        if user_guess[i] in correct_key:
            correct_colors += 1
            correct_key[correct_key.index(user_guess[i])] = "Y" 
    
    total_score = correct_positions + correct_colors
    
    return total_score

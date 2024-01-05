from cards import *

BLACK_SUITS = SUITS[0::3]
NUMBER_RANKS = RANKS[:9]
LETTER_RANKS = RANKS[9:]

def get_card_value(card: Card):
    multiplier = 2 if card[0] in BLACK_SUITS else 1
    value = int(card[1]) if card[1] in NUMBER_RANKS else 10 if card[1] in LETTER_RANKS[:-1] else 11
    return value * multiplier

def play(seed_value:int):
    random.seed(seed_value)
    deck = create_deck(shuffle=True)
    player_names = "P1 P2 P3 P4".split()
    player_hands = {name: hand for name, hand in zip(player_names, deal_hands(deck))}
    start_player = choose(player_names)
    turn_order = player_order(player_names, start=start_player)

    # Randomly play cards from each player's hand until empty
    player_points = {name: 0 for name in player_names}
    while player_hands[start_player]:
        turn_cards = {}
        for name in turn_order:
            card = choose(player_hands[name])
            player_hands[name].remove(card)
            turn_cards[name] = card
        turn_points = {}
        for name in turn_cards: 
            turn_points[name] = get_card_value(turn_cards[name])
        turn_score = sorted(turn_points.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(turn_score)):
            if i == 0: player_points[turn_score[i][0]] += 1
            elif turn_score[i][1] == turn_score[i-1][1]:
                player_points[turn_score[i][0]] += 1
            else:
                break

    game_score = sorted(player_points.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for i in range(len(game_score)):
        if i == 0: result += game_score[i][0]
        elif game_score[i][1] == game_score[i-1][1]:
            result += " " + game_score[i][0]
        else:
            break
    return result
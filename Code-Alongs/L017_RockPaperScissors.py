from random import choice

SIGNS = ["rock", "paper", "scissors"]           # CAPITAL letters means that the variable is GLOBAL (convention, not required)

def main():
    print(f"Welcome to the {', '.join(SIGNS)} game")
    print_rules()
    
    number_of_rounds = select_number_of_rounds()
    
    print(f'\nBest of {number_of_rounds} wins. Let\'s start!')
    
    game_loop(number_of_rounds)
    

def print_rules():
    print("\nRules: Each player picks a sign: ")
    for winner, loser in zip([0, 1, 2], [2, 0, 1]):
        print(f'{SIGNS[winner].title()} wins over {SIGNS[loser]}')

def select_number_of_rounds():
    while True:
        try:
            rounds = int(input("\nPlease select the number of rounds: "))
            if 1 < rounds <= 10: return rounds
            else:
                print("Rounds must be between 1 and 10.")
        except ValueError:
            print("Number of rounds must be an integer.")
    

def game_loop(number_of_rounds):
    for current_round in range(1, number_of_rounds + 1):
        print(f'\nRound: {current_round}')
        sign_player_a = get_sign_from_user()
        sign_player_b = get_sign_from_computer()
        print(f'\nPlayer: {sign_player_a}, Computer: {sign_player_b}')
        
        if is_draw(sign_player_a, sign_player_b):
            return "It's a draw!"
        elif wins_over(sign_player_a, sign_player_b):
            return"Player wins!"
        else:
            return "Computer wins!"

def get_sign_from_user():
    sign = input("Pick a sign: ".strip().lower())
    
    while True:
        if sign in SIGNS:
            return sign
        else:
            print(f"You must pick one of {', '.join(SIGNS)}")
        
def get_sign_from_computer():
    return choice(SIGNS)

def is_draw(sign_a, sign_b):
    if sign_a == sign_b:
        return True
    else:
        return False
    
def wins_over(sign_a, sign_b):
    for winner, loser in zip([0, 1, 2], [2, 0, 1]):
        print(f'{SIGNS[winner].title()} wins over {SIGNS[loser]}')
        if sign_a == SIGNS[winner] and sign_b == SIGNS[loser]: return True
            
    return False
        

main()









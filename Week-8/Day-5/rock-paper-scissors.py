from Game import Game

def get_user_menu_choice():
    while True:
        choice = input('Enter "P" to play a new game, "S" to show scores, or "Q" to quit: ')
        if choice == 'P' or choice == "S" or choice == "Q":
            break
    return choice

def print_results(results:dict):
    for item in results:
        print(f'{item}: {results[item]}')
    print('Thank you for playing!')

def main():
    results = {'win':0, 'loss':0, 'draw':0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'P':
            new_game = Game()
            score = new_game.play()
            results[score] += 1
        elif choice == 'S':
            print_results(results)
        elif choice == 'Q':
            print(f'Bye bye now!\n{print_results(results)}')
            break
    return

main()



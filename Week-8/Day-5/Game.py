import random

class Game():
    def get_user_item(self):
        while True:
            item = input("Type rock, paper, or scissors: ")
            if item == 'rock' or item == 'paper' or item == 'scissors' :
                break
        return item

    def get_computer_item(self):
        rps = ['rock', 'paper', 'scissors']
        return random.choices(rps)[0]

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return 'draw'
        if user_item == 'rock' and computer_item == 'scissors' or user_item == 'paper' and computer_item == 'rock' or user_item == 'scissors' and computer_item == 'paper':
            return 'win'
        if user_item == 'rock' and computer_item == 'paper' or user_item == 'paper' and computer_item == 'scissors' or user_item == 'scissors' and computer_item == 'rock':
            return 'loss'

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        result = self.get_game_result(user, computer)
        if result == 'win':
            print(f'You selected {user}. The computer selected {computer}. You Win!')
        elif result == 'loss':
            print(f'You selected {user}. The computer selected {computer}. You Lose!')
        elif result == 'draw':
            print(f'You selected {user}. The computer selected {computer}. Its a Draw!')
        return result


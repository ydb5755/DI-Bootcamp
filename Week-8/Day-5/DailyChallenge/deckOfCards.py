# Instructions
# Part 1 : Quizz :
# Answer the following questions

# What is a class? - A blueprint for creating objects
# What is an instance? - An object created through the use of a class
# What is encapsulation? - Bundling of data and methods of that data into a single unit
# What is abstraction? - process of hiding internal data and implementation from outside world
# What is inheritance? - When a class derives data from another class
# What is multiple inheritance? - When a class inherits from multiple parent classes
# What is polymorphism? - The ability of different objects to respond in their own ways to an identical message
# What is method resolution order or MRO? - The order in which a method is searched for in a classes hierarchy


# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card():
    
    def pick(self):
        suits = ['s', 'h', 'c', 'd']
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        Card = value[random.randint(0,12)] + suits[random.randint(0,3)]
        return Card

    
class Deck():
    def __init__(self) -> None:
        self.drawn = []
    
    def shuffle(self):
        self.drawn = []
    
    def deal(self):
        while True:
            if len(self.drawn) == 52:
                print('There are no more cards!')
                break
            new_card = Card().pick()
            if new_card not in self.drawn:
                self.drawn.append(new_card)
                return new_card
            
    def check_deck(self):
        return self.drawn


n = Deck()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
n.deal()
print(n.check_deck())
full_deck = n.check_deck()
print(len(full_deck))

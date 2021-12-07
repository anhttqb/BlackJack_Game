import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Step 1: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

def deal_card():
    return random.choice(cards)

# step 3: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
def calculate_score(cards):
    '''Take the list of cards and return the score calculated from the cards'''
    # step 4: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # step 5: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if sum(cards) > 21 and 11 in cards:
        cards.append(1)
        cards.remove(11)

    return sum(cards)


# step 10: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_cards, user_score, computer_cards, computer_score):
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    if computer_score == 0:
        print("Opponent has a blackjack. You lose!")
    elif user_score == 0:
        print("You get a blackjack. You win!")
    elif user_score > 21:
        print("You went over. You lose!")
    elif computer_score > 21:
        print("Opponent went over. You win!")
    else:
        if user_score == computer_score:
            print("Draw!")
        elif user_score > computer_score:
            print("You win!")
        else:
            print("You lose!")


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    # step 2: Deal the user and computer 2 cards each using deal_card() and append().
    for n in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # step 6: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over
    # 21, then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    # step 7: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    while not is_game_over:
        if user_score > 21:
            is_game_over = True
        elif input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
            user_cards.append(deal_card())
            # step 8: The score will need to be rechecked with every new card drawn and the checks in step 6 need to be repeated until the game ends.
            user_score = calculate_score(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: {computer_cards[0]}")
        else:
            is_game_over = True

    # step 9: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 16.
    while computer_score != 0 and computer_score < 16:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    compare(user_cards, user_score, computer_cards, computer_score)


# step 11: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()

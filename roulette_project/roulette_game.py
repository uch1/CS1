import random

random.seed(1)

bank_account = 1000000
bet_amount = 0
bet_color = None
bet_number = None

green = [0, 37]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

def take_bet(color, number, amount):
    bet_color = color
    bet_number = number
    bet_amount = amount

    return [bet_color, bet_number, bet_amount]

def roll_ball():
    '''returns a random number between 0 and 37'''
    ball_roll = random.randint(0, 38)
    return ball_roll

def check_results(bet_number, bet_color):
    '''Compares bet_color to color rolled.  Compares
    bet_number to number_rolled.'''
    color_result = None

    if bet_number in green:
        color_result = "green"
    elif bet_number in red:
        color_result = "red"
    elif bet_number in black:
        color_result = "black"

    print("The ball rolled on a {} {}").format(bet_number, color_result)


def payout(wins, bet_results):
    '''returns total amount won or lost by user based on results of roll. '''
    if wins == "Winner!!!":
        print("You won $", str(bank_account + bet_results[2]))
    else:
        print("You lost $", str(bank_account - bet_results[2]))

def play_game():
    """This is the main function for the game.
    When this function is called, one full iteration of roulette,
    including:
    Take the user's bet.
    Roll the ball.
    Determine if the user won or lost.
    Pay or deduct money from the user accordingly.
    """

from tkinter import *
import random
from PIL import ImageTk, Image

# Dictionary containing card name and value
value = {
    '2C':2,
    '2S':2, 
    '2D':2, 
    '2H':2, 
    '3C':3, 
    '3S':3, 
    '3D':3, 
    '3H':3, 
    '4C':4, 
    '4S':4, 
    '4D':4, 
    '4H':4, 
    '5C':5, 
    '5S':5, 
    '5D':5, 
    '5H':5, 
    '6C':6,
    '6S':6, 
    '6D':6, 
    '6H':6, 
    '7C':7, 
    '7S':7, 
    '7D':7, 
    '7H':7, 
    '8C':8, 
    '8S':8, 
    '8D':8, 
    '8H':8, 
    '9C':9, 
    '9S':9, 
    '9D':9, 
    '9H':9, 
    '10C':10,
    '10S':10, 
    '10D':10,
    '10H':10, 
    'AC':11, 
    'AS':11, 
    'AD':11, 
    'AH':11, 
    'KC':10, 
    'KS':10, 
    'KD':10, 
    'KH':10, 
    'QC':10, 
    'QS':10, 
    'QD':10, 
    'QH':10, 
    'JC':10, 
    'JS':10, 
    'JD':10, 
    'JH':10
}

# List containing all cards
deck = ['2C', '2S', '2D', '2H', '3C', '3S', '3D', '3H', '4C', '4S', '4D', '4H', '5C', '5S', '5D', '5H', '6C',
'6S', '6D', '6H', '7C', '7S', '7D', '7H', '8C', '8S', '8D', '8H', '9C', '9S', '9D', '9H', '10C', '10S', '10D',
'10H', 'AC', 'AS', 'AD', 'AH', 'KC', 'KS', 'KD', 'KH', 'QC', 'QS', 'QD', 'QH', 'JC', 'JS', 'JD', 'JH']

# Payouts list with payouts
payouts = {
    "Win": 2,
    "Loss": 0,
    "Draw": 1,
    "Blackjack": 2.5
}

# Creating window with size and title
root = Tk()
root.geometry('500x550') 
root.title('BLACKJACK')

# Empty lists to store the player's and dealer's hand
player_cards = []
dealer_cards = []

# Lists of lists where the first value in each inner list is the label used to 
# show the pictures of the cards, and the second value to show whether or not 
# the label has been used yet

dealer_labels = [[Label(), False] for i in range(10)] 
# 10 because this is the highest possible number of cards that a dealer's hand
# can have at any one time (4 Aces, 4 2's, 2 3's to make 18, at which point 
# the dealer must stand as it is greater than 17)
                                                    
player_labels = [[Label(), False] for i in range(12)]
# 12 because this is the highest possible number of cards that a player's hand
# can have at any one time (4 Aces, 4 2's, 4 3's to make 24, at which point 
# the player is bust)

# Sets dealer and player score to 0
dealer_score = 0
player_score = 0

# Variable to keep track of player's chips
player_chips = 50  # Start with 50 chips

# Label to display player's chip count
chips_label = Label(text=f"Chips: {player_chips}")
chips_label.place(x=10, y=10)

# Chip image
chip_img = Image.open('cards/chips.png')
chip_img = chip_img.resize((30, 30), Image.ANTIALIAS)
chip_image = ImageTk.PhotoImage(chip_img)

# Variable to keep track of player's bet
player_bet = 0
bet_placed = False # initialize this to false, so game only deals when a bet is placed

# Label to display player's current bet
bet_label = Label(text=f"Bet: {player_bet}")
bet_label.place(x=10, y=40)

# Betting buttons
def increase_bet():
    global player_bet
    if player_bet < player_chips:
        player_bet += 10  # You can change the bet increment as needed
        update_bet_label()

def decrease_bet():
    global player_bet
    if player_bet > 0:
        player_bet -= 10  # You can change the bet decrement as needed
        update_bet_label()

# Function to update the bet label
def update_bet_label():
    bet_label.config(text=f"Bet: {player_bet}")

# Buttons to increase and decrease the bet
increase_bet_button = Button(text="Increase Bet", command=increase_bet)
increase_bet_button.place(x=10, y=70)

decrease_bet_button = Button(text="Decrease Bet", command=decrease_bet)
decrease_bet_button.place(x=10, y=100)

# Cards are stored within this class as objects
# Their attributes are self.name and self.value, and they can be placed in the 
# window using self.place(dealer: bool), where dealer is True or False (card
# placed on either dealers side or players side)
class Card():

    def __init__(self, name, value) -> None:
        self.name = name
        self.value = value

    def place(self, dealer=True):
        
        if dealer == True: # Dealer's card
            # Y-value of all dealer cards 
            y = 65

            for i in range(len(dealer_labels)):

                label = dealer_labels[i]

                if label[1] == False:
                    
                    # Gets the png file of the card
                    path = 'cards/' + self.name + '.png'
                    img = Image.open(path)
                    img = img.resize((96, 136), Image.ANTIALIAS)
                    image = ImageTk.PhotoImage(img)
                    label[0].configure(image=image)
                    label[0].image = image
                    
                    # Places cards and repositions depending on the number of cards
                    if i == 0:
                        label[0].place(x=172 ,y=y)
                    elif i == 1:
                        dealer_labels[i-1][0].place(x=172, y=y)
                        label[0].place(x=232 ,y=y)
                    elif i == 2:
                        dealer_labels[i-2][0].place(x=142, y=y)
                        dealer_labels[i-1][0].place(x=202, y=y)
                        label[0].place(x=262 ,y=y)
                    elif i == 3:
                        dealer_labels[i-3][0].place(x=157, y=y)
                        dealer_labels[i-2][0].place(x=187, y=y)
                        dealer_labels[i-1][0].place(x=217, y=y)
                        label[0].place(x=247 ,y=y)
                    elif i == 4:
                        dealer_labels[i-4][0].place(x=142, y=y)
                        dealer_labels[i-3][0].place(x=177, y=y)
                        dealer_labels[i-2][0].place(x=207, y=y)
                        dealer_labels[i-1][0].place(x=237, y=y)
                        label[0].place(x=267 ,y=y)
                    elif i == 5:
                        dealer_labels[i-5][0].place(x=127, y=y)
                        dealer_labels[i-4][0].place(x=157, y=y)
                        dealer_labels[i-3][0].place(x=187, y=y)
                        dealer_labels[i-2][0].place(x=217, y=y)
                        dealer_labels[i-1][0].place(x=247, y=y)
                        label[0].place(x=277 ,y=y)
                    elif i == 6:
                        dealer_labels[i-6][0].place(x=112, y=y)
                        dealer_labels[i-5][0].place(x=142, y=y)
                        dealer_labels[i-4][0].place(x=172, y=y)
                        dealer_labels[i-3][0].place(x=202, y=y)
                        dealer_labels[i-2][0].place(x=232, y=y)
                        dealer_labels[i-1][0].place(x=262, y=y)
                        label[0].place(x=292 ,y=y)
                    elif i == 7:
                        dealer_labels[i-7][0].place(x=97, y=y)
                        dealer_labels[i-6][0].place(x=127, y=y)
                        dealer_labels[i-5][0].place(x=157, y=y)
                        dealer_labels[i-4][0].place(x=187, y=y)
                        dealer_labels[i-3][0].place(x=217, y=y)
                        dealer_labels[i-2][0].place(x=247, y=y)
                        dealer_labels[i-1][0].place(x=277, y=y)
                        label[0].place(x=307 ,y=y)
                    elif i == 8:
                        dealer_labels[i-8][0].place(x=82, y=y)
                        dealer_labels[i-7][0].place(x=112, y=y)
                        dealer_labels[i-6][0].place(x=142, y=y)
                        dealer_labels[i-5][0].place(x=172, y=y)
                        dealer_labels[i-4][0].place(x=202, y=y)
                        dealer_labels[i-3][0].place(x=232, y=y)
                        dealer_labels[i-2][0].place(x=262, y=y)
                        dealer_labels[i-1][0].place(x=292, y=y)
                        label[0].place(x=322 ,y=y)
                    elif i == 9:
                        dealer_labels[i-9][0].place(x=67, y=y)
                        dealer_labels[i-8][0].place(x=97, y=y)
                        dealer_labels[i-7][0].place(x=127, y=y)
                        dealer_labels[i-6][0].place(x=157, y=y)
                        dealer_labels[i-5][0].place(x=187, y=y)
                        dealer_labels[i-4][0].place(x=217, y=y)
                        dealer_labels[i-3][0].place(x=247, y=y)
                        dealer_labels[i-2][0].place(x=277, y=y)
                        dealer_labels[i-1][0].place(x=307, y=y)
                        label[0].place(x=337 ,y=y)
                    label[1] = True
                    break
        if dealer == False: # Player's card
            # Y-value of all player cards
            y = 350 
            for i in range(len(player_labels)):

                label = player_labels[i]

                if label[1] == False:

                    # Gets the png file of the card
                    path = 'cards/' + self.name + '.png'
                    img = Image.open(path)
                    img = img.resize((96, 136), Image.ANTIALIAS)
                    image = ImageTk.PhotoImage(img)
                    label[0].configure(image=image)
                    label[0].image = image
                    
                    # Places cards and repositions depending on the number of cards, this
                    # goes higher than that for dealer cards as the highest possible 
                    # number of cards in a player's hand is higher
                    if i == 0:
                        label[0].place(x=172 ,y=y)
                    elif i == 1:
                        player_labels[i-1][0].place(x=172, y=y)
                        label[0].place(x=232 ,y=y)
                    elif i == 2:
                        player_labels[i-2][0].place(x=142, y=y)
                        player_labels[i-1][0].place(x=202, y=y)
                        label[0].place(x=262 ,y=y)
                    elif i == 3:
                        player_labels[i-3][0].place(x=157, y=y)
                        player_labels[i-2][0].place(x=187, y=y)
                        player_labels[i-1][0].place(x=217, y=y)
                        label[0].place(x=247 ,y=y)
                    elif i == 4:
                        player_labels[i-4][0].place(x=142, y=y)
                        player_labels[i-3][0].place(x=177, y=y)
                        player_labels[i-2][0].place(x=207, y=y)
                        player_labels[i-1][0].place(x=237, y=y)
                        label[0].place(x=267 ,y=y)
                    elif i == 5:
                        player_labels[i-5][0].place(x=127, y=y)
                        player_labels[i-4][0].place(x=157, y=y)
                        player_labels[i-3][0].place(x=187, y=y)
                        player_labels[i-2][0].place(x=217, y=y)
                        player_labels[i-1][0].place(x=247, y=y)
                        label[0].place(x=277 ,y=y)
                    elif i == 6:
                        player_labels[i-6][0].place(x=112, y=y)
                        player_labels[i-5][0].place(x=142, y=y)
                        player_labels[i-4][0].place(x=172, y=y)
                        player_labels[i-3][0].place(x=202, y=y)
                        player_labels[i-2][0].place(x=232, y=y)
                        player_labels[i-1][0].place(x=262, y=y)
                        label[0].place(x=292 ,y=y)
                    elif i == 7:
                        player_labels[i-7][0].place(x=97, y=y)
                        player_labels[i-6][0].place(x=127, y=y)
                        player_labels[i-5][0].place(x=157, y=y)
                        player_labels[i-4][0].place(x=187, y=y)
                        player_labels[i-3][0].place(x=217, y=y)
                        player_labels[i-2][0].place(x=247, y=y)
                        player_labels[i-1][0].place(x=277, y=y)
                        label[0].place(x=307 ,y=y)
                    elif i == 8:
                        player_labels[i-8][0].place(x=82, y=y)
                        player_labels[i-7][0].place(x=112, y=y)
                        player_labels[i-6][0].place(x=142, y=y)
                        player_labels[i-5][0].place(x=172, y=y)
                        player_labels[i-4][0].place(x=202, y=y)
                        player_labels[i-3][0].place(x=232, y=y)
                        player_labels[i-2][0].place(x=262, y=y)
                        player_labels[i-1][0].place(x=292, y=y)
                        label[0].place(x=322 ,y=y)
                    elif i == 9:
                        player_labels[i-9][0].place(x=67, y=y)
                        player_labels[i-8][0].place(x=97, y=y)
                        player_labels[i-7][0].place(x=127, y=y)
                        player_labels[i-6][0].place(x=157, y=y)
                        player_labels[i-5][0].place(x=187, y=y)
                        player_labels[i-4][0].place(x=217, y=y)
                        player_labels[i-3][0].place(x=247, y=y)
                        player_labels[i-2][0].place(x=277, y=y)
                        player_labels[i-1][0].place(x=307, y=y)
                        label[0].place(x=337 ,y=y)
                    elif i == 10:
                        player_labels[i-10][0].place(x=52, y=y)
                        player_labels[i-9][0].place(x=82, y=y)
                        player_labels[i-8][0].place(x=112, y=y)
                        player_labels[i-7][0].place(x=142, y=y)
                        player_labels[i-6][0].place(x=172, y=y)
                        player_labels[i-5][0].place(x=202, y=y)
                        player_labels[i-4][0].place(x=232, y=y)
                        player_labels[i-3][0].place(x=262, y=y)
                        player_labels[i-2][0].place(x=292, y=y)
                        player_labels[i-1][0].place(x=322, y=y)
                        label[0].place(x=352 ,y=y)
                    elif i == 11:
                        player_labels[i-11][0].place(x=37, y=y)
                        player_labels[i-10][0].place(x=67, y=y)
                        player_labels[i-9][0].place(x=97, y=y)
                        player_labels[i-8][0].place(x=127, y=y)
                        player_labels[i-7][0].place(x=157, y=y)
                        player_labels[i-6][0].place(x=187, y=y)
                        player_labels[i-5][0].place(x=217, y=y)
                        player_labels[i-4][0].place(x=247, y=y)
                        player_labels[i-3][0].place(x=277, y=y)
                        player_labels[i-2][0].place(x=307, y=y)
                        player_labels[i-1][0].place(x=337, y=y)
                        label[0].place(x=367 ,y=y)
                    label[1] = True
                    break


# Creates 52 card objects and appends to list
card_objs = []
for i in range(52):
    card_name = deck[i]
    card_value = value[card_name]
    card_objs.append(Card(name=card_name, value=card_value))

# Path to face down card, used at the start of each round
facedowncardpng = 'cards/cardback.png'

# Function that is executed when hit button is pressed
def hit():

    global player_score

    # Gets card at top of deck
    player_card = card_objs.pop(0)
    # Puts it back in at the bottom
    card_objs.append(player_card)
    # Adds it to the list containing the player's hand
    player_cards.append(player_card)

    player_score += player_card.value
    player_card.place(dealer=False)

    if player_score > 21:
        for card in player_cards:
            # Checks if there is an ace, and makes value of it 1 if necessary
            # to prevent player from going bust
            if card.value == 11:
                player_score -= 10
                break
        if player_score > 21:
            finished('Loss')
        player_score += 10

# Function that is executed when stand button is pressed
def stand():

    global player_score
    global dealer_score

    # Once player stands, dealer hits until bust or total > 17
    while dealer_score < 17:
        dealer_card = card_objs.pop(0)
        card_objs.append(dealer_card)
        dealer_cards.append(dealer_card)

        dealer_score += dealer_card.value
        dealer_card.place(dealer=True)
    
    if dealer_score > 21 or player_score > dealer_score:
        finished('Win')
    elif dealer_score == player_score:
        finished('Draw')
    elif dealer_score > player_score:
        finished('Loss')

# Executes when the round is over, takes the result as an argument and creates
# labels that show the result along with the dealer total and player total that
# are displayed on the screen
def finished(result):
    global player_score
    global text
    global player_score_text
    global dealer_score_text
    global player_chips

    hit_button.place_forget()
    stand_button.place_forget()

    payout = player_bet * payouts[result]
    player_score_text = Label(text=f"Your total: {player_score}")
    dealer_score_text = Label(text=f"Dealer's total: {dealer_score}")
    player_score_text.place(x=200, y=320)
    dealer_score_text.place(x=185, y=220)

    if result == "Win" or result == "Blackjack":
        player_chips += payout
    elif result == 'Draw':
        text = Label(text="Draw")
        player_chips += player_bet  # Return the bet for a draw
    elif result == 'Loss':
        text = Label(text="You lost.")
        player_chips -= player_bet  # Lose the bet for a loss

    chips_label.config(text=f"Chips: {player_chips}")  # Update chip count

    text.place(x=215, y=260)

    reset_game()

    new_round_button = Button(text="New Round", command=reset_game)
    new_round_button.place(x=195, y=280)

def reset_game():

    global player_cards, dealer_cards
    global player_score, dealer_score 
    global player_bet
    global hit_button, stand_button
    
    # Reset card hands
    player_cards = [] 
    dealer_cards = []

    # Reset scores
    player_score = 0
    dealer_score = 0 
    
    # Reset bet
    player_bet = 0
    update_bet_label()

    # Replace hit/stand buttons 
    hit_button = Button(text="Hit", command=hit)
    hit_button.place(x=110, y=300)

    stand_button = Button(text="Stand", command=stand) 
    stand_button.place(x=320, y=300)

    # Shuffle deck
    random.shuffle(card_objs)

    # Deal new hand
    play()

    
def deal():
    global bet_placed
    if not bet_placed:
        print("Place bet first!")
        return
    
    play()

# Starts game
def play():

    global dealer_score
    global player_score
    global dealer_labels
    global player_labels
    player_score = calculate_score(player_cards)
    
    # Resets labels
    dealer_labels = [[Label(), False] for i in range(10)]
    player_labels = [[Label(), False] for i in range(12)]

    # Shuffles cards
    random.shuffle(card_objs)

    # Reveals one of the dealer's cards
    dealer_card = card_objs.pop(0)
    card_objs.append(dealer_card)
    dealer_cards.append(dealer_card)

    dealer_score += dealer_card.value
    dealer_card.place(dealer=True)

    # Gives 2 cards to the player
    for i in range(2):
        player_card = card_objs.pop(0)
        card_objs.append(player_card)
        player_cards.append(player_card)

        player_score += player_card.value
        player_card.place(dealer=False)

    if player_score == 21: # Stop the game if user is dealt blackjack
        finished("Blackjack")
        return

# Calculate score to check for blackjack    
def calculate_score(cards):
    score = 0
    for card in cards:
        score += card.value
    return score

# Places one of the dealer's cards face down
img1 = Image.open('cards/cardback.png')
img1 = img1.resize((96, 136), Image.ANTIALIAS)
image1 = ImageTk.PhotoImage(img1)
facedownlabel = Label(image=image1).place(x=232,y=65)

def place_bet():
    global bet_placed
    bet_placed = True

deal_button = Button(text="Deal", command=deal)
deal_button.place(x=225, y=300)

dealer_hand_text = Label(text="Dealer's hand")
dealer_hand_text.place(x=205, y=30)
hit_button = Button(text="Hit", command=hit)
hit_button.place(x=110, y=300)
stand_button = Button(text="Stand", command=stand)
stand_button.place(x=320, y=300)

text = Label()
player_score_text = Label()
dealer_score_text = Label()

# Starts game for the first time
place_bet()

# Creates window
root.mainloop()
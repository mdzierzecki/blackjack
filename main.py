import tkinter
import random


def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    # for each suits retrieve image for the cards

    for suit in suits:
        # first the card number 1 to 10
        for card in range(1, 10):
            name = 'cards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # next the face cards
        for card in face_cards:
            name = 'cards/{}_{}.png'.format(str(card), suit)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


# deal card
def deal_card(frame):
    # pop next card of the deck
    next_card = deck.pop(0)
    # add the image to the label
    tkinter.Label(frame, image=next_card[1], relief='raised').pack(side='left')
    # return card the face value
    return next_card

def score_hand(hand):
    # Calcualte the total score of all cards in the list
    # ace is calculate to 11 or 1 - depends on player position
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        if card_value == 1 and ace:
            ace = False
            card_value = 11



def deal_dealer():
    global dealer_score
    global dealer_ace
    card_value = deal_card(dealer_card_frame)[0]
    if card_value == 1 and not dealer_ace:
        dealer_ace = True
        card_value = 11
    dealer_score += card_value
    # when we bust
    if card_value > 21 and dealer_ace:
        dealer_score -= 10
        dealer_ace = False
    dealer_score_label.set(dealer_score)
    if dealer_score > 21:
        result_text.set("Przegrales zjebie")


def deal_player():
    global player_score
    global player_ace
    card_value = deal_card(player_card_frame)[0]
    if card_value == 1 and not player_ace:
        player_ace = True
        card_value = 11
    player_score += card_value
    # when we bust
    if card_value > 21 and player_ace:
        player_score -= 10
        player_ace = False
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Krupier cipa przegral")


mainWindow = tkinter.Tk()

# set up a screen and frames
mainWindow.title("Czarny Jacek")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")


result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# dealer
dealer_score_label = tkinter.IntVar()
dealer_score = 0
dealer_ace = False
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to whole the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player
player_score_label = tkinter.IntVar()
player_score = 0
player_ace = False

tkinter.Label(card_frame, text="player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame to whole the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# buttons frame
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
print(cards)

# create list of cards randomly
deck = list(cards)
random.shuffle(deck)

# create list to store dealers and players cards
dealer_cards = []
player_cards = []

mainWindow.mainloop()

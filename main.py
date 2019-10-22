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
        score += card_value
        # when we bust
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    player_score = score_hand(player_hand)
    # the brain of dealer
    while (0 < dealer_score < 17) or dealer_score < player_score:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    if player_score > 21:
        result_text.set("Dealer wins")
    elif dealer_score > 21 or player_score > dealer_score:
        result_text.set("Player wins")
    elif dealer_score > player_score:
        result_text.set("Dealer wins")
    else:
        result_text.set("Push")


def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer wins")


# function that creates new game
def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand

    # reset dealer position
    dealer_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

    # reset player position
    player_card_frame.destroy()
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

    result_text.set("")

    # create list to store dealers and players cards
    dealer_hand = []
    player_hand = []

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))


mainWindow = tkinter.Tk()

# set up a screen and frames
mainWindow.title("Black Jack 1.1")
mainWindow.geometry("840x450")
mainWindow.configure(background="green")

background_image = tkinter.PhotoImage(file='files/background.png')
background_label = tkinter.Label(mainWindow, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)


# # embedded frame to whole the card images
# def dealer_frame():
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player
player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
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

player_button = tkinter.Button(button_frame, text="New game", command=new_game)
player_button.grid(row=0, column=2)

# load cards
cards = []
load_images(cards)
print(cards)

# create list of cards randomly
deck = list(cards) + list(cards) + list(cards)
random.shuffle(deck)

new_game()

mainWindow.mainloop()

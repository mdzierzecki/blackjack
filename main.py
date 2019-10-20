import tkinter
import random

print(tkinter.TclVersion)
print(tkinter.TkVersion)

mainWindow = tkinter.Tk()


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


# set up a screen and frames
mainWindow.title("Czarny Jacek")
mainWindow.geometry("640x480")
mainWindow['padx'] = 10

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)
card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# dealer
dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, text=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embedded frame to whole the card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

# player
player_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, text=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embedded frame to whole the card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# buttons frame
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tkinter.Button(button_frame, text="Dealer").grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text="Player").grid(row=0, column=1)

# load cards
cards = []
load_images(cards)
print(cards)

# create list of cards randomly
deck = cards
random.shuffle(deck)

# create list to store dealers and players cards
dealer_cards = []
player_cards = []

mainWindow.mainloop()

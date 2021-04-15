import random
from IPython.display import clear_output
keep_play = True
dealer_want_cont = True
bank = 5000
won_the_bet = ""



def make_the_cards():
    int_cards = [2,3,4,5,6,7,8,9,10,10,10,10, 11] * 4
    random.shuffle(int_cards)
    return int_cards


def start_game():
    start = input("Do you want to start the game?").lower()
    if start.startswith("y"):
        return True
    elif start.startswith("n"):
        return False
    
def first_cards():
      
    player1 = []
    dealer = []
    while len(player1) < 2 and len(dealer) < 2:
        
        dealer.append(int_cards[-1])
        int_cards.pop()
        
        player1.append(int_cards[-1])
        int_cards.pop()

    return int_cards, player1, dealer

def display_hand(): 
    print(f"Player's hand: {player1}")
    print(f"Dealer's hand: {dealer}\n")

def player1_cont():
    draw = input("Do you want to draw one more card?").lower()
    if draw.startswith("y"):
        return True
    elif draw.startswith("n"):
        return False
    
def dealer_cont():
    if sum(dealer) <= sum(player1) and sum(dealer) < 17 and sum(player1) < 21:
        return True
    else:
        return False 

def give_player1_card():
    if player1_want_cont == True:
        player1.append(int_cards[-1])
        int_cards.pop()
    return int_cards, player1

def give_dealer_card():
    if dealer_want_cont== True:
        dealer.append(int_cards[-1])
        int_cards.pop()
    return int_cards, dealer
    
def bust():
    busted = 1
    if sum(dealer) > 21:
        print(f"Dealer got bust at: {sum(dealer)}, player wins\n")
        return False
    elif sum(player1) > 21:
        print(f"Player got bust at: {sum(player1)}, dealer wins\n")
        return False
    else:
        return True
def check_jackpot():
    if sum(player1) == 21:
        print("Player hit jackpot! and wins")
        return False
    if sum(dealer) == 21:
        print("Dealer hit jackpot! and wins")
        return False
    return True
def check_winner():
    if sum(player1) > 21 and sum(dealer) > 21:
        print("no one has won")
        return ""
    elif sum(player1) < sum(dealer) and sum(dealer) < 21 :
        print(f"Dealer has won at: {sum(dealer)} against player {sum(player1)}")
        return "dealer"
    elif sum(player1) > sum(dealer) and sum(player1) < 21:
        print(f"Player has won at: {sum(player1)} against dealer {sum(dealer)}")
        return "player1"
    elif sum(player1) == sum(dealer):
        print("its a tie")
        return ""
    elif sum(player1) > 22:
        print(f"Dealer has won at: {sum(dealer)} against player {sum(player1)}")
        return "dealer"
    elif sum(dealer) > 22:
        print(f"Player has won at: {sum(player1)} against dealer {sum(dealer)}")
        return "player1"
        
def change_ace_player():
    for i in player1:
        if i == 11:
            player1[player1.index(i)] = 1
    return player1
def change_ace_dealer():
    for i in dealer:
        if i == 11:
            dealer[dealer.index(i)] = 1
    return dealer

def play_again():
    play = input("Do you want to play again?").lower()
    if play.startswith("y"):
        return True
    elif play.startswith("n"):
        return False
    
def bet():
    bank2 = bank
    curent_bet2 = curent_bet
    if won_the_bet == "player1":
        bank2 += curent_bet
        return bank2
    elif won_the_bet == "":
        return bank2
    else:
        bank2 = bank2 - curent_bet
        return bank2
    
def amount_betted():
    '''
    returnar beloppet som spelaren vill satsa
    '''
    while True:
        try:   
            curent_bet2 = int(input("Enter your bet: "))
            if curent_bet2 > bank:
                print("you don't have that kind of money...")
            else:
                return curent_bet2
        except:
            print("Only numbers")



        
        
play = True

while play == True: 
    curent_bet = amount_betted()
    int_cards = make_the_cards() #görkorten
    int_cards, player1, dealer = first_cards() #dealer ut de första korten till båda
    display_hand() # visar korten
    keep_play = check_jackpot()
    if keep_play == True:
        player1_want_cont = player1_cont() # frågar spelaren om den vill fortsätta
        int_cards, player1 = give_player1_card() # ger seplaren kot 
        player1 = change_ace_player() # kollar efter ess
        keep_play = bust()
        if keep_play == True:
            keep_play = check_jackpot()
        display_hand()
    if keep_play == True:
        keep_play = check_jackpot()
        if keep_play == False:
            dealer_want_cont = False
            
    dealer_want_cont = dealer_cont()       
    while keep_play == True or dealer_want_cont == True:
        while player1_want_cont == True and keep_play == True: 
            player1_want_cont = player1_cont()
            int_cards, player1 = give_player1_card()
            display_hand()
            keep_play = bust()
            if keep_play == True:
                keep_play = check_jackpot()
                if keep_play == False:
                    dealer_want_cont = False
        if dealer_want_cont == True:
            dealer = change_ace_dealer()
            dealer_want_cont = dealer_cont()
            while dealer_want_cont == True:
                int_cards, dealer = give_dealer_card()
                dealer_want_cont = dealer_cont()
                display_hand()
                if keep_play == True:
                    keep_play = bust()
                    if keep_play == True:
                        keep_play = check_jackpot()
        else: 
            keep_play = False
    won_the_bet = check_winner()
    bank = bet()
    print(f"\nBank: {bank}$")
    if bank <= 0:
        keep_play = False
        print("You are broke!\nYou can not play again")
        break
    print("")
    play = play_again()
    clear_output(wait = True)
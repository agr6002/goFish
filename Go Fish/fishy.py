import random
cards = ["A", "A", "A", "A", "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J", "10", "10", "10", "10", "9", "9", "9", "9", "8", "8", "8", "8", "7", "7", "7", "7", "6", "6", "6", "6", "5", "5", "5", "5", "4", "4", "4", "4", "3", "3", "3", "3", "2", "2", "2", "2"]
computer_hand= []
player_hand = []
computer_matches = []
player_matches = []

def deal():
    for i in range(5) :
        computer_hand.append(cards.pop()) 
        player_hand.append(cards.pop()) 
def shuffle():
    random.shuffle(cards)
def match():
    for i in range(len(computer_hand)- 2):
        for j in range(i+ 1, len(computer_hand)-1):
            if computer_hand[i] == computer_hand[j]:
                computer_matches.append(computer_hand[i])
                del computer_hand[i]
                del computer_hand[j]
    for i in range(len(player_hand)- 2):
        for j in range(i + 1, len(player_hand)-1):
            print(i)
            print(j)
            if player_hand[i] == player_hand[j]:
                player_matches.append(player_hand[i])
                del player_hand[i]
                del player_hand[j]
def IsMatchPlayer(card):
    Match = False
    for i in range(len(computer_hand) -2):
        if computer_hand[i] == card:
            Match = True
            player_matches.append(card)
            del computer_hand[i]
            player_hand.remove(card)
            print("You got a match")
    if Match == False:
        print("Go Fish")
        player_hand.append(cards.pop()) 
def IsMatchComputer():
    Match = False
    card = random.choice(computer_hand)
    for i in range(len(player_hand) -2):
        if player_hand[i] == card:
            Match = True
            computer_matches.append(card)
            del player_hand[i]
            computer_hand.remove(card)
            #print(card)
    if Match == False:
        computer_hand.append(cards.pop()) 



shuffle()
deal()
#print(computer_hand)
#print(player_hand)
match()
#print(computer_hand)
#print(computer_matches)
print(player_hand)
print(player_matches)
if int(len(player_hand)) != 0:
    if int(len(computer_hand)) != 0 :
        player_move = input("What is your card?")
        IsMatchPlayer(player_move)
        IsMatchComputer()
        print(player_hand)
        print(player_matches)
        #print(computer_hand)
        #print(computer_matches)



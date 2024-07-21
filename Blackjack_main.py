import random
import os

from logo import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0 #blackjack
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def checkifgameover(user_score,comp_score):
    if comp_score==0:
        return True
    elif user_score==0:
        return True
    elif user_score > 21:
        return True
        
def compare_scores(user_score,comp_score):
    
    if(comp_score==user_score):
        print("Its a Draw :(")
    elif(comp_score==0):
        print("Computer Wins")
    elif(user_score==0):
        print("You Win :) ")
    elif(user_score>21):
        print("You Lose")
    elif(comp_score>21):
        print("You Win!!")
    elif(user_score>comp_score):
        print("You Win!!!")
    else:
        print("Computer Wins :(")
        
choice = "y"
while choice == "y":  
    os.system('cls')  
    print(logo)
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    print(f"User Cards:{user_cards[0],user_cards[1]}")
    print(f"Computer Cards:{computer_cards[0]}")
    
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)
    
    print(f"User Score:{user_score}")
    
    over=checkifgameover(user_score,comp_score)
    
    while not over:
        
        new_card=input("Do You Want to Draw Another Card?y/n?")
        
        if(new_card.lower()=="y"):
            user_cards.append(deal_card())
            user_score=calculate_score(user_cards)
            over=checkifgameover(user_score,comp_score)
        elif(new_card.lower()=="n"):
            while(calculate_score(computer_cards)<17):
                computer_cards.append(deal_card())
                comp_score=calculate_score(computer_cards)
            over=True   
    compare_scores(user_score,comp_score)
    print(f"Final User Cards: {user_cards}, score: {user_score}")
    print(f"Final Computer Cards: {computer_cards}, score: {comp_score}")
    choice = input("Do you want To restart the game?y/n?").lower()
        

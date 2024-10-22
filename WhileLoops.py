### Part Two -- your code goes here. 
import random

x = random.randint(1, 100)

def intro():
    print("Hello, I'm TRON! Shall we play a game?!")
    print("Enter YES or NO")
32

    z = input().upper()

    if z == "YES":
        print("YAY! LET'S GO!")
        game() 
    elif z == "NO":
        print("AWW...Another time then...")
    else:
        print("Invalid input. Please enter YES or NO.")
        intro()

def game():
    while True:
        y = input("Start! Guess the number Tron is thinking (between 1 and 100): ")
        y = int(y)
        if y < x:
            print("Nahh it's higher. Try again.")
        elif y > x:
            print("Nope it's lower. Try again.")
        else:
            print(f"That's Crazy! YOU WON!! The number was {x}.")
            break 

intro()

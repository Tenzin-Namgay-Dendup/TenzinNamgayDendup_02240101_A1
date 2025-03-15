print("Do you want to play one game")
Owner = input ("Press start :")

import random

def guess_number_game():
    answer = random.randint(1,100) # Generate a random number between 1 to 100
    chance = 0
    
    while chance < 3:
         
         try:
            guess = int(input("Guess a number between 1 and 100: "))
         except ValueError:
            print("Invalid input! Please enter a number.")
            #Ask for input again
         
         if guess > answer:
            print("Go little lower")
            # retuen a function immediately 
         elif guess < answer :
            print (" Go little higher")
         else:
            print("You Won!")
            break

         chance += 1
    print (f"Game Over. The correct answer was {answer}.")
    




import random

def rock_paper_scissor_game():
    while True:
        player = input("Choose one: [rock, paper, scissor]: ")
        choices = ["rock", "paper", "scissor"]
        robot = random.choice(choices)


        print(f"You choose : {player}")
        print(f"Robot choose : {robot}")
        

        if player == robot:
            print("Tie....")

        elif player == "rock":
            if robot == "scissor":
                print("You win")
            else:
                print("You lose")

        elif player == "paper":
            if robot == "rock":
                print("You win")
            else:
                print("You lose")

        elif player == "scissor":
            if robot == "paper":
                print("You win")
            else:
                print("You lose")
        break
        
           

def main():
    
     while True:
        print("\nMenu:")
        print("select a function (1-3)")
        print("1. Guess number game")
        print("2. Rock Paper Scissors game with robot ")
        print("3. Do you want to exit")
    
        
        choice = input("Select a game that you wish to play : ")

        if choice == '1':
            print("starting the Guess number game")
            guess_number_game()
            
        
        elif choice == '2':
            print("Starting the Rock Paper Scissor game")
            rock_paper_scissor_game()

        elif choice == '3':
            print("Thank you for playing....Goodbye!")
        else : 
            print("invalid")
        choice = input("Do you want to continue playing (yes/no) : ")
        if choice != 'yes': 
            print("THANK YOU! ")
            break
        

if __name__ == "__main__":
    main()
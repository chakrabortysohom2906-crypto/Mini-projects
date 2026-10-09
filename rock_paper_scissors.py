import random
# display rule
print("This is ROCK --> ✊")
print("this is paper --> 🖐️")
print("this is scissor --> ✌️")
print("--- This are the playing rules ---")
print("Rock defeats Scissors.(✊ x ✌️  = ✊)")
print("Scissors defeats Paper.(✌️  x 🖐️  = ✌️  )")
print("Paper defeats Rock.(🖐️  x ✊ = 🖐️  )")
print("If both players choose the same option, the round ends in a draw.")

choice=["rock","paper","scissor"]

while True:
    print("---Enter your choice from bellow---")
    print("1. rock")
    print("2. paper")
    print("3. scissor")
    print("4. Quit game")
# Accept the user's choice.
    x = int(input("enter your choice between(1,2,3,3" \
    "4):"))

# if dosenot want to paly more.
    if x == 4:
        print("thanks for playing.Goodbye.")
        break
# Validate the input and ensure it is within the allowed options.
    if x not in [1,2,3]:
        print("please enter a valid choice.")
        continue
    user_choice = choice[x-1]
# this is the random choice generater
    y = random.randint(0,2)
    computer_choice = choice[y]
    print("this is your choice:",user_choice)
    print( "this is computer choice:",computer_choice)

# comparition of both choice
# game draw situation 
    if user_choice == computer_choice:
        print("It is a draw.")
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print("--> YOU WIN <--")
    else:
        print("--> COMPUTER WIN <--")
# ask to repeat the game
    ans = input("you want to play the game again(y/n):")
    if ans == 'n':
        break
    print()
print()
print("thanks for playing.goodbye!")
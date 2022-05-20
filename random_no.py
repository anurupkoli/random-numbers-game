import random

comp = random.randint(1, 100)
name = input("Enter your name CHAMP: ")
result = False
no_turns = 0

try:
    while result != True:
        player = int(input(f"{name},Guess the number between 1-100: "))
        if player > comp:
            print(f"{name},Lower number please")
            result = False
        elif player < comp:
            print(f"{name},Higher number please number please")
            result = False
        elif player == comp:
            print(
                f"Congratulations {name},you guessed it right!!!\nNumber was {comp}")
            result = True
        no_turns += 1

    

    print(f"{name},You took {no_turns} guesses to win!!!")

    with open("High_score.txt") as f:
        score = int(f.read())
        if no_turns < score:
            print(f"You are a Hero {name}, you just broke a high record!!!")
            with open("High_score.txt", "w") as f:
                f.write(str(no_turns))
        elif no_turns == score:
            print(
                f"{name}You were close to brake High record!!\nCurrent High record is {score} guesses")

    print(f"Thankyou for Playing {name} :)")
except :
    print("Please Enter a valid number")


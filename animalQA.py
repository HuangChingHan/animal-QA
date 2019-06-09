def check_answer(guess, answer):
    global score
    still_guess = True
    count = 0
    while still_guess and count < 3:
        if guess.lower() == answer.lower():
            print("correct!")
            score = score + 1
            still_guess = False
        else:
            if count < 2:
                guess = input("Try again.")
            count = count + 1

    if count == 3:
        print("The correct answer is " + answer)
          
score = 0
print("Guess the Animal!")

guess1 = input("Which bear lives at the North Pole?")
check_answer(guess1, "polar bear")
guess2 = input("Which is the fastest land animal?")
check_answer(guess2, "cheetah")
guess3 = input("Which is the largest animal?")
check_answer(guess3, "blue whale")       

print("Your score is " + str(score))

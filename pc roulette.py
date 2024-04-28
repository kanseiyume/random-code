'''

"buckshot roulette your pc"

'''

import sys, os, random, time

def clearTerm():
    os.system('cls' if os.name == 'nt' else 'clear')

def roulette():
    print("are you sure about this? (type 'yes' to continue)")
    response = input()
    if response == "yes":
        print("alright then")
        time.sleep(2)
        clearTerm()
        print("1 live, 5 blanks")
        time.sleep(2)
        round = random.randint(1, 6)
        print("pick a number between 1 and 6")
        # print("the live is currently chambered at number " + str(round))
        choice = input()
        if int(choice) > 6 or int(choice) < 1:
            print("you're not very good at following instructions, are you?")
            time.sleep(2)
            clearTerm()
            sys.exit()
        if int(choice) == round:
            # os.remove("C:/Windows/System32")
            print("you would've died")
        else:
            print("good job")
            time.sleep(2)
            clearTerm()
while True:
    roulette()
    print("play again? (type 'yes' to continue)")
    response = input()
    if response != "yes":
        print("smart.")
        time.sleep(2)
        clearTerm()
        sys.exit()
    clearTerm()
    continue

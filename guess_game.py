import cowsay
from morsell import details, quitting_tab
from random import randint

def lucky_guess():
    return randint(1, 5)

def main():
    details()
    game_guess()

def game_guess():
    number_one = lucky_guess()

    while True:
        try:
            number = int(input("What's your guess number? "))
        except ValueError:
            cowsay.daemon("I only need integers inserted kindly")
            continue

        if number == number_one:
            print("\nCongratulations::::::You got the number right!!!!! Hurray!!!!\n")
            wishing_part()
            break
        else: 
            print(f"\nIt was only ONE TRIAL ATTEMPT! Sorry, the correct number was {number_one}.\n")
            wishing_part()
            break

def wishing_part():
    wish = input("\nWish to continue playing? (Y or N): \n")
    if wish.upper() in ["Y", "YES"]:
        print("\nSure thing, I will replay the game once more!!!\n")
        game_guess()
    elif wish.upper() in ["N", "NO"]:
        quitting_tab()
    else:
        print("Please respond with Y or N.")
        wishing_part()

if __name__ == "__main__":
    main()

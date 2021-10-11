import time

print("Welcome to the Adventure Game!\n\n")

name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 12:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()

    if (wants_to_play == "yes") or (wants_to_play == "y"):
        print("Starting...\n")
        time.sleep(1)  # Adding delays for extra effects
        print("Please wait!")
        time.sleep(1)
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1

        print("\nYou are staring with", health, "health.")
        print("Let's play!\n")

        time.sleep(2)

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            ans = input(
                "\nNice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou went around and reached the other side of the lake.")
            elif ans == "across":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou managed to get across, but were bit by a fish.")
                print("You lose 5 health.")
                health -= 5

            ans = input(
                "\nYou notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print(
                    "\nYou go to the house and are greeted by the owner... He doesn't like you and hits you with a stick.")
                print("You lose 5 health.")
                health -= 5

                if health <= 0:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1

                    print("\nYou now have 0 health and you lost the game...")
                else:
                    count = 0
                    while count != 5:
                        print(".", end="")
                        time.sleep(2/5)
                        count += 1

                    print("\nYou have survived... You win!")

            else:
                count = 0
                while count != 5:
                    print(".", end="")
                    time.sleep(2/5)
                    count += 1

                print("\nYou fell in the river and die...")

        else:
            count = 0
            while count != 5:
                print(".", end="")
                time.sleep(2/5)
                count += 1

            print("\nYou enter a jungle and get eaten by a bear...")

    else:
        print("\nExiting...")
        count = 0
        while count != 5:
            print(".", end="")
            time.sleep(2/5)
            count += 1
        print()

else:
    print("\nYou are not old enough to play...")
    print("\nExiting...")
    count = 0
    while count != 5:
        print(".", end="")
        time.sleep(2/5)
        count += 1
    print()
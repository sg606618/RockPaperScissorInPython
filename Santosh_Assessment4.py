# Create a Simulation for Rock Paper Scissors | Assessment 4

import random


class HumanVsComputer:
    def __init__(self, selection, computer_selection):
        self.selection = selection
        self.computer_selection = computer_selection
        self.enter = int(
            input("\n1. For Rock \n2. For Paper \n3. For Scissor \nChoose Your Number ::: "))

    def result(self):
        print(
            f"Your input ::: {self.selection[self.enter]} \nand Computer is {self.selection[self.computer_selection]}")

        user_choice = self.selection[self.enter]
        computer_choice = self.selection[self.computer_selection]

        if user_choice == computer_choice:
            return "Draw"
        elif (user_choice == "Rock" and computer_choice == "Scissor") or (user_choice == "Scissor" and computer_choice == "Paper") or (user_choice == "Paper" and computer_choice == "Rock"):
            return "Bravo!! You Win."
        else:
            return "Boo!!! You Lose."


class ComputerVsComputer:
    def __init__(self, selection, first_comp, second_comp):
        self.selection = selection
        self.first_comp = first_comp
        self.second_comp = second_comp

    def result(self):
        print(
            f"First Computer input ::: {self.selection[self.first_comp]} \nand Second Computer is {self.selection[self.second_comp]}")

        first_computer_choice = self.selection[self.first_comp]
        second_computer_choice = self.selection[self.second_comp]

        if first_computer_choice == second_computer_choice:
            return "Draw"
        elif (first_computer_choice == "Rock" and second_computer_choice == "Scissor") or (first_computer_choice == "Scissor" and second_computer_choice == "Paper") or (first_computer_choice == "Paper" and second_computer_choice == "Rock"):
            return "First Computer Win"
        else:
            return "Second Computer Win"


print("You have 3 options below just press one of the numbers to play the game:::")


def play_game():

    select = {1: "Rock", 2: "Paper", 3: "Scissor"}
    comp_select = random.randint(1, 3)

    first_comp_select = random.randint(1, 3)
    second_comp_select = random.randint(1, 3)

    try:
        condition = int(input(
            "1. Play with Computer \n2. Just sit and watch playing Computer \n3. To EXIT \n"))

        match condition:
            case 1:
                print("\nYou are now playing with computer ::: ")
                print(HumanVsComputer(select, comp_select).result())
            case 2:
                print("\nJust sit and watch computer gameplay :::\n\n")
                print(ComputerVsComputer(
                    select, first_comp_select, second_comp_select).result())
            case 3:
                exit()
            case _:
                print("\nYour input is invalid !!!! Try again...")
                play_game()

    except ValueError as ve:
        print("\nYour input is invalid !!!! Try again...")
        play_game()
    except Exception as e:
        print(e)


play_game()

# Import necessary modules
import random
import os
from time import sleep
from simple_term_menu import TerminalMenu
from colorama import Fore, Style
from art import *

# CONSTANTS
# Define the colors used in the game
COLORS = ["R", "G", "B", "Y", "W", "O"]


def print_welcome_message():
    """ Display a welcome message """
    os.system('clear')
    print(f"""
    {Fore.RED + logo}
    {Style.RESET_ALL}      Select an option from the menu below:
    """)


print_welcome_message()


def display_rules():
    """ Display the rules of the game """
    os.system('clear')
    print(f"""
    {Fore.RED + rules}
    {Style.RESET_ALL}
1. The computer will generate a secret code consisting of a
   sequence of colors.
2. Your task is to guess the code.
3. You have a limited number of tries to guess the code.
4. After each guess, you will receive feedback on the correctness
   of your guess.
   - 'Correct Positions'
      indicates the number of colors in the correct positions.
   - 'Incorrect Positions'
      indicates the number of correct colors in the wrong positions.
5. The game ends when you correctly guess the code or run out of tries.
   The colors are Red, Green, Blue, Yellow, White and Orange.
   Good luck!
    """)


def display_levels():
    """
    Display the levels of the game in the menu.
    every level has its own part and there is an option
    for back.
    """
    os.system('clear')
    print(f"""
    {Fore.RED + lvls}
    {Style.RESET_ALL}  Select a difficulty level:
    """)
    # Define level items
    level_items = [
        "Easy - 15 tries, code length 4",
        "Medium - 10 tries, code length 4",
        "Hard - 10 tries, code length 5",
        "Back"
    ]
    # Create a level menu object
    level_menu = TerminalMenu(level_items)
    # Show the level menu and get the user's selection
    level_entry_index = level_menu.show()

    print(level_entry_index)
    # Handle user selection.
    # First number = TRIES, second number = LENGTH
    if level_entry_index == 0:
        return 15, 4
    elif level_entry_index == 1:
        return 10, 4
    elif level_entry_index == 2:
        return 10, 5
    elif level_entry_index == 3:
        print_welcome_message()
        return None, None


def main_menu():
    """
    Displays the menu.
    Rules
    Start - With levels later
    Quit
    """
    # Define menu items
    menu_items = ["Rules of MasterMind", "Start MasterMind", "Quit"]
    # Create a menu object
    menu = TerminalMenu(menu_items)
    # Show the menu and get the user's selection
    menu_entry_index = menu.show()

    # Handle user selection
    if menu_entry_index == 0:
        display_rules()
        input("Press any key to return to menu.")
    elif menu_entry_index == 1:
        tries, code_length = display_levels()
        if tries is not None and code_length is not None:
            game(tries, code_length)
    elif menu_entry_index == 2:
        os.system('clear')
        print("Quiting...")
        quit()


def generate_code(code_length):
    """
    Generate a random code of specified length from the list of colors
    and returns it
    """
    code = [random.choice(COLORS) for _ in range(code_length)]
    return code


def guess_code(code_length):
    """
    Player / Users guess.
    The player makes a guess until they guess a valid color.
    They guess a color based on the current loop index.
    If they guess a valid color, it is added to the list of guessed colors.
    The current state of the guess is displayed, including placeholders
    for the remaining colors.
    Once a valid color is guessed, the loop ends.
    """
    guess = []
    for _ in range(code_length):
        while True:
            color = input(f"Guess color {_ + 1}: ").upper()
            if color in COLORS:
                guess.append(color)
                # This is the magic!
                print(
                    f"[ {' '.join(guess)}{' - '* (code_length - len(guess))} ]"
                )
                break
            else:
                # ERROR on invalid letter
                print(f"""
                Invalid color: {color}. Try again.
                The valid colors are", {COLORS}
                """)
    return guess


def check_code(guess, real_code, tries):
    """
    Checks code 'guess' against 'real_code'
    First for loop counts occurrences of each
    color in the real code

    Second loop checks guess against real_code for
    correct posstion.

    Third for incorrect.
    """
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    # zip is used to check two lists guess and real_code in parallel.
    for guess_color, real_color in zip(guess, real_code):
        # If the guessed color are in correct posstion
        if guess_color == real_color:
            # correct pos +1
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        # if color real, but place wrong
        if guess_color != real_color and guess_color in \
                color_counts and color_counts[guess_color] > 0:
            # incorrect pos +1
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    # Print feedback on the guess Clear screen
    os.system('clear')
    print(f"""You have {tries} tries left.

Guess: {guess}
Correct Positions: {correct_pos} | Incorrect Positions: {incorrect_pos}.
    """)


def game(tries, code_length):
    """ HERE BE GAME! """
    os.system('clear')
    print(f"""Test your skill.

You have {tries} tries to guess the code using {code_length} colors...

The valid colors are, {COLORS}
""")
    # Generate the code - colors lenght
    real_code = generate_code(code_length)
    # Iterate through the allowed number of tries
    for attempts in range(1, tries + 1):
        # Get the player's guess
        guess = guess_code(code_length)
        # Check the guess against the real code
        # Here we also have tries - attempts for the counter
        check_code(guess, real_code, tries - attempts)
        # Check if the guess is correct
        if sorted(guess) == sorted(real_code):
            os.system('clear')
            print(f"""
            {Fore.YELLOW + win}
You guessed the code in {attempts} tries!
           A real MasterMind
            """)
            break

    # If the player runs out of tries, display the correct code
    else:
        os.system('clear')
        print(f"""
        {Fore.RED + lose}
You ran out of tries, the code was", {real_code}
        """)


# Main entry point of the game
if __name__ == "__main__":
    while True:
        main_menu()

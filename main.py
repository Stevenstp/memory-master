"""
main.py - Entry point for MemoryMaster.

Run this file to start the game:
    python main.py
"""

from game import MemoryMasterGame


def get_mode():
    """
    Ask the player to pick a game mode and return their choice.

    Returns:
        str: 'numbers', 'phrases', or 'pictures'
    """
    print("Choose a game mode:")
    print("1. Numbers - Remember a sequence of digits")
    print("2. Phrases - Remember a list of words in order")
    print("3. Pictures - Remember character pattern")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return "numbers"
    elif choice == "2":
        return "phrases"
    elif choice == "3":
        return "pictures"
    else:
        print("Invalid choice, defaulting to numbers")
        return "numbers"


def get_difficulty():
    """
    Ask the player to pick a difficulty and return their choice.

    Returns:
        str: 'easy', 'medium', or 'hard'
    """
    pass


if __name__ == "__main__":
    mode = get_mode()
    difficulty = get_difficulty()

    game = MemoryMasterGame(mode=mode, difficulty=difficulty)
    game.run()

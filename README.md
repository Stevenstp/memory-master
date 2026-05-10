# MemoryMaster

A command-line memory game where you memorize and recall numbers, words, or patterns before the screen clears.

## How to Run

Make sure Python 3 is installed. No extra packages needed. Run this from inside the memory-master folder:

python main.py

## How to Play

1. Pick a mode:
   - Numbers - memorize a sequence of digits
   - Phrases - memorize a list of words in order
   - Pictures - memorize a grid of symbols

2. Pick a difficulty:
   - Easy - 5 seconds to memorize
   - Medium - 3 seconds to memorize
   - Hard - 1.5 seconds to memorize

3. Memorize what's on screen before it disappears
4. Type it back correctly to advance to the next level
5. Get it wrong and the game ends — your high score is saved automatically

## Sources

Python Software Foundation. random - Generate pseudo-random numbers.
https://docs.python.org/3/library/random.html
Used for random.randint() in number_generator.py to generate random digits, random.sample() in word_generator.py to pick unique words, and random.choice() in pattern_generator.py to pick random symbols.

Python Software Foundation. os - Miscellaneous operating system interfaces.
https://docs.python.org/3/library/os.html
Used for os.path.exists() in score_tracker.py to check if the high score file exists, and os.system() in game.py to clear the terminal screen.

Python Software Foundation. time - Time access and conversions.
https://docs.python.org/3/library/time.html
Used for time.sleep() in game.py to control how long the challenge stays on screen before it disappears.

Python Software Foundation. unittest - Unit testing framework.
https://docs.python.org/3/library/unittest.html
Used to write and run all the unit tests in test_memory_master.py.

GeeksforGeeks. Random Module in Python.
https://www.geeksforgeeks.org/python-random-module/
Referenced for examples of how to use random.sample() when building the word list generator.
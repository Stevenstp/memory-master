"""
pattern_generator.py - Generates ASCII patterns for MemoryMaster pictures mode.
"""

import random

SYMBOLS = ["#", "@", "*", "+", "=", "%", "&", "?", "!", "~"]


def generate_pattern(rows, cols):
    """Create a grid of random symbols as a list of strings."""
    if rows < 1 or cols < 1:
        raise ValueError("rows and cols must be at least 1")
    pattern = []
    for i in range(rows):
        row = ""
        for j in range(cols):
            row += random.choice(SYMBOLS)
        pattern.append(row)
    return pattern 


def format_pattern(pattern):
    """Return the pattern as a printable string with spaces between characters."""
    result = ""
    for row in pattern:
        result += " ".join(row) + "\n"
    return result.strip()


def check_pattern_answer(target, answer):
    """Return True if the player's answer matches the pattern, False if not."""
    answer_rows = [row.replace(" ", "") for row in answer.strip().splitlines()] # removes spaces from answer  
    target_rows = [row.replace (" ", "") for row in target] # removes spaces from target 
    return answer_rows == target_rows # check if they match 


def get_pattern_size(level):
    """Return the (rows, cols) grid size for a given level."""
    if level < 1: 
        raise ValueError("level must be at least 1")
    if level <= 3: 
        return(1, level + 1) # levels 1-3 are one row that gets wider 
    rows = min((level - 1) // 3 + 1, 4) # adds a new row every 3 levels, max 4 rows 
    cols = ((level-1) % 3) + 2 # cycles columns between 2 and 4 
    return (rows, cols)
    
    
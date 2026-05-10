"""
test_memory_master.py - Unit tests for MemoryMaster.
"""

import unittest
import os
import tempfile 

from number_generator import generate_number
from word_generator import generate_word_list, check_word_list_answer
from pattern_generator import generate_pattern, check_pattern_answer, get_pattern_size
from score_tracker import ScoreTracker
from game import MemoryMasterGame


class TestNumberGenerator(unittest.TestCase):

    def test_correct_length(self):
        for digits in range(1, 8):
            self.assertEqual(len(generate_number(digits)), digits)

    def test_returns_string(self):
        self.assertIsInstance(generate_number(3), str)

    def test_no_leading_zero(self):
        self.assertNotEqual(generate_number(4)[0], "0")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            generate_number(0)


# rest of tests still need to be written

class TestWordGenerator(unittest.TestCase):

    def test_correct_count(self):
        # should return exactly the number of words we ask for 
        self.assertEqual(len(generate_word_list(3)), 3)

    def test_correct_answer(self):
        # typing the right words in order should return True 
        self.assertTrue(check_word_list_answer(["apple", "bridge"], "apple bridge"))


class TestPatternGenerator(unittest.TestCase):

    def test_correct_rows_and_cols(self):
        # pattern should have the right number of rows and columns 
        p = generate_pattern(2, 3)
        self.assertEqual(len(p), 2)
        self.assertTrue(all(len(row) == 3 for row in p))
                            
    def test_correct_pattern_answer(self):
        # typing the pattern exactly right should return True 
        self.assertTrue(check_pattern_answer(["#@", "*+"], "#@\n*+"))


class TestScoreTracker(unittest.TestCase):

    def test_starts_at_zero(self):
        # return 0 when there's no file yet 
        self.assertEqual(self.tracker.get_high_score(), 0)
        
    def test_saves_high_score(self):
        # saving score should store it correctly 
        self.tracker.save_score(100)
        self.assertEqual(self.tracker.get_high_score(), 100)


class TestGame(unittest.TestCase):

    def test_starts_at_level_1(self):
        g = MemoryMasterGame()
        self.assertEqual(g.level, 1)
        
    def test_advance_level(self):
        g = MemoryMasterGame()
        g.advance_level()
        self.assertEqual(g.level, 2)
        self.assertGreater(g.score, 0)


if __name__ == "__main__":
    unittest.main()
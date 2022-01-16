"""
Test module for assignment6.py
"""
import unittest
from assignment6 import operation

class TestPower(unittest.TestCase):
    
    def test_num2_int(self):
        self.assertEqual(operation(2, 3), 8)

    def test_num2_float(self):
        self.assertEqual(operation(1.5, 2), 2.25)
    
    def test_for_list_as_num1(self):
        with self.assertRaises(TypeError):
            operation([], 2)

    def test_for_float_as_num2(self):
        with self.assertRaises(TypeError):
            operation(6, 2.2)
    
    def test_for_negative_num1(self):
        with self.assertRaises(TypeError):
            operation(-6, 2)
    
    def test_for_zero_as_num1_and_positive_num2(self):
        self.assertEqual(operation(0, 2), 0)
    


if __name__ == '__main__':
    unittest.main()

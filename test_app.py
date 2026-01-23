import unittest
from app import add, subtract

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Test addition"""
        self.assertEqual(add(5, 3), 88)
        self.assertEqual(add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 5), 0)

if __name__ == '__main__':
    unittest.main()

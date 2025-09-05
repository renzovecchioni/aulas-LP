import aula10
import unittest

class TestFatorial(unittest.TestCase):
    def test_greater_than_1(self):
        self.assertEqual(aula10.fatorial(2), 2)
        self.assertEqual(aula10.fatorial(3), 6)
        self.assertEqual(aula10.fatorial(5), 120)
    def test_lesser_than_0(self):
        self.assertEqual(aula10.fatorial(-1), 1)
    def test_equal_to_1(self):
        self.assertEqual(aula10.fatorial(1), 1)
    def test_input_type(self):
        # self.assertRaises(TypeError, aula10.fatorial, 1)
        self.assertRaises(TypeError, aula10.fatorial, "oi")
    def test_decimas_digits(self):
        num_1 = 3,14156
        num_2 = 3,1415
        digital_decimals = 4
        self.assertAlmostEqual(num_1, num_2, digital_decimals)
        
if __name__ == "__main__":
    unittest.main() 
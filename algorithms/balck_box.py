import unittest

def _sum(num_1, num_2):
    return num_1 + num_2


class BlackBoxTest(unittest.TestCase):
    #always the function to test have to start with the word test example: test_sum_two_positives


    def test_sum_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = _sum(num_1, num_2)

        self.assertEqual(result, 15)

    def test_sum_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = _sum(num_1, num_2)

        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()

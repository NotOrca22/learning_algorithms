import math
import unittest
class Trip(unittest.TestCase):
    def test_trip(self):
        costs = []
        for i in range(int(input())):
            costs.append(float(input()))

        total = sum(costs)

        perPerson = sum(costs)/len(costs)

        amtPaid = 0

        for i in range(len(costs)):
            if costs[i] - perPerson < 0:
                amtPaid += perPerson - costs[i]
                amtPaid = math.floor(amtPaid*100)/100 # Rounding to 2 decimal places

        self.assertEqual(math.floor(amtPaid*100)/100, 11.99)

if __name__ == "__main__":
    unittest.main()
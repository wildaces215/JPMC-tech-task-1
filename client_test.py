import unittest
from client import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getDataPoint(quotes[0])[3], 120.84)
        self.assertEqual(getDataPoint(quotes[1])[3], 119.775)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        self.assertEqual(getDataPoint(quotes[0])[3], 119.84)
        self.assertEqual(getDataPoint(quotes[1])[3], 119.775)

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_returnRatio(self):
        test_one = [3.45, 6.78]
        self.assertEqual(
            getRatio(test_one[0], test_one[1]), 0.509)

    def test_getRatio_returnStringError(self):
        test_two = ['hello', 0]
        self.assertEqual(
            getRatio(test_two[0], test_two[1]), "Error a varaible is a string")

    def test_getRatio_returnNone(self):
        test_three = [None, None]
        self.assertEqual(
            getRatio(test_three[0], test_three[1]), "A variable is NULL")


if __name__ == '__main__':
    unittest.main()

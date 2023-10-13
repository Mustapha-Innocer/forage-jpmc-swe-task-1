import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            ask_price = float(quote["top_ask"]["price"])
            bid_price = float(quote["top_bid"]["price"])
            actual_price = (ask_price + bid_price) / 2

            _, _, _, price = getDataPoint(quote)

            self.assertEqual(actual_price, price)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            ask_price = float(quote["top_ask"]["price"])
            bid_price = float(quote["top_bid"]["price"])
            actual_price = (ask_price + bid_price) / 2
            _, _, _, price = getDataPoint(quote)
            self.assertEqual(actual_price, price)


  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()

#!/home/python/venv/main/bin/python
import sys
sys.path.append("..")
import unittest
from house_robber.house_robber import HouseRobber

class HouseRobberTest(unittest.TestCase):
  def test_default(self):
    bounty = [1, 2, 3, 1]
    expected = 4
    house_robber = HouseRobber()
    response = house_robber.max_spoils_loop(bounty)
    self.assertEqual(expected, response)

if __name__ == "__main__":
  unittest.main()

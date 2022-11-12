class HouseRobber():
  def max_spoils_loop(self, neighborhood):
    first, second = 0, 0
    for n in neighborhood:
      temp = max(n + first, second)
      first = second
      second = temp
    return second

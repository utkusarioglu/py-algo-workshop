class Node:
    def __init__(self):
        self.value = None
        self.next = None


class NumberReversal:
    def usingInts(self, x: int) -> int:
        if x <= -2**31 or x > 2**31:
            return 0
        reversed = 0
        abs_factor = 1 if x >= 0 else -1
        temp = x * abs_factor
        while temp > 0:
            lastDigit = temp % 10
            temp = temp // 10
            reversed = reversed * 10 + lastDigit
            print(reversed)
        reversed = reversed * abs_factor
        if reversed <= -2**31 or reversed > 2**31:
            return 0
        return reversed

    def usingNodes(self, x: int) -> int:
        """Create a linked list value as the digit value,
        while looping through the number, take notice of what
        digit you are in, and compare it to the max and min
        limits, if any of the digits put you in a position to
        exceed the limits, return 0.
        if not, loop till you create the linked list for the number,
        then do a regular ll reversal and return the result.
        """
        ll = Node()
        sign = 1 if x >= 0 else -1
        curr_x = x * sign
        curr_ll = ll
        while curr_x != 0:
            curr_ll.value = curr_x % 10
            curr_x = curr_x // 10
            new_node = Node()
            curr_ll.next = new_node
            curr_ll = new_node
        reversed = 0
        curr_ll = ll
        max_safe = 2**31 - 1
        min_safe = -2**31
        while curr_ll.next is not None:
            reversed = reversed * 10 + curr_ll.value
            curr_ll = curr_ll.next
            if reversed * sign > max_safe or reversed * sign < min_safe:
                return 0
        return reversed * sign

    def usingMath(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = x * sign
        reversed = 0
        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10
        max_safe = 2**31 - 1
        min_safe = -2**31
        reversed = reversed * sign
        if reversed < min_safe or reversed > max_safe:
            return 0
        return reversed

    def fastest(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        if sign * res < -2**31 or sign * res > 2**31 - 1:
            return 0
        return res * sign

from math import ceil, inf, floor
from statistics import mean


class Koko:
    def brute_force(self, piles: list[int], h: int) -> int:
        """
        there is no upper or lower ran
        """
        piles = sorted(piles)
        if h < len(piles):
            return inf
        if h == len(piles):
            return piles[-1]
        for k in range(1, piles[-1] + 1):
            turns = [ceil(pile/k) for pile in piles]
            total_turns = sum(turns)
            if total_turns == h:
                return k

    def iterative(self, piles: list[int], h: int) -> int:
        upper_bound = max(piles)
        piles_length = len(piles)
        lower_bound = 1

        if piles_length > h:
            return inf
        if piles_length == h:
            return upper_bound
        lower_bound_total = self.compute_total(piles, lower_bound)
        if lower_bound_total <= h:
            return lower_bound

        run_count = 0
        while run_count < 100:
            run_count += 1
            mid = (upper_bound + lower_bound) // 2
            mid_total = self.compute_total(piles, mid)
            if mid_total <= h:
                upper_bound = mid
            if mid_total > h:
                lower_bound = mid
            if upper_bound - lower_bound == 1:
                return upper_bound

    def compute_total(self, piles: list[int], candidate: int) -> int:
        return sum([ceil(pile/candidate) for pile in piles])
        

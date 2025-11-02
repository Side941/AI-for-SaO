import random
from typing import List, Tuple


class Solution:

    def __init__(self, dist_matrix: List[List[float]], N: int, route: List[int] = None):
        self.dist_matrix = dist_matrix
        self.N = N
        self.route = route if route is not None else random.sample(range(N), N)
        self.utility = self.evaluate()

    def evaluate(self) -> float:
        total = 0
        for i in range(self.N):
            total += self.dist_matrix[self.route[i]][self.route[(i + 1) % self.N]]
        return total


def hill_climber(dist_matrix: List[List[float]], N: int, loops: int) -> Tuple[Solution, List[float]]:
  
    current = Solution(dist_matrix, N)
    best_scores = []

    for _ in range(loops):
        # Generate neighbor by swapping two cities
        new_route = current.route.copy()
        i, j = random.sample(range(N), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        neighbor = Solution(dist_matrix, N, new_route)

        # Accept neighbor if better
        if neighbor.utility < current.utility:
            current = neighbor

        best_scores.append(current.utility)

    return current, best_scores

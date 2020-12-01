from itertools import combinations
from typing import List

import numpy as np

with open("01_input", "r") as f:
    data = f.read().splitlines()


def data_to_integers(data: List[str]) -> List[int]:
    return [int(value) for value in data]


def get_product_of_values(data: List[int], num_of_values: int) -> int:
    combs = combinations(data, num_of_values)
    return int([np.prod(comb) for comb in combs if sum(comb) == 2020][0])


if __name__ == "__main__":
    data = data_to_integers(data)
    solution = get_product_of_values(data, 3)
    print(solution)

from dataclasses import dataclass
from math import prod
from typing import List

with open("03_input", "r") as f:
    data = f.read().splitlines()


@dataclass
class Step:
    step_right: int
    step_down: int


class Exercise:
    def __init__(self, data: List[str]) -> None:
        self.data = data

    def solve_second_part(self) -> int:
        steps = [Step(1, 1), Step(3, 1), Step(5, 1), Step(7, 1), Step(1, 2)]
        trees = [
            self.count_trees(step_right=step.step_right, step_down=step.step_down)
            for step in steps
        ]
        return prod(trees)

    def count_trees(self, step_right: int, step_down: int) -> int:
        is_tree_on_the_spot = [
            row[((idx // step_down) * step_right) % len(row)] == "#"
            for idx, row in enumerate(self.data)
            if idx % step_down == 0
        ]
        return sum(is_tree_on_the_spot)


if __name__ == "__main__":
    exercise = Exercise(data)
    trees_counter = exercise.count_trees(step_right=3, step_down=1)
    second_part_result = exercise.solve_second_part()
    print(second_part_result)

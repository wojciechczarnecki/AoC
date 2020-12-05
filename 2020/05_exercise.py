from typing import List, Dict, Optional

with open("05_input", "r") as f:
    data = f.read().splitlines()


def split_rows_and_columns(data: List[str]) -> List[Dict[str, str]]:
    return [{"row": code[:7], "column": code[7:]} for code in data]


class SeatIdsGenerator:
    def __init__(self, data: List[Dict[str, str]]) -> None:
        self.data = data
        self.rows: List[int] = [number for number in range(128)]
        self.columns: List[int] = [number for number in range(8)]
        self.indices: Optional[List[int]] = None

    def get_seat_ids(self) -> List[int]:
        seat_positions = self._generate_seat_positions()
        return [
            seat_position["row"] * 8 + seat_position["column"]
            for seat_position in seat_positions
        ]

    def _generate_seat_positions(self) -> List[Dict[str, int]]:
        return [
            self._generate_idx_of_row_and_column(binary_space_positioning)
            for binary_space_positioning in self.data
        ]

    def _generate_idx_of_row_and_column(
        self, binary_space_positioning: Dict[str, str]
    ) -> Dict[str, int]:
        seat = {}
        for key, value in binary_space_positioning.items():
            if key == "row":
                self.indices = self.rows
            else:
                self.indices = self.columns
            seat[key] = self._find_idx(value)
        return seat

    def _find_idx(self, instruction: str) -> int:
        for char in instruction:
            self._cut_list(char)
        return self.indices[0]

    def _cut_list(self, char: str) -> None:
        half_of_the_length = len(self.indices) // 2
        if char in ["B", "R"]:
            self.indices = self.indices[half_of_the_length:]
        else:
            self.indices = self.indices[:half_of_the_length]


def find_my_seat_id(seat_ids: List[int]) -> int:
    return [
        seat_id
        for seat_id in range(min(seat_ids), max(seat_ids))
        if seat_id not in seat_ids
    ][0]


if __name__ == "__main__":
    data = split_rows_and_columns(data)
    seat_ids_generator = SeatIdsGenerator(data)
    seat_ids = seat_ids_generator.get_seat_ids()
    first_part_result = max(seat_ids)
    print(first_part_result)
    second_part_result = find_my_seat_id(seat_ids)
    print(second_part_result)

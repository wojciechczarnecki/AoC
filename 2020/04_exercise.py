from typing import List, Dict

with open("04_input", "r") as f:
    data = f.read().split("\n\n")


class DataPreprocessor:
    def __init__(self, data: List[str]) -> None:
        self.data = self.replace_wrong_chars(data)

    def replace_wrong_chars(self, data: List[str]) -> List[str]:
        return [row.replace("\n", " ") for row in data]

    def generate_dictionaries(self) -> List[Dict[str, str]]:
        return [
            {item.split(":")[0]: item.split(":")[1] for item in row.split(" ")}
            for row in self.data
        ]


class Exercise:
    def __init__(self, data: List[Dict[str, str]]) -> None:
        self.data = data

    def count_correct_passports(self, num_of_part: int) -> int:
        passports_with_required_fields = self._get_passports_with_required_fields()
        if num_of_part == 1:
            return len(passports_with_required_fields)

        validated_passports = self._get_validated_passports(
            passports_with_required_fields
        )
        return len(validated_passports)

    def _get_passports_with_required_fields(self) -> List[Dict[str, str]]:
        return [
            passport for passport in self.data if self._are_required_fields(passport)
        ]

    def _are_required_fields(self, passport: Dict[str, str]) -> bool:
        first_condition = len(passport) == 8
        second_condition = len(passport) == 7 and "cid" not in passport
        return first_condition or second_condition

    def _get_validated_passports(
        self, passports: List[Dict[str, str]]
    ) -> List[Dict[str, str]]:
        return [
            passport for passport in passports if self._are_fields_correct(passport)
        ]

    def _are_fields_correct(self, passport: Dict[str, str]) -> bool:
        return (
            self._is_birth_year_correct(passport["byr"])
            and self._is_issue_year_correct(passport["iyr"])
            and self._is_expiration_year_correct(passport["eyr"])
            and self._is_height_correct(passport["hgt"])
            and self._is_hair_color_correct(passport["hcl"])
            and self._is_eye_color_correct(passport["ecl"])
            and self._is_passport_id_correct(passport["pid"])
        )

    def _is_birth_year_correct(self, field: str) -> bool:
        return len(field) == 4 and 1920 <= int(field) <= 2002

    def _is_issue_year_correct(self, field: str) -> bool:
        return len(field) == 4 and 2010 <= int(field) <= 2020

    def _is_expiration_year_correct(self, field: str) -> bool:
        return len(field) == 4 and 2020 <= int(field) <= 2030

    def _is_height_correct(self, field: str) -> bool:
        unit = field[-2:]
        if unit not in ["cm", "in"]:
            return False
        else:
            value = int(field[:-2])

        if unit == "cm":
            return 150 <= value <= 193

        return 59 <= value <= 76

    def _is_hair_color_correct(self, field: str) -> bool:
        correct_characters = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
        ]
        if field[0] != "#":
            return False
        value = field[1:]
        are_characters_correct = [
            character in correct_characters for character in value
        ]
        return len(value) == 6 == sum(are_characters_correct)

    def _is_eye_color_correct(self, field: str) -> bool:
        return field in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def _is_passport_id_correct(self, field: str) -> bool:
        try:
            int(field)
        except ValueError:
            return False
        return len(field) == 9


if __name__ == "__main__":
    data_preprocessor = DataPreprocessor(data)
    new_data = data_preprocessor.generate_dictionaries()

    exercise = Exercise(new_data)
    num_of_correct_passports = exercise.count_correct_passports(num_of_part=2)
    print(num_of_correct_passports)

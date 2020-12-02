from typing import List

with open("02_input", "r") as f:
    data = f.read().splitlines()


def count_correct_passwords(data: List[str], which_part: int) -> int:
    num_of_correct_passwords = 0
    for line in data:
        splitted_line: List[str] = line.split(" ")
        extreme_numbers = splitted_line[0].split("-")
        character_to_find = splitted_line[1][0]
        password = splitted_line[2]

        if which_part == 1:
            condition = (
                int(extreme_numbers[0])
                <= password.count(character_to_find)
                <= int(extreme_numbers[1])
            )
        else:
            condition = (
                password[int(extreme_numbers[0]) - 1] == character_to_find
            ) != (password[int(extreme_numbers[1]) - 1] == character_to_find)

        if condition:
            num_of_correct_passwords += 1

    return num_of_correct_passwords


if __name__ == "__main__":
    num_of_correct_passwords = count_correct_passwords(data, which_part=2)
    print(num_of_correct_passwords)

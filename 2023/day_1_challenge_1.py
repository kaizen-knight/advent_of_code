import logging

logging.basicConfig(level='DEBUG')
logger = logging.getLogger(__name__)

with open('2023/day_1_input.txt', 'r') as file:
    logger.info(f"File read successfully")
    challenge_file = file.read().splitlines()

calibration_digits = []
run_sum = 0
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
str_digits = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

for line in challenge_file:
    logger.debug(f"Line {line} processing")
    first = None
    last = None
    min_index = 0
    while not first:
        x = line[min_index]
        logger.debug(f"First char processing {x}")
        if x in digits:
            logger.debug(f"Set first to {x}")
            first = x
        min_index += 1
    max_index = len(line) - 1
    while not last:
        y = line[max_index]
        logger.debug(f"last char processing {y}")
        if y in digits:
            last = y
        max_index -= 1
    calibration_digits.append(int(f"{first}{last}"))
    run_sum += int(f"{first}{last}")


final_calibration_digits = []
final_run_sum = 0
line_detail = []

for line in challenge_file:
    logger.debug(f"Checking line {line} for string digits")
    found_str_digits = {}
    location_string_digits = []
    digit_value = -1
    for num in str_digits:
        digit_value += 1
        found_dig = line.find(num)
        if found_dig > -1:
            logger.debug(f"Found {num} at {found_dig}, value {digit_value}")
            found_str_digits[found_dig] = {
                'str_digit_found': num,
                'digit_value': digit_value
            }
            location_string_digits.append(found_dig)
    if len(found_str_digits) > 0:
        logger.debug(f"At least one digit identified, checking for duplicates")
        for dig in found_str_digits.copy():
            found_digit = found_str_digits[dig]
            logger.debug(f"Rechecking for {found_digit['str_digit_found']}")
            found_dig = line.find(found_digit['str_digit_found'], dig+1)
            if line.find(found_digit['str_digit_found'], dig+1) > -1:
                found_str_digits[found_dig] = {
                    'str_digit_found': found_digit['str_digit_found'],
                    'digit_value': found_digit['digit_value']
                }
                location_string_digits.append(found_dig)
            else:
                logger.debug(f"No duplicate found for {line} and digit {found_digit['str_digit_found']}")
    logger.debug(f"Now slicing line {line} accounting for found {len(found_str_digits)} string digits")
    cursor_pos = 0
    line_digits = {}
    while cursor_pos < len(line):
        if cursor_pos in location_string_digits:
            string_digit_found = found_str_digits[cursor_pos]
            logger.debug(f"Cursor at start of string digit {cursor_pos} with {string_digit_found['str_digit_found']}")
            line_digits[cursor_pos] = string_digit_found['digit_value']
            cursor_pos += len(string_digit_found['str_digit_found'])
            logger.debug(f"Cursor ffwd to {cursor_pos}")
        else:
            char = line[cursor_pos]
            if char in digits:
                logger.debug(f"Individual digit {char} found at {cursor_pos}")
                line_digits[cursor_pos] = int(char)
                cursor_pos += 1
            else:
                logger.debug(f"Char {char} discarded")
                cursor_pos += 1
    logger.debug(f"Line values found to be {line_digits}")
    keys = list(line_digits.keys())
    first_digit = line_digits[min(keys)]
    last_digit = line_digits[max(keys)]
    final_calibration_digits.append(int(f"{str(first_digit)}{str(last_digit)}"))
    final_run_sum += int(f"{str(first_digit)}{str(last_digit)}")
    line_detail.append(
        {
            'raw_line': line,
            'found_string_digits': found_str_digits,
            'all_found_digits': line_digits,
            'first': first_digit,
            'last': last_digit,
            'run_sum_digit': int(f"{str(first_digit)}{str(last_digit)}"),
            'run_sum': final_run_sum
        }
    )

# This time no story, no theory. The examples below show you how to write function accum:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# The parameter of accum is a string which includes only letters from a..z and A..Z.
# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python


def accum(input: str):
    output = ""
    loop_count = 1
    for l in input:
        repeated_letters = l * loop_count
        if loop_count != 1:
            output = output + "-"
        output = output + repeated_letters.capitalize()
        loop_count = loop_count + 1
    return output

assert accum("abcd") == "A-Bb-Ccc-Dddd"
assert accum("RqaEzty") == "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
assert accum("cwAt") == "C-Ww-Aaa-Tttt"
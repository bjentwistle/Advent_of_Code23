# Test data
# testData = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f","treb7uchet"]

file = open("advent_day1.txt", "r")
content=file.readlines()
file.close()

def remove_characters(array):
    data = []
    for word in array:
        newWord = word.rstrip('\n')
        data.append(newWord)
    return data

data = remove_characters(content)
# data = remove_characters(testData)

def find_digits(array):
    digits = []
    for word in array:
        digits_per_word = []
        for char in word:
           if char.isdigit():
                digits_per_word.append(char)
        digits.append(digits_per_word)

    return digits

digits = find_digits(data)
# digits = find_digits(testData)

def make_2_digit_nums(array):
    two_digit_nums = []
    for each in array:
        first_digit = each[0]
        last_digit = each[-1]
        concat_digits = first_digit + last_digit
        two_digit_nums.append(int(concat_digits))

    return two_digit_nums

two_digits = make_2_digit_nums(digits)

total = sum(two_digits)
print(total)

# Test to check testData
# actual = total
# expected = 142
# if  actual == expected:
#   print("Test passed")
# else:
#   print("Test failed, expected", expected, "but got", actual)
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

def find_digits(array):
    digits = []
    for word in array:
        for char in word:
           if char.isdigit():
                digits.append(int(char))
    return digits

digits = find_digits(data)

total = sum(digits)
print(total)

        

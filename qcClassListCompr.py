__author__ = 'vikram'


def vowel_names(names):
    return [x for x in names if x[0] in "AEIOU"]


print vowel_names(["Alice", "Bob", "Christy", "Jules"])
names = ["Scott", "Arthur", "Jan", "Elizabeth"]
print vowel_names(names)


def power_list(numbers):
    return [n[1] ** n[0] for n in enumerate(numbers)]


numbers = [3, 2, 5]
for n in enumerate(numbers):
    print n[0], n[1]
print power_list(numbers)
numbers = [3, 2.33, 5.238729437394]
print power_list(numbers)

matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
print matrix
flatMat = []
for row in enumerate(matrix):
    # print matrix[row[0]]
    for col in enumerate(matrix[row[0]]):
        flatMat.append(matrix[row[0]][col[0]])
print flatMat

# goodFlatMat = [matrix[row[0]][col[0]] for col in enumerate(matrix[row[0]]) for row in enumerate(matrix)]
# print goodFlatMat

bestFlatMat = [matrix[row[0]][col[0]] for row in enumerate(matrix) for col in enumerate(matrix[row[0]])]
print bestFlatMat


def get_factors(number):
    return [n for n in range(1, number + 1) if not number % n]


numSet = {62, 293, 314}
print numSet

def get_all_factors(numSet):
    return {num: get_factors(num) for num in numSet}

print get_all_factors(numSet)
numSet = {23094832, 2587245, 76, 4000}
# print get_all_factors(numSet)

unflipped = {'Python': "2015-09-15", 'Java': "2015-09-14", 'C': "2015-09-13", 'Fortran': "2015-09-13"}
print unflipped.items()
flipped = {v: k for k, v in unflipped.items()}
print flipped

__author__ = 'vikram'


def is_even(x):
    """

    :rtype : bool
    """
    if not x % 2:
        return True
    else:
        return False


def is_int(x):
    if abs(x - round(x)) > 0:
        print("float")
        return False
    else:
        print("int")
        return True


def digit_sum(n):
    sumOfN = 0
    i = 1
    while n != 0:
        modN = n % (10 ** 1)
        sumOfN += modN
        n = (n - modN) / 10
        print(n, modN, sumOfN)


def factorial(x):
    i = 4
    fact = 1
    while x > 1:
        fact = x * fact
        print(fact)
        x -= 1
        print(x)
        i -= 1
    print("final %d" % fact)
    return fact


def newfact(x):
    if x == 1:
        return 1
    else:
        return x * newfact(x - 1)


# is_even(3)
# is_int(-3)
# is_int(-1.3)
# is_int(4)
# digit_sum(189805)
# print factorial(8)
# print newfact(8)

def is_prime(x):
    prime = 0
    if x != 0:
        for n in range(2, x, 1):
            if x % n == 0:
                prime = 0
                break
            else:
                prime = 1
        print n
        if prime:
            return True
        else:
            return False


# print is_prime(0)

def reverse(text):
    print text
    sizeText = len(text)
    revText = ""
    print sizeText
    print text[sizeText - 1]
    for n in range(sizeText - 1, -1, -1):
        print text[n]
        revText = revText + text[n]
    return revText


# print reverse("hello6565g")

def anti_vowel(text):
    outtext = ""
    for n in range(len(text)):
        if text[n] not in "aeiouAEIOU":
            outtext = outtext + text[n]
    return outtext


# print anti_vowel("hello@ 897 #$wwer")

def trial_list(glist):
    if 'c' in glist:
        print("got it")
    else:
        print("no")


# trial_list(['a', 'b', 'd'])

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    scrab_sum = 0
    word = word.lower()
    for letter in range(len(word)):
        scrab_sum += score[word[letter]]
    return scrab_sum


# print scrabble_score("SDKLSDLKoiuJSDLKJSDKLJdslkdsjdklj")

def censor(text, word):
    textSplit = text.split()
    for item in range(len(textSplit)):
        if word == textSplit[item]:
            textSplit[item] = "*" * len(word)
    return " ".join(textSplit)


# print censor("hello how sdkfjsdlfkjhowlskdjf are you", "are")

def count(sequence, item):
    num = 0
    print(type(sequence))
    for member in range(len(sequence)):
        if item == sequence[member]:
            num += 1
    return num


# print count([2, 3, 4, 2], 3)
# print count("asdfa", "d")
# print count([[1, 2, 3], [2, 3, 4], [7, 8, 9]], [7, 80, 9])

def purify(nums):
    purified = []
    for num in nums:
        if not num % 2:
            purified.append(num)
    return purified

#print purify([1, 2, 3, 4, 5, 6, 7, 8, 90])

def product(nums):
    answer = 1
    for num in nums:
        answer *= num
    return answer

def remove_duplicates(nums):
    numbers = []
    for n in nums:
        numbers.append(n)
    unique = []
    numbers.sort()
    for num in numbers:
        if num not in unique:
            unique.append(num)
    return unique
#print remove_duplicates([4, 2, 1, 4, 3, 2, 4, 5, 6, 3])

def median(nums):
    numList = nums
    size = len(numList)
    numList.sort()
    print(numList, size)
    if size%2 == 1:
        return numList[size/2]
    else:
        return (numList[size/2] + numList[(size - 1)/2])/2.0
print median([1, 1, 2, 5, 4, 4])
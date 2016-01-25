__author__ = 'vikram'

even_sqaures = [x ** 2 for x in range(1, 12) if x % 2 == 0]
print even_sqaures

cubes_by_four = [n ** 3 for n in range(1, 11) if (n ** 3) % 4 == 0]
print cubes_by_four

sqaures = [x ** 2 for x in range(1, 11)]
print sqaures
special_sq = filter(lambda sq: 30 <= sq <= 70, sqaures)
print special_sq

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
print movies.items()

threes_and_fives = [x for x in range(1, 16) if x%3 == 0 or x%5 == 0]
print threes_and_fives

garbled1 = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled1[::-1]
message = message[::2]
print message

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
garbled = filter(lambda st: st != "X", garbled)
print garbled

four = 0b0100
print bin(1)
print type(bin(1))
print int("11001001", 2)

def flip_bit(number, n):
    print(bin(number))
    theNthBit = number >> n
    print(bin(theNthBit))
    print(bin(theNthBit)[0])

flip_bit(9,2)
flip_bit(9,3)



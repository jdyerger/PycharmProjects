from random import randint
def hello():
   print "hello world"
   a = 2
   b = 5
   a += b
   diceA = randint(1, 6)
   diceB = randint(1, 6)
   sum = diceA + diceB
   print "random numbers are: " + str(diceA) + ", " + str(diceB) + " -> " + str(sum)
hello()


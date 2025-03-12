
tries = 0
guess = 0

while guess != 6 and tries < 10:
  guess = int(input("Guess the number:  "))
  tries += 1

if guess == 6:
  print("You got it!")
else:
  print("Bad.")
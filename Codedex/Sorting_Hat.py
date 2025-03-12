# Write code below 💖

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Do you like Dawn or Dusk?")
print("    1) Dawn")
print("    2) Dusk")
q1 = int(input("Respuesta: "))

if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")


print("When I’m dead, I want people to remember me as:")
print("    1) The Good")
print("    2) The Great")
print("    3) The Wise")
print("    4) The Bold")
q2 = int(input("Respuesta: "))

if q2 == 1:
    Hufflepuff += 2
elif q2 == 2:
    Slytherin += 2
elif q2 == 3:
    Ravenclaw += 2
elif q2 == 4:
    Gryffindor += 2
else:
    print("Wrong input.")



print("Which kind of instrument most pleases your ear?")
print("    1) The violin")
print("    2) The trumpet")
print("    3) The piano")
print("    4) The drum")
q3 = int(input("Respuesta: "))
if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

print(f"Gryffindor {Gryffindor} points")
print(f"Ravenclaw {Ravenclaw} points" )
print(f"Hufflepuff {Hufflepuff} points")
print(f"Slytherin {Slytherin} points")

max = Slytherin
if max <= Hufflepuff:
    max = Hufflepuff
if max <= Ravenclaw:
    max = Ravenclaw
if max <= Gryffindor:
    max = Gryffindor
print(max)




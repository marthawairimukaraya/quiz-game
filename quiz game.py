print("welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("okay! Let's play :)")
score= 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")

answer = input("What does GPU stand for?")
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
    score += 1
else:
    print("incorrect!")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')
    score+= 1
else:
    print("incorrect!")

print("You got" + str (score) + "questions correct!")
x = 1
#Asking User for choice of quiz
print("1. Animal quiz\n2. General Quiz\n3. Vehicle Quiz\n4. Funny Quiz(cap and 18+)")
while x == 1:
    c = int(input("Enter the number corresponding to the type of quiz to select it "))
    if c != 1 and c != 2 and c!= 3 and c!=4:
        print("Invalid choice please enter again carefully")
    else:
        print("Ok moving on to quiz...")
        x+=1
#function for animal quiz
def animal():
    marks = 0
    a = int(input("Which of the following animals has 4 legs..\n1. Cow\n2. Parrot\n3. Hen\n4. Rhinoceros "))
    if a!=1 and a!=2 and a!=3 and a!=4:
        print("Ahh...Wrong option the correct answer was option 1 cow!!!!\nMoving on to next question")
    elif a == 1:
        print("Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...Wrong option the correct answer was option 1 cow!!!!\nMoving on to next question")

    a = int(input("Which of the following animals is the fastest..\n1. Tiger\n2. Lion\n3. Cheetah\n4. Dog "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...Wrong option the correct answer was option 3 cheetah!!!!\nMoving on to next question")
    elif a == 3:
        print("Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...Wrong option the correct answer was option 3 cheetah!!!!\nMoving on to next question")

    a = int(input("Which of the following animals has night vision..\n1. Cow\n2. Parrot\n3. Snake\n4. Cat "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...Wrong option the correct answer was option 3 snake!!!!")
        print("That was it for the questions come back again....!!")
        print("You achieved a total of",marks,"out of 3")
    elif a == 3:
        print("Correct!!!\n")
        marks += 1
        print("That was it for the questions come back again....!!")
        print("You achieved a total of", marks, "out of 3")
    else:
        print("Ahh...Wrong option the correct answer was option 3 snake!!!!")
        print("You achieved a total of", marks, "out of 3")
        print("That was it for the questions come back again....!!")
#function for general quiz
def general():
    marks = 0
    a = int(input("Which of the following countries is also known as the land of the midnight sun?..\n1. Greenland\n2. Canada\n3. Russia\n4. Norway "))
    if a!=1 and a!=2 and a!=3 and a!=4:
        print("Ahh...Wrong option the correct answer was option 4 Norway!!!!\nMoving on to next question")
    elif a == 4:
        print("Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...Wrong option the correct answer was option 4 Norway!!!!\nMoving on to next question")

    a = int(input("How many inches make up 1 foot?..\n1. 10 inches\n2. 15 inches\n3. 12 inches\n4. 69 inches "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...Wrong option the correct answer was option 3 12 inches!!!!\nMoving on to next question")
    elif a == 3:
        print("Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...Wrong option the correct answer was option 3 12 inches!!!!\nMoving on to next question")

    a = int(input("Which of the following countries is not democratic..\n1. India\n2. USA\n3. Azerbaijan\n4. North Korea "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...Wrong option the correct answer was option 4 North Korea!!!!")
        print("You achieved a total of", marks, "out of 3")
        print("That was it for the questions come back again....!!")
    elif a == 4:
        print("Correct!!!\n")
        marks += 1
        print("You achieved a total of", marks, "out of 3")
        print("That was it for the questions come back again....!!")
    else:
        print("Ahh...Wrong option the correct answer was option 4 North Korea!!!!")
        print("You achieved a total of", marks, "out of 3")
        print("That was it for the questions come back again....!!")
#function for vehicle quiz
def Vehicle():
    marks = 0
    a = int(input("Who made the first mass producing car..\n1. McLaren\n2. Audi\n3. Ford\n4. Stanley Brothers "))
    if a!=1 and a!=2 and a!=3 and a!=4:
        print("Ahh...Wrong option the correct answer was option 3 Ford!!!!\nMoving on to next question")
    elif a == 3:
        print("Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...Wrong option the correct answer was option 3 Ford!!!!\nMoving on to next question")

    a = int(input("Who invented the first internal combustion engine..\n1. Nicolaus Otto\n2. Rudolf Diezel\n3. Carl Benz\n4. Aniket Mondal "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...Wrong option the correct answer was option 1 Nicolaus!!!!\nMoving on to next question")
    elif a == 1:
        print("Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...Wrong option the correct answer was option 1 Nicolaus!!!!\nMoving on to next question")

    a = int(input("Which of the following cars is driven by Secret Agent James Bond 007..\n1. DeLorean\n2. Chitty Chitty Bang Bang\n3. Herbie \n4. Aston Martin "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...Wrong option the correct answer was option 4 Aston Martin!!!!")
        print("You achieved a total of", marks, "out of 3")
        print("Come back again!!!")
    elif a == 4:
        print("Correct!!!\nMoving on to next question")
        marks += 1
        print("You achieved a total of", marks, "out of 3")
        print("Come back again")
    else:
        print("Ahh...Wrong option the correct answer was option 4 Aston Martin!!!!")
        print("You achieved a total of", marks, "out of 3")
        print("That was it for the questions come back again....!!")
#function for funny quiz
def Funny():
    marks = 0
    a = int(input("How many dicks does your mum choke on..\n1. 0\n2. 1\n3. 2\n4. Infinity "))
    if a!=1 and a!=2 and a!=3 and a!=4:
        print("Stfu kid your mum doesn't choke on any number of dicks cuz she a veteran!!!!\nMoving on to next question")
    elif a == 1:
        print("Fuck you bro you were Correct!!!\nMoving on to next question")
        marks += 1
    else:
        print("Stfu kid your mum doesn't choke on any number of dicks cuz she a veteran!!!!\nMoving on to next question")

    a = int(input("Who banged your gf..\n1. You\n2. Me\n3. Your Best Friend\n4. Your dad "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Ahh...I feel sorry for you bruv your girl slept with your best friend\nMoving on to next question")
    elif a == 3:
        print("Correct but sed lyf!!!\nMoving on to next question")
        marks += 1
    else:
        print("Ahh...I feel sorry for you bruv your girl slept with your best friend\nMoving on to next question")

    a = int(input("How wet is your girl's pussy.\n1. 5L\n2. 2ml\n3. 400KL\n4. 0 "))
    if a != 1 and a != 2 and a != 3 and a != 4:
        print("Your gf wet as fuck she squirting 400 Kilo Litres!!!!")
        print("Homie visit again...")
        print("You achieved a total of", marks, "out of 3")
    elif a == 3:
        print("Damn bro your gf has the entire Nile River flowing down there Correct answer tho!!!")
        print("Nigga be back bro...")
        marks += 1
        print("You achieved a total of", marks, "out of 3")
    else:
        print("Your gf wet as fuck she squirting 400 Kilo Litres!!!!")
        print("That was it for the questions come back again....!!")
        print("You achieved a total of", marks, "out of 3")

#Calling the quiz functions
if c == 1:
    animal()
elif c == 2:
    general()
elif c == 3:
    Vehicle()
else:
    Funny()

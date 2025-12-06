#Working out howmany times a padlock goes to and past zero to create a password

#Grabbing the numbers from sequence and sorting them
with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]

#Setting a start point, being the number 50, including the previously found password and a variable for the newly created sequence
Start = 50
Password = 1031
Passes = 0
HundredPasses = 0
Magnitudes = []
New_Sequence = []
#Changing the property of R to addition and L to subtraction and turning it into an integer
sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]

#Adds one for every 100 in magnitude
for number in sequence:
    HundredPasses += abs(number) // 100
    print(abs(number) // 100)

#for number in sequence:
    #Start += number
    #print(Start)




#print(New_Sequence)

#for number in range(len(New_Sequence)):
    #previous = Start

#for number in sequence:
    #previous = Start
    # += number

    #crosses = abs((previous // 100) - (Start // 100))
    #Passes += crosses
    #print(previous, "→", Start, "crossed:", crosses)


#for number in sequence:
    #Start += number
    #Start %= 100
    #print(Start)

#for number in sequence:
    #previous = Start
    #Start += number

    # Count how many 100's crossed
    #Passes += abs(Start - previous) // 100

    #Start %= 100

Passes = 0

for number in sequence:
    previous = Start          # value before applying change
    Start += number           # apply change

    # Count how many thresholds of 100 were crossed
    Passes += abs(Start - previous) // 100

    # Wrap to 0–99 range
    Start %= 100

    print(Start)

print("Total passes:", Passes)

#print(Password)
print(HundredPasses)
print(Passes)
Final = (Password + Passes - HundredPasses)
print ("The final password is " + str(Password + Passes + HundredPasses))




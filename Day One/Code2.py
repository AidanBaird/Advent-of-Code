#Working out howmany times a padlock goes to and past zero to create a password

#Grabbing the numbers from sequence and sorting them
with open("sequence") as rotations:
    sequence = [line.strip() for line in rotations]

#Setting a start point, being the number 50, including the previously found password and a variable for the newly created sequence
Start = 50
Password = 1031
Passes = 0
HundredPasses = 0
New_Sequence = []
#Changing the property of R to addition and L to subtraction and turning it into an integer
sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]

#Adds one for every 100 in magnitude, adjusts the number after checking how many times it passes 100 on its own
for number in sequence:

    HundredPasses += abs(number) // 100

    remainder = abs(number) % 100
    if number < 0:
        adjusted_number = -remainder if remainder != 0 else -1
    else:
        adjusted_number = remainder if remainder != 0 else 1

    New_Sequence.append(adjusted_number)

#Checking the conversion was successful
#for number in range(len(sequence)):
    #print(f"Sequence[{number}] = {sequence[number]}, New_Sequence[{number}] = {New_Sequence[number]}")

print(New_Sequence)

for number in range(len(New_Sequence)):
    previous = Start


#print(Password)
#print(HundredPasses)
#print(Passes)
Final = (Password + HundredPasses + Passes)
#print ("The final password is " + str(Final))




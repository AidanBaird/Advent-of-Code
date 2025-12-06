#Working out howmany times a padlock goes to and past zero to create a password

#Grabbing the numbers from sequence and sorting them
with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]

#Setting a start point, being the number 50, including the previously found password and a variable for the newly created sequence
Start = 50
Password = 1031
Passes = 0
hundredpasses = 0
Magnitudes = []
new_sequence = []
current = 0
sequence_length = []
biggestdigit = 0
#Changing the property of R to addition and L to subtraction and turning it into an integer
second_sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]
simplified_sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]

#print(second_sequence)
#print(simplified_sequence)

#Find the absolute number and add that to hundredpasses as it is one rotation.

for number in second_sequence:
    hundredpasses += abs(number) // 100


for i, number in enumerate(second_sequence):


    while abs(number) >= 100:
        sign = -1 if number < 0 else 1
        number_str = str(abs(number))
        number = int(number_str[1:])
        number *= sign


    second_sequence[i] = number


#print(second_sequence)

# Creating a way to check if the numbers are incrementing correctly
#for number in second_sequence:
   #Start += number
   #if abs(Start) // 100 <= 1:
       #Passes += abs(Start) // 100

    #print(number)
    #print(Start)

#
#for number, digit in enumerate(sequence):
    #print(number, digit)

#
#for number, digit in enumerate(simplified_sequence):
    #length = len(str(digit))
    #print(number, digit, length)
    #sequence_length.append(str(length))

#print(sequence_length)

#
#biggestdigit = max(sequence_length)
#print(biggestdigit)

#

#for digit in simplified_sequence:
    #length = len(str(digit))
    #print(length)
    #if str(length) < biggestdigit:
        #print("yes")







print ("The password is ", Password + hundredpasses + Passes)






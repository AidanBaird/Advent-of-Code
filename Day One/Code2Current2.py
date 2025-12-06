with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]

#with open("dummysequence") as rotations:
    #sequence = [line.strip() for line in rotations]

second_sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]

start = 50
password = 1031
passes = 0
hundredpasses = 0

for number in second_sequence:
    if start < 0 or start > 99:
        sign = -1 if number < 0 else 1
        number = abs(number)
        hundredpasses += number // 100
        number = sign * number
    previous = start
    start += number
    print(previous, "+", number, "=", start)
    if start < 0:
        start = start + 100
        passes += 1
    elif start > 99:
        start = start - 100
        passes += 1



print(passes + password)
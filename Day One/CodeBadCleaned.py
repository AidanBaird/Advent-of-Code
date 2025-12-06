with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]


start = 50
password = 1031
passes = 0
hundredpasses = 0
wrapped_sequence = []
second_sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]

for number in second_sequence:
    hundredpasses += abs(number) // 100
    sign = -1 if number < 0 else 1
    mag = abs(number)
    wrapped_mag = mag % 100
    wrapped_number = sign * wrapped_mag
    wrapped_sequence.append(wrapped_number)

for number in wrapped_sequence:
    previous = start
    start += number
    if start < 0:
        start = start + 100
        passes += 1
    elif start > 99:
        start = start - 100
        passes += 1

print(password + passes + hundredpasses)
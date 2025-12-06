with open("Sequence") as rotations:
    sequence = [line.strip() for line in rotations]

# Convert R/L to signed integers
second_sequence = [int(s.replace("R", "+").replace("L", "-")) for s in sequence]

start = 50
zero_hits = 0

for number in second_sequence:
    previous = start
    end = previous + number

    # Count all zero crossings during this rotation
    zero_hits += abs(end // 100 - previous // 100)

    # Wrap for next rotation
    start = end % 100

print(zero_hits)

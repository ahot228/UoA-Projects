import sys
import random

# Read 10 Māori words from stdin
words = [line.strip() for line in sys.stdin if line.strip()]
if len(words) != 10:
    print("Error: Exactly 10 words required.")
    sys.exit(1)

# Convert each word into an integer key (sum of Unicode code points)
keys = [sum(ord(c) for c in word) for word in words]

# Constants
p = 20011
m = 100

# Try random a and b until a perfect hash is found
while True:
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    slots = {}
    collision = False

    for i in range(10):
        k = keys[i]
        slot = ((a * k + b) % p) % m
        if slot in slots:
            collision = True
            break
        slots[slot] = i  # store index to avoid duplicates

    if not collision:
        break

# Print results
print("Perfect hash function found:")
print(f"a = {a}, b = {b}, p = {p}, m = {m}\n")
print("Word-to-slot mapping:")
for i in range(10):
    key = keys[i]
    slot = ((a * key + b) % p) % m
    print(f"{words[i]} (key={key}) -> slot {slot}")
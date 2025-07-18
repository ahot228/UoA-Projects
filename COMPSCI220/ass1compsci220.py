import sys

for line in sys.stdin:
  words = line.strip().split(' ')
  reduplicated = [word + word if word else '' for word in words]
  print(' '.join(reduplicated))
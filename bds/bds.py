import hashlib
import random

# Perform 2 random plaintext for finding collision with the same hash values
def str(x):
	plaintext = "01abcd02dfg"
	return ''.join(random.choice(plaintext) for _ in range(x))


# Birthday Attack on a MD5 hash function
def battack():
  hash = {}
  attack = 0
  while True:
    attack = attack + 1
    selection = str(10)
    value = hashlib.md5(selection.encode()).hexdigest()
    if value in hash:
      print("Possible attack numbers: ", attack)
      print("First plaintext:", hash[value])
      print("Second plaintext: ", selection)
      break
    hash[value] = selection

battack()
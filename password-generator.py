import string
import random

password = ""

alphabet = string.ascii_lowercase
alphabet_list = list(alphabet)

for character in range(0, 12):
    num = random.randint(0, 25)
    char = alphabet_list[num]
    password += char

print(password)


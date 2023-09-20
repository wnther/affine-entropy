from math import gcd, log2
from typing import List, Tuple

N: int = 26

# Calculate all numbers in z*
z_star: List[int] = [i for i in range(N) if gcd(i, N) == 1]

print("z* =", z_star)
print("|z*| =", len(z_star))

# Calculate number of possible keys, given a key is made up of the tuple (a, b)
no_of_possible_keys: int = len(z_star) * N

print("Number of possible keys:", no_of_possible_keys)

# Define affine encryption
def affine_encrypt(a: int, b: int, p: int) -> int:
    return (a * p + b) % N

# Define entropy
def entropy(p: float) -> float:
    return p * log2(1/p)

# Uniform plaintext letter, known ciphertext
used_keys: List[Tuple[int, int]] = []
no_of_valid_keys_given_ciphertext: int = 0

for plaintext_letter in range(N):
    for i in z_star:
        for j in range(N):
            if affine_encrypt(i, j, plaintext_letter) == 8:
                no_of_valid_keys_given_ciphertext = no_of_valid_keys_given_ciphertext + 1
                if (i, j) not in used_keys:
                    used_keys.append((i, j))

print("Number of valid keys given only ciphertext:", no_of_valid_keys_given_ciphertext)
print("No of used keys:", len(used_keys))

# Known plaintext letter, Known ciphertext
no_of_valid_keys_given_plaintext_ciphertext: int = 0

for i in z_star:
    for j in range(N):
        if affine_encrypt(i, j, 6) == 8:
            no_of_valid_keys_given_plaintext_ciphertext = no_of_valid_keys_given_plaintext_ciphertext + 1

print("Number of valid keys given plain- and ciphertext:", no_of_valid_keys_given_plaintext_ciphertext)

# Results
print("H(K|C) =", no_of_valid_keys_given_ciphertext * entropy(1 / no_of_valid_keys_given_ciphertext))
print("H(K|P,C) =", no_of_valid_keys_given_plaintext_ciphertext * entropy(1 / no_of_valid_keys_given_plaintext_ciphertext))

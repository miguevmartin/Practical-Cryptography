"""
Demo of power2round function for scalars

Last modified: March 2026
Author: Original code by Gemini and adapted by Miguel Vargas Martin
"""

import random

def power2round_scalar(r, d, q):
    """
    Standard Power2Round for a single integer.
    r_0 is the centered remainder: -2^(d-1) < r0 <= 2^(d-1)
    """
    two_d = 1 << d
    half_two_d = 1 << (d - 1)
    
    # Standard centered modular reduction
    r0 = ((r + half_two_d - 1) % two_d) - half_two_d + 1
    r1 = (r - r0) // two_d
    return r1, r0

# --- Example using ML-DSA Parameters ---
#q = 8380417 # ML-DSA Q
#d = 13      # Standard d for ML-DSA

# --- Toy example ---
q = 23
d = 3

example = random.randint(0, q)

r1, r0 = power2round_scalar(example, d, q)

print(f"Original: {example}")
print(f"High bits (r1): {r1}")
print(f"Low bits (r0): {r0}")
print(f"Verification (r1 * 2^d + r0): {r1 * (2**d) + r0}")

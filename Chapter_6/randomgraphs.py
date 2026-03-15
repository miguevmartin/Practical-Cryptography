"""
Visual and Compression-Based Comparison of Random Number Generators

Created on: February 2026
Author: Prof. Miguel Vargas Martin

This program compares:
  1) A cryptographically secure random number generator (CSPRNG), and
  2) A simple linear congruential generator (LCG).

The comparison is performed using:
  - Scatter plots (visual structure),
  - Gzip compression (empirical compressibility).

⚠️ IMPORTANT:
- This code is for educational purposes only.
- LCGs are NOT cryptographically secure.
- Visual randomness does NOT imply cryptographic security.
"""

import random
from sympy import nextprime
import matplotlib.pyplot as plt
import gzip

# Parameters
iter = 1000          # Number of random values generated
fill = 4             # Number of decimal digits retained per value

# Byte strings used for compression comparison
rand_crypto = b''
rand_strd = b''

# Cryptographically secure RNG
# SystemRandom draws entropy directly from the OS (CSPRNG)
rng = random.SystemRandom()

for i in range(iter):
    x = rng.random()                     # Uniform float in [0, 1)
    plt.scatter(i, x, color='b', alpha=0.3)# Visual inspection of randomness

    # Keep only the last few decimal digits to create a byte stream
    # (This is intentionally lossy and pedagogical, not secure.)
    rand_crypto += str(x)[-fill:].encode('utf-8')

plt.title("CSPRNG output (SystemRandom)")
plt.xlabel("Iteration")
plt.ylabel("Random value")
plt.show()

# Linear Congruential Generator (LCG)
# LCG parameters (chosen for simplicity, not quality)
a = 5           # multiplier
c = 3           # increment
x = 2           # seed

# Modulus chosen as a prime slightly larger than the number of samples
m = nextprime(iter)

# First iteration
x = (a * x + c) % m

for i in range(iter):
    # Normalize to [0, 1) for visual comparison with CSPRNG
    plt.scatter(i, x / iter, color='r', alpha=0.3)

    x = (a * x + c) % m

    # Store fixed-width decimal representation
    # This preserves structure and makes compression effects visible
    rand_strd += str(x).zfill(fill).encode('utf-8')

plt.title("LCG output")
plt.xlabel("Iteration")
plt.ylabel("Normalized value")
plt.show()

# Compression-based comparison

# Both byte streams should have comparable size
print(len(rand_strd), len(rand_crypto))

# Compress both outputs using gzip
# Structured data (LCG) should compress significantly better
with gzip.open('rand_crypto.gz', 'wb') as c:
    c.write(rand_crypto)

with gzip.open('rand_strd.gz', 'wb') as s:
    s.write(rand_strd)

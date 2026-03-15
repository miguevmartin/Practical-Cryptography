"""
Demo of power2round function for vector of polynomials in Rq^k

Last modified: March 2026
Author: Original code by Gemini and adapted by Miguel Vargas Martin
"""

import numpy as np

def power2round_vector_numpy(vector_coeffs, d, q):
    """
    Extends Power2Round to a vector of polynomials in Rq^k.
    vector_coeffs: numpy array of shape (k, n)
    """
    # Ensure input is a numpy array and reduced mod q
    r = np.array(vector_coeffs) % q
    
    # The logic is identical; NumPy handles the (k, n) shape automatically
    r0 = ((r + half_two_d - 1) % two_d) - half_two_d + 1
    r1 = (r - r0) // two_d
    
    return r1, r0

# --- ML-DSA Parameter Example (e.g., ML-DSA-65/Dilithium3) ---
#q = 8380417
#d = 13
#n = 256 
#k = 6    # Vector dimension for ML-DSA-65

# --- Toy example ---
q = 23
d = 3
n = 5
k = 2

two_d = 1 << d
half_two_d = 1 << (d - 1) 

# Create a random vector of k polynomials, each of degree n-1
# Shape: (6, 256)
vector_r = np.random.randint(0, q, size=(k, n))

# Process the entire vector at once
v1, v0 = power2round_vector_numpy(vector_r, d, q)

# --- Verification ---
# Reconstruct the vector
reconstructed = (v1 * (1 << d) + v0) % q

# Check if the entire matrix matches
all_match = np.array_equal(vector_r % q, reconstructed)

print(f"Vector Shape: {vector_r.shape}")
print(f"All {k*n} coefficients correctly decomposed: {all_match}")

# Check specific bounds for ML-DSA
print(f"Max r0: {v0.max()} (Should be <= {half_two_d})")
print(f"Min r0: {v0.min()} (Should be > -{half_two_d})")

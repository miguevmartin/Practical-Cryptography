"""
Implementation of Decompose for coefficients in Rq^k

Last modified: March 2026
Author: Original code by Gemini and adapted by Miguel Vargas Martin
"""

import numpy as np

def decompose_vector_numpy(vector_coeffs, alpha, q):
    """
    Extends Decompose to a vector of polynomials in Rq^k.
    vector_coeffs: numpy array of shape (k, n)
    """
    # 1. Ensure input is a numpy array and reduced mod q
    r = np.array(vector_coeffs) % q
    
    # 2. Initial remainder r0 in [0, alpha-1]
    r0 = r % alpha
    
    # 3. Center the remainder: -alpha/2 < r0 <= alpha/2
    mask_centered = r0 > (alpha // 2)
    r0[mask_centered] -= alpha
    
    # 4. Handle the overflow condition (r - r0 == q - 1)
    mask_overflow = (r - r0 == q - 1)
    
    # 5. Calculate r1
    # Initialize r1 with standard division
    r1 = (r - r0) // alpha
    
    # Apply special case logic for overflow coefficients
    r1[mask_overflow] = 0
    r0[mask_overflow] = r0[mask_overflow] - 1
    
    return r1.astype(np.int64), r0.astype(np.int64)

# --- ML-DSA Parameter Example (ML-DSA-65) ---
#q = 8380417
#k, n = 6, 256
#gamma2 = (q - 1) // 32
#alpha = 2 * gamma2

# Create a random vector of k polynomials, each of degree n-1
#vector_r = np.random.randint(0, q, size=(k, n))

# --- Toy example ---
q = 23
k, n = 2, 4
gamma2 = (q - 1) // 2
alpha = 2 * gamma2
vector_r = np.array([
    [10, 22, 5, 0],   # First polynomial
    [15, 2, 19, 11]   # Second polynomial
])

# Process the entire vector at once
v1, v0 = decompose_vector_numpy(vector_r, alpha, q)
is_handled = np.any((v1 == 0) & (v0 == -1))

# --- Verification ---
# Reconstruct the vector: r = r1 * alpha + r0 (mod q)
reconstructed = (v1 * alpha + v0) % q
all_match = np.array_equal(vector_r % q, reconstructed)

print(f"Vector Shape: {vector_r.shape}")
print(f"All {k*n} coefficients correctly decomposed: {all_match}")
print(f"Overflow cases handled: {is_handled}")
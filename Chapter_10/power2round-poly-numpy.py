"""
Demo of power2round function for polynomials in Rq

Last modified: March 2026
Author: Original code by Gemini and adapted by Miguel Vargas Martin
"""

import numpy as np

def power2round_poly_numpy(poly_coeffs, d, q):
    """
    Vectorized Power2Round for polynomials in Rq.
    poly_coeffs: a numpy array of coefficients
    """
    # Convert input to numpy array and ensure it is in [0, q-1]
    r = np.array(poly_coeffs) % q
    
    two_d = 1 << d
    half_two_d = 1 << (d - 1)
    
    # Vectorized centered modular reduction for r0:
    # -2^(d-1) < r0 <= 2^(d-1)
    r0 = ((r + half_two_d - 1) % two_d) - half_two_d + 1
    
    # Compute r1 based on r0
    r1 = (r - r0) // two_d
    
    return r1, r0

# --- ML-DSA Parameter Example ---
#q = 8380417
#d = 13
#n = 256 # Degree of polynomial in Rq

# --- Toy example ---
q = 23
d = 3
n = 5

# Create a random polynomial with n coefficients
coeffs = np.random.randint(0, q, n)

r1_poly, r0_poly = power2round_poly_numpy(coeffs, d, q)

# Verify that the decomposition is correct for the entire polynomial
# (r1 * 2^d + r0) should perfectly reconstruct the coefficients (mod q)
reconstructed = (r1_poly * (1 << d) + r0_poly) % q
is_correct = np.all(coeffs % q == reconstructed)

print(f"Full Polynomial Reconstruction Successful: {is_correct}")
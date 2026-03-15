"""
Last modified: February 2026

@author: Miguel Vargas Martin (adapted from ChatGPT iterations)

Secure implementation of Centered Binomial Distribution (CBD)
sampling using a cryptographically secure RNG.

Used in lattice-based cryptography schemes such as CRYSTALS-Kyber.
"""

import secrets

def cbd_sample(eta):
    """
    Sample a single integer coefficient from a Centered Binomial Distribution (CBD).

    X = sum_{i=1..eta}(a_i) - sum_{i=1..eta}(b_i)
    where a_i, b_i ∈ {0,1} are independent uniform random bits.

    Output range: [-eta, +eta]
    """

    # Generate 2*eta bits at once (efficient + closer to real implementations)
    r = secrets.randbits(2 * eta)

    a_sum = 0
    b_sum = 0

    for i in range(eta):
        a_sum += (r >> i) & 1
        b_sum += (r >> (i + eta)) & 1

    return a_sum - b_sum

def sample_small_polynomial(n, eta):
    """
    Generate a polynomial with n coefficients sampled from CBD(eta).
    """
    return [cbd_sample(eta) for _ in range(n)]

# Example usage (Kyber-768 uses eta = 2)
n = 256
eta = 2

small_poly = sample_small_polynomial(n, eta)

print(small_poly)
print(f"Max absolute value: {max(abs(c) for c in small_poly)}")

# TODO 1 (Basic):
# Empirically verify that coefficients are always in [-eta, +eta].
# Raise an exception if a value falls outside the expected range.

# TODO 2 (Statistics):
# Generate 100,000 samples from cbd_sample(eta) and:
#   - Plot the empirical distribution.
#   - Compare it with the theoretical CBD distribution.
#   - Is it symmetric? Is it centered at 0?

# TODO 3 (Theory):
# Derive the expected value and variance of CBD(eta).
# Verify empirically that:
#   E[X] ≈ 0
#   Var[X] ≈ eta / 2

# TODO 4 (Security Engineering):
# Replace secrets.randbits with random.randint and:
#   - Measure performance difference.
#   - Discuss why random is insecure in cryptographic contexts.
#   - Explain how predictability could break a KEM scheme.

# TODO 5 (Cryptographic Context):
# Research how CRYSTALS-Kyber actually samples noise.
#   - Does it sample bits individually?
#   - How does it ensure constant-time behavior?
#   - Why is constant-time important here?

# TODO 6 (Advanced – Parameter Exploration):
# Experiment with eta = 1, 2, 3, 4.
#   - How does increasing eta affect:
#       * variance?
#       * coefficient spread?
#       * potential decryption failure probability?

# Modify the function to explicitly exclude the mismatched case (X1=1, X2=0, X3=1, X4=1)
def Z1_fixed(X1, X2, X3, X4):
    return ((not X1 and not X2 and (not X3 or X4)) or
            (not X1 and X2 and (X3 or X4)) or
            (X1 and not X2 and (X3 or X4)) or
            (X1 and X2 and X4)) and not (X1 and not X2 and X3 and X4)

# Compute the fixed output
fixed_Z1 = np.array([Z1_fixed(X1, X2, X3, X4) for X1, X2, X3, X4 in inputs])

# Compare outputs again
fixed_match = np.all(fixed_Z1 == expected_Z1)

# Show results
fixed_match, fixed_Z1

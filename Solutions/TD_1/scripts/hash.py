# Fast hash using XOR operator

def simple_hash(inputString):
    output = 0                            # Output is initialised to 0
    for character in inputString:         # For each character in input string...
        output += ord(character)          # Add the character's ASCII code
        output ^= (output * 31)           # Apply XOR with output and 31 times the output
        output %= 2 ** 32                 # Clamp between 0 and 4294967296
    return output
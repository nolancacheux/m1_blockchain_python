# Simple hash function using XOR and ASCII values

def simple_hash(input_string):
    hash_value = 0  # Initialize hash value to 0
    for char in input_string:  # Iterate over each character in the input string
        hash_value += ord(char)  # Add ASCII value of the character to hash_value
        hash_value ^= (hash_value * 31)  # XOR hash_value with 31 times itself
        hash_value %= 2 ** 32  # Ensure hash_value stays within 32-bit range
    return hash_value
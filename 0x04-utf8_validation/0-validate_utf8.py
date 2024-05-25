#!/usr/bin/python3
"""
Define validUTF8(data) function that validates whether a
string of ints represents a valid UTF-8 encoding.
"""
def int_to_bits(nums):
    """
    Helper function to convert ints to bits
    """
    for num in nums:
        yield f"{num:08b}"

def validUTF8(data):
    """
    Takes a list of ints and returns true if the list is
    a valid UTF-8 encoding, else returns false
    Args:
        data : List of ints representing possible UTF-8 encoding
    Return:
        bool : True or False
    """
    bits = int_to_bits(data)
    try:
        while True:
            byte = next(bits)
            if byte[0] == '0':
                continue
            # count the number of leading 1s
            ones = byte.find('0')
            if ones == -1 or ones == 1 or ones > 4:
                return False
            # check that the following bytes have the form 10xxxxxx
            for _ in range(ones - 1):
                byte = next(bits)
                if byte[:2] != '10':
                    return False
    except StopIteration:
        pass
    return True

# Test cases
print(validUTF8([467, 133, 108]))  # False
print(validUTF8([240, 188, 128, 167]))  # True
print(validUTF8([235, 140]))  # False
print(validUTF8([345, 467]))  # False
print(validUTF8([250, 145, 145, 145, 145]))  # False
print(validUTF8([0, 0, 0, 0, 0, 0]))  # True
print(validUTF8([]))  # True
print(validUTF8([197, 130, 1]))  # True
print(validUTF8([235, 140, 4]))  # False

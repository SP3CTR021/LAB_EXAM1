def isPalindrome(valStr):
    """Check if a given string is a palindrome."""
    return valStr == valStr[::-1]

def toBinaryIfNumber(value):
    """Convert value to binary if it's numeric."""
    if value.isdigit():  # Check if the input is a number
        num = int(value)
        return bin(num)[2:]  # remove '0b' prefix
    return None

# Main Program
user_input = input("Enter a value: ")

# Check if input itself is a palindrome
print("Input is a palindrome:", isPalindrome(user_input))

# Try to convert to binary if it's a number
binary_equivalent = toBinaryIfNumber(user_input)

if binary_equivalent:
    print("Binary equivalent:", binary_equivalent)
    print("Binary is a palindrome:", isPalindrome(binary_equivalent))
else:
    print("(No binary conversion since input is text)")

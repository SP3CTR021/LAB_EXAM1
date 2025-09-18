def gcd(x, y): #define function greatest common denominator
    # Recursive GCD function
    if y == 0:
        return x
    return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)

# Input validation loop
while True:
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    if x > 0 and y > 0:
        break
    else:
        print("Please enter positive non-zero integers only!")

print(f"The LCM of {x} and {y} is = {lcm(x, y)}")

def tower_of_hanoi(n, source='A', target='C', auxiliary='B'):
    """
    Print moves in the exact requested style:
      Move disk <k>: <source> ➔ <target>
    """
    if n == 1:
        print(f"Move disk 1: {source} ➔ {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n}: {source} ➔ {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)


def get_positive_int(prompt="Enter number of disks: "):
    """Prompt until the user gives a positive non-zero integer."""
    while True:
        s = input(prompt)
        try:
            v = int(s)
            if v <= 0:
                print("Please enter a positive, non-zero integer.")
            else:
                return v
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


if __name__ == "__main__":
    n = get_positive_int("Enter number of disks: ")
    # Header printed in the same style as your sample outputs
    print(f"Input values = [{n}]")
    tower_of_hanoi(n, "A", "C", "B")

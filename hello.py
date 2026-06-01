def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract y from x"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


if __name__ == "__main__":
    print(f"5 + 3 = {add(5,3)}")
    print(f"5 - 3 = {subtract(5,3)}")
    print(f"5 * 3 = {multiply(5,3)}")

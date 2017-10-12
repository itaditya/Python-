"""
This is a really simple version of the fibonacci sequence in python,
feel free to use it in your own code
"""

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

if __name__ == "__main__":
    # You can change 10 for any number so you can have more numbers
    for x in range(10):
        print(fibonacci(x))

#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the fibonacci sequence
    fib_seq = []

    if length == 0:
        print(fib_seq)
    elif length == 1:
        fib_seq = [0]
        print(fib_seq)
    elif length == 2:
        fib_seq = [0, 1]
        print(fib_seq)
    else:
        # Initialize the fibonacci sequence with the first two numbers
        fib_seq = [0, 1]
        # While loop will continue adding numbers to the fibonacci sequence
        while len(fib_seq) < length:
            # Append the sum of the last two numbers in the sequence to the sequence
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        # Print the sequence
        print(fib_seq)


# Test the function
print_fibonacci(9)
print_fibonacci(0) # []
print_fibonacci(1)  # [0]
print_fibonacci(2)  # [0,1]

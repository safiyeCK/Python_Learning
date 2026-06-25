# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …) | EN: See Turkish explanation


def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(b)
        a, b = b, a + b
    return fib_sequence 

n = int(input("How many Fibonacci numbers would you like to generate? "))
print(fibonacci(n))

# This code defines a function to generate Fibonacci numbers and then prompts the user for input.
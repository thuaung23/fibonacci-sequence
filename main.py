# This program implements algorithms for fibonacci sequence.
# Written by: Thu Aung
# Written on: Dec 5, 2020

# This is a recursive method.
def fib_seq_re(num):
  # Check if the input is a valid integer.
  if num < 0:
    print("Invalid Number.")

  else:
    # Fib(0) is 0.
    if num == 0:
      return 0
    # Fib(1) is 1.
    elif num == 1:
      return 1
    else:
      # Add last and second last items in the sequence.
      return fib_seq_re(num-1) + fib_seq_re(num-2)
    
num = int(input("Please type in a positive number: "))
for i in range(num):
    print(fib_seq_re(i))
print("The recursive Fibonacci sequence is: ", fib_seq_re(num))



def fibonacci_of(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

n = int(input("How cpunt fibbonaci yes?"))
print(fibonacci_of(n))
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

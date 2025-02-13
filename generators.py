# Task 1
def square(n):
  for i in range(n):
    if i == 0:
      continue
    print(i**2)

square(5)

#Task 2
def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            if i == n or (i == n - 1 and n % 2 == 1):
                print(i)
            else:
                print(i, end=', ')

n = int(input())
even(n)


#Task 3


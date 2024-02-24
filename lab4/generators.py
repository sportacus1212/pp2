#1
def squaregen(N):
    for i in range(1, N+1):
        yield i**2
N = int(input)
for square in squaregen(N):
    print(square)

#2
def even_generator(n):
    for i in range(0, n+1, 2):
        yield i
n = int(input())
evens = even_generator(n)
print(", ".join(map(str, evens)))

#3
def div3and4(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for num in div3and4(n):
    print(num)

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
n = int(input())
for i in countdown(n):
    print(i)
   
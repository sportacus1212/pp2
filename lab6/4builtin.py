import time
import math

def sqrtt(number, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(number)
    return result

number = int(input())
delay = int(input())

result = sqrtt(number, delay)
print(f"Square root of {number} after {delay} milliseconds is {result}")

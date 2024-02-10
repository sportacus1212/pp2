numbers = [44, 54156, 3, 1, 0, 77, 4, 7, 8, 47, 51] 
def is_prime ( n ) :
    if n <= 1 :        
        return False
    for i in range ( 2, (int(n**0.5)) + 1 ) :
        if n % i == 0 :
            return False
    return True 
prime_numbers = list ( filter ( lambda n : is_prime(n), numbers ))
print ( prime_numbers )
"""DECORE"""
def is_even(is_prime):
    def even_odd(num):
        if num % 2 == 0:
            return (num, "is even")
        else:
            return is_prime(num)
    return even_odd

@is_even
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return (num, "is not a prime number")
        return (num, "is a prime number")
    else:
        return (num, "is not a prime number")

print(is_prime(3))
print(is_prime(10))

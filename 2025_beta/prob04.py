num = int(input())

def check_prime(n):
    end = n // 2

    if n == 1:
        return False

    for i in range(2, end + 1):
        if n % i == 0 and n != 0:
            return False
    
    return True
already_prime = check_prime(num)
possible_prime = check_prime(num + 1) or check_prime(num - 1)

if already_prime:
    print(f"{num} is already prime")
elif possible_prime:
    print(f"{num} could be prime!")
else:
    print(f"{num} is a bad test specimen")
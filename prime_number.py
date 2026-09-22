# 1부터 100 사이의 자연수 중 소수 구하기
primes = []

for num in range(1, 101):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print("1부터 100 사이의 소수:")
print(primes)
print(f"\n총 개수: {len(primes)}개")

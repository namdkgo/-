num = int(input("숫자 입력 : "))
if num <= 1:
    print(f"{num}는 소수가 아닙니다.")
else:
    is_prime = True
    i = 2
    while i * i < num:
        if num % i == 0:
            print(f"{num}는 소수가 아닙니다.")
            is_prime = False
            break
        print(i, end=" ")
        i = i + 1
    if is_prime:
        print(f"{num}는 소수입니다.")
        
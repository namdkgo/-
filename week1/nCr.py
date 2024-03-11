def factorial(num) -> int:
    """
    매개변수, 리턴 둘다 integer
    return num * num-1 * num-2 * ... * 1
    """
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num-1)

def nCr(n, r) -> int:
    """
    매개변수, 리턴 둘다 integer
    return n! / (r! * (n-r)!)
    """
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

n = int(input("n 입력 : "))
r = int(input("r 입력 : "))

print(f"{n}C{r} = {str(nCr(n, r))}")

help(nCr)
help(factorial)
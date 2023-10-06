'''import math

def Kiem_tra_soNT(n):
    if(n<2):
        return False
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def liet_ke_so_nguyen_to(a, b):
   for i in range(a, b + 1):
       if Kiem_tra_soNT(i):
            print( i, end=(' '))

a=int(input("Nhập số đầu tiên trong khoảng = "))
b=int(input("Nhập số cuối trong khoảng = "))

liet_ke_so_nguyen_to(a,b)

def kiem_tra_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        tong = a + b
        a = b
        b = tong
    if b == n:
        return True
    else:
        return False
    
n=int(input('Nhập 1 số nguyên: '))
if kiem_tra_fibonacci(n):print(f"{n} là số fibonaci")
else:
    print(f'{n} ko phải sô fibonaci')

def fibonacci_thu_n(n):
    if n < 0:
        print("Số không hợp lệ")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_thu_n(n-1) + fibonacci_thu_n(n-2) 
    
n=int(input('Nhập n = '))
print(f"Số fibonaci thứ {n} = ",fibonacci_thu_n(n))


def tong_fibonacci_ko_de_quy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        sum=a+b
        for i in range(2, n+1):
            Tong = a + b
            a = b
            b = Tong
            sum += b
        return sum
n=int(input('Nhập n = '))
print(f"Tổng {n} so fibonacci đầu tiên = ",tong_fibonacci_ko_de_quy(n))

'''
def fibonacci_thu_n(n):
    if n < 0:
        print("Số không hợp lệ")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_thu_n(n-1) + fibonacci_thu_n(n-2) 

def TinhTongFibonacci(n):
    for i in range(0,n+1):
        if(fibonacci_thu_n(i)):
            n=int(input('Nhập n = '))
            print(f"Số fibonaci thứ {n} = ",fibonacci_thu_n(n))

import math

x = float(input("Enter X:"))
while x > 1:
    x = float(input("try enter X:"))
eps = float(input("Enter Eps:"))

def fact(num):
    iter = 1
    Fact = 1
    while iter < num:
        iter += 1
        Fact = Fact * iter
    return Fact

def Cycle():
    n = 1
    mySin = 0

    sumat = ((pow(2, 2 * n - 1) * pow(x, 2 * n)) / fact(2 * n))
    while sumat > eps:
        mySin += pow(-1, n + 1) * sumat
        n += 1
        sumat = ((pow(2, 2 * n - 1) * pow(x, 2 * n)) / fact(2 * n))
    print("My sinx:^2:", mySin, "*  ,sinx^2:", pow(math.sin(x), 2), "  ,n: ", n-1)   # Виводимо результат

def Rec(mySin = 0, n = 1):
    sumat = ((pow(2, 2 * n - 1) * pow(x, 2 * n)) / fact(2 * n))
    if( ( sumat > eps) ):
        mySin += pow(-1, n + 1) * sumat   # Рахуємо по формулі
        return Rec(mySin, n +1)
    else:
        print("My sinx:^2:", mySin, "*  ,sinx^2:", pow(math.sin(x), 2), "  ,n: ", n-1)  # Виводимо результат
        return mySin

print("*"*34, "CYCLE", "*"*34)
print("*"*74)
Cycle()
print("*"*74)
Rec()

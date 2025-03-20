import sympy as sp
import time

x = sp.symbols("x")
f = sp.sympify("x**2-2*x-1")
tol = 10**-15
iter = 1000


def Newton():
    while True:
        try:
            n = float(input("Ingrese el punto inicial: "))
            break
        except:
            print("Ingrese un valor válido.")
    n_time = time.time()
    fd = sp.diff(f)
    for i in range(iter):
        n = n - f.evalf(subs={x: n}) / fd.evalf(subs={x: n})
        if abs(f.evalf(subs={x: n})) < tol:
            return n, i, time.time() - n_time
    return n, i, time.time() - n_time


def Biseccion():
    while True:
        try:
            a = float(input("Ingrese el límite inferior del intervalo: "))
            b = float(input("Ingrese el límite superior del intervalo: "))
            if ((a < -0.41421) & (b > -0.41421)) | ((a < 2.41421) & (b > 2.41421)):
                break
            else:
                print("El intervalo no contiene una raíz. Ingrese otro.")
        except:
            print("Ingrese valores válidos.")

    c_time = time.time()
    for i in range(iter):
        c = (a + b) / 2
        if abs(f.evalf(subs={x: c})) < tol:
            return c, i, time.time() - c_time
        elif f.evalf(subs={x: a}) * f.evalf(subs={x: c}) < 0:
            b = c
        else:
            a = c
    return c, i, time.time() - c_time


def Steffensen():
    while True:
        try:
            s = float(input("Ingrese el punto inicial: "))
            break
        except:
            print("Ingrese un valor válido.")

    s_time = time.time()
    for i in range(iter):
        fs = f.evalf(subs={x: s})
        s = s - (fs**2 / (f.evalf(subs={x: s + fs}) - fs))
        if abs(f.evalf(subs={x: s})) < tol:
            return s, i, time.time() - s_time
    return s, i, time.time() - s_time


while True:
    try:
        z = int(
            input(
                "1. Newton \n2. Bisección \n3. Steffensen \nIngrese el numero del metodo a usar: "
            )
        )
        if (z > 0) & (z < 4):
            break
    except:
        print("Ingrese un valor válido.")

if z == 1:
    run = Newton()
elif z == 2:
    run = Biseccion()
else:
    run = Steffensen()

print(
    "El valor encontrado fue ",
    run[0],
    " tras ",
    run[1],
    " iteraciones y ",
    run[2] * 1000,
    " milisegundos",
)

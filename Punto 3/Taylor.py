import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        n = int(input("Ingrese el número de términos de la expansión: "))
        if n > 0:
            break
        else:
            print("Por favor, ingrese un número mayor a 0.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

while True:
    try:
        a = int(input("Ingrese el punto de expansión: "))
        break
    except:
        print("Ingrese un valor válido.")

x = sp.symbols("x")

while True:
    try:
        entrada = input("Ingrese la función a aproximar usando como variable x: ")
        f = sp.sympify(entrada)
        if x in f.free_symbols:
            break
    except sp.SympifyError:
        print("Por favor, ingrese una función válida.")

fd = f
s = 0
for i in range(n):
    s += (fd.subs(x, a) / sp.factorial(i)) * (x - a) ** i
    fd = sp.diff(fd)
print("Polinomio de Taylor: ", s)

xs = np.linspace(1, 10, 1000)
taylor = [float(s.evalf(subs={x: j})) for j in xs]
regular = [float(f.evalf(subs={x: j})) for j in xs]

plt.plot(xs, taylor, color="red", label="Aproximación (Taylor)")
plt.plot(xs, regular, linestyle="--", color="blue", label="Función Original")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Aproximación de Taylor vs Función Original")
plt.legend()
plt.grid(True)
plt.autoscale()
plt.show()

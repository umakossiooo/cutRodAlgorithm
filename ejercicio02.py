import random
import time

def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, p[i-1] + cut_rod(p, n - i))
    return q

p = [
    1, 5, 8, 9, 10, 17, 17, 20, 24, 30,
    35, 39, 40, 42, 44, 45, 47, 50, 52, 55,
    58, 60, 62, 65, 67, 70, 72, 74, 76, 78,
    80, 82, 85, 87, 89, 90, 92, 94, 96, 98,
    100, 102, 105, 107, 110, 112, 114, 117, 119, 120
]

n = 40

startTime = time.time()

max_revenue = cut_rod(p, n)

endTime = time.time()

executionTime = endTime - startTime

print(f"La ganancia máxima para una varilla con longitud {n}: {max_revenue}")
print(f"Tiempo de ejcución: {executionTime} segundos")

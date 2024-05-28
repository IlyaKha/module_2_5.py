


def get_matrix(n, m, value):
    matrix = []
    if n <= 0 or m <= 0:
        return matrix  # Возвращает пустой список если n или m < или = 0

    for _ in range(n):
        matrix.append([])
        for _ in range(m):
            matrix[-1].append(value)

    return matrix

# Примеры
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1) 
print(result2)  
print(result3)  

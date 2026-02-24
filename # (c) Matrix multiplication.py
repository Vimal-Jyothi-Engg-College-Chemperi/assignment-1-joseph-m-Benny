# (c) Matrix multiplication

r1 = int(input("Enter rows of matrix A: "))
c1 = int(input("Enter columns of matrix A: "))
r2 = int(input("Enter rows of matrix B: "))
c2 = int(input("Enter columns of matrix B: "))

if c1 != r2:
    print("Matrix multiplication not possible")
else:
    A = []
    B = []

    print("Enter elements of matrix A:")
    for i in range(r1):
        row = list(map(int, input().split()))
        A.append(row)

    print("Enter elements of matrix B:")
    for i in range(r2):
        row = list(map(int, input().split()))
        B.append(row)

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant matrix:")
    for row in result:
        print(row)
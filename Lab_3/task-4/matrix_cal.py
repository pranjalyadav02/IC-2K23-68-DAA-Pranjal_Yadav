def input_matrix():
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    if r <= 0 or c <= 0:
        raise ValueError("Invalid dimensions")
    mat = []
    print("Enter rows:")
    for i in range(r):
        vals = input(f"Row {i + 1}: ").split()
        row = list(map(int, vals))
        if len(row) != c:
            raise ValueError("Row length does not match column count")
        mat.append(row)
    return mat


def display_matrix(mat):
    print("\nMatrix:")
    for row in mat:
        for val in row:
            print(val, end="\t")
        print()


def add_matrices(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Matrices must have identical shapes")
        return None
    res = []
    i = 0
    while i < len(a):
        row = []
        j = 0
        while j < len(a[0]):
            row.append(a[i][j] + b[i][j])
            j += 1
        res.append(row)
        i += 1
    return res


def multiply_matrices(a, b):
    if len(a[0]) != len(b):
        print("Columns of A must match rows of B")
        return None
    r1 = len(a)
    c1 = len(a[0])
    c2 = len(b[0])
    res = []
    i = 0
    while i < r1:
        row = []
        j = 0
        while j < c2:
            total = 0
            k = 0
            while k < c1:
                total += a[i][k] * b[k][j]
                k += 1
            row.append(total)
            j += 1
        res.append(row)
        i += 1
    return res


def transpose_matrix(mat):
    r = len(mat)
    c = len(mat[0])
    res = []
    j = 0
    while j < c:
        row = []
        i = 0
        while i < r:
            row.append(mat[i][j])
            i += 1
        res.append(row)
        j += 1
    return res


def determinant_2x2(mat):
    return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]


def determinant_3x3(mat):
    a = mat[0][0]
    b = mat[0][1]
    c = mat[0][2]
    d = mat[1][0]
    e = mat[1][1]
    f = mat[1][2]
    g = mat[2][0]
    h = mat[2][1]
    i = mat[2][2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return det


def calculate_determinant(mat):
    r = len(mat)
    c = len(mat[0])
    if r != c:
        print("Matrix must be square")
        return None
    if r == 2:
        return determinant_2x2(mat)
    elif r == 3:
        return determinant_3x3(mat)
    else:
        print("Only 2x2 and 3x3 supported")
        return None


def main():
    while True:
        print("\n===== MATRIX CALCULATOR =====")
        print("1. Matrix Addition")
        print("2. Matrix Multiplication")
        print("3. Transpose")
        print("4. Determinant")
        print("5. Exit")

        ch = input("Enter choice: ")

        try:
            if ch == "1":
                print("Matrix 1:")
                m1 = input_matrix()
                print("Matrix 2:")
                m2 = input_matrix()
                res = add_matrices(m1, m2)
                if res is not None:
                    display_matrix(res)
            elif ch == "2":
                print("Matrix 1:")
                m1 = input_matrix()
                print("Matrix 2:")
                m2 = input_matrix()
                res = multiply_matrices(m1, m2)
                if res is not None:
                    display_matrix(res)
            elif ch == "3":
                print("Matrix:")
                m = input_matrix()
                res = transpose_matrix(m)
                display_matrix(res)
            elif ch == "4":
                print("Matrix:")
                m = input_matrix()
                ans = calculate_determinant(m)
                if ans is not None:
                    print("Determinant:", ans)
            elif ch == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice")
        except ValueError as err:
            print("Input error:", err)
        except Exception as err:
            print("Error:", err)


if __name__ == "__main__":
    main()


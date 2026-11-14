def convert_to_sparse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j] != 0:
                count += 1
            j += 1
        i += 1

    sparse = [[rows, cols, count]]

    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if matrix[i][j] != 0:
                sparse.append([i, j, matrix[i][j]])
            j += 1
        i += 1

    return sparse


def reconstruct_matrix(sparse):
    rows = sparse[0][0]
    cols = sparse[0][1]

    matrix = []
    i = 0
    while i < rows:
        row = []
        j = 0
        while j < cols:
            row.append(0)
            j += 1
        matrix.append(row)
        i += 1

    k = 1
    while k < len(sparse):
        r = sparse[k][0]
        c = sparse[k][1]
        val = sparse[k][2]
        matrix[r][c] = val
        k += 1

    return matrix


def add_sparse(m1, m2):
    if m1[0][0] != m2[0][0] or m1[0][1] != m2[0][1]:
        print("Dimensions mismatch")
        return None

    rows = m1[0][0]
    cols = m1[0][1]
    res = []

    i = 1
    j = 1
    while i < len(m1) and j < len(m2):
        r1, c1, v1 = m1[i]
        r2, c2, v2 = m2[j]

        if r1 < r2 or (r1 == r2 and c1 < c2):
            res.append([r1, c1, v1])
            i += 1
        elif r2 < r1 or (r1 == r2 and c2 < c1):
            res.append([r2, c2, v2])
            j += 1
        else:
            total = v1 + v2
            if total != 0:
                res.append([r1, c1, total])
            i += 1
            j += 1

    while i < len(m1):
        res.append(m1[i])
        i += 1

    while j < len(m2):
        res.append(m2[j])
        j += 1

    res.insert(0, [rows, cols, len(res)])
    return res


def display_sparse(sparse):
    print("\nRow\tCol\tVal")
    print("-" * 24)
    for entry in sparse:
        print(entry[0], "\t", entry[1], "\t", entry[2])


def display_matrix(matrix):
    for row in matrix:
        for x in row:
            print(x, end=" ")
        print()


def main():
    matrix1 = [
        [0, 0, 5, 0],
        [0, 2, 0, 0],
        [7, 0, 0, 4],
        [0, 0, 0, 1]
    ]

    matrix2 = [
        [0, 3, 0, 0],
        [0, 0, 6, 0],
        [2, 0, 0, 1],
        [0, 4, 0, 0]
    ]

    print("Matrix 1:")
    display_matrix(matrix1)
    sp1 = convert_to_sparse(matrix1)
    print("\nSparse 1:")
    display_sparse(sp1)

    print("\nMatrix 2:")
    display_matrix(matrix2)
    sp2 = convert_to_sparse(matrix2)
    print("\nSparse 2:")
    display_sparse(sp2)

    added = add_sparse(sp1, sp2)
    if added is not None:
        print("\nSparse Addition Result:")
        display_sparse(added)
        print("\nReconstructed Matrix Sum:")
        display_matrix(reconstruct_matrix(added))


if __name__ == "__main__":
    main()


def display_array(arr):
    print("\nCurrent 2D Array:")
    for row in arr:
        print(row)


def insert_row(arr, pos, new_row):
    if pos < 0 or pos > len(arr):
        print("Invalid row index")
        return
    arr.insert(pos, new_row)
    print("Row added successfully")
    display_array(arr)


def delete_row(arr, pos):
    if pos < 0 or pos >= len(arr):
        print("Invalid row index")
        return
    removed = arr.pop(pos)
    print("Removed Row:", removed)
    display_array(arr)


def search_element(arr, target):
    found = False
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] == target:
                print("Found at Row:", i, "Col:", j)
                found = True
            j += 1
        i += 1
    if not found:
        print("Element not found")
    return found


def rotate_clockwise(arr):
    if len(arr) == 0:
        print("Empty array")
        return
    rows = len(arr)
    cols = len(arr[0])
    for r in arr:
        if len(r) != cols:
            print("Array must be rectangular")
            return

    rotated = []
    j = 0
    while j < cols:
        new_row = []
        i = rows - 1
        while i >= 0:
            new_row.append(arr[i][j])
            i -= 1
        rotated.append(new_row)
        j += 1

    arr.clear()
    for row in rotated:
        arr.append(row)

    print("Rotated 90 degrees clockwise:")
    display_array(arr)


def main():
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    while True:
        print("\n===== 2D ARRAY OPERATIONS =====")
        display_array(arr)
        print("1. Insert Row")
        print("2. Delete Row")
        print("3. Search Element")
        print("4. Rotate 90 Degrees Clockwise")
        print("5. Display Array")
        print("6. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            try:
                pos = int(input("Enter index to insert row: "))
                if pos < 0 or pos > len(arr):
                    print("Position out of range")
                    continue
                vals = input("Enter row elements separated by space: ")
                row = list(map(int, vals.split()))
                if len(arr) > 0 and len(row) != len(arr[0]):
                    print("Row length mismatch")
                    continue
                insert_row(arr, pos, row)
            except ValueError:
                print("Invalid integer entered")
        elif ch == "2":
            try:
                pos = int(input("Enter row index to remove: "))
                delete_row(arr, pos)
            except ValueError:
                print("Invalid index")
        elif ch == "3":
            try:
                target = int(input("Enter value to search: "))
                search_element(arr, target)
            except ValueError:
                print("Invalid integer")
        elif ch == "4":
            rotate_clockwise(arr)
        elif ch == "5":
            display_array(arr)
        elif ch == "6":
            print("Terminating...")
            break
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()


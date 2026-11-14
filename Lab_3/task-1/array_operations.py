def display_array(arr):
    print("\nCurrent Array:", arr)


def insert_element(arr, pos, val):
    if pos < 0 or pos > len(arr):
        print("Invalid position")
        return
    arr.insert(pos, val)
    print("Inserted", val, "at index", pos)


def delete_element(arr, pos):
    if pos < 0 or pos >= len(arr):
        print("Invalid position")
        return
    val = arr.pop(pos)
    print("Deleted element:", val)


def search_element(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            print("Element", val, "found at index", i)
            return i
        i += 1
    print("Element", val, "not found")
    return -1


def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    print("Array reversed")


def main():
    arr = [10, 25, 30, 45, 50]

    while True:
        print("\n===== 1D ARRAY OPERATIONS =====")
        display_array(arr)
        print("1. Insert Element")
        print("2. Delete Element")
        print("3. Search Element")
        print("4. Reverse Array")
        print("5. Display Array")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                pos = int(input("Enter index to insert at: "))
                val = int(input("Enter value: "))
                insert_element(arr, pos, val)
            except ValueError:
                print("Invalid integer input")
        elif choice == "2":
            try:
                pos = int(input("Enter index to delete: "))
                delete_element(arr, pos)
            except ValueError:
                print("Invalid integer input")
        elif choice == "3":
            try:
                val = int(input("Enter value to search: "))
                search_element(arr, val)
            except ValueError:
                print("Invalid integer input")
        elif choice == "4":
            reverse_array(arr)
        elif choice == "5":
            display_array(arr)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()


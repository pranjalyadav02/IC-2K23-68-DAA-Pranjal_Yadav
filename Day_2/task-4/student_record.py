import time

students = [
    {"roll": 108, "name": "Pranjal", "marks": 88},
    {"roll": 102, "name": "Aman", "marks": 91},
    {"roll": 105, "name": "Bhavya", "marks": 76},
    {"roll": 101, "name": "Karan", "marks": 84},
    {"roll": 107, "name": "Sneha", "marks": 95},
    {"roll": 103, "name": "Rohan", "marks": 70},
    {"roll": 106, "name": "Ananya", "marks": 89},
    {"roll": 104, "name": "Varun", "marks": 82}
]


def bubble_sort(data, key):
    a = [dict(item) for item in data]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if a[j][key] > a[j + 1][key]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(data, key):
    a = [dict(item) for item in data]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][key] < a[min_idx][key]:
                min_idx = j
        if min_idx != i:
            temp = a[i]
            a[i] = a[min_idx]
            a[min_idx] = temp
    return a


def insertion_sort(data, key):
    a = [dict(item) for item in data]
    n = len(a)
    for i in range(1, n):
        cur = a[i]
        j = i - 1
        while j >= 0 and a[j][key] > cur[key]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = cur
    return a


def merge_sort(data, key):
    if len(data) <= 1:
        return [dict(item) for item in data]
    mid = len(data) // 2
    left = merge_sort(data[:mid], key)
    right = merge_sort(data[mid:], key)
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res


def quick_sort(data, key):
    a = [dict(item) for item in data]
    stack = [(0, len(a) - 1)]
    while len(stack) > 0:
        low, high = stack.pop()
        if low >= high:
            continue
        pivot = a[high][key]
        i = low - 1
        for j in range(low, high):
            if a[j][key] <= pivot:
                i += 1
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
        temp = a[i + 1]
        a[i + 1] = a[high]
        a[high] = temp
        p = i + 1
        stack.append((low, p - 1))
        stack.append((p + 1, high))
    return a


def heap_sort(data, key):
    a = [dict(item) for item in data]
    n = len(a)

    def heapify(size, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < size and a[l][key] > a[largest][key]:
            largest = l
        if r < size and a[r][key] > a[largest][key]:
            largest = r
        if largest != i:
            temp = a[i]
            a[i] = a[largest]
            a[largest] = temp
            heapify(size, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        temp = a[0]
        a[0] = a[i]
        a[i] = temp
        heapify(i, 0)
    return a


algorithms = {
    "1": ("Bubble Sort", bubble_sort),
    "2": ("Selection Sort", selection_sort),
    "3": ("Insertion Sort", insertion_sort),
    "4": ("Merge Sort", merge_sort),
    "5": ("Quick Sort", quick_sort),
    "6": ("Heap Sort", heap_sort)
}


def display_students(data):
    print("\n" + "-" * 40)
    print("{:<10} {:<18} {:<10}".format("Roll No.", "Name", "Marks"))
    print("-" * 40)
    for s in data:
        print("{:<10} {:<18} {:<10}".format(s["roll"], s["name"], s["marks"]))
    print("-" * 40)


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid]["roll"] == target:
            return mid
        elif data[mid]["roll"] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def compare_performance(data, key):
    print("\nSorting Performance Comparison:")
    print("=" * 45)
    results = []
    reps = 1000

    for name, algo in algorithms.values():
        t1 = time.perf_counter()
        for _ in range(reps):
            res = algo(data, key)
        t2 = time.perf_counter()
        avg = (t2 - t1) / reps
        results.append((name, avg))
        print("{:<18} {:.8f} s".format(name, avg))

    fastest = min(results, key=lambda x: x[1])
    slowest = max(results, key=lambda x: x[1])
    print("-" * 45)
    print("Fastest:", fastest[0], "with", fastest[1], "s")
    print("Slowest:", slowest[0], "with", slowest[1], "s")
    print("Difference:", slowest[1] - fastest[1], "s")


def main():
    global students
    while True:
        print("\nStudent Record Manager")
        print("1. Display All Records")
        print("2. Sort Records")
        print("3. Search Record by Roll No.")
        print("4. Compare Sorting Performance")
        print("5. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            display_students(students)
        elif ch == "2":
            print("\nSelect key:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Marks")
            k_choice = input("Enter option: ")
            field_map = {"1": "roll", "2": "name", "3": "marks"}
            if k_choice not in field_map:
                print("Invalid choice")
                continue
            key = field_map[k_choice]

            print("\nAlgorithms:")
            for num, (name, _) in algorithms.items():
                print(num + ".", name)
            a_choice = input("Enter choice: ")
            if a_choice not in algorithms:
                print("Invalid algorithm")
                continue
            name, algo = algorithms[a_choice]
            students = algo(students, key)
            print("\nSorted using", name)
            display_students(students)
        elif ch == "3":
            students = merge_sort(students, "roll")
            val = input("Enter roll to search: ")
            if not val.isdigit():
                print("Enter an integer")
                continue
            r = int(val)
            idx = binary_search(students, r)
            if idx != -1:
                print("Record found:")
                display_students([students[idx]])
            else:
                print("Record not found")
        elif ch == "4":
            print("\nCompare by:")
            print("1. Roll Number")
            print("2. Name")
            print("3. Marks")
            k_choice = input("Enter option: ")
            field_map = {"1": "roll", "2": "name", "3": "marks"}
            if k_choice not in field_map:
                print("Invalid choice")
                continue
            compare_performance(students, field_map[k_choice])
        elif ch == "5":
            print("Done")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()


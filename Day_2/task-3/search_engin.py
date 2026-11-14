documents = {
    "algorithm": 101,
    "array": 102,
    "binary": 103,
    "computer": 104,
    "database": 105,
    "data": 106,
    "development": 107,
    "function": 108,
    "graph": 109,
    "hashing": 110,
    "index": 111,
    "java": 112,
    "keyword": 113,
    "linked": 114,
    "machine": 115,
    "network": 116,
    "object": 117,
    "program": 118,
    "python": 119,
    "query": 120,
    "recursion": 121,
    "search": 122,
    "sorting": 123,
    "stack": 124,
    "structure": 125,
    "tree": 126,
    "variable": 127,
    "website": 128,
    "software": 129,
    "compiler": 130
}


def binary_search(words, target):
    low = 0
    high = len(words) - 1
    count = 0
    while low <= high:
        mid = (low + high) // 2
        count += 1
        if words[mid][0] == target:
            return words[mid][1], count
        elif words[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None, count


def hash_func(word, size):
    val = 0
    for ch in word:
        val = (val * 31 + ord(ch)) % size
    return val


class ChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = []
        for _ in range(size):
            self.table.append([])

    def insert(self, word, doc_id):
        idx = hash_func(word, self.size)
        self.table[idx].append((word, doc_id))

    def search(self, target):
        idx = hash_func(target, self.size)
        comparisons = 0
        bucket = self.table[idx]
        i = 0
        while i < len(bucket):
            comparisons += 1
            if bucket[i][0] == target:
                return bucket[i][1], comparisons
            i += 1
        return None, comparisons


class ProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, word, doc_id):
        idx = hash_func(word, self.size)
        i = 0
        while i < self.size:
            pos = (idx + i) % self.size
            if self.table[pos] is None:
                self.table[pos] = (word, doc_id)
                return
            elif self.table[pos][0] == word:
                self.table[pos] = (word, doc_id)
                return
            i += 1
        raise OverflowError("Table is full")

    def search(self, target):
        idx = hash_func(target, self.size)
        probes = 0
        i = 0
        while i < self.size:
            pos = (idx + i) % self.size
            probes += 1
            if self.table[pos] is None:
                return None, probes
            if self.table[pos][0] == target:
                return self.table[pos][1], probes
            i += 1
        return None, probes


sorted_words = sorted(documents.items())
table_size = 37

chaining_table = ChainingHashTable(table_size)
probing_table = ProbingHashTable(table_size)

for word, doc_id in documents.items():
    chaining_table.insert(word, doc_id)
    probing_table.insert(word, doc_id)


def search_word(target):
    target = target.strip().lower()
    print("\nSearching for:", target)
    print("=" * 45)

    doc1, count1 = binary_search(sorted_words, target)
    doc2, count2 = chaining_table.search(target)
    doc3, count3 = probing_table.search(target)

    print("\n1. Binary Search:")
    if doc1 is not None:
        print("Found with Document ID:", doc1)
    else:
        print("Not Found")
    print("Comparisons:", count1)

    print("\n2. Chaining Hash Table:")
    if doc2 is not None:
        print("Found with Document ID:", doc2)
    else:
        print("Not Found")
    print("Comparisons:", count2)

    print("\n3. Linear Probing Hash Table:")
    if doc3 is not None:
        print("Found with Document ID:", doc3)
    else:
        print("Not Found")
    print("Probes:", count3)

    print("\nSummary:")
    print("-" * 45)
    print("{:<25} {:<15}".format("Method", "Cost"))
    print("-" * 45)
    print("{:<25} {:<15}".format("Binary Search", count1))
    print("{:<25} {:<15}".format("Chaining", count2))
    print("{:<25} {:<15}".format("Linear Probing", count3))
    print("-" * 45)


def main():
    print("Simplified Search Engine Simulator")
    print("Total dictionary terms:", len(documents))

    while True:
        print("\n1. Search word")
        print("2. Display all words")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            word = input("Enter keyword: ")
            if len(word.strip()) == 0:
                print("Empty input")
                continue
            search_word(word)
        elif choice == "2":
            print("\nDictionary entries:")
            for w, d in sorted_words:
                print(w, "->", d)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()


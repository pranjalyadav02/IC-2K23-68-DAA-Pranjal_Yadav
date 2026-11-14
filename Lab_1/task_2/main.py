# Show how a stack and a queue process the same tasks

def stack_order(tasks):
    stack = tasks.copy()
    result = []
    while stack:
        result.append(stack.pop())
    return result


def queue_order(tasks):
    queue = tasks.copy()
    result = []
    while queue:
        result.append(queue.pop(0))
    return result


if __name__ == "__main__":
    tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
    print("Arrival order:", tasks)
    print("Stack (LIFO):", stack_order(tasks))
    print("Queue (FIFO):", queue_order(tasks))

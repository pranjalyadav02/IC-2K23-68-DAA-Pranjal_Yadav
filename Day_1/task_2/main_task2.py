from stack_order import StackOrder

if __name__ == "__main__":
    tasks = ["Task1", "Task2", "Task3", "Task4", "Task5"]
    print("Arrival order:", tasks)
    runner = StackOrder()
    stk_order = runner.process_stack(tasks)
    print("Stack completion order:")
    for t in stk_order:
        print(t, end=" ")
    print()
    q_order = runner.process_queue(tasks)
    print("Queue completion order:")
    for t in q_order:
        print(t, end=" ")
    print()


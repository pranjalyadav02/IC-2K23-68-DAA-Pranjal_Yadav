class StackOrder:
    def process_stack(self, tasks):
        stack = []
        top = -1
        i = 0
        while i < len(tasks):
            stack.append(tasks[i])
            top += 1
            i += 1
        result = []
        while top >= 0:
            result.append(stack[top])
            top -= 1
        return result

    def process_queue(self, tasks):
        queue = []
        i = 0
        while i < len(tasks):
            queue.append(tasks[i])
            i += 1
        result = []
        front = 0
        while front < len(queue):
            result.append(queue[front])
            front += 1
        return result


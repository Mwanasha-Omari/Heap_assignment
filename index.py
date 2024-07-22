class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._percolate_up(len(self.heap) - 1)

    def _percolate_up(self, i):
        while i > 0:
            parent = (i - 1) 
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def remove_max(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            max_val = self.heap[0]
            self.heap[0] = self.heap.pop()
            self._percolate_down(0)
            return max_val

    def _percolate_down(self, i):
        while 2 * i + 1 < len(self.heap):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            max_child = left_child

            if right_child < len(self.heap) and self.heap[right_child] > self.heap[left_child]:
                max_child = right_child

            if self.heap[i] < self.heap[max_child]:
                self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
                i = max_child
            else:
                break

    def peek_max(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
    
heap = MaxHeap()
heap.insert(5)
heap.insert(10)
heap.insert(7)
print(heap.remove_max())  
print(heap.peek_max())  
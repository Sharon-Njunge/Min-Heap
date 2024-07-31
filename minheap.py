import heapq
class MinHeap:
    def __init__(self):
        self.heap = []
    def insert(self, value):
        heapq.heappush(self.heap, value)
    def extract_min(self):
        if not self.heap:
            raise IndexError("Extracting from an empty heap")
        return heapq.heappop(self.heap)
    def peek(self):
        if not self.heap:
            raise IndexError("Peeking from an empty heap")
        return self.heap[0]

min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(1)
min_heap.insert(2)
print(min_heap.peek())  
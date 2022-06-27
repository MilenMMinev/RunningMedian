from heapq import heappush, heappop


class RunningMedian:
    """
    A simple data structure that calculates running median of its elements.
    """
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def add(self, number):
        if not self.min_heap or number > self.min_heap[0]:
            heappush(self.min_heap, number)
        else:
            heappush(self.max_heap, -number)
        self.rebalance()

    def items(self):
        return self.min_heap + [-x for x in self.max_heap]

    def rebalance(self):
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -heappop(self.min_heap))

    def median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0])/2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]


if __name__ == "__main__":
    rm = RunningMedian()
    vals = [0, 1, 2]
    for v in vals:
        rm.add(v)
    print("median: ", rm.median())


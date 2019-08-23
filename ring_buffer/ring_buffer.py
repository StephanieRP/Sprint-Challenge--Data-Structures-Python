class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # adding item to current
        self.storage[self.current] = item
    # checking if current is the length of storage or greater
        if self.current >= len(self.storage) - 1:
            # if it is, we are adding item to the head of the array
            self.current = 0
        else:
                # else, adding it to the end and incrementing current
            self.current += 1

    def get(self):
            # returning values only when it is not null
        return [x for x in self.storage if x is not None]

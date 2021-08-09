class minHeapPQ:
    def __init__(self, collection=None):
        self.heap = []

    def upheap(self, heap, i):
        # AFter insertion, must now start from the newly inserted node and work upward to ensure the heap-order is not violatedf
        p_i = (i - 1) // 2  # p_i = parent index
        # Return if we arrive at the root node
        if p_i < 0:
            return
        # Swap nodes if current is less than the parent
        if heap[i] < heap[p_i]:
            self.swap(heap, i, p_i)
            self.upheap(heap, p_i)

    def downheap(self, heap, i):
        # After deletion, must now start from the root and work downward to ensure the heap-order is not violated
        c_i = 2 * i + 1  # c_i = child index
        # Return if we reach the end of the heap
        if c_i >= len(self.heap):
            return

        # If node has 2 children, then swap w/ smaller child node
        if c_i + 1 < len(self.heap) and heap[c_i] > heap[c_i + 1]:
            c_i += 1

        # Swap if child node is greater than current node
        if heap[c_i] < heap[i]:
            self.swap(heap, c_i, i)
            self.downheap(heap, c_i)

    def insert(self, value):
        self.heap.append(value)
        # After insertion, must upheap.
        self.upheap(self.heap, len(self.heap) - 1)

    def delete_Min(self):
        # Swap root w/ last node
        self.swap(self.heap, len(self.heap) - 1, 0)
        # Delete last node
        element = self.heap.pop()
        # After deletion, must downheap
        self.downheap(self.heap, 0)
        return element

    def swap(self, heap, i, j):
        # A simple/straightforward swap function
        heap[i], heap[j] = heap[j], heap[i]

    def print_(self):
        # Prints the array self.heap
        print(self.heap)


def main():
    h = minHeapPQ()
    print("\n------------ Min Heap - Priority Queue ------------")
    insert = True
    while (True):
        if insert:
            print(
                "\nEnter an INTEGER into the Min Heap.\nEnter \"f\" or \"F\" to finish.\n")
            choice = validate()
            if choice not in (["f", "F"]):
                h.insert(choice)
                continue
        print()
        h.print_()
        print("\n1. Insert more values\n2. Delete min\nF. Quit\n")
        choice = validate()
        if choice == 1:
            insert = True
            continue
        elif choice == 2:
            h.delete_Min()
            insert = False
            continue
        elif choice in ["f", "F"]:
            break


def validate():
    while True:
        try:
            choice = input("Please enter a valid choice: ")
            if choice in (["f", "F"]):
                return choice
            return int(choice)
        except ValueError:
            print("That was not a valid choice...\n")


if __name__ == "__main__":
    main()

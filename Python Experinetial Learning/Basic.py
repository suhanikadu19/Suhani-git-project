class MemoryBlock:
    def __init__(self, size):
        self.size = size
        self.process = None
        self.next = None


# Create memory
head = MemoryBlock(1000)

# Allocate memory
head.process = "P1"
head.size = 400

# Display memory
print("Memory Status:")

if head.process is None:
    print("Free Memory:", head.size, "KB")
else:
    print(head.process, "is using", head.size, "KB")
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.count = 0
        self.table = [None] * initial_size
        self.load_factor = 0.75

    def _get_index(self, key) -> int:
        return hash(key) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0

        for node in old_table:
            current = node
            while current:
                self.insert(current.key, current.value)
                current = current.next

    def insert(self, key, value) -> None:
        index = self._get_index(key)

        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.count += 1

        if self.get_load_factor() > self.load_factor:
            self._resize()

    def get_load_factor(self) -> float:
        return self.count / self.size

    def get(self, key: str):
        index = self._get_index(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key) -> bool:
        index = self._get_index(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.count -= 1
                return True
            prev = current
            current = current.next
        return False

    def __str__(self) -> str:
        result = []
        for i in range(self.size):
            chain = []
            current = self.table[i]
            while current:
                chain.append(f"{current.key}: {current.value}")
                current = current.next
            result.append(f"[{i}] -> {' -> '.join(chain) if chain else 'None'}")
        return "\n".join(result)



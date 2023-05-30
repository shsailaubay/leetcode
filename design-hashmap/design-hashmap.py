class MyHashMap:

    def __init__(self):
        self.table = []
    
    def _coord(self, key: int) -> tuple[int, int]:
        return divmod(key, 1000)

    def put(self, key: int, value: int) -> None:
        r, c = self._coord(key)
        if r >= len(self.table):
            self.table.extend([-1] * (r - len(self.table) + 1))
        if self.table[r] == -1:
            self.table[r] = [-1] * 1001
        self.table[r][c] = value
        

    def get(self, key: int) -> int:
        r, c = self._coord(key)
        if len(self.table) <= r:
            return -1
        if self.table[r] == -1:
            return -1
        return self.table[r][c]

    def remove(self, key: int) -> None:
        r, c = self._coord(key)
        if len(self.table) <= r:
            return
        if self.table[r] == -1:
            return
        self.table[r][c] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
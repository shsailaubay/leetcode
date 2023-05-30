class MyHashSet:

    def __init__(self):
        self.list = [False] * 1001
        
    def _get_bucket(self, key: int):
        return divmod(key, 1000)

    def add(self, key: int) -> None:
        i, b = self._get_bucket(key)
        if self.list[i] == False:
            self.list[i] = [False] * 1001
        self.list[i][b] = True
        

    def remove(self, key: int) -> None:
        i, b = self._get_bucket(key)
        if self.list[i] != False:
            self.list[i][b] = False
        

    def contains(self, key: int) -> bool:
        i, b = self._get_bucket(key)
        if self.list[i] == False:
            return False
        return self.list[i][b]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
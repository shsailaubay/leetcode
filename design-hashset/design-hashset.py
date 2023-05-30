from array import array

class MyHashSet:

    def __init__(self):
        self.list = [False]
        
    def _get_bucket(self, key: int):
        return divmod(key, 1000)

    def add(self, key: int) -> None:
        i, b = self._get_bucket(key)
        if i >= len(self.list):
            self.list.extend([False] * (i - len(self.list) + 1))
        if self.list[i] == False:
            self.list[i] = array('B', [0] * 1001)
        self.list[i][b] = 1
        

    def remove(self, key: int) -> None:
        i, b = self._get_bucket(key)
        if i < len(self.list) and self.list[i] != False:
            self.list[i][b] = 0
        

    def contains(self, key: int) -> bool:
        i, b = self._get_bucket(key)
        if i >= len(self.list) or self.list[i] == False:
            return False
        return self.list[i][b]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
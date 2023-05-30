from array import array

class MyHashSet:

    def __init__(self):
        self.bitVector = array('H', [0] * 62501)
    
    def _get_coord(self, key: int) -> tuple[int, int]:
        return divmod(key, 16)
    
    def _is_set_bit(self, row, col) -> bool:
        return (self.bitVector[row] & (1 << col)) != 0

    def add(self, key: int) -> None:
        row, col = self._get_coord(key)
        self.bitVector[row] |= 1 << col

    def remove(self, key: int) -> None:
        row, col = self._get_coord(key)
        if self._is_set_bit(row, col):
            self.bitVector[row] &= ~(1 << col)

    def contains(self, key: int) -> bool:
        row, col = self._get_coord(key)
        return self._is_set_bit(row, col)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
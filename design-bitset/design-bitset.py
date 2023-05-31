class Bitset:
    ROW_SIZE = 32

    def __init__(self, size: int):
        self.last_row_ind, self.last_row_size = divmod(size, self.ROW_SIZE)
        self.one_count = 0
        self.size = size
        self.arr = [0] * (self.last_row_ind + (1 if self.last_row_size > 0 else 0))
    
    def _coord(self, ind: int) -> tuple[int, int]:
        return divmod(ind, self.ROW_SIZE)

    def _is_set_bit(self, row, col) -> bool:
        return (self.arr[row] & (1 << col)) != 0

    def fix(self, idx: int) -> None:
        row, col = self._coord(idx)
        if not self._is_set_bit(row, col):
            self.arr[row] |= 1 << col
            self.one_count += 1

    def unfix(self, idx: int) -> None:
        row, col = self._coord(idx)
        if self._is_set_bit(row, col):
            self.arr[row] &= ~(1 << col)
            self.one_count -= 1

    def flip(self) -> None:
        self.arr = [e ^ 0xFFFFFFFF for e in self.arr]
        self.one_count = self.size - self.one_count

    def all(self) -> bool:
        return self.one_count == self.size

    def one(self) -> bool:
        return self.one_count > 0

    def count(self) -> int:
        return self.one_count
    
    @cache
    def _decToBinStr(self, val: int) -> str:
        return str(bin(val))[34:1:-1]

    def _rowToBinStr(self, row: int) -> str:
        val = self._decToBinStr(self.arr[row])
        if row == self.last_row_ind:
            if len(val) > self.last_row_size:
                return val[:self.last_row_size]
            return val.ljust(self.last_row_size, '0')
        return val.ljust(self.ROW_SIZE, '0')

    def toString(self) -> str:
        print(self.arr)
        return "".join([self._rowToBinStr(r) for r in range(0, len(self.arr))])


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
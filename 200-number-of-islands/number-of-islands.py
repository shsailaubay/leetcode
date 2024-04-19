class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        been: Set[Tuple[str, str]] = set()

        def is_point_exist(x, y) -> bool:
            if x < 0 or y < 0:
                return False
            try:
                grid[x][y]
                return True
            except IndexError:
                return False

        def make_island(x, y, coord: Set[Tuple[str, str]]):
            
            if (x, y) in been:
                return 
            
            been.add((x,y))
            if grid[x][y] == "1":
                coord.add((x, y))

            variants = [
                (x, y - 1),
                (x, y + 1),
                (x - 1, y),
                (x + 1, y)
            ]

            for i, j in variants:
                if not is_point_exist(i, j):
                    continue
                s = (i, j)
                if s in been:
                    continue
                if grid[i][j] == "1":
                    coord.add(s)
                    make_island(i, j, coord)
            
            return

        islands = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "0":
                    continue
                island = set()
                make_island(i, j, island)

                if len(island) != 0:
                    islands.append(island)

        return len(islands)

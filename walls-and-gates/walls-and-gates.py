class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        deq = collections.deque([(i, j, 0) for i in range(len(rooms)) for j in range(len(rooms[0])) if rooms[i][j] == 0])
        row_max = len(rooms) - 1
        col_max = len(rooms[0]) - 1
        while deq:
            row, col, steps = deq.popleft()
            for new_row, new_col in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= new_row <= row_max and 0 <= new_col <= col_max and rooms[new_row][new_col] == 2147483647:
                    rooms[new_row][new_col] = steps + 1
                    deq.append((new_row, new_col, steps + 1))
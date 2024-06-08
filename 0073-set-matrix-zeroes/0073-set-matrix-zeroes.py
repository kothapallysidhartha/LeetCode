class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        len_m = len(matrix)
        len_n = len(matrix[0])
        rows, cols = set(), set()

        for i in range(len_m):
            for j in range(len_n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(len_m):
            for j in range(len_n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

        print(matrix)


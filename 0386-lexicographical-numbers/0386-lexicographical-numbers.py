class Solution:
    def lexicalOrder(self, n):
        res = []
        cur = 1
        for i in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                if cur >= n:
                    cur //= 10
                cur += 1
                while cur % 10 == 0:
                    cur //= 10
        return res

# Example usage:
# solution = Solution()
# result = solution.lexicalOrder(100)
# print(result)

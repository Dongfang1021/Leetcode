class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)
        dp = [0]*K + [1]
        for i in range(K - 1, -1, -1):
            for d in digits:
                if d < S[i]:
                    dp[i] += len(digits)**(K - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i + 1]
        return dp[0] + sum(len(digits)**i for i in range(1, K))
# The path to the Xerox

n, k = map(int, input().split())
i = max(n // k, 1)
ans1 = abs(n - k * i)
i += 1
ans2 = abs(n - k * i)
print(min(ans1, ans2))
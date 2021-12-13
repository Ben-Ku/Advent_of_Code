
with open('input6.1.txt') as file:
    s = list(map(int, file.read().split(',')))

print(s)

dp = [0]*9
for i in s:
    dp[i] += 1

for _ in range(256):
    temp_dp = [0]*9
    for j in range(8):
        if j == 0:
            temp_dp[6] += dp[0]
            temp_dp[8] += dp[0]
        temp_dp[j] += dp[j+1]
    dp = temp_dp

res = sum(dp)

print(res)

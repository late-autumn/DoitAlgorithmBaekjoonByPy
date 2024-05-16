n = input()

achievementList = list(map(int, input().split()))

sum = sum(achievementList)
maxScore = max(achievementList)

print(sum * 100 / maxScore / int(n))

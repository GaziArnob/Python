# 

sqaures = []

for i in range(5):
    sqaures.append(i*i)

print(sqaures)

sq = [i*i for i in range(6) if i%2 !=0]

print(sq)


nums = [-2 ,-3,-4,4,4,1,2,3]

nums = [9 if val < 0 else val for val in nums ]

print(nums)
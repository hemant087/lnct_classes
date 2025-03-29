# x = 10
# y = 20
# z = x+y




# print(z)


lst = [1,2,3,4,5,6]
temp = []
for i in range(len(lst)):
    for j in range(len(lst)):
        if i<j:
            temp.append(lst[i:j])

ans = {}
for i in temp:
    ans[sum(i)] = i

print(ans)

print(ans[max(ans.keys())], max(ans.keys()))

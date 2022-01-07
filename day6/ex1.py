def calc(n,*nums): #0個でするとエラーがおきる　*numsだけだったら0個でもOK
    return n+sum(nums)

result=calc(2,3,5)
print(result)

result=calc(5) #nに5が入る
print(result)

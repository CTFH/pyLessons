for i in range(1,10):
    if i % 2==0:
        continue
    for j in range(1,10):
        print(f'{i}*{j}={i*j}',end=' ')
        if i*j > 50:
            break
    print()
print()

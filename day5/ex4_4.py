for i in range(9):
    if(i+1)%2==0: #奇数の段のみ計算
        continue
    for j in range(9):
        if(i+1)*(j+1)>50: #答えが50を超えたら計算中止
            break
        print(f'{i+1}×{j+1}={(i+1)*(j+1)}')

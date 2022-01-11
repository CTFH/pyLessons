#計算データの入力
def int_input(msg):
    return int(input('{}を入力してください>>'.format(msg)))

def calc_payment(amount, people=2):
#割り勘の計算
    dnum = amount/people #総額を人数で割る（端数も保持）
    pay = dnum//100*100 #100円未満を切り捨てる  //割り算の商
    if dnum > pay: #元の値と比較して、
        pay =int(pay +100) #小さければ100円未満があったので上乗せ

#幹事の支払額の計算
    payorg = amount -pay * (people -1)

    return pay, payorg


def show_payment(pay, payorg, people=2):
#結果の表示
    print('***支払額***')
    print('1人あたり{}円({}人)、幹事は{}円です'
        .format(pay, people -1, payorg))


#計算データの入力
amount = int_input('支払総額');
people = int_input('参加人数');

#割り勘の計算
[pay, payorg] = calc_payment(amount, people)

#結果の表示
show_payment(pay, payorg, people)

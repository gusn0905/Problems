# D3 영준이의 카드 카운팅
T = int(input())
error_list = []
result_list = []
for i in range(T):
    cards = input()
    cards = cards.rstrip() # 우측 공백 제거 위해
    card_list = []
    for j in range(0,len(cards),3):
        temp = list(cards[j:j+3])
        card_list.append(temp)
    spade,diamond,heart,clover = [],[],[],[]
    for j in range(len(card_list)):
        if card_list[j][0] == 'S':
            temp = ''.join(card_list[j][1:3])
            spade.append(temp)
        elif card_list[j][0] == 'D':
            temp = ''.join(card_list[j][1:3])
            diamond.append(temp)
        elif card_list[j][0] == 'H':
            temp = ''.join(card_list[j][1:3])
            heart.append(temp)
        else:
            temp = ''.join(card_list[j][1:3])
            clover.append(temp)
    error = 0
    result1 =[len(spade),len(diamond),len(heart),len(clover)]
    result2 =[len(set(spade)),len(set(diamond)),len(set(heart)),len(set(clover))]
    for j in range(len(result1)):
        if result1[j] != result2[j]:
            error+=1
    error_list.append(error)
    temp = []
    for j in range(len(result1)):
        temp.append(13-result1[j])
    result_list.append(temp)

for i in range(T):
    if error_list[i] != 0:
        print("#{0} {1}".format(i+1,'ERROR'))
    else:
        print("#{}".format(i+1),end=' ')
        for j in range(4):
            print(result_list[i][j],end=' ')
        print()
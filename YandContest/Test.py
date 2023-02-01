n = int(input(''))
ai = input('').split(' ')[:n]
ai = [int(i) for i in ai]

for i in ai:
    pos_i = ai.index(i)
    if len(ai) == 1:
        print(0)
        break
    elif pos_i != ai[-2]:
        if ai[pos_i] > ai[pos_i+1]:
            print(-1)
            break
    print(ai[-1] - ai[0])
    break

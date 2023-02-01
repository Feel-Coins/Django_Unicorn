n = int(input(''))
ai = input('').split(' ')[:n]
try:
    for i in ai:
        ind = ai.index(i)
        if ai[ind] > ai[ind+1]:
            print(-1)
            break
        else:
            napolnator = int(ai[-1]) - int(ai[0])
            print(napolnator)
            break
except IndexError:
    pass
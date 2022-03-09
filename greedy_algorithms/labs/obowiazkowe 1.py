def min_tankowan(S,bak):
    gdzie_jestem = 0
    pkt_koncowy = len(S)-1
    ile_tankowan = 0
    i = 0
    while i != pkt_koncowy:
        if i >= len(S):
            return ile_tankowan
        if bak - S[i] + gdzie_jestem < 0:
            gdzie_jestem = S[i-1]
            ile_tankowan += 1
        elif bak - S[i] + gdzie_jestem == 0:
            gdzie_jestem = S[i]
            ile_tankowan += 1
            i += 1
        else:
            i += 1
    return ile_tankowan
S = [1, 2, 4, 9, 14, 19, 21, 22, 25, 30, 35]
print(min_tankowan(S,5))
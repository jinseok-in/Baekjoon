gwa_score = []
jeon_score = []
hak_score = []

for i in range(20):
    t, h, g = map(str, input().split())
    if g == 'P':
        continue
    else :
        if g == 'A+' :
            gwa_score.append(4.5)
            hak_score.append(float(h))
        elif g == 'A0' :
            gwa_score.append(4.0)
            hak_score.append(float(h))
        elif g == 'B+' :
            gwa_score.append(3.5)
            hak_score.append(float(h))
        elif g == 'B0' :
            gwa_score.append(3.0)
            hak_score.append(float(h))
        elif g == 'C+' :
            gwa_score.append(2.5)
            hak_score.append(float(h))
        elif g == 'C0' :
            gwa_score.append(2.0)
            hak_score.append(float(h))
        elif g == 'D+' :
            gwa_score.append(1.5)
            hak_score.append(float(h))
        elif g == 'D0' :
            gwa_score.append(1.0)
            hak_score.append(float(h))
        elif g == 'F' :
            gwa_score.append(0.0)
            hak_score.append(float(h))
            
for i in range(len(gwa_score)) :    
    jeon_score.append(gwa_score[i]*hak_score[i])

print(sum(jeon_score)/sum(hak_score))

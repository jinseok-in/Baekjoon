def solution(data, ext, val_ext, sort_by):
    arr_index = []
    r = []
    a = 0
    if sort_by == 'date':
        a=1
    elif sort_by == 'maximum':
        a=2
    elif sort_by == 'remain':
        a=3
    if ext == 'code' :
        for i in range(len(data)) :
            if data[i][0] < val_ext :
                arr_index.append(i)
    elif ext == 'date' :
        for i in range(len(data)) :
            if data[i][1] < val_ext :
                arr_index.append(i)         
    elif ext == 'maximum' :
        for i in range(len(data)) :
            if data[i][2] < val_ext :
                arr_index.append(i)
    else :
        for i in range(len(data)) :
            if data[i][3] < val_ext :
                arr_index.append(i)
    for i in arr_index :
        r.append(data[:][i])
    answer = sorted(r,key=lambda x:x[a])
    return answer

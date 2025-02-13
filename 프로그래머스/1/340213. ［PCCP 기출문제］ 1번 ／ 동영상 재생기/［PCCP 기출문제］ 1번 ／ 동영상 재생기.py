def solution(video_len, pos, op_start, op_end, commands):
    
    def change(time) :
        time_sp = time.split(":")
        time = int(time_sp[0])*60 + int(time_sp[1])
        return time
    
    def reChange(time) :
        time_m = str(time//60)
        time_s = str(time%60)
        if len(time_m) == 1 :
            time_m = f"0{time_m}"
        if len(time_s) == 1 :
            time_s = f"0{time_s}"
        return f"{time_m}:{time_s}"

    video_len = change(video_len)
    pos = change(pos)
    op_start = change(op_start)
    op_end = change(op_end)

    for i in range(len(commands)) :
        if (pos <= op_end) and (pos >= op_start) :
            pos = op_end
        if commands[i] == "next" :
            pos += 10
            if pos >= video_len :
                pos = video_len
        elif commands[i] == "prev" :
            pos -= 10
            if pos <= 0 :
                pos = 0
    
    if (pos <= op_end) and (pos >= op_start) :
        return reChange(op_end)
    else :
        return reChange(pos)
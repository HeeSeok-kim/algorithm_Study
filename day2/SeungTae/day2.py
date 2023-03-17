s = "09:13:50AM"

def timeConversion(s):
    if s[-2:] == "AM":
        hh = int(s[0:2])
        s = s[2:-2]
        if hh==12:
            s = "00" +s
            return s
        elif hh<10:
            s = "0"+ str(hh) + s
            return s
        else:
            s = str(hh) + s
    if s[-2:] == "PM":
        hh = int(s[0:2])
        s = s[2:-2]
        if(hh==12):
            s = "12" + s
            return s
        elif(1<=hh and hh<12):
            hh+=12
        else:
            return
        s = str(hh)+ s
    return s

print(timeConversion(s))

# 인텔리제이 깃 연동
# 오류 이유 : am 12시가 00시이다.

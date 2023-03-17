global s
s = "12:13:50PM"

def timeConversion(s):
    if s[-2:] == "PM":
        hh = int(s[0:2])
        s = s[2:-2]
        if(hh==12):
            s = "00" + s
            print(s)
            return
        elif(1<=hh and hh<12):
            hh+=12
        else: return
        s = str(hh)+ s
    print(s)

timeConversion(s)

# 인텔리제이 깃 연동

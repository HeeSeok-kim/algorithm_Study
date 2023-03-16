from datetime import datetime

def timeConversion(s):
    time_obj = datetime.strptime(s, "%I:%M:%S%p")
    time_str_24hr = time_obj.strftime("%H:%M:%S")

    return time_str_24hr


s = "07:05:45PM"
print(timeConversion(s))

#!usr/bin/env python3
def timeConversion(s):
    if s.endswith("AM"):
        s=s.strip("AM")
        x=s.split(':')
        if x[0]=='12':
            x[0]='00'
            result=':'.join(x)
            return result
        else:
            result=':'.join(x)
            return result
    elif s.endswith("PM"):
        s=s.strip("PM")
        x=s.split(':')
        if x[0]=='12':
            result=':'.join(x)
            return result
        else:
            x[0]=str(int(x[0])+12)
            result=':'.join(x)
            return result

s="12:45:54PM"
result = timeConversion(s)
print(result)

TIMES = [["CRO", 7], ["NGA", 2], ["AWA", 2], ["SIM", 2], ["BOX", 1], ["KAN", 1], ["RAR", 3], ["JOH", 2]]




time = float(input("What time do you want to depart Wellington in 24 hour time? (e.g. 14.34) "))



hour = time // 1
minute = (time % 1) * 100
for time in TIMES:
    print(time)
    minute += time[1]
    if minute >= 60:
        hour += 1
        minute -= 60
    #print(minute)
    if minute < 10:
        print("{:.0f}:0{:.0f}".format(hour, minute))
    else:
        print("{:.0f}:{:.0f}".format(hour, minute))

#emily and olivia
#28/02
#ex 9

#list
TIMES = [["Crofton Downs", 7],["Ngaio", 2],["Awarua St", 2],["Simla Cres", 2],["Box Hill", 1],["Kandallah", 2],["Raroa", 3],["Johnsonville", 2]]

def time_calculation(i):
    hour = i // 1
    minute = i % 1 * 100
    for time in TIMES:
        print(time)
        minute += time[1]
        if minute >= 60:
            hour += 1
            minute -= 60
        if minute < 10:
            print("{:.0f}:0{:.0f}".format(hour, minute))
        else:
            print("{:.0f}:{:.0f}".format(hour, minute))
        

#main routine
time_calculation(float(input("What time do you want to depart Wellington (in 24 hour time e.g. 13.01)? ")))

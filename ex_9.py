#emily and olivia
#28/02
#ex 9

#declaring constant
TIMES = [["Crofton Downs", 7],["Ngaio", 2],["Awarua St", 2],["Simla Cres", 2],["Box Hill", 1],["Kandallah", 2],["Raroa", 3],["Johnsonville", 2]]

#the function that calculates and outputs the timetable
def time_calculation(i):
    print("-----------------")
    #splitting the time into hours and minutes
    hour = i // 1
    minute = i % 1 * 100
    #adding the departure time to the start of the list
    TIMES.insert(0, ["Wellington", 0])
    #adding and outputting times
    for time in TIMES:
        minute += time[1]
        #rolling over to the next hour
        if minute >= 60:
            hour += 1
            minute -= 60
        #making sure the output has the right amount of digits
        if minute < 9:
            print("{}  {:.0f}:0{:.0f}".format(time[0], hour, minute), end = ". ")
        else:
            print("{}  {:.0f}:{:.0f}".format(time[0], hour, minute), end = ". ")

#main routine
#getting input - depart. time
time_calculation(float(input("What time do you want to depart Wellington (in 24 hour time e.g. 13.01)? ")))


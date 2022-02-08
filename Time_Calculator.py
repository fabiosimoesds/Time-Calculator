def add_time(tm1, tm2, wkday=None):
    tm1_list = tm1.split()
    hour1_list = tm1_list[0].split(':')
    hour2_list = tm2.split(':')
    actual_time = int(hour1_list[0])
    weekdays = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thrusday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

# Transforming Hours to a Whole Number first
    if tm1_list[1] == 'PM':
        actual_time += 12


    minutes = int(hour1_list[1]) + int(hour2_list[1])
    added_hours = actual_time + int(hour2_list[0])


# Transforming Minutes to Hours if needed
    if minutes > 60:
        extra = minutes//60
        minutes = minutes % 60
        if extra != 0:
            added_hours = actual_time + int(hour2_list[0]) + extra

    added_time = added_hours % 24  # To find the hours of the day
    extra_days = added_hours // 24  # To find if there is any extra day


# Transforming Hours back to AM PM style
    if added_time > 12:
        added_time -= 12
        PmAm = 'PM'
    elif added_time == 0:
        added_time = 12
        PmAm = 'AM'
    else:
        PmAm = 'AM'

# Adding 0 before the minute if this is a lonely digit
    if len(str(minutes)) == 1:
        minutes = '0' + str(minutes)

#Finding days of the week
    if wkday != None:
        for key, value in weekdays.items():
            if wkday.capitalize() == value:
                sum_wk = key + extra_days
        if sum_wk > 7:
            sum_wk -= 7
            wkday = weekdays[sum_wk]
        else:
            wkday = weekdays[sum_wk]




# Conditional Print statement
    if extra_days == 1 :
        if wkday != None:
            print(f'{added_time}:{minutes} {PmAm}, {wkday.capitalize()} (next Day)')
        else:
            print(f'{added_time}:{minutes} {PmAm} (next Day)')
    elif extra_days > 1:
        if wkday != None:
            print(f'{added_time}:{minutes} {PmAm}, {wkday.capitalize()} ({extra_days} days later)')
        else:
            print(f'{added_time}:{minutes} {PmAm} ({extra_days} days later)')
    else:
        if wkday != None:
            print(f'{added_time}:{minutes} {PmAm}, {wkday.capitalize()}')
        else:
            print(f'{added_time}:{minutes} {PmAm}')


#Tests:

add_time("3:00 PM", "3:10")


add_time("11:30 AM", "2:32", "Monday")


add_time("11:43 AM", "00:20")


add_time("10:10 PM", "3:30")


add_time("11:43 PM", "24:20", "tueSday")


add_time("6:30 PM", "205:12")


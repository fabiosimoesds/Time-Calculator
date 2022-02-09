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
    elif added_time == 12:
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
            sum_wk = extra_days
            sum_wk = sum_wk/7
            sum_wk = sum_wk - (sum_wk//1)
            sum_wk = sum_wk*7
            sum_wk = 7 - sum_wk
            wkday = weekdays[sum_wk]
        else:
            wkday = weekdays[sum_wk]




# Conditional Print statement
    if extra_days == 1 :
        if wkday != None:
            a = f'{added_time}:{minutes} {PmAm}, {wkday.capitalize()} (next day)'
        else:
            a = f'{added_time}:{minutes} {PmAm} (next day)'
    elif extra_days > 1:
        if wkday != None:
            a = f'{added_time}:{minutes} {PmAm}, {wkday.capitalize()} ({extra_days} days later)'
        else:
            a = f'{added_time}:{minutes} {PmAm} ({extra_days} days later)'
    else:
        if wkday != None:
            a = f'{added_time}:{minutes} {PmAm}, {wkday.capitalize()}'
        else:
            a = f'{added_time}:{minutes} {PmAm}'
    return a

#Tests:
print(add_time("11:06 PM", "2:02"))

print(add_time("11:40 AM", "0:25"))

add_time("8:16 PM", "466:02")

add_time("5:01 AM", "0:00")

add_time("3:30 PM", "2:12", "Monday")

add_time("2:59 AM", "24:00", "saturDay")

add_time("11:59 PM", "24:05", "Wednesday")

add_time("8:16 PM", "466:02", "tuesday")


def calc(day_d, month_d, day, month, week):
    weekdays = ["shanbeh", "1shanbeh", "2shanbeh", "3shanbeh", "4shanbeh", "5shanbeh", "jome"]
    refr = {"Farvardin": 31, "Ordibehesht": 31, "Khordad": 31, "Tir": 31, "Mordad": 31, "Shahrivar": 31,
            "Mehr": 30, "Aban": 30, "Azar": 30, "Dey": 30,
            "Bahman": 30, "Esfand": 29}
    months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey",
              "Bahman", "Esfand"]
    m = 0
    if (month == month_d and day > day_d) or month_d < month_d:
        m = 1
    if month == month_d:
        alldays = abs(day_d - day)
    else:
        if months.index(month) > months.index(month_d):
            month, month_d = month_d, month
            day, day_d = day_d, day
        vasat = months[months.index(month) + 1: months.index(month_d)]
        alldays = sum([refr[maah] for maah in vasat]) + day_d + (refr[month] - day)
    if m == 0:
        rooz = weekdays[((alldays + weekdays.index(week)) % 7)]
    else:
        rooz = weekdays[-(alldays + weekdays.index(week)) % 7 + 1]
    print(rooz)


calc(22, "Ordibehesht", 23, "Tir", "3shanbeh")

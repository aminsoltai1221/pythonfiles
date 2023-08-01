months = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey",
          "Bahman", "Esfand"]

def calc(day_d, month_d, day, month, week ):
    l_month = sorted([month, month_d], key=lambda x: months.index(x))
    month_d = l_month[1]
    month = l_month[0]
    refr = {"Farvardin":31, "Ordibehesht":31, "Khordad":31, "Tir":31, "Mordad":31, "Shahrivar":31,
    "Mehr":30, "Aban":30, "Azar":30, "Dey":30,
    "Bahman":30, "Esfand":29}
    between_m = []
    for maah in months:
        if months.index(month_d) > months.index(maah) > months.index(month):
            between_m.append(maah)
    between_m_to_days = sum([refr[maah] for maah in between_m])
    print(between_m_to_days)
    print(between_m)
    print("month  :", month)
    print(month_d)

calc(19, "Ordibehesht", 4,  "Mordad", "jome")


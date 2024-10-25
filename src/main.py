
def main():

    # variables
    months = {
        "January": 31,
        "February": 29, # 2024 is a leap year
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    
    dates = []
    for month in months:
        for i in range(months[month]):
            dates.append(f"{month}_{i+1}")

    zeroday_dates = []
    for i in range(13):
        for ii in range(28):
            zeroday_dates.append(f"Month{i+1}_{ii+1}")
    zeroday_dates.append("ZERO DAY")
    if months["February"] == 29:
        zeroday_dates.insert(dates.index("February_29"), "LEAPYEAR DAY")

    # output
    print("Month_Day ---> ???_???")
    month = input("Enter month: ")
    day = input("Enter day: ")
    print(f"{month}_{day} ---> {zeroday_dates[dates.index(f"{month}_{day}")]}")


if __name__ == "__main__":
    main()
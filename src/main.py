
def main():
    months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}
    dates = []
    for month in months:
        for i in range(months[month]):
            dates.append(f"{month}_{i+1}")

    zeroday_dates = ["ZERODAY"]
    for i in range(13):
        for ii in range(28):
            zeroday_dates.append(f"Month{i+1}_{ii+1}")

    input_month = input("Enter the month: ")
    input_day = input("Enter the day: ")
    print(zeroday_dates[dates.index(f"{input_month}_{input_day}")])

if __name__ == "__main__":
    main()
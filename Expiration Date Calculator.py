import datetime, time, os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def expiry_calc():
    clear_screen()
    while not (expiry_date := input('Enter expiry date (YY/MM): ')):
        pass
    try:
        year, month = map(int, expiry_date.split('/'))
        if not (0 <= year <= 99 and 1 <= month <= 12):
            raise ValueError()
    except:
        print(f"\n[\033[91merror\033[0m] Invalid expiry date."); time.sleep(2); expiry_calc()

    year += 2000 if year < 50 else 1900
    day = 31 if month == 12 else (datetime.date(year, month+1, 1) - datetime.timedelta(days=1)).day
    expiry_dt = datetime.date(year, month, day)
    print(f"\nExpiry date: \033[94m{expiry_dt.strftime('%y%m%d')}\033[0m")
    print(f"\nExpiry date: \033[94m{expiry_dt.strftime('%y/%m/%d')}\033[0m")
    
    try:
        input('\nPress [ENTER] to calculate another expiry date...'); expiry_calc()
    except KeyboardInterrupt:
        clear_screen(); exit()


if __name__ == '__main__':
    expiry_calc()

while True:
    user_month = input('Insert month number: ')
    if user_month.isdigit() and 0 < int(user_month) <= 12:
        season_1 = ['winter', 'spring', 'summer', 'autumn', 'winter']
        season_2 = {0: 'winter', 1: 'spring', 2: 'summer', 3: 'autumn', 4: 'winter'}
        print(f'Seasons list - {season_1[int(user_month) // 3]}\nSeasons dict - {season_2[int(user_month) // 3]}')
        break
    else:
        print('Error')
        
list = [1, 2, 4.4, ('None', True, False, ['bravo', 'alfa']), {'margin': 'маржа', 'profit': 'прибыль'}]
for i, item in enumerate(list,1):
    print(f"{i}) {item} - {type(item)}")

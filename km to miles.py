while True:
    km = int(input("Unesi broj kilometara: "))

    ratio = 0.621371

    mi = km * ratio

    print("Rjesenje: ", mi)

    while True:
        answer = raw_input('Zelite li racunati jos?: ')
        if answer in ('da', 'ne'):
            break
        print 'Invalid input.'
    if answer == 'da':
        continue
    else:
        print 'Pozdrav!'
        break



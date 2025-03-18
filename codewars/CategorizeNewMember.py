def open_or_senior(data):
    list = []
    for i in range (len(data)):
        if data[i][0] >= 55 and data[i][1] >= 7:
            print(data[i][1])
            list.append('Senior')
        else:

            list.append('Open')

    return list



if __name__ == '__main__':
    print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
    print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))

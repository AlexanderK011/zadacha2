inputstr=input('введите слово')
bukvi=list(set(inputstr))
for i in range(len(bukvi)):
    print('буква ',bukvi[i],' - ' ,inputstr.count(bukvi[i]),' штуки')
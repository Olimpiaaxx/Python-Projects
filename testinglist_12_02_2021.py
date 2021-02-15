
a = ['sylan', 'to', 'wiesniak']

skip = True
for item in a:
    if skip:
        skip = False
        continue
    print(item)

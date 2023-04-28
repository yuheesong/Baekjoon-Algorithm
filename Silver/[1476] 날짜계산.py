E,S,M=map(int, input().split()) #E=지구, S=태양, M=달
count=0
a, b, c = 0, 0, 0
while True:
    if a>15:
        a=1
    if b>28:
        b=1
    if c>19:
        c=1
    if a==E and b==S and c==M: #앞 3개의 if문보다 앞서 나오면 안된다.
        print(count)
        break
    count += 1
    a, b, c = a+1, b+1, c+1

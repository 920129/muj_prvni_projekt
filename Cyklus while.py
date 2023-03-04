print("hello world")


#Obecně while loop

i = 1
while i < 6:
    print(i)
    i = i+1
    print("hotovo")

index = 0

while index < 20 and len(str(index)) == 2:
    print(index)
    index = index + 1
index = 1

while index > 0:  # vyhodnocené ohlášení má stále hodnotu `True`
    print(index)
    index = index + 1
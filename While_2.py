
# while index <= 20:
#     if len(str(index)) != 2:
#         index = index + 1
#     else:
#         print(index)
#         index = index + 1

#;;;;;;;;;

index = 0
#
# while index < 20:
#     if len(str(index)) != 2:  # pokud není číselná hodnota ze dvou znaků
#         index = index + 2
#         print(index)
#         continue

# jmeno = "Matous"
# print(jmeno)
#
# print(jmen:= "Matous"),
#
# jmeno = input ("Zapiš jmeno: ".upper())
# if jmeno == "Matous":
#     print("Toto je", jmeno, sep="")
# else:
#     print("Tak,", jmeno,"Toho neznám.", sep="")

# matouš

# d = []
#
# for cislo in range(30):
#     d.append(cislo ** 2)
# print(d)
#
# for x in d:
#     print(x-50,x-60,x-70, sep=",")

# data = [1, 2, 3, "a", 5, 6, "@", "7", 7]
#
# dvojnasobek = [cislo * 2 for cislo in data if isinstance(cislo, int)]
# print(dvojnasobek)

# obyvatele = {
#     "Praha": 1_335_084,
#     "Brno": 382_405,
#     "Ostrava": 284_982,
#     "Plzen": 175_219,
#     "Liberec": 104_261
# }
#
# velka_mesta = {
#     klic.upper(): hodnota
#     for klic, hodnota in obyvatele.items()
#     if hodnota > 200_000
# }
#
# print(velka_mesta)
#
# velka_mesta = dict()
# for klic, hodnota in obyvatele.items():
#     if hodnota > 200_000:
#         velka_mesta[klic.upper()] = hodnota

# arr1 = [5,1,4,2,8]
# arr2 = [1,2,3,4,5]

# print(arr1 == sorted(arr1))

# arr = arr2
# for i in range(1,len(arr)):
#     print(arr[i-1], arr[i])
#     if arr[i-1] > arr[i]:
#         print("Not sorted")
#         break
#     else:
#         continue
# else:
#     print("Sorted")


# #Bubble sort function:
# arr=arr1
# n = len(arr)
# for i in range(n-1):
#     print((i), "0....", n-i-1)
#     for j in range(0,n-i-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j + 1] = arr[j+1], arr[j]
#             # print(arr[j],arr[j+1])
#             swapped = True
#     if not swapped:
#         break
#     else:
#         continue
# print(arr)



#### dalsi razeni

#
# arr = [85, 12, 59, 45, 72, 51]
#
# # rozdelit na sorte/ unsorted
#
# []
#
# if (n:=len(arr))>1:
#     for i in range(1,n):
#         v = arr[i] # frist value == 12
#         print(v)
#         j = i - 1   #hranice
#         while j>=0 and v < arr[j]:
#             arr[j+1] = arr[j]
#             j = j-1
#         arr[j+1] = v
#         print(v)
#         print(arr, "Sorrted")


# arr  = [29, 72, 98, 13, 87, 66, 52, 51, 36]
#
# []
#
# ind = 0 # zacatek neserazene casti
#
# for ind in range (len(arr)):
#     min_index = ind
#     for j in range(ind+1,len(arr)):
#         if arr[j] < arr[min_index]: #13<29
#             min_index = j #
#     arr[ind], arr[min_index] = arr[min_index], arr[ind]
#     print(arr)

arr = [1,2,3,4]

n = len(arr)
sums = []
soucet = 0
for i in arr:
    soucet = soucet + i
    sums.append(soucet)
    print(soucet)
print(soucet)

X = [[1,2],
     [3,4]
]

Y = [[5,6],
     [7,8]
]

print(X,Y)

result = [[0,0],[0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(2):
            result [i][j] +=X[i][k] * Y[k][j]
print(result)


# text = "Korunovace českých panovníků byla událost mimořádného státního" \
#        " a duchovního významu, při které byl král během korunovační mše" \
#        " arcibiskupem pomazán svatými oleji a korunován. Představovala " \
#        "symbolické potvrzení a uznání nového krále, " \
#        "jeho spojení se zemí, jíž vládl, a také zdůrazňovala duchovní přesah j" \
#        "eho úřadu. První český král Vratislav byl nejprve korunován v dubnu 1085 císařem Jindřichem IV. a v červnu následujícího roku společně s manželkou pomazán a korunován v Praze arcibiskupem trevírským. "
#
# sentences = text.replace("\n", "").split(".")
# # print(sentences)
#
# max_n = 0
# longest_sentence = None
# for sentence in sentences:
#     sentence = sentence.lstrip().split(" ")
#     if len(sentence) > max_n:
#         max_n = len(sentence)
#         longest_sentence = sentence
#
#
# print(" ". join(longest_sentence))
# print(len(longest_sentence))


()(())()()



















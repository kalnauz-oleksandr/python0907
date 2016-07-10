def year_old ():
    a = int (input ("Введите год рождения "))
    old = 2016 - a
    print ("Ваш возраст ",old)
    if old < 18:
        print ("Алкоголь запрещён")
    elif old < 60:
        print ("Алоголь разрешен, но вмеру")
    else:
        print ("Алкоголь не рекомендуется!")
year_old()

words= ['cat','dog','horse',]
lst = [1,2,3,4,5,]
print (list (range (5)))
for num in lst:
    print ('ok')
for num in range (5):
    print (num)
for num in range (2,5):
    print (num)
for num in range (2,5,2):
    print (num)
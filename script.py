def is_even(x):
    if x % 2 == 0:
        return 'even'
    elif x % 2 == 1:
        return 'odd'
print (is_even(11))

def is_even2 (n):
    if n % 2:
        print ('nechet')
    else:
        print ('chet')
is_even2(345)
print (bool(is_even2))
is_even2(500)
print (bool(is_even2))

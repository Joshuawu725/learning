def binary_search(list, item):
    low = 0
    hight = len(list) - 1
    
    while low <= hight:
        mid = (low + hight)//2 #向下取余
        guess = list[mid]
        if guess == item:
        	return mid
        if guess > item:
            hight = mid - 1
        else:
            low = mid + 1
    return None

myList = [1,2,5,8,12,15,19,234,456,789,1000]
print (binary_search(myList, 19))
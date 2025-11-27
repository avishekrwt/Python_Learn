def is_valid(orgisbn):
    isbn = orgisbn.replace("-","")
    if len(isbn)!=10:
        return False

    if not isbn[:9].isdigit():
        return False

    if not (isbn[9].isdigit() or isbn[9]=='X'):
        return False
    
    isbn_list = list(isbn)
    if not isbn_list[9].isdigit():
        isbn_list[9] = 10

    total = 0
    for i in range(0,10):
        total += int(isbn_list[i])*(10-i)
 
    return total%11==0   
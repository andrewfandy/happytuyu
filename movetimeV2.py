def leapYear(year):
    if year%400 == 0:
        return False
    if year%100 == 0:
        return False
    if year%4 == 0:
        return False
    return True

def checkMonth(day, month, year):
    if day > 31 and (month in [1, 3, 5, 7, 8, 10, 12]):
        return False
    elif day > 30 and (month in [4, 6, 9, 11]):
        return False
    elif day > 28 and month == 2 and leapYear(year):
        return False
    elif day > 29 and month == 2:
        return False
    return True
    
def listMonth(month):
    monthList = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
    return monthList[month-1]

def subMonth (day, month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2 and leapYear(year):
        return 28
    elif month == 2:
        return 29
 
    
        
def moveForward(day, month, year):
    try:
        forDay = int(input('Majukan berapa hari?, input: '))
    except:
        print('Invalid input')
        return moveForward(day, month, year)
    day += forDay
    while day > 1 and not checkMonth(day, month, year):
        day -= subMonth(day, month, year)
        month += 1
        if month > 12:
            month = 1
            year += 1
    return '\n\nHasil : %d %s %d C.E'%(day, listMonth(month), year)


def moveBackward(day, month, year):
    try:
        backDay = int(input('Mundurkan berapa hari?, input: '))
    except:
        print('Invalid input')
        return moveBackward(day, month, year)

    day -= backDay
    while day < 1 and checkMonth(day, month, year):
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day += subMonth(day, month, year)
    if year < 0:
        return '\n\nHasil : %d %s %d B.C'%(day, listMonth(month), abs(year))
    return '\n\nHasil : %d %s %d C.E'%(day, listMonth(month), year)
        
        
def main():
    day = int(input('Input tanggal : '))
    month = int(input('Input bulan : '))
    year = int(input('Input tahun : '))

    if checkMonth(day, month, year):
        while True:
            forward_backward_input = int(input('[1] Majukan hari\n[2] Mundurkan hari\nInput :'))
            if forward_backward_input == 1:
                return moveForward(day, month, year)
            elif forward_backward_input == 2:
                return moveBackward(day, month, year)
            else:
                print('Pilih 1 atau 2')
              
    else:
        print('Invalid input')
        return main()
        
        

print('-'*5+'SELAMAT DATANG'+'-'*(5)+'\n'*5)
print(main())

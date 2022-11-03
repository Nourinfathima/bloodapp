import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'bloodbankdb')

mycursor = mydb.cursor()
while True:
    print("select an option from the menu")
    print('1 add donar')
    print('2 view all donar')
    print('3 search a donar')
    print('4 update a donar')
    print('5 delete a donar')
    print('6 Average blood donated')
    print('7 Name of the doner with starting letter')
    print('8 exit')

    choice = int(input('Enter an option: '))
    if(choice == 1):
        print(' enter selected')
        
        name = input('enter the name: ')
        bloodgroup = input('enter the grp: ')
        unit = input('enter the unit: ')
        phno= input('enter the  phnno: ')
        place = input('place: ')
        sql = 'INSERT INTO `donors`(`Name`, `bloodgroup`, `unit`, `phno`, `place`) VALUES (%s,%s,%s,%s,%s)'
        data = (name, bloodgroup,unit,phno,place)
        mycursor.execute(sql , data)
        mydb.commit()
        
    elif(choice == 2):
        print('view blood')
        sql = 'SELECT * FROM `donors`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print('search a book selected')
    elif(choice==4):
        print('update the book selected')
    elif(choice==5):
        print('delete the book selected')
    elif(choice==6):
        break    
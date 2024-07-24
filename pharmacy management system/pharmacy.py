#creating database and table
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost",user="root",passwd="udgam")
cursor=mycon.cursor()
cursor.execute("create database if not exists pharmacy")
cursor.execute("use pharmacy")
cursor.execute(" create table if not exists Medi(s_no int primary key not null,name_item char(60),quantity int,price int,company_name char(60),description char(100))")


#printing welcome
#creating a menu profile

def mainmenu():
 print("                                             Welcome to ROYAL PHARMACY      ")
 print("1.Show Inventory\n2.Search Item\n3.Add Item\n4.Remove Item\n5.Update Details\n6.exit")
 select=int(input("Enter Choice:"))
 if select==1:
    show()
 elif select==2:
    search()
 elif select==3:
    add()
 elif select==4:
    remove()
 elif select==5:
    update()
 elif select==6:
    exit
 else:
     print("Invalid choice.Enter between 1-5")
     mainmenu()

#showing the inventory
def show():
 import mysql.connector as sqltor
 mycon=sqltor.connect(host="localhost",user="root",passwd="udgam",database="pharmacy")
 if mycon.is_connected()==False:
    print("error")
 cursor=mycon.cursor()
 cursor.execute("select * from Medi")
 data=cursor.fetchall()
 for row in data:
     print("S_no=",row[0],)
     print("Name_Item=",row[1],)
     print("Quantiy=",row[2],)
     print("Price per item=",row[3],)
     print("Company_Name=",row[4],)
     print("Description=",row[5],)
 print("1.yes\n2.no")
 cont=int(input("Do you want to continue?:"))
 if cont==1:
  mainmenu()
 elif  cont==2:
      exit
     


#searching inventory based on name of item
#user input

def search():
  import mysql.connector as sqltor
  mycon=sqltor.connect(host="localhost",user="root",passwd="udgam",database="pharmacy")
  cursor=mycon.cursor()
  if mycon.is_connected()==False:
    print("error")
  nam=input("Enter the name of item:")
  cursor.execute("SELECT * FROM Medi WHERE name_item=%s",(nam,))
  result=cursor.fetchall()
  if result:
      print("data exists")
      for row in result:
       print("S_no=",row[0],)
       print("Name_Item=",row[1],)
       print("Quantiy=",row[2],)
       print("Price per item=",row[3],)
       print("Company_Name=",row[4],)
       print("Description=",row[5],)
      
  else:
      print("No such Data exists")
  print("1.yes\n2.no")
  cont=int(input("Do you want to continue?:"))
  if cont==1:
      mainmenu()
  elif  cont==2:
      exit
#inserting a new item in the record

#user input
def add():
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd="udgam",database="pharmacy")
    cursor=mycon.cursor()
    s_no=input("Enter Serial No:")
    name_item=input("Enter Name of Item:")
    quantity=input("Enter Quantitiy:")
    price=input("Enter Price:")
    company_name=input("Enter Company Name:")
    description=input("Enter Description:")
    cursor.execute("INSERT INTO Medi(s_no,name_item,quantity,price,company_name,description) VALUES({},'{}',{},{},'{}','{}')".
    format(s_no,name_item,quantity,price,company_name,description))
    mycon.commit()
    print("Record Added")
    print("1.yes\n2.no")
    cont=int(input("Do you want to continue?:"))
    if cont==1:
     mainmenu()
    elif  cont==2:
      exit



#removing item  from the record

#user input      
def remove():
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd="udgam",database="pharmacy")
    cursor=mycon.cursor()
    rec=input("Name of item to be deleted:")
    deleterec="DELETE FROM Medi Where name_item=%s"
    cursor.execute(deleterec,(rec,))
    mycon.commit()
    print("Record Deleted")
    print("1.yes\n2.no")
    cont=int(input("Do you want to continue?:"))
    if cont==1:
      mainmenu()
    elif  cont==2:
      exit


#updating the records

#user input
def update():
    import mysql.connector as sqltor
    mycon=sqltor.connect(host="localhost",user="root",passwd="udgam",database="pharmacy")
    cursor=mycon.cursor()
    print("1.Price\n2.Quantity")
    e=int(input("What do you want to update?"))
    if e==1:
        q=input("Enter name of the item needed to be updated:")
        pr=int(input("Enter updated price"))
        up=" update Medi set price=%s where name_item=%s"
        data=(pr,q)
        cursor.execute(up,data)
        mycon.commit()
        print("Price updated")
    elif e==2:
        upname=input("Enter name of the item needed to be updated:")
        qu=int(input("Enter updated quantity"))
        x=" update Medi set quantity=%s where name_item=%s"
        d=(qu,upname)
        cursor.execute(x,d)
        mycon.commit()
        print("Quantity updated")
    print("1.yes\n2.no")
    cont=int(input("Do you want to continue?:"))
    if cont==1:
         mainmenu()
    elif cont==2:
         exit

mainmenu()

import psycopg2 as pgsql

connection=pgsql.connect(host="localhost", dbname="phonebook", user="postgres", 
                         password="asdf", port=5432)
cur=connection.cursor()


def createpattern():
    global query
    query="""SELECT * FROM PhoneBook
    WHERE """
    print(r"Do you want to search by ID(0)/name(1)/break(any num) enter the number:")
    mode=int(input())
    if mode==0:
            query+="ID"
            print("Enter string")
            substr=input()
            print("""Select option:
            1-ID is equal to string
            2-ID starts with the string
            3-ID ends with the string
            4-ID contains the string""")
            mode1=int(input())
            if mode1==1:
                query+="='{}'".format(substr)
            elif mode1==2:
                query+=" iLIKE '{}%'".format(substr)
            elif mode1==3:
                query+=" iLIKE '%{}'".format(substr)
            else:
                query+=" iLIKE '%{}%'".format(substr)
    elif mode==1:
            query+="""name"""
            print("Enter string")
            substr=input()
            print("""Select option:
            1-name is equal to string
            2-name starts with the string
            3-name ends with the string
            4-name contains the string""")
            mode1=int(input())
            if mode1==1:
                query+="='{}'".format(substr)
            elif mode1==2:
                query+=" iLIKE '{}%'".format(substr)
            elif mode1==3:
                query+=" iLIKE '%{}'".format(substr)
            else:
                query+=" iLIKE '%{}%'".format(substr)
    else:
         return "error"
    return query


def insert(surname, name, phone):
    cur.execute("SELECT count(*) FROM PhoneBook WHERE surname='{}' AND name='{}'".format(surname, name))
    if cur.fetchone()[0]==0:
         cur.execute("""INSERT INTO PhoneBook VALUES ('{}','{}', {})""".format(surname, name, phone))
    else:
         cur.execute("""UPDATE PhoneBook
         SET number={}
         WHERE surname='{}' AND name='{}'
         """.format(phone,surname, name))

def loopinsert():
    banned=[]
    while True:
        print("Want to enter a person's data? yes/no")
        mode=input()
        if mode=="no":
             break
        person=input().split()
        if len(person)>3:
             banned.append(person)
             continue
        
        if not person[2].isdigit():
             banned.append(person)
             continue
        
        insert(*person)
    if len(banned)==0:
         return
    print("This data were not added due to incorrect format:")
    for i in banned:
         print(i)
        

def pagination():
    query=createpattern()
    if query=="error":
        return "error"
    print("Need offset? yes/no:")
    mode=input()
    if mode=="yes":
         print("Enter offset:")
         offset=int(input())
         query+=" OFFSET {}".format(offset)
    print("Need limit? yes/no:")
    mode=input()
    if mode=="yes":
         print("Enter limit:")
         limit=int(input())
         query+=" LIMIT {}".format(limit)
    query +=";"
    return query

def delete():
    query="""DELETE FROM PhoneBook
    WHERE """
    cur.execute("SELECT * from PhoneBook")
    print(cur.fetchall())
    print("Do you wanna delete by ID(0)/name(1)/number(2) enter the number")
    mode=int(input())
    if mode==0:
         print("Enter ID to delete:")
         surname=input()
         query+="ID='{}'".format(ID)
    elif mode==1:
         print("Enter name to delete:")
         name=input()
         query+="name='{}'".format(name)
    else:
         print("Enter number to delete:")
         number=input()
         query+="number={}".format(number)
    cur.execute(query)
         

s1=createpattern()
if s1!="error":
     cur.execute(s1+";")
     print(cur.fetchall())
#insert("Berik", "Serik", 12345)
loopinsert()
s1=pagination()
if s1!="error":
     cur.execute(s1+";")
     print(cur.fetchall())
delete()

connection.commit()
cur.close()
connection.close()
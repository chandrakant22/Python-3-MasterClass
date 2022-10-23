import mysql.connector as mysql

mysqldb=mysql.connect(
  host="localhost",
  user="root",
  password="abc123",
  charset='utf8',
  database="mydb")

cr=mysqldb.cursor()

name=input("enter your good name")
address=input("enter your Address")

# sql = "insert into emp (name, address) values( %s, %s)"
# val=(name,address)

sql="delete from emp where name='om'"
cr.execute(sql)

mysqldb.commit()

print("Data Inserted!!")
print("done")



# cr.execute("create database mydb")
# cr.execute("create table emp(id int,name varchar(45),address varchar(255))")
# sql = "insert into emp (name, address) values( %s, %s)"
# val=[
# ("sham","pune"),
# ("geeta","nagpur"),
# ("om","pune"),
# ("pooja","nagpur")
# ]


a=20
a=30
print(a)

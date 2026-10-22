import sqlite3
conn = sqlite3.connect("demo.db")
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(20) UNIQUE,
    password TEXT
    )
    ''')



cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tname VARCHAR(20),
        tdes TEXT,
        user_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
        ''')

def register():
    username = input("enter username : ")
    password = input("enter password : ")

    cursor.execute('''
        INSERT INTO users(username,password)
        VALUES(?,?)
        ''',(username,password))
    conn.commit()
    print("USER Registerred successfully!!!!!!!!!!!!!!!!!!")


def login():
    username = input("enter username : ")
    password = input("enter password : ")
    cursor.execute('''
        SELECT id FROM users WHERE username = ? AND password = ?
        ''',(username,password))

    user = cursor.fetchone()
    if user:
        return user[0]
    else:
        print("invalid credentials")


def addtask(user_id):    
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    name = input("enter task name :--") 
    des = input("enter task des :---")

    cursor.execute('''
        INSERT into tasks(tname,tdes,user_id)
        VALUES(?,?,?)
        ''',(name,des,user_id))

    conn.commit()
    print("TAsk added 😁")


def viewtasks(user_id):
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM tasks WHERE user_id =?
        ''',(user_id,))
    data = cursor.fetchall() #reteives all data from last executed querry 
    # [(),(),()]
    if data:
        print("tasks found ")
        for i in data:
                print(f"{i[0]}--:{i[1]}--:{i[2]}")
    else:
        print("No tasks found")
def searchtask():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    t_id = int(input("enter task id :--"))
    cursor.execute('''
        SELECT * FROM tasks WHERE id = ?
        ''',(t_id,))
    data = cursor.fetchone()
    if data:
        print("data found")
        print(data[1])

def edittasks():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    t_id = int(input("enter task id :"))
    name = input("enter new task name:-")
    des = input("enter new task des:-")
    cursor.execute('''
        UPDATE tasks SET tname = ?,tdes = ? WHERE id = ?
        ''',(name,des,t_id))
    conn.commit()
    print("Task updated")

def deletetask():
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    t_id = int(input("enter task id ---"))
    cursor.execute('''
        DELETE FROM tasks WHERE id =?
        ''',(t_id,))
    ch = input("Are you sure you want to delete this task ... y/n ? --")
    if ch == "y":
        conn.commit()
        print("task deleted")
    else:
        print("cancelled")
def main2(user_id):
    print("Welcome to Task Management System")
    while True:
        ch = int(input("Enter your choice \n1.Addtask\n2.View task\n3.Search task\n4.Edit Task\n5.Delete task\n6.exit\n:-------"))
        if ch == 1:
            addtask(user_id)
            pass
        elif ch == 2:
            viewtasks(user_id)
        elif ch == 3:
            searchtask(user_id)
        elif ch == 4:
            edittasks(user_id)
        elif ch == 5:
            deletetask(user_id)
        elif ch == 6:
            break


def main1():
    print("WElcome")
    while True:
        ch = int(input("1.Login\n2.Register\n3.Exit\nchoose---"))
        if ch == 1:
            user_id = login()
            main2(user_id)
        elif ch == 2:
            register()
        else:
            print("invalid")

main1()
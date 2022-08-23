import sqlite3

roll_no = int(input("Enter Roll No of Student: "))


def viewall(roll_no):
    conn = sqlite3.connect("IITK.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where roll_no=?  ", (roll_no,))
    global data
    data = cur.fetchall()


def feedfile(data):
    f = open('details_for_a_student.csv', 'w')
    for row in data:
        for element in row:
            f.write(str(element))
            f.write(',')
        f.write('\n')
    f.close()


viewall(roll_no)
feedfile(data)

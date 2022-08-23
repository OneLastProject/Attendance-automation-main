# for any student based on month/year
import datetime
import sqlite3

roll_no = int(input("Enter Roll No of Student: "))
month = int(input("Enter Month in digits: "))
year = int(input("Enter year : "))


def viewall():
    sdate = datetime.date(year, month, 1)
    if month == 12:
        edate = datetime.date(year + 1, month, 1)
    else:
        edate = datetime.date(year, month + 1, 1)
    #print(sdate,edate)
    conn = sqlite3.connect("IITK.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM attendance where roll_no=? and day>=? and day<? ", (roll_no, sdate, edate))
    global data
    data = cur.fetchall()



def feedfile(data):
    f = open('student_details_for_a_month.csv', 'w')
    for row in data:
        for element in row:
            f.write(str(element))
            f.write(',')
        f.write('\n')
    f.close()


viewall()
feedfile(data)

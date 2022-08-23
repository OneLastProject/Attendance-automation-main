import sqlite3
import datetime


def insert(roll_no, firstname, lastname, day, att):
    conn = sqlite3.connect("IITK.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO attendance VALUES (?,?,?,?,?)", (roll_no, firstname, lastname, day, att))
    conn.commit()
    conn.close()


def parse(name):
    table = []
    with open(name, "r") as csvfile:
        for line in csvfile:
            line = line.rstrip()
            columns = line.split(',')
            table.append(columns)
    return table


def feed_db(table):
    for col in table:
        roll = int(col[0])
        fname = str(col[1])
        lname = str(col[2])
        d = (col[3].strip()).split('-')
        dy = int(d[0])
        mon = int(d[1])
        yr = int(d[2])
        d1 = datetime.date(yr, mon, dy)
        att = str(col[4])
        insert(roll, fname, lname, d1, att)


table = parse("stu.csv")
feed_db(table)

def byfirstname(x):
    bname = ''
    bcost = ''
    bqty = ''

    import sqlite3
    try:
        direct = sqlite3.connect('books.db')
        sql = "SELECT * from details WHERE name='" + x + "';"
        curse = direct.cursor()
        curse.execute(sql)
        result = curse.fetchall()
        for record in result:
            bname = bname + str(record[0])
            bcost = bcost + str(record[1])
            bqty = bqty + str(record[2])


        if bqty != '':
            f = [bname,bcost,bqty]
            return f
        else:
            return -1
    except:
        print("Error in operation.")
        direct.rollback()
    direct.close()

"""z='Olivar Twist'
print(byfirstname(z)[2])"""
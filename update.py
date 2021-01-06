def byqty(s, w, x):
    import sqlite3
    try:
        direct = sqlite3.connect('books.db')
        sql = "SELECT * from details WHERE name='" + s + "';"
        curse = direct.cursor()
        curse.execute(sql)
        record = curse.fetchone()
        if record != None:
            sql = "UPDATE details SET name='" + str(s) + "', cost='" + str(w) + "', qty='" + str(
                x) + "' WHERE name='" + str(s) + "';"
            curse.execute(sql)
            direct.commit()
            return 'updated now'
        else:
            return 'Number does not exist'


    except:
        return "Error in operation."
        direct.rollback()
    direct.close()



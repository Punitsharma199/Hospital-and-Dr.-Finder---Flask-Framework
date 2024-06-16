import pymysql

def check_photo(email):
    cn = pymysql.connect(host='localhost',port=3306,user='root',passwd="",db="punit",autocommit=True)
    cur = cn.cursor()
    cur.execute("select * from photodata where user_email='"+email+"'")
    n = cur.rowcount
    photo = "no"
    if(n>0):
        row = cur.fetchone()
        photo = row[1]
    return photo
def make_connection():
    cn = pymysql.connect(host='localhost', port=3306, user='root', passwd="", db="punit", autocommit=True)
    cur = cn.cursor()
    return cur
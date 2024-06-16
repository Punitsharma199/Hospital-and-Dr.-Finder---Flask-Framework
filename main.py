import pymysql
import os
import time

from Tools.i18n.msgfmt import make
from flask import Flask, render_template,request,url_for,redirect,session
from werkzeug.utils import secure_filename

from mylib import *
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './static/photos'

app.secret_key = "super secret key"


# for index
@app.route('/')
def hello_world():
    cur = make_connection()
    cur.execute("SELECT * FROM hospital_with_photo")
    n=cur.rowcount
    if(n>0):
        result = cur.fetchall()
        return render_template('index.html', result=result)
    else:
        return render_template("index.html",msg="no data found")


# for admin_reg
@app.route('/admin_reg',methods=["GET","POST"])
def admin_reg():
    if(request.method=="POST"):
        #recive from data
        name=request.form["T1"]
        address=request.form["T2"]
        contact=request.form["T3"]
        email=request.form["T4"]
        password=request.form["T5"]
        con_pass=request.form["T6"]
        usertype="admin"
        msg=""
        if(password!=con_pass):
            msg="Data saved and login created"
        else:
            cn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="punit",autocommit=True)
            sql1="insert into admindata values('"+name+"','"+address+"','"+contact+"','"+email+"')"
            sql2="insert into logindata values('"+email+"','"+password+"','"+usertype+"','"+con_pass+"')"
            cur=cn.cursor()
            cur.execute(sql1)
            m=cur.rowcount
            cur=cn.cursor()
            cur.execute(sql2)
            n=cur.rowcount
            if(m==1 and n==1):
                msg="Data is saved and login created"
            elif(m==1):
                msg="Only data is saved"
            elif(n==1):
                msg="Only login created"
            else:
                msg="No data saved and no login created"
            return render_template('admin_reg.html',vgt=msg)
    else:
        return render_template("admin_reg.html")

#for show_admin
@app.route('/show_admin')
def show_admin():
    cn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="punit",autocommit=True)
    s1 = "select * from admindata"
    cur=cn.cursor()
    cur.execute(s1)
    a=cur.rowcount
    if(a>0):
        #fetch data
        data=cur.fetchall()
        return render_template("show_admin.html",vgt=data)
    else:
        return render_template("show_admin.html",msg="no data")
'''
as admin cannot delete edit other admin that's why don't neet to write this progrome.
'''
# edit_admin
@app.route('/edit_admin',methods=["GET","POST"])
def edit_admin():
    if( request.method=="POST" ):
        email=request.form["H1"]
        cn=pymysql.connect(host="localhost",port=3306,db="punit",passwd="",user="root",autocommit=True)
        s1="select * from admindata where email='"+email+"'"
        cur=cn.cursor()
        cur.execute(s1)
        a=cur.rowcount
        if(a>0):
            data=cur.fetchone()
            return render_template("edit_admin.html",vgt=data)
        else:
            return render_template("edit_admin.html",msg="No data found")
    else:
        return redirect(url_for("show_admin"))

# edit_admin1
@app.route('/edit_admin1',methods=["GET","POST"])
def edit_admin1():
    if(request.method=="POST"):
        #grab from data
        name = request.form["T1"]
        address = request.form["T2"]
        contact = request.form["T3"]
        email = request.form["T4"]

        cn = pymysql.connect(host="localhost",user="root",db="punit",port=3306,passwd="",autocommit=True)
        s1="update admindata set name='"+name+"', address='"+address+"',contact='"+contact+"' where email='"+email+"' "

        cur=cn.cursor()
        cur.execute(s1)
        a=cur.rowcount
        if(a>0):
            return render_template("edit_admin1.html",msg="Data changed and save successfully")
        else:
            return render_template("edit_admin1.html",msg="Datachanged are not saved")
    else:
        return redirect(url_for("show_admin"))

# for delete_admin
@app.route("/delete_admin",methods=["GET","POST"])
def delete_admin():
    if(request.method=="POST"):
        email=request.form["H1"]
        cn=pymysql.connect(host="localhost",user="root",port=3306,db="punit",passwd="",autocommit=True)
        s1="select * from admindata where email='"+email+"'"

        cur=cn.cursor()
        cur.execute(s1)
        a=cur.rowcount
        if(a>0):
            data=cur.fetchone()
            return render_template("delete_admin.html",vgt=data)
        else:
            return render_template("delete_admin.html",msg="No data found")
    else:
        return redirect(url_for("show_admin"))

# delete_admin1
@app.route('/delete_admin1',methods=["GET","POST"])
def delete_admin1():
    if(request.method=="POST"):
        name = request.form["T1"]
        address = request.form["T2"]
        contact = request.form["T3"]
        email = request.form["T4"]

        cn=pymysql.connect(host="localhost",db="punit",user="root",passwd="",port=3306,autocommit=True)
        s1="delete from admindata where email='"+email+"' "
        cur=cn.cursor()
        cur.execute(s1)
        a=cur.rowcount
        if(a>0):
            return render_template("delete_admin1.html",msg="Data is deleted succesfully")
        else:
            return render_template("delete_admin1.html",msg="Data  are not deleted")

    else:
        return redirect(url_for("show_admin"))

# hospital_reg
@app.route('/hospital_reg',methods=["GET","POST"])
def hospital_reg():
    if(request.method=="POST"):
        print("This is the post request")
        #recive from data
        name = request.form["T1"]
        l_number = request.form["T2"]
        address = request.form["T3"]
        contact = request.form["T4"]
        emergency = request.form["T5"]
        genral_beds = request.form["T6"]
        ac_beds = request.form["T7"]
        email = request.form["T8"]
        password = request.form["T9"]
        con_pass = request.form["T10"]
        usertype = "hospital"
        msg = ""
        if(password!=con_pass):
            msg="Data saved and login created"
        else:
            cn = pymysql.connect(host="localhost",port=3306,user="root",db="punit",passwd="", autocommit=True)
            s1 = "insert into hospital_data values('"+name+"','"+l_number+"','"+address+"','"+contact+"','"+emergency+"','"+genral_beds+"','"+ac_beds+"','"+email+"')"
            s2 = "insert into logindata values('"+email+"','"+password+"','"+usertype+"','"+con_pass+"')"
            cur = cn.cursor()
            cur.execute(s1)
            m = cur.rowcount

            cur = cn.cursor()
            cur.execute(s2)
            n= cur.rowcount

            if(m==1 and n==1):
                msg = "Data is saved and login created"
            elif(m==1):
                msg = "Only data is saved"
            elif(n==1):
                msg = "Only login is saved"
            else:
                msg = "No data is saved and no login saved"
            return render_template('hospital_reg.html',vgt=msg)
    else:
        print("This is get request")
        return render_template('hospital_reg.html')

# show_hospital_data
@app.route('/show_hospital_data',methods=["GET","POST"])
def show_hospital_data():
    cn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="punit",autocommit=True)
    s1 = "select * from hospital_data"
    cur = cn.cursor()
    cur.execute(s1)
    n = cur.rowcount
    if(n>0):
        data = cur.fetchall()
        return render_template("show_hospital_data.html",vgt=data)
    else:
        return render_template("show_hospital_data.html",msg="No Data")
# show_hospital_for_admin
@app.route('/show_hospital_for_admin',methods=["GET","POST"])
def show_hospital_for_admin():
    cn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="punit",autocommit=True)
    s1 = "select * from hospital_data"
    cur = cn.cursor()
    cur.execute(s1)
    n = cur.rowcount
    if(n>0):
        data = cur.fetchall()
        return render_template("show_hospital_for_admin.html",vgt=data)
    else:
        return render_template("show_hospital_for_admin.html",msg="No Data")


# edit_hospital_data
@app.route('/edit_hospital_data', methods=["GET", "POST"])
def edit_hospital_data():
    if(request.method=="POST"):
        email = request.form["H1"]
        cn = pymysql.connect(host="localhost",port=3306,db="punit",passwd="",user="root",autocommit=True)
        s1 = "select * from hospital_data where email='"+email+"'"
        cur = cn.cursor()
        cur.execute(s1)
        a = cur.rowcount
        if(a>0):
            data = cur.fetchone()
            return render_template("edit_hospital_data.html",vgt=data)
        else:
            return render_template("edit_hospital_data.html",msg="No Data")
    else:
        return redirect(url_for("show_hospital_for_admin"))

# edit_hospital_data1
@app.route('/edit_hospital_data1',methods=["GET","POST"])
def edit_hospital_data1():
    if(request.method=="POST"):
        name = request.form["T1"]
        l_no = request.form["T2"]
        address = request.form["T3"]
        contact = request.form["T4"]
        emergency = request.form["T5"]
        g_beds = request.form["T6"]
        ac_beds = request.form["T7"]
        email = request.form["T8"]

        cn = pymysql.connect(host="localhost",port=3306,db="punit",passwd="",user="root",autocommit=True)
        s1 = "update hospital_data set hname='"+name+"',lno='"+l_no+"',address='"+address+"',contact='"+contact+"',emergency='"+emergency+"',g_beds='"+g_beds+"',ac_beds='"+ac_beds+"' where email='"+email+"'"
        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n>0):
            return render_template("edit_hospital_data1.html",msg="Data changed are successfully")
        else:
            return render_template("edit_hospital_data1.html",msg="Data changed are not saved")
    else:
        return redirect(url_for("show_hospital_for_admin"))

# for delete_hospital_data
@app.route("/delete_hospital_data",methods=["GET","POST"])
def delete_hospital_data():
    if(request.method=="POST"):
        email=request.form["H1"]
        cn=pymysql.connect(host="localhost",user="root",port=3306,db="punit",passwd="",autocommit=True)
        s1="select * from hospital_data where email='"+email+"'"

        cur=cn.cursor()
        cur.execute(s1)
        n=cur.rowcount
        if(n>0):
            data=cur.fetchone()
            return render_template("delete_hospital_data.html",vgt=data)
        else:
            return render_template("delete_hospital_data.html",msg="No data found")
    else:
        return redirect(url_for("show_hospital_data"))

# delete_hospital_data1
@app.route('/delete_hospital_data1',methods=["GET","POST"])
def delete_hospital_data1():
    if(request.method=="POST"):
        name = request.form["T1"]
        l_no = request.form["T2"]
        address = request.form["T3"]
        contact = request.form["T4"]
        emergency = request.form["T5"]
        g_beds = request.form["T6"]
        ac_beds = request.form["T7"]
        email = request.form["T8"]

        cn=pymysql.connect(host="localhost",db="punit",user="root",passwd="",port=3306,autocommit=True)
        s1="delete from hospital_data where email='"+email+"' "
        cur=cn.cursor()
        cur.execute(s1)
        n=cur.rowcount
        if(n>0):
            return render_template("delete_hospital_data1.html",msg="Data is deleted succesfully")
        else:
            return render_template("delete_hospital_data1.html",msg="Data  are not deleted")

    else:
        return redirect(url_for("show_hospital_data"))

# for doctor Reg
@app.route('/doctor_reg',methods=["GET","POST"])
def doctor_reg():
    if(request.method=="POST"):
        name = request.form["T1"]
        address = request.form["T2"]
        contact = request.form["T3"]
        speciality = request.form["T4"]
        current_hospital = request.form["T5"]
        work_exprirence = request. form["T6"]
        days = request.form.getlist('T7')
        mon = "no"
        tues = "no"
        wed = "no"
        thu = "no"
        fri = "no"
        sat = "no"
        sun = "no"

        if('mon' in days):
            mon = "yes"
        if ('tues' in days):
            tues = "yes"
        if ('wed' in days):
            wed = "yes"
        if ('thu' in days):
            thu = "yes"
        if ('fri' in days):
            fri = "yes"
        if ('sat' in days):
            sat = "yes"
        if ('sun' in days):
            sun = "yes"

        timing = request.form["T8"]
        email = request.form["T9"]
        usertype = "admin"
        msg = ""

        cn=pymysql.connect(host="localhost",port=3306,user="root",db="punit",passwd="",autocommit=True)
        s1 = "insert into doctor_data values('"+name+"','"+address+"','"+contact+"','"+speciality+"','"+current_hospital+"','"+work_exprirence+"','"+mon+"','"+tues+"','"+wed+"','"+thu+"','"+fri+"','"+sat+"','"+sun+"','"+timing+"','"+email+"',0)"
        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n>0):
            msg = "Data is saved"
        else:
            msg = "Data is not saved"
        return render_template('doctor_reg.html',vgt=msg)
    else:
        print("This is get request")
        return render_template('doctor_reg.html')

# show_doctor_for_admin
@app.route('/show_doctor_for_admin',methods=["GET","POST"])
def show_doctor_for_admin():
    cn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="punit",autocommit=True)
    s1 = "select * from doctor_data"
    cur = cn.cursor()
    cur.execute(s1)
    n = cur.rowcount

    if(n>0):
        data = cur.fetchall()
        return render_template("show_doctor_for_admin.html",vgt=data)
    else:
        return render_template("show_doctor_for_admin.html",msg="No data found")

# show_doctor_data
@app.route('/show_doctor_data',methods=["GET","POST"])
def show_doctor_data():
    cn = pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="punit",autocommit=True)
    s1 = "select * from doctor_data"
    cur = cn.cursor()
    cur.execute(s1)
    n = cur.rowcount

    if(n>0):
        data = cur.fetchall()
        return render_template("show_doctor_data.html",vgt=data)
    else:
        return render_template("show_doctor_data.html",msg="No data found")

# edit_doctor_data
@app.route('/edit_doctor_data',methods=["GET","POST"])
def edit_doctor_data():
    if(request.method=="POST"):
        doc_id = request.form["H1"]
        cn = pymysql.connect(host="localhost",db="punit",passwd="", user="root",autocommit=True,port=3306)
        s1 = "select * from doctor_data where doctor_id="+doc_id
        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n>0):
            data = cur.fetchone()
            return render_template("edit_doctor_data.html",vgt=data)
        else:
            return render_template("edit_doctor_data.html",msg="NO data ")
    else:
        return redirect(url_for("show_doctor_data"))
# edit_doctor_data1
@app.route('/edit_doctor_data1',methods=["GET","POST"])
def edit_doctor_data1():
    if(request.method=="POST"):
        name = request.form["T1"]
        address = request.form["T2"]
        contact = request.form["T3"]
        speciality = request.form["T4"]
        current_hospital = request.form["T5"]
        work_experience = request.form["T6"]
        days = request.form.getlist("T7")
        mon = 'no'
        tues = 'no'
        wed = 'no'
        thu = 'no'
        fri = 'no'
        sat = 'no'
        sun = 'no'

        if ('mon' in days):
            mon = "yes"
        if ('tues' in days):
            tues = "yes"
        if ('wed' in days):
            wed = "yes"
        if ('thu' in days):
            thu = "yes"
        if ('fri' in days):
            fri = "yes"
        if ('sat' in days):
            sat = "yes"
        if ('sun' in days):
            sun = "yes"

        timing = request.form["T8"]
        email = request.form["T9"]
        doc_id = request.form["T10"]
        cn = pymysql.connect(host="localhost",port=3306,db="punit",passwd="",user="root",autocommit=True)
        s1 = "update doctor_data set name='"+name+"',address='"+address+"',contact='"+contact+"',speciality='"+speciality+"',work_experience='"+work_experience+"',current_hospital='"+current_hospital+"',mon='"+mon+"',tues='"+tues+"',wed='"+wed+"',thu='"+thu+"',fri='"+fri+"',sat='"+sat+"',sun='"+sun+"',timing='"+timing+"', email='"+email+"' where doctor_id='"+doc_id+"'"
        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n>0):
            return render_template("edit_doctor_data1.html",msg="Data are changed successfully")
        else:
            return render_template("edit_doctor_data1.html",msg="data changed  are not saved")
    else:
        return redirect(url_for("show_doctor_data"))

# delete_doctor_data
@app.route('/delete_doctor_data',methods=["GET","POST"])
def delete_doctor_data():
    if(request.method=="POST"):
        doc_id = request.form["H1"]
        cn = pymysql.connect(host="localhost",port=3306,passwd="",db="punit",user="root",autocommit=True)
        s1 = "select * from doctor_data where doctor_id='"+doc_id+"'"
        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n>0):
            data = cur.fetchone()
            return render_template("delete_doctor_data.html",vgt=data)
        else:
            return render_template("delete_doctor_data.html",msg="No data found")
    else:
        return redirect(url_for("show_doctor_data"))

# delete_doctor_data1
@app.route('/delete_doctor_data1',methods=["GET","POST"])
def delete_doctor_data1():
    if(request.method=="POST"):
        name = request.form["T1"]
        address = request.form["T2"]
        contact = request.form["T3"]
        speciality = request.form["T4"]
        current_hospital = request.form["T5"]
        work_experience = request.form["T6"]
        week_days = request.form["T7"]
        timing = request.form["T8"]
        email = request.form["T9"]

        cn = pymysql.connect(host="localhost",port=3306,db="punit",passwd="",user="root",autocommit=True)
        s1 = "delete from doctor_data where email='"+email+"'"
        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n>0):
            return render_template("delete_doctor_data1.html",msg="Data are changed successfully")
        else:
            return render_template("delete_doctor_data1.html",msg="data changed  are not saved")
    else:
        return redirect(url_for("show_doctor_data"))

# for login
@app.route('/login',methods=["GET","POST"])
def login():
    if(request.method=="POST"):
        email = request.form["T1"]
        password = request.form["T2"]

        cn = pymysql.connect(host="localhost",port=3306,passwd="",autocommit=True,user="root",db="punit")
        s1 = "select * from logindata where email='"+email+"' AND password='"+password+"'"

        cur = cn.cursor()
        cur.execute(s1)
        n = cur.rowcount
        if(n==1):
            data = cur.fetchone()
            ut = data[2] #fetch usertype from column index 2
            #create session
            session["email"]=email
            session["usertype"]=ut
            #send to page
            if(ut=="admin"):
                return redirect(url_for("admin_home"))
            elif(ut=="hospital"):
                return redirect(url_for("hospital_home"))
            else:
                return render_template("login.html",msg="usertype does not exist")
        else:
            return render_template("login.html",msg="Enter email and password is incorrect")
    else:
        return render_template("login.html")

'''# for  check_login
@app.route('/checklogin', methods=['GET', 'POST'])
def checklogin():
    if (request.method == 'POST'):
        email = request.form["T1"]
        password = request.form["T2"]
        # connection

        sql = "select * from logindata where email='" + email + "' and password='" + password + "'"
        cur = make_connection()
        cur.execute(sql)
        n = cur.rowcount
        if (n > 0):
            # create cookie
            row = cur.fetchone()
            usertype = row[2]
            session["usertype"] = usertype
            session["email"] = email
            if (usertype == "admin"):
                return redirect(url_for('admin_home'))
            elif (usertype == "hospital"):
                return redirect(url_for('hospital_home'))
        else:
            return render_template("loginerror.html")'''

# logout
@app.route("/logout")
def logout():
    #check and remove session
    if "email" in session:
        #remove keys email,usertype from session
        session.pop("email",None)
        session.pop("usertype",None)
        return redirect(url_for("login"))
    else:
        return redirect(url_for("login"))

# admin_home
@app.route("/admin_home")
def admin_home():
    #check session
    if("email" in session):
        email=session["email"]
        ut=session["usertype"]
        if(ut=="admin"):
            photo = check_photo(email)
            cur=make_connection()
            s1="select * from admindata where email='"+email+"'"
            cur.execute(s1)
            a=cur.rowcount
            if(a>0):
                data=cur.fetchone()
            return render_template("admin_home.html",photo=photo,punit=data)
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))

# hospital_home
@app.route("/hospital_home")
def hospital_home():
    # check session
    if ("email" in session):
        e1 = session["email"]
        ut = session["usertype"]
        if (ut == "hospital"):
            photo = check_photo(e1)
            cur = make_connection()
            s1 = "select * from hospital_data where email='" + e1 + "'"
            cur.execute(s1)
            n = cur.rowcount

            if( n > 0):
                data = cur.fetchone()
                s2="select * from doctor_data where email_of_hospital='"+e1+"'"
                cur.execute(s2)
                m=cur.rowcount
                if( m>0 ):
                    data1=cur.fetchall()
                    return render_template("hospital_home.html",photo=photo,punit=data,doctors=data1)
                else:
                    return render_template("hospital_home.html",photo=photo,punit=data,msg="No dcotor found, register doctor")
            else:
                return render_template("hospital_home.html",msg="No profile found")
        else:
            return redirect(url_for("auth_error"))
    else:
        return redirect(url_for("auth_error"))


# auth_error
@app.route("/auth_error")
def auth_error():
    return render_template("auth_error.html")

# admin_photo
@app.route('/admin_photo')
def admin_photo():
    return render_template('photoupload_admin.html')

# admin_photo1
@app.route('/admin_photo1',methods=['GET','POST'])
def admin_photo1():
    if 'usertype' in session:
        usertype=session['usertype']
        email=session['email']
        if usertype=='admin':
            if request.method == 'POST' :
                file = request.files['F1']
                if(file):
                    path = os.path.basename(file.filename)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) + '.' + file_ext
                    filename = secure_filename(filename)
                    cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='punit',autocommit=True)
                    cur = cn.cursor()
                    sql = "insert into photodata values('"+email+"','" + filename + "')"

                    try:
                        cur.execute(sql)
                        n = cur.rowcount
                        if(n == 1):
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                            return render_template('photoupload_admin1.html', result="success")
                        else:
                            return render_template('photoupload_admin1.html', result="failure")
                    except:
                        return render_template('photoupload_admin1.html', result="duplicate")
            else:
                return render_template('photoupload_admin.html')
        else:
            return redirect(url_for('auth_error'))
    else:
        return redirect(url_for('auth_error'))

# hospital_photo
@app.route('/hospital_photo')
def hospital_photo():
    return render_template('photoupload_hospital.html')

# hospital_photo1
@app.route('/hospital_photo1',methods=['GET','POST'])
def hospital_photo1():
    if 'usertype' in session:
        usertype=session['usertype']
        email=session['email']
        if usertype=='hospital':
            if request.method == 'POST':
                file = request.files['F1']
                if(file):
                    path = os.path.basename(file.filename)
                    file_ext = os.path.splitext(path)[1][1:]
                    filename = str(int(time.time())) + '.' + file_ext
                    filename = secure_filename(filename)
                    cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='punit',autocommit=True)
                    cur = cn.cursor()
                    sql = "insert into photodata values('"+email+"','" + filename + "')"

                    try:
                        cur.execute(sql)
                        n = cur.rowcount
                        if(n == 1):
                            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                            return render_template('photoupload_hospital1.html', result="success")
                        else:
                            return render_template('photoupload_hospital1.html', result="failure")
                    except:
                        return render_template('photoupload_hospital1.html', result="duplicate")
            else:
                return render_template('photoupload_hospital.html')
        else:
            return redirect(url_for('auth_error'))
    else:
        return redirect(url_for('auth_error'))

#change_admin_photo
@app.route('/change_admin_photo')
def change_admin_photo():
    if 'usertype' in session:
        usertype = session['usertype']
        email = session['email']
        if usertype=='admin':
            photo = check_photo(email)
            cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='punit',autocommit=True)
            cur = cn.cursor()
            sql = "delete from photodata where user_email='"+email+"'"
            cur.execute(sql)
            n = cur.rowcount
            if(n>0):
                os.remove("./static/photos/"+photo)
                return render_template('change_admin_photo.html',data="success")
            else:
                return render_template('change_admin_photo.html',data="faliure")
        else:
            return redirect(url_for('auth_error'))
    else:
        return redirect(url_for('auth_error'))

#change_hospital_photo
@app.route('/change_hospital_photo')
def change_hospitsal_photo():
    if 'usertype' in session:
        usertype = session['usertype']
        email = session['email']
        if usertype=='hospital':
            photo = check_photo(email)
            cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='punit',autocommit=True)
            cur = cn.cursor()
            sql = "delete from photodata where user_email='"+email+"'"
            cur.execute(sql)
            n = cur.rowcount
            if(n>0):
                os.remove("./static/photos/"+photo)
                return render_template('change_hospital_photo.html',data="success")
            else:
                return render_template('change_hospital_photo.html',data="faliure")
        else:
            return redirect(url_for('auth_error'))
    else:
        return redirect(url_for('auth_error'))
'''
#show_hospitals
@app.route('/show_hospitals')
def show_hospitals():
    if 'usertype' in session:
        usertype = session['usertype']
        email = session['email']
        if usertype == 'admin':
            cn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='punit',autocommit=True)
            cur = cn.cursor()
            cur.execute("select * from hospital_data")
            result = cur.fetchall()
            return  render_template('show_hospitals.html',result = result)
        else:
            return redirect(url_for('auth_error'))
    else:
        return redirect(url_for('auth_error'))
'''
# for search
@app.route('/search',methods=['GET','POST'])
def search():
    if(request.method=='POST'):
        spec = request.form['T1']
        sql = "select * from doctor_data where speciality='"+spec+"'"
        cur = make_connection()
        cur.execute(sql)
        result = cur.fetchall()
        return render_template('search.html',result=result)
    else:
        return render_template('search.html')
# admin_password
@app.route('/admin_password', methods=['GET', 'POST'])
def admin_password():
    if 'usertype' in session:
        usertype = session['usertype']
        email = session['email']
        if usertype == 'admin':
            if (request.method == 'POST'):
                oldpass = request.form['T1']
                newpass = request.form['T2']
                cur = make_connection()
                s1 = "update logindata set password='" +newpass+ "' where password='" +oldpass+ "' AND email='" +email+ "'"
                cur.execute(s1)
                n = cur.rowcount
                if(n > 0):
                    return render_template('admin_password.html', result="Password Changed")
                else:
                    return render_template('admin_password.html', result="Invalid Old Password")
            else:
                return render_template('admin_password.html')
        else:
            return redirect(url_for('auth_error'))
    else:
        return redirect(url_for('auth_error'))

if __name__=="__main__":
    app.run(debug=True)


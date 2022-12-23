import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql 
import re

#========================================Class Cake Creation========================================================

class Cake:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1280x720")
        self.win.title("Delicious Cakes")
        image1 = Image.open("win.jpeg")
        self.test1 = ImageTk.PhotoImage(image1)
        label1 = Label(self.win,image=self.test1)
        label1.place(x=600,y=0)
        label2=Label(self.win, text="Welcome To Delicious Cakes",font="BrushScriptMT 60",fg="#7346FF",bg="#FFE4F7")
        label2.place(x=10,y=10)
        win.configure(bg="#FFE4F7")
        l1=Label(win, text=" User ")
        l1.configure(font='ArialRoundedMTBold 18',bg="#7346FF",fg="white")
        l1.place(x=50,y=175)
        l1=Label(win, text="Email")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=50,y=220)
        l1=Label(win, text="Password")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=50,y=270)
        self.loginmail=Entry(win, width=20)
        self.loginmail.place(x=160,y=220)
        self.loginpw=Entry(win, width=20,show="*")
        self.loginpw.place(x=160,y=270)
        aw=Button(text="Admin",font='ArialRoundedMTBold 18',fg="#7346FF",bg="white",command=self.addwin)
        aw.place(x=120,y=173)
        lw=Button(text="Login",font='ArialRoundedMTBold 18',fg="#7346FF",bg="white", command=self.login)
        lw.place(x=270,y=320)
        sw=Button(text="Sign-up",font='ArialRoundedMTBold',fg="#7346FF",command=self.su)
        sw.place(x=48,y=420)
        fw=Button(text="Forgot-password?",font='ArialRoundedMTBold',fg="#7346FF",command=self.forget)
        fw.place(x=48,y=320)

#========================================login========================================================


    def login(self):
        self.le=str(self.loginmail.get())
        self.lp=str(self.loginpw.get())
        self.sqlconct()
        lsql=("SELECT username FROM customer WHERE emailid=%s and password=%s")
        self.cursor.execute(lsql,[(self.le),(self.lp)])
        self.username=self.cursor.fetchone()[0]
        if self.username==None:
            messagebox.showerror("Error", "Invalid emailid or Password")
        else:
            messagebox.showinfo("Success" , f"Welcome {self.username}!")
            self.product()

#========================================Menu Screen========================================================


    def product(self):
        self.winp=Toplevel()
        self.winp.geometry("1280x720")
        self.winp.title("Product Details")
        self.winp.configure(bg="#FFE4F7")
        sl=Label(self.winp, text=f"Hello {self.username}!", font='ArialRoundedMTBold 25',fg="#7346FF",bg="#FFE4F7")
        sl.place(x=25,y=15)
        self.frame1=Frame(self.winp)
        self.frame1.configure(bg="#FFE4F7")
        self.frame1.place(x=30,y=75,width=850,height=600)
        self.frame2=Frame(self.winp)
        self.frame2.place(x=905,y=75,width=350,height=230)
        self.frame2.configure(bg="#FFE4F7")
        l1=Label(self.frame2, text="Enter Product", font='ArialRoundedMTBold 18',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=10,y=80)
        self.userpro=Entry(self.frame2, width=30)
        self.userpro.place(x=10,y=110)
        l1=Label(self.frame2, text="Enter Address", font='ArialRoundedMTBold 18',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=10,y=140)
        self.useradd=Entry(self.frame2, width=30)
        self.useradd.place(x=10,y=170)
        imsp1=Image.open("des.png")
        self.ress1=imsp1.resize((330,330))
        self.imgps1=ImageTk.PhotoImage(self.ress1)
        lp91=Label(self.winp,image=self.imgps1)
        lp91.place(x=890, y=340)
        l1=Label(self.frame1,text="Best Selling Cakes",font='ArialRoundedMTBold 18',fg="#FD1B1B",bg="#FFE4F7")
        l1.place(x=15,y=0)
        b1=Button(self.frame2,text="Place Order", font='ArialRoundedMTBold', fg="#7346FF",bg="#FFE4F7", command=self.buy)
        b1.place(x=90,y=200)
        imp1=Image.open("Black-forest-cake.jpeg")
        self.res1=imp1.resize((190,190))
        self.imgp1=ImageTk.PhotoImage(self.res1)
        lp1=Label(self.frame1,image=self.imgp1)
        lp1.place(x=25, y=25)
        p1=Label(self.frame1,text='Black Forest',font='ArialRoundedMTBold 15', fg="#7346FF",bg="#FFE4F7")
        p1.place(x=60,y=220)
        imp2=Image.open("RedVelvetCake1.jpg")
        res2=imp2.resize((190,190))
        self.imgp2=ImageTk.PhotoImage(res2)
        lp2=Label(self.frame1,image=self.imgp2)
        lp2.place(x=295, y=25)
        p1=Label(self.frame1,text='Red-Velvet',font='ArialRoundedMTBold 15', fg="#7346FF",bg="#FFE4F7")
        p1.place(x=360,y=220)
        imp3=Image.open("dcc.jpeg")
        self.res3=imp3.resize((190,190))
        self.imgp3=ImageTk.PhotoImage(self.res3)
        lp3=Label(self.frame1,image=self.imgp3)
        lp3.place(x=550, y=25)
        p1=Label(self.frame1,text='Double Delight',font='ArialRoundedMTBold 15', fg="#0357FF",bg="#FFE4F7")
        p1.place(x=590,y=220)
        style=ttk.Style()
        style.configure('Treeview', rowheight=30)
        tree=ttk.Treeview(self.frame1, selectmode='browse')
        tree.place(x=25,y=270)
        tree["columns"]=("1","2","3","4")
        tree["show"]='headings'
        tree.column("1",width=180,anchor='c')
        tree.column("2",width=180,anchor='c')
        tree.column("3",width=180,anchor='c')
        tree.column("4",width=180,anchor='c')

        tree.heading("1",text="Product_Id")
        tree.heading("2",text="Product_Name")
        tree.heading("3",text="Quantiy")
        tree.heading("4",text="Price")
        self.sqlconct()
        self.cursor.execute("SELECT * FROM product")
        b=self.cursor.fetchall()
        for dt in b:
            tree.insert("",'end',values=(dt[0],dt[1],dt[2],dt[3]))

            
    def buy(self):
        self.usepro=str(self.userpro.get())
        userad=str(self.useradd.get())
        self.sqlconct()
        bsql="SELECT price FROM product WHERE product_name=%s"
        self.cursor.execute(bsql,self.usepro)
        self.getpro=self.cursor.fetchone()[0]
        flag=0
        while True:
            if self.usepro == "" or userad == "":
                 messagebox.showerror("Error", "All fields Required to be Filled")
                 flag=-1
                 break
                
            elif self.getpro==None:
                messagebox.showerror("Error", "Product Not There")
                flag=-1
                break
        
            else:
                flag=0
                a=messagebox.askyesno("askyesno", f"Confirm Order of \n {self.usepro} ₹ {self.getpro}")
                if a>0:
                    self.sqlconct()
                    odsql="INSERT INTO orders(userid, productname, total, address) VALUES (%s, %s, %s, %s)"
                    self.cursor.execute(odsql, [(self.le),(self.usepro), (self.getpro), (userad)])
                    self.conn.commit()
                    messagebox.showinfo("Success" , f"Order for {self.usepro} Placed Sucessfully")
                    break

#========================================Sign up========================================================



    def su(self):
        self.winup=Toplevel()
        self.winup.geometry("1280x720")
        self.winup.title("Delicious Cakes")
        self.winup.configure(bg="#FFE4F7")
        image2 = Image.open("cake_720.jpg")
        label2=Label(self.winup, text="Welcome To Delicious Cakes",font="BrushScriptMT 60",fg="#7346FF",bg="#FFE4F7")
        label2.place(x=10,y=10)
        self.test2 = ImageTk.PhotoImage(image2)
        label1 = Label(self.winup,image=self.test2)
        label1.place(x=640, y=0)
        l1=Label(self.winup, text="First Name")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=125)
        self.usernmr=Entry(self.winup, width=20)
        self.usernmr.place(x=35,y=150)
        l1=Label(self.winup, text="Last Name")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=250,y=125)
        self.usernmr1=Entry(self.winup, width=20)
        self.usernmr1.place(x=250,y=150)
        l1=Label(self.winup, text="Email i'd")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=205)
        self.useremailr=Entry(self.winup, width=20)
        self.useremailr.place(x=35,y=230)
        l1=Label(self.winup, text="Phone No.")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=250,y=205)
        self.userphone=Entry(self.winup, width=20)
        self.userphone.place(x=250,y=230)
        l1=Label(self.winup, text="Password")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=285)
        self.userpwr1=Entry(self.winup, width=20,show="*")
        self.userpwr1.place(x=35,y=310)
        l1=Label(self.winup, text="Re-Enter Password")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=250,y=285)
        self.userpwr2=Entry(self.winup, width=20,show="*")
        self.userpwr2.place(x=250,y=310)
        l1=Label(self.winup, text="Security Question?")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=360)
        l1=Label(self.winup, text="What's name of your Favourite Book, Show or Game?")
        l1.configure(font='ArialRoundedMTBold 16',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=390)
        self.userfav=Entry(self.winup, width=20)
        self.userfav.place(x=35,y=415)
        bs=Button(self.winup, text="Submit",font='ArialRoundedMTBold 18',fg="#7346FF",bg="white",command=self.register)
        bs.place(x=180,y=480)

    def register(self):
        un=str(self.usernmr.get())
        ue=str(self.useremailr.get())
        up=int(self.userphone.get())
        upd=str(self.userpwr1.get())
        urp=str(self.userpwr2.get())
        usa=str(self.userfav.get())
        self.sqlconct()
        reqe=("SELECT * FROM customer WHERE emailid=%s")
        self.cursor.execute(reqe, ue)
        self.alpe=self.cursor.fetchone()
        self.cursor.close()
        self.sqlconct()
        reqp=("SELECT * FROM customer WHERE poneno=%s")
        self.cursor.execute(reqp, up)
        self.alpp=self.cursor.fetchone()
        self.cursor.close()
        
        a=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        flag = 0
        while True:
            if upd != urp:
                flag = -1
                messagebox.showerror("showerror", "Password and Re-Enter Password Should be same")
                break
            elif (len(urp)<8):
                flag=-1
                messagebox.showerror("showerror", "Password Should be of minimum 8 Characters")
                break
            elif not re.search("[a-z]", urp):
                flag = -1
                messagebox.showerror("showerror", "Password Should include at least a lowercase character")
                break
            elif not re.search("[A-Z]", urp):
                flag = -1
                messagebox.showerror("showerror", "Password Should include at least an uppercase character")
                break
            elif not re.search("[0-9]", urp):
                flag = -1
                messagebox.showerror("showerror", "Password Should include at least a numeric character")
                break
            elif not re.search("[_@$]", urp):
                flag = -1
                messagebox.showerror("showerror", "Password Should include at least a Special character")
                break
            elif re.search("\s", urp):
                flag = -1
                messagebox.showerror("showerror", "Password Shouldn't include any space")
                break
            
            elif self.alpe != None:
                flag = -1
                messagebox.showerror("showerror", "Entered Email is already present")
                break

            elif self.alpp != None:
                flag = -1
                messagebox.showerror("showerror", "Entered Phone No. is already present")
                break
            
            else:
                flag=0
                rsql="INSERT INTO customer (username, emailid, password, poneno, answer) VALUES (%s, %s, %s, %s, %s)"
                vsql=(un, ue, urp, up, usa)
                self.sqlconct()
                self.cursor.execute(rsql, vsql)
                self.conn.commit()
                messagebox.showinfo("showinfo", "Registered Sucessfully")
                messagebox.showinfo("Success" , f"Welcome {un}!")
                self.sqlconct()
                lsql=("SELECT username FROM customer WHERE poneno=%s")
                self.cursor.execute(lsql,up)
                self.username=self.cursor.fetchone()[0]
                self.product()
                break

#========================================Admin========================================================


    def addwin(self):
        self.winal=Toplevel()
        self.winal.geometry("1280x720")
        self.winal.configure(bg="#FFE4F7")
        la=Label(self.winal,text="Welcome To",font=('BrushScriptMT 50'),fg="#7346FF",bg="#FFE4F7")
        la.place(x=20,y=25)
        la=Label(self.winal,text="Delilcious Cakes (Admin)",font=('BrushScriptMT 50'),fg="#7346FF",bg="#FFE4F7")
        la.place(x=20,y=100)
        imga=Image.open("win.jpeg")
        self.impa=ImageTk.PhotoImage(imga)
        lai=Label(self.winal,image=self.impa)
        lai.pack(side="right")
        la1=Label(self.winal, text="Email")
        la1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        la1.place(x=50,y=220)
        la1=Label(self.winal, text="Password")
        la1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        la1.place(x=50,y=270)
        self.adnmail=Entry(self.winal, width=20)
        self.adnmail.place(x=160,y=220)
        self.adnpw=Entry(self.winal, width=20,show="*")
        self.adnpw.place(x=160,y=270)
        bwo=Button(self.winal,text="Go-to Products & Orders",font='ArialRoundedMTBold',fg="#7346FF",command=self.adlogin)
        bwo.place(x=170,y=310)

    def adlogin(self):
        adem=str(self.adnmail.get())
        adpw=str(self.adnpw.get())
        self.sqlconct()
        adql=("SELECT admin_name FROM admin WHERE emailid=%s and password=%s")
        self.cursor.execute(adql,[(adem),(adpw)])
        adminnm=self.cursor.fetchone()[0]
        if adminnm==None:
            messagebox.showerror("Error", "You are Not Authorized to Login Here")
        else:
            messagebox.showinfo("Success" , f"Welcome {adminnm}!")
            self.admpro()

    
    def admpro(self):
        self.winP=Tk()
        self.winP.geometry('1280x720')
        self.winP.title('Admin window')
        label2=Label(self.winP, text="Delicious Cakes",font="BrushScriptMT 60",fg="#0357FF",bg="#FFE4F7")
        label2.place(x=15,y=15)
        self.winP.configure(bg="#FFE4F7")
        p_i=Label(self.winP, text="Product I'd",font='ArialRoundedMTBold 17',fg="#0357FF",bg="#FFE4F7")
        p_i.place(x=50,y=125)
        p_n=Label(self.winP,text='Product Name',font='ArialRoundedMTBold 17',fg="#0357FF",bg="#FFE4F7")
        p_n.place(x=50,y=175)
        p_q=Label(self.winP,text='Quantity',font='ArialRoundedMTBold 17',fg="#0357FF",bg="#FFE4F7")
        p_q.place(x=50,y=225)
        p=Label(self.winP,text='Price',font='ArialRoundedMTBold 17',fg="#0357FF",bg="#FFE4F7")
        p.place(x=50,y=275)
        self.proid=Entry(self.winP, width=20) #make it auto increament later
        self.proid.place(x=180,y=125)
        self.pronm=Entry(self.winP,width=20)
        self.pronm.place(x=180,y=175)
        self.pros=Entry(self.winP,width=20)
        self.pros.place(x=180,y=225)
        self.propr=Entry(self.winP,width=20)
        self.propr.place(x=180,y=275)
        l1=Label(self.winP, text="Your Products",font='ArialRoundedMTBold 15',fg="#0357FF",bg="#FFE4F7")
        l1.place(x=530,y=10)
        l1=Label(self.winP, text="Your Orders",font='ArialRoundedMTBold 15',fg="#0357FF",bg="#FFE4F7")
        l1.place(x=530,y=360)
        addbtn=Button(self.winP,text='Add product',font='ArialRoundedMTBold',fg="#0357FF",command=self.addproduct)
        addbtn.place(x=230,y=310)

        style=ttk.Style()
        style.configure('Treeview', rowheight=30)
        tree=ttk.Treeview(self.winP, selectmode='browse')
        tree.place(x=530,y=45)
        tree["columns"]=("1","2","3","4")
        tree["show"]='headings'
        tree.column("1",width=180,anchor='c')
        tree.column("2",width=180,anchor='c')
        tree.column("3",width=180,anchor='c')
        tree.column("4",width=180,anchor='c')

        tree.heading("1",text="Product_Id")
        tree.heading("2",text="Product_Name")
        tree.heading("3",text="Quantiy")
        tree.heading("4",text="Price")
        self.sqlconct()
        self.cursor.execute("SELECT * FROM product")
        b=self.cursor.fetchall()
        for dt in b:
            tree.insert("",'end',values=(dt[0],dt[1],dt[2],dt[3]))
            dt=dt+dt

        tree1=ttk.Treeview(self.winP, selectmode='browse')
        tree1.place(x=530,y=390)
        tree1["columns"]=("1","2","3","4")
        tree1["show"]='headings'
        tree1.column("1",width=180,anchor='c')
        tree1.column("2",width=180,anchor='c')
        tree1.column("3",width=180,anchor='c')
        tree1.column("4",width=180,anchor='c')

        tree1.heading("1",text="UserId")
        tree1.heading("2",text="Product_Name")
        tree1.heading("3",text="Amount")
        tree1.heading("4",text="Address")
        self.sqlconct()
        self.cursor.execute("SELECT * FROM orders")
        b=self.cursor.fetchall()
        for dt in b:
            tree1.insert("",'end',values=(dt[0],dt[1],dt[2],dt[3]))
            b=dt+dt

            
    def addproduct(self):
        pid=str(self.proid.get())
        pr=str(self.pronm.get())
        ps=str(self.pros.get())
        pp=str(self.propr.get())
        self.sqlconct()
        rsql="INSERT INTO product (product_id,product_name,quantity,price) VALUES (%s,%s, %s, %s)"
        vsql=(pid,pr,ps,pp)
        self.cursor.execute(rsql, vsql)
        self.conn.commit()
        messagebox.showinfo("showinfo", "Product Added")


#========================================forget password========================================================
        
    def forget(self):
        self.winfp=Toplevel()
        self.winfp.geometry("1280x720")
        self.winfp.title("Delicious Cakes")
        self.winfp.configure(bg="#FFE4F7")
        image2 = Image.open("sinup.jpg")
        label2=Label(self.winfp, text="Welcome To Delicious Cakes",font="BrushScriptMT 60",fg="#7346FF",bg="#FFE4F7")
        label2.place(x=10,y=10)
        self.test2 = ImageTk.PhotoImage(image2)
        label1 = Label(self.winfp,image=self.test2)
        label1.place(x=640, y=0)
        l1=Label(self.winfp, text="Phone No.")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=145)
        self.userpn=Entry(self.winfp, width=20)
        self.userpn.place(x=35,y=170)
        l1=Label(self.winfp, text="Security Question?")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=210)
        l1=Label(self.winfp, text="What's name of your Favourite Book, Show or Game?")
        l1.configure(font='ArialRoundedMTBold 16',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=240)
        self.userans=Entry(self.winfp, width=20)
        self.userans.place(x=35,y=265)
        l1=Label(self.winfp, text="New Password")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=300)
        self.npass=Entry(self.winfp, width=20,show="*")
        self.npass.place(x=35,y=325)
        l1=Label(self.winfp, text="Re-Enter New Password")
        l1.configure(font='ArialRoundedMTBold 17',fg="#7346FF",bg="#FFE4F7")
        l1.place(x=35,y=360)
        self.newpassr=Entry(self.winfp, width=20,show="*")
        self.newpassr.place(x=35,y=385)
        fgb=Button(self.winfp, text="Submit",font='ArialRoundedMTBold 16',fg="#7346FF",command=self.forgetpass)
        fgb.place(x=160, y=420)



    def forgetpass(self):
        usph=str(self.userpn.get())
        ussa=str(self.userans.get())
        usnp=str(self.npass.get())
        usrp=str(self.newpassr.get())
        self.sqlconct()
        fsql=("SELECT username FROM customer WHERE poneno=%s and answer=%s")
        self.cursor.execute(fsql,[(usph),(ussa)])
        self.username=self.cursor.fetchone()[0]
        if self.username==None:
            messagebox.showerror("Error", "Invalid Phone No or Security Answer")
        else:
            a=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            flag = 0
            while True:
                if usnp != usrp:
                    flag = -1
                    messagebox.showerror("showerror", "Password and Re-Enter Password Should be same")
                    break
                elif (len(usrp)<8):
                    flag=-1
                    messagebox.showerror("showerror", "Password Should be of minimum 8 Characters")
                    break
                elif not re.search("[a-z]", usrp):
                    flag = -1
                    messagebox.showerror("showerror", "Password Should include at least a lowercase character")
                    break
                elif not re.search("[A-Z]", usrp):
                    flag = -1
                    messagebox.showerror("showerror", "Password Should include at least an uppercase character")
                    break
                elif not re.search("[0-9]", usrp):
                    flag = -1
                    messagebox.showerror("showerror", "Password Should include at least a numeric character")
                    break
                elif not re.search("[_@$]", usrp):
                    flag = -1
                    messagebox.showerror("showerror", "Password Should include at least a Special character")
                    break
                elif re.search("\s", usrp):
                    flag = -1
                    messagebox.showerror("showerror", "Password Shouldn't include any space")
                    break
                else:
                    flag=0
                    self.sqlconct()
                    fgsql="UPDATE customer SET password=%s WHERE poneno=%s"
                    fusql=(usrp, usph)
                    self.cursor.execute(fgsql, fusql)
                    self.conn.commit()
                    messagebox.showinfo("Success" , "Password Updated Sucessfully")
                    messagebox.showinfo("Success" , f"Welcome {self.username}!")
                    self.product()
                    break

#========================================Database Connectivity========================================================

    
    def sqlconct(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',db='cake_shop')
        self.cursor=self.conn.cursor()


win=Tk()
obj=Cake(win)

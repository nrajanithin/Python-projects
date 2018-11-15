import random
import MySQLdb
from Tkinter import *
import pyttsx
import tkMessageBox
class Raj():
  def __init__(self):
   self.win=Tk()
   self.win.title('YOUR EXAM PORTAL')
   self.win.geometry('1240x700')
   self.win.config(background='green')
   photo=PhotoImage(file="his.png")
   self.btn=Button(self.win,text="TAKE TEST ON HISTORY",image=photo,command=self.hisexam,width=300,height=300)
   self.btn.place(x=10,y=10)
   gphoto=PhotoImage(file="geo.png")
   self.btn1=Button(self.win,text="TAKE TEST ON GEOGRAPHY",image=gphoto,command=self.geoexam,width=300,height=300)
   self.btn1.place(x=400,y=10)
   cphoto=PhotoImage(file="c.png")
   self.btn2=Button(self.win,text="TAKE TEST ON C",image=cphoto,command=self.cexam,width=300,height=300)
   self.btn2.place(x=800,y=10)
   jphoto=PhotoImage(file="java.png")
   self.btn3=Button(self.win,text="TAKE TEST ON JAVA",image=jphoto,command=self.javaexam,width=300,height=300)
   self.btn3.place(x=10,y=350)  
   pyphoto=PhotoImage(file="python.png")
   self.btn4=Button(self.win,text="TAKE TEST ON PYTHON",image=pyphoto,command=self.pythonexam,width=300,height=300)
   self.btn4.place(x=400,y=350)
   post=PhotoImage(file="login.png")
   self.btn5=Button(self.win,text="POST QUESTIONS",image=post,command=self.nit,width=300,height=300)
   self.btn5.place(x=800,y=350)
   self.win.mainloop()
  def pythonexam(self):
   engine=pyttsx.init()
   engine.say('welcome to python exam')
   engine.runAndWait()
   print 'python exam'
   self.win8=Toplevel()
   self.win8.geometry('700x650')
   self.win8.config(background='blue')
   self.win8.title('python exam')
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   sql='select * from python'
   questions=[]
   answers=[]
   try:
    cursor.execute(sql)
    result=cursor.fetchall()
   except:
    db.rollback()
   for i in range(0,len(result)):
    for j in range(0,2):
      if j==0:
        questions.append(result[i][j])
      else:
        answers.append(result[i][j])
   print len(result)
   print questions[2]
    #print answers
   self.li=[]
   self.li=random.sample(range(0,len(answers)),5)
   print self.li
   self.answer=[]
   for i in self.li:
     self.answer.append(answers[i])
   dar=10
   ref=1
   for i in self.li:
     print 'watch this'
     lb=Label(self.win8,text=str(ref)+'.'+questions[i],bg='red')
     lb.place(x=10,y=dar)
     dar+=50
     ref+=1
   self.a1=StringVar()
   self.a11=Entry(self.win8,textvariable=self.a1,width=20)
   self.a11.place(x=10,y=300)
   self.a2=StringVar()
   self.a22=Entry(self.win8,textvariable=self.a2,width=20)
   self.a22.place(x=10,y=350)
   self.a3=StringVar()
   self.a33=Entry(self.win8,textvariable=self.a3,width=20)
   self.a33.place(x=10,y=400) 
   self.a4=StringVar()
   self.a44=Entry(self.win8,textvariable=self.a4,width=20)
   self.a44.place(x=10,y=450)     
   self.a5=StringVar()
   self.a55=Entry(self.win8,textvariable=self.a5,width=20)
   self.a55.place(x=10,y=500)
   self.btn=Button(self.win8,text="submit answers",command=self.getpymarks)
   self.btn.place(x=100,y=550)
  def getpymarks(self):
   print self.answer
   li=[]
   li.append(self.a11.get())
   li.append(self.a22.get())
   li.append(self.a33.get())
   li.append(self.a44.get())
   li.append(self.a55.get())
   print li
   co=0
   for i in range(0,5):
    if self.answer[i].strip()==li[i].strip():
     co+=1
   tkMessageBox.showinfo('Result','You got:'+str(co)+' marks')
  def cexam(self):
   print 'c exam'
   engine=pyttsx.init()
   engine.say('welcome to c exam')
   engine.runAndWait()
   self.win9=Toplevel()
   self.win9.geometry('700x650')
   self.win9.config(background='blue')
   self.win9.title('c exam')
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   sql='select * from c'
   questions=[]
   answers=[]
   try:
    cursor.execute(sql)
    result=cursor.fetchall()
   except:
    db.rollback()
   for i in range(0,len(result)):
    for j in range(0,2):
      if j==0:
        questions.append(result[i][j])
      else:
        answers.append(result[i][j])
   print len(result)
   print questions[2]
    #print answers
   self.li=[]
   self.li=random.sample(range(0,len(answers)),5)
   print self.li
   self.answer=[]
   for i in self.li:
     self.answer.append(answers[i])
   dar=10
   ref=1
   for i in self.li:
     print 'watch this'
     lb=Label(self.win9,text=str(ref)+'.'+questions[i],bg='red')
     lb.place(x=10,y=dar)
     dar+=50
     ref+=1
   self.a1=StringVar()
   self.a11=Entry(self.win9,textvariable=self.a1,width=20)
   self.a11.place(x=10,y=300)
   self.a2=StringVar()
   self.a22=Entry(self.win9,textvariable=self.a2,width=20)
   self.a22.place(x=10,y=350)
   self.a3=StringVar()
   self.a33=Entry(self.win9,textvariable=self.a3,width=20)
   self.a33.place(x=10,y=400) 
   self.a4=StringVar()
   self.a44=Entry(self.win9,textvariable=self.a4,width=20)
   self.a44.place(x=10,y=450)     
   self.a5=StringVar()
   self.a55=Entry(self.win9,textvariable=self.a5,width=20)
   self.a55.place(x=10,y=500)
   self.btn=Button(self.win9,text="submit answers",command=self.getcmarks)
   self.btn.place(x=100,y=550)
  def getcmarks(self):
   print self.answer
   li=[]
   li.append(self.a11.get())
   li.append(self.a22.get())
   li.append(self.a33.get())
   li.append(self.a44.get())
   li.append(self.a55.get())
   print li
   co=0
   for i in range(0,5):
    if self.answer[i].strip()==li[i].strip():
     co+=1
   tkMessageBox.showinfo('Result','You got:'+str(co)+' marks')
  def javaexam(self):
   print 'java exam'
   engine=pyttsx.init()
   engine.say('welcome to java exam')
   engine.runAndWait()
   self.win10=Toplevel()
   self.win10.geometry('700x650')
   self.win10.config(background='blue')
   self.win10.title('java exam')
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   sql='select * from java'
   questions=[]
   answers=[]
   try:
    cursor.execute(sql)
    result=cursor.fetchall()
   except:
    db.rollback()
   for i in range(0,len(result)):
    for j in range(0,2):
      if j==0:
        questions.append(result[i][j])
      else:
        answers.append(result[i][j])
   print len(result)
   print questions[2]
    #print answers
   self.li=[]
   self.li=random.sample(range(0,len(answers)),5)
   print self.li
   self.answer=[]
   for i in self.li:
     self.answer.append(answers[i])
   dar=10
   ref=1
   for i in self.li:
     print 'watch this'
     lb=Label(self.win10,text=str(ref)+'.'+questions[i],bg='red')
     lb.place(x=10,y=dar)
     dar+=50
     ref+=1
   self.a1=StringVar()
   self.a11=Entry(self.win10,textvariable=self.a1,width=20)
   self.a11.place(x=10,y=300)
   self.a2=StringVar()
   self.a22=Entry(self.win10,textvariable=self.a2,width=20)
   self.a22.place(x=10,y=350)
   self.a3=StringVar()
   self.a33=Entry(self.win10,textvariable=self.a3,width=20)
   self.a33.place(x=10,y=400) 
   self.a4=StringVar()
   self.a44=Entry(self.win10,textvariable=self.a4,width=20)
   self.a44.place(x=10,y=450)     
   self.a5=StringVar()
   self.a55=Entry(self.win10,textvariable=self.a5,width=20)
   self.a55.place(x=10,y=500)
   self.btn=Button(self.win10,text="submit answers",command=self.getjavamarks)
   self.btn.place(x=100,y=550)
  def getjavamarks(self):
   print self.answer
   li=[]
   li.append(self.a11.get())
   li.append(self.a22.get())
   li.append(self.a33.get())
   li.append(self.a44.get())
   li.append(self.a55.get())
   print li
   co=0
   for i in range(0,5):
    if self.answer[i].strip()==li[i].strip():
     co+=1
   tkMessageBox.showinfo('Result','You got:'+str(co)+' marks')
  def hisexam(self):
   print 'history exam'
   engine=pyttsx.init()
   engine.say('welcome to history exam')
   engine.runAndWait()
   self.win11=Toplevel()
   self.win11.geometry('700x650')
   self.win11.config(background='blue')
   self.win11.title('history exam')
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   sql='select * from history'
   questions=[]
   answers=[]
   try:
    cursor.execute(sql)
    result=cursor.fetchall()
   except:
    db.rollback()
   for i in range(0,len(result)):
    for j in range(0,2):
      if j==0:
        questions.append(result[i][j])
      else:
        answers.append(result[i][j])
   print len(result)
   print questions[2]
    #print answers
   self.li=[]
   self.li=random.sample(range(0,len(answers)),5)
   print self.li
   self.answer=[]
   for i in self.li:
     self.answer.append(answers[i])
   dar=10
   ref=1
   for i in self.li:
     print 'watch this'
     lb=Label(self.win11,text=str(ref)+'.'+questions[i],bg='red')
     lb.place(x=10,y=dar)
     dar+=50
     ref+=1
   self.a1=StringVar()
   self.a11=Entry(self.win11,textvariable=self.a1,width=20)
   self.a11.place(x=10,y=300)
   self.a2=StringVar()
   self.a22=Entry(self.win11,textvariable=self.a2,width=20)
   self.a22.place(x=10,y=350)
   self.a3=StringVar()
   self.a33=Entry(self.win11,textvariable=self.a3,width=20)
   self.a33.place(x=10,y=400) 
   self.a4=StringVar()
   self.a44=Entry(self.win11,textvariable=self.a4,width=20)
   self.a44.place(x=10,y=450)     
   self.a5=StringVar()
   self.a55=Entry(self.win11,textvariable=self.a5,width=20)
   self.a55.place(x=10,y=500)
   self.btn=Button(self.win11,text="submit answers",command=self.gethismarks)
   self.btn.place(x=100,y=550)
  def gethismarks(self):
   print self.answer
   li=[]
   li.append(self.a11.get())
   li.append(self.a22.get())
   li.append(self.a33.get())
   li.append(self.a44.get())
   li.append(self.a55.get())
   print li
   co=0
   for i in range(0,5):
    if self.answer[i].strip()==li[i].strip():
     co+=1
   tkMessageBox.showinfo('Result','You got:'+str(co)+' marks')
  def geoexam(self):
   print 'geography exam'
   engine=pyttsx.init()
   engine.say('welcome to geography exam')
   engine.runAndWait()
   self.win12=Toplevel()
   self.win12.geometry('700x650')
   self.win12.config(background='blue')
   self.win12.title('geography exam')
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   sql='select * from geography'
   questions=[]
   answers=[]
   try:
    cursor.execute(sql)
    result=cursor.fetchall()
   except:
    db.rollback()
   for i in range(0,len(result)):
    for j in range(0,2):
      if j==0:
        questions.append(result[i][j])
      else:
        answers.append(result[i][j])
   print len(result)
   print questions[2]
    #print answers
   self.li=[]
   self.li=random.sample(range(0,len(answers)),5)
   print self.li
   self.answer=[]
   for i in self.li:
     self.answer.append(answers[i])
   dar=10
   ref=1
   for i in self.li:
     print 'watch this'
     lb=Label(self.win12,text=str(ref)+'.'+questions[i],bg='red')
     lb.place(x=10,y=dar)
     dar+=50
     ref+=1
   self.a1=StringVar()
   self.a11=Entry(self.win12,textvariable=self.a1,width=20)
   self.a11.place(x=10,y=300)
   self.a2=StringVar()
   self.a22=Entry(self.win12,textvariable=self.a2,width=20)
   self.a22.place(x=10,y=350)
   self.a3=StringVar()
   self.a33=Entry(self.win12,textvariable=self.a3,width=20)
   self.a33.place(x=10,y=400) 
   self.a4=StringVar()
   self.a44=Entry(self.win12,textvariable=self.a4,width=20)
   self.a44.place(x=10,y=450)     
   self.a5=StringVar()
   self.a55=Entry(self.win12,textvariable=self.a5,width=20)
   self.a55.place(x=10,y=500)
   self.btn=Button(self.win12,text="submit answers",command=self.getgeomarks)
   self.btn.place(x=100,y=550)
  def getgeomarks(self):
   print self.answer
   li=[]
   li.append(self.a11.get())
   li.append(self.a22.get())
   li.append(self.a33.get())
   li.append(self.a44.get())
   li.append(self.a55.get())
   print li
   co=0
   for i in range(0,5):
    if self.answer[i].strip()==li[i].strip():
     co+=1
   tkMessageBox.showinfo('Result','You got:'+str(co)+' marks')
  def nit(self):
   print "please login dear admin"
   self.win1=Toplevel()
   self.win1.title('ADMIN LOGIN')
   self.win1.geometry('250x250')
   self.win1.config(background='blue')
   lb=Label(self.win1,text='ENTER THE USERNAME:',bg='green',font='timesnewroman')
   lb.place(x=10,y=10)
   self.usna=StringVar();
   self.enusna=Entry(self.win1,textvariable=self.usna,width=20)
   self.enusna.place(x=10,y=50)
   lb1=Label(self.win1,text='ENTER THE PASSWORD:',bg='green',font='timesnewroman')
   lb1.place(x=10,y=100)
   self.pas=StringVar();
   self.pas1=Entry(self.win1,textvariable=self.pas,width=20,show='*')
   self.pas1.place(x=10,y=150)  
   b=Button(self.win1,text="LOGIN",command=self.adminpage)
   b.place(x=50,y=200)
  def adminpage(self):
   un=self.enusna.get()
   pw=self.pas1.get()
   if un=="rajanithinvarma" and pw=="rajanithinvarma":
    self.win1.destroy()
    self.win2=Toplevel()
    self.win2.title('questions Posting page')
    self.win2.configure(background='green')
    self.win2.geometry('1200x1000')
    photo=PhotoImage(file="his.png")
    self.btn=Button(self.win2,text="TAKE TEST ON HISTORY",image=photo,command=self.hispost,width=300,height=300)
    self.btn.place(x=10,y=10)
    self.btn.image=photo
    gphoto=PhotoImage(file="geo.png")
    self.btn1=Button(self.win2,text="TAKE TEST ON GEOGRAPHY",image=gphoto,command=self.geopost,width=300,height=300)
    self.btn1.place(x=400,y=10)
    self.btn1.image=gphoto
    cphoto=PhotoImage(file="c.png")
    self.btn2=Button(self.win2,text="TAKE TEST ON C",image=cphoto,command=self.cpost,width=300,height=300)
    self.btn2.place(x=800,y=10)
    self.btn2.image=cphoto
    jphoto=PhotoImage(file="java.png")
    self.btn3=Button(self.win2,text="TAKE TEST ON JAVA",image=jphoto,command=self.javapost,width=300,height=300)
    self.btn3.place(x=10,y=350)
    self.btn3.image=jphoto  
    pyphoto=PhotoImage(file="python.png")
    self.btn4=Button(self.win2,text="TAKE TEST ON PYTHON",image=pyphoto,command=self.pythonpost,width=300,height=300)
    self.btn4.place(x=400,y=350)
    self.btn4.image=pyphoto  
   else:
    print 'try again'
  def hispost(self):
   print 'history'
   self.win3=Toplevel()
   self.win3.title('History')
   self.win3.configure(background='blue')
   self.win3.geometry('800x500')
   lb=Label(self.win3,text='ENTER THE QUESTION:',bg='green',font='timesnewroman')
   lb.place(x=10,y=10)
   self.t=Text(self.win3,width=100,height=10)
   self.t.place(x=10,y=30)
   lb1=Label(self.win3,text='ENTER THE ANSWER:',bg='green',font='timesnewroman')
   lb1.place(x=10,y=250)
   self.ans=StringVar()
   self.pans=Entry(self.win3,width=30,textvariable=self.ans)
   self.pans.place(x=10,y=280)
   btn=	Button(self.win3,text="POST THE QUESTION",command=self.hposting,padx=10, pady=10)
   btn.place(x=100,y=350)
  def hposting(self):
   te=self.t.get('0.0',END)
   a=self.pans.get()
   self.win3.destroy()
   #print te
   #print a
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   try:
    sql='insert into history values("'+te+'","'+a+'")'
    print sql
    cursor.execute(sql)
    db.commit()
    print 'ok'
    db.close()
    self.hispost()
   except:
    db.rollback()
  def geopost(self):
   print 'geography'
   self.win4=Toplevel()
   self.win4.title('GEOGRAPHY')
   self.win4.configure(background='blue')
   self.win4.geometry('800x500')
   lb=Label(self.win4,text='ENTER THE QUESTION:',bg='green',font='timesnewroman')
   lb.place(x=10,y=10)
   self.t1=Text(self.win4,width=100,height=10)
   self.t1.place(x=10,y=30)
   lb1=Label(self.win4,text='ENTER THE ANSWER:',bg='green',font='timesnewroman')
   lb1.place(x=10,y=250)
   self.ans1=StringVar()
   self.pans1=Entry(self.win4,width=30,textvariable=self.ans1)
   self.pans1.place(x=10,y=280)
   btn=	Button(self.win4,text="POST THE QUESTION",command=self.gposting,padx=10, pady=10)
   btn.place(x=100,y=350)
  def gposting(self):
   te=self.t1.get('0.0',END)
   a=self.pans1.get()
   self.win4.destroy()
   #print te
   #print a
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   try:
    sql='insert into geography values("'+te+'","'+a+'")'
    print sql
    cursor.execute(sql)
    db.commit()
    print 'ok'
    db.close()
    self.geopost()
   except:
    db.rollback()
  def cpost(self):
   print 'c'
   self.win5=Toplevel()
   self.win5.title('C')
   self.win5.configure(background='blue')
   self.win5.geometry('800x500')
   lb=Label(self.win5,text='ENTER THE QUESTION:',bg='green',font='timesnewroman')
   lb.place(x=10,y=10)
   self.t2=Text(self.win5,width=100,height=10)
   self.t2.place(x=10,y=30)
   lb1=Label(self.win5,text='ENTER THE ANSWER:',bg='green',font='timesnewroman')
   lb1.place(x=10,y=250)
   self.ans2=StringVar()
   self.pans2=Entry(self.win5,width=30,textvariable=self.ans2)
   self.pans2.place(x=10,y=280)
   btn=	Button(self.win5,text="POST THE QUESTION",command=self.cposting,padx=10, pady=10)
   btn.place(x=100,y=350)
  def cposting(self):
   te=self.t2.get('0.0',END)
   a=self.pans2.get()
   self.win5.destroy()
   #print te
   #print a
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   try:
    sql='insert into c values("'+te+'","'+a+'")'
    print sql
    cursor.execute(sql)
    db.commit()
    print 'ok'
    db.close()
    self.cpost()
   except:
    db.rollback()
  def javapost(self):
   self.win6=Toplevel()
   self.win6.title('JAVA')
   self.win6.configure(background='blue')
   self.win6.geometry('800x500')
   lb=Label(self.win6,text='ENTER THE QUESTION:',bg='green',font='timesnewroman')
   lb.place(x=10,y=10)
   self.t3=Text(self.win6,width=100,height=10)
   self.t3.place(x=10,y=30)
   lb1=Label(self.win6,text='ENTER THE ANSWER:',bg='green',font='timesnewroman')
   lb1.place(x=10,y=250)
   self.ans3=StringVar()
   self.pans3=Entry(self.win6,width=30,textvariable=self.ans3)
   self.pans3.place(x=10,y=280)
   btn=	Button(self.win6,text="POST THE QUESTION",command=self.jposting,padx=10, pady=10)
   btn.place(x=100,y=350)
  def jposting(self):
   te=self.t3.get('0.0',END)
   a=self.pans3.get()
   self.win6.destroy()
   #print te
   #print a
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   try:
    sql='insert into java values("'+te+'","'+a+'")'
    print sql
    cursor.execute(sql)
    db.commit()
    print 'ok'
    db.close()
    self.javapost()
   except:
    db.rollback()
  def pythonpost(self):
   print 'python'
   self.win7=Toplevel()
   self.win7.title('PYTHON')
   self.win7.configure(background='blue')
   self.win7.geometry('800x500')
   lb=Label(self.win7,text='ENTER THE QUESTION:',bg='green',font='timesnewroman')
   lb.place(x=10,y=10)
   self.t4=Text(self.win7,width=100,height=10)
   self.t4.place(x=10,y=30)
   lb1=Label(self.win7,text='ENTER THE ANSWER:',bg='green',font='timesnewroman')
   lb1.place(x=10,y=250)
   self.ans4=StringVar()
   self.pans4=Entry(self.win7,width=30,textvariable=self.ans4)
   self.pans4.place(x=10,y=280)
   btn=	Button(self.win7,text="POST THE QUESTION",command=self.pposting,padx=10, pady=10)
   btn.place(x=100,y=350)
  def pposting(self):
   te=self.t4.get('0.0',END)
   a=self.pans4.get()
   self.win7.destroy()
   #print te
   #print a
   db=MySQLdb.connect('localhost','root','varma','nithinraj')
   cursor=db.cursor()
   try:
    sql='insert into python values("'+te+'","'+a+'")'
    print sql
    cursor.execute(sql)
    db.commit()
    print 'ok'
    db.close()
    self.pythonpost()
   except:
    db.rollback()
Raj()


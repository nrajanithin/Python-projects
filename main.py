from Tkinter import *
from pytube import YouTube
#from moviepy.editor import VideoFileClip
import pygame
import smtplib
import MySQLdb
import urllib
import speech_recognition as sr
import webbrowser
import calendar
import pyttsx
import tkMessageBox
import time
#from demo import *
from pygame import mixer
engine=pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)
engine.say('hello ')
engine.say('i am your personal assistant')
engine.say(' how can i help you')
engine.runAndWait()
class main():
 def __init__(self):
  win=Tk()
  win.title('PERSONAL ASSISTANT')
  win.geometry('1000x1000')
  win.configure(background='red')
  lb=Label(win,text='CLICK THE BUTTON FOR SETTING THE ALARM',bg='green',font='timesnewroman')
  lb.place(x=10,y=50)
  lb1=Label(win,text='CLICK THE BUTTON FOR CREATING THE NOTIFICATION',bg='green',font='timesnewroman')
  lb1.place(x=450,y=50)
  lb2=Label(win,text='ENTER THE SONG NAME OF YOUR WISH',bg='green',font='timesnewroman')
  lb2.place(x=25,y=250)
  lb3=Label(win,text='ENTER DATA TO SEARCH',bg='green',font='timesnewroman')
  lb3.place(x=450,y=250)
  lb4=Label(win,text='DATABASE MANAGEMENT :',bg='green',font='timesnewroman')
  lb4.place(x=40,y=500)
  lb5=Label(win,text='VIDEO PLAYER',bg='green',font='timesnewroman')
  lb5.place(x=40,y=545)
  btn=Button(win,text='OPEN VIDEO PLAYER',command=self.ovp)
  btn.place(x=300,y=540)
  btnmail=Button(win,text='SEND MAIL',command=self.sendmail)
  btnmail.place(x=300,y=580)
  b=Button(win,text='SET',padx=10,pady=10)
  b.place(x=100,y=100)
  b1=Button(win,text='CREATE',padx=10,pady=10) 
  b1.place(x=520,y=100)
  self.a=StringVar()
  self.e=Entry(win,textvariable=self.a)
  self.e.place(x=70,y=300)
  self.b=StringVar()
  self.f=Entry(win,textvariable=self.b)
  self.f.place(x=520,y=300)
  b2=Button(win,text='PLAY',command=self.song)
  b2.place(x=100,y=350)
  b3=Button(win,text='STOP',command=self.stop)
  b3.place(x=175,y=350)
  b4=Button(win,text='PAUSE',command=self.pause)
  b4.place(x=100,y=390)
  b5=Button(win,text='RESUME',command=self.unpause)
  b5.place(x=175,y=390)
  b6=Button(win,text='RESTART',padx=10,pady=10,command=self.rewind)
  b6.place(x=65,y=430)
  b7=Button(win,text='SEARCH',command=self.search,padx=8,pady=5)
  b7.place(x=500,y=335)
  b8=Button(win,text='IMAGES',command=self.img,padx=8,pady=5)
  b8.place(x=575,y=335)
  b9=Button(win,text='MAPS',command=self.map,padx=8,pady=5)
  b9.place(x=650,y=335)
  b10=Button(win,text='SEARCH BY VOICE',command=self.voice,padx=5,pady=15)
  b10.place(x=550,y=375)
  b11=Button(win,text='VOICE INPUT',command=self.vo,padx=10,pady=10)
  b11.place(x=150,y=430)
  b12=Button(win,text='SPEAK',command=self.sp,padx=30,pady=10)
  b12.place(x=330,y=160)
  b13=Button(win,text='OPEN DATABASE CONTROLLER',command=self.dbcontrol)
  b13.place(x=280,y=500)
  win.mainloop()
 def sendmail(self):
  win21=Tk()
  win21.title('GMAIL LOGIN')
  win21.geometry('600x300')
  win21.config(background='green')
  l=Label(win21,text='ENTER YOUR EMAIL ADDRESS',bg='red')
  l.place(x=30,y=30)
  self.vivma=StringVar()
  self.vivma1=Entry(win21,textvariable=self.vivma,width=50)
  self.vivma1.place(x=30,y=60)
  l1=Label(win21,text='ENTER THE PASSWORD',bg='red')
  l1.place(x=30,y=120)
  self.vivpas=StringVar()
  self.vivpas1=Entry(win21,textvariable=self.vivpas,show='*',width=50)
  self.vivpas1.place(x=30,y=150)
  btn=Button(win21,text="LOG IN",command=self.check,padx=10,pady=10)
  btn.place(x=200,y=220)
 def check(self):
  ga=self.vivma1.get()
  gp=self.vivpas1.get()
  try:
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(ga,gp)
   self.nigm()
  except:
   print('PLEASE CONNECT TO INTERNET or YOUR INPUTS')
 def nigm(self):
  win22=Tk()
  win22.title('EMAIL SENDER')
  win22.geometry('800x700')
  win22.config(background='blue')
  l=Label(win22,text='ENTER THE RECIEVER ADDRESSES SEPERATED BY COMMA(,)')
  l.place(x=30,y=30)
  self.recadd=StringVar()
  self.recadd1=Entry(win22,textvariable=self.recadd,width=60)
  self.recadd1.place(x=30,y=60)
  l1=Label(win22,text='ENTER THE TEXT')
  l1.place(x=30,y=100)
  self.msg=Text(win22,width=75,height=25)
  self.msg.place(x=30,y=135)
  btnilov=Button(win22,text='SEND MAIL',command=self.sendilo)
  btnilov.place(x=300,y=650)
  btnilove=Button(win22,text='ADD CONTACT',command=self.sendilo1)
  btnilove.place(x=410,y=650)
 def sendilo1(self):
  win23=Tk()
  win23.title('ADD CONTACT')
  win23.geometry('350x250')
  win23.config(background='yellow')
  l=Label(win23,text='ENTER THE CONTACT NAME',bg='red')
  l.place(x=30,y=30)
  self.cone=StringVar()
  self.cone1=Entry(win23,textvariable=self.cone,width=20)
  self.cone1.place(x=30,y=60)
  l1=Label(win23,text='ENTER THE MAIL ADDRESS OF THE CONTACT')
  l1.place(x=30,y=100)
  self.cong=StringVar()
  self.cong1=Entry(win23,textvariable=self.cong,width=30)
  self.cong1.place(x=30,y=130)
  kk=Button(win23,text='save contact',command=self.addcdb)
  kk.place(x=75,y=160)
 def addcdb(self):
  cn=self.cone1.get()
  cg=self.cong1.get()
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  sql='insert into email values('+"'"+cn+"'"+','+"'"+cg+"'"+')'
  print sql
  try:
   cursor.execute(sql)
   db.commit()
   tkMessageBox.showinfo('NOTE','CONTACT ADDED :)')
  except:
   db.rollback()
 def sendilo(self):
  s=self.vivma1.get()
  p=self.vivpas1.get()
  r=self.recadd1.get()
  r1=r.split(',')
  r2=[]
  for i in r1:
   if '@gmail.com' in i:
     r2.append(i)
   else:
     db=MySQLdb.connect('localhost','root','pbl123','new')
     cursor=db.cursor()
     sql='select mail from email where name='+"'"+i+"'"
     try:
      cursor.execute(sql)
      result=cursor.fetchall()
      r2.append(result[0][0])
     except:
      db.rollback()
     db.close
  print r2
  msg1=self.msg.get('0.0',END)
  try:
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(s,p)  
   for i in r2:
    server.sendmail(s,i,msg1)
   server.quit()
  except:
   print 'error'
 def ovp(self):
  win15=Tk()
  win15.title('VIDEO PLAYER')
  win15.geometry('250x250')
  win15.configure(background='blue')
  lb=Label(win15,text='ENTER THE VIDEO NAME',bg='red')
  lb.place(x=10,y=10)
  self.ovpe=StringVar()
  self.ovpe1=Entry(win15,textvariable=self.ovpe)
  self.ovpe1.place(x=10,y=50)
  btn=Button(win15,text='PLAY',command=self.ovp1,padx=10,pady=10)
  btn.place(x=10,y=100)
  btn1=Button(win15,text='STOP',command=self.ovp2,padx=10,pady=10)
  btn1.place(x=100,y=100)
 def ovp1(self):
  '''x=self.ovpe1.get()
  p='/home/pbl/Desktop/python/'+x+'.webm'
  pygame.display.set_caption('My video!')
  clip = VideoFileClip(p)
  try:
   clip.preview()
  except:
   tkMessageBox.showinfo('ALERT','ERROR')'''
 def ovp2(self):
  #pygame.quit()
  pass
 def dbcontrol(self):
  print('opened data base controller')
  win4=Tk()
  win4.title('DATABASE CONTROLLER')
  win4.configure(background='blue')
  win4.geometry('500x500')
  cre=Button(win4,text='CREATE A TABLE',command=self.createtable,padx=10,pady=10)
  cre.place(x=20,y=10)
  alter=Button(win4,text='ALTER A TABLE',command=self.al,padx=10,pady=10)
  alter.place(x=20,y=60)
  update=Button(win4,text='UPDATE A TABLE',command=self.update,padx=10,pady=10)
  update.place(x=20,y=110)
  rename=Button(win4,text='RENAME A COLUMN',command=self.rena,padx=10,pady=10)
  rename.place(x=20,y=160)
  info=Button(win4,text='INFORMATION LOCATOR',command=self.infor,padx=10,pady=10)
  info.place(x=200,y=160)
  trunc=Button(win4,text='TRUNCATE TABLE',command=self.tru,padx=10,pady=10)
  trunc.place(x=20,y=210)
  insert=Button(win4,text='INSERT DATA INTO TABLES',command=self.instab,padx=10,pady=20)
  insert.place(x=20,y=280)
  drop=Button(win4,text='DROP A TABLE',command=self.drotab,padx=10,pady=10)
  drop.place(x=200,y=10)
  query=Button(win4,text='GIVE QUERIES MANUALLY',command=self.givque,padx=10,pady=10)
  query.place(x=200,y=60)
  delete=Button(win4,text='DELETE A ROW IN TABLE',command=self.de,padx=10,pady=10)
  delete.place(x=200,y=110)
 def al(self):
  win16=Tk()
  win16.title('ALTER A TABLE')
  win16.geometry('500x500')
  win16.configure(background='green')
  lb=Label(win16,text='ENTER THE TABLE NAME',bg='red')
  lb.place(x=10,y=10)
  self.ale=StringVar()
  self.ale1=Entry(win16,textvariable=self.ale)
  self.ale1.place(x=10,y=40)
 def de(self):
  win14=Tk()
  win14.title('DELETE TABLE')
  win14.geometry('350x350')
  win14.configure(background='green')
  lb=Label(win14,text='ENTER THE TABLE NAME',bg='red')
  lb.place(x=10,y=10)
  self.der=StringVar()
  self.dero=Entry(win14,textvariable=self.der)
  self.dero.place(x=10,y=45)
  lb1=Label(win14,text='ENTER THE COLUMN NAME',bg='red')
  lb1.place(x=10,y=75)
  self.der1=StringVar()
  self.der11=Entry(win14,textvariable=self.der1)
  self.der11.place(x=10,y=115)
  lb2=Label(win14,text='ENTER THE REFERENCE VALUE',bg='red')
  lb2.place(x=10,y=140)
  self.der2=StringVar()
  self.der22=Entry(win14,textvariable=self.der2)
  self.der22.place(x=10,y=180)  
  btn=Button(win14,text='DELETE ROW WITH THE VALUE',command=self.derow,padx=10,pady=10)
  btn.place(x=50,y=240)
 def derow(self):
  t=self.dero.get()
  w=self.der11.get()
  x=self.der22.get()
  print(t)
  print(w)
  print(x)
  tys='ni'
  ref=type(tys)
  if type(x)==ref:
    x="'"+x+"'"
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  sql="""delete from """+t+""" where """+w+"""="""+x
  print(sql)
  try:
   cursor.execute(sql)
   db.commit()
   tkMessageBox.showinfo('NOTIFICATION','ROW DELETED :)')
  except:
   db.rollback()
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
  db.close()
 def tru(self):
  win13=Tk()
  win13.title('TRUNCATE TABLE')
  win13.configure(background='green')
  win13.geometry('250x250')
  lb=Label(win13,text='ENTER THE TABLE NAME',bg='red')
  lb.place(x=10,y=10)
  self.tr=StringVar()
  self.tru=Entry(win13,textvariable=self.tr)
  self.tru.place(x=10,y=40)
  btn=Button(win13,text='TRUNCATE',command=self.trunc,padx=10,pady=10)
  btn.place(x=50,y=120)
 def trunc(self):
  x=self.tru.get()
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  sql="""truncate table """+x
  try:
   cursor.execute(sql)
   tkMessageBox.showinfo('NOTIFIACTION','TRUNCATED :)')
  except:
   db.rollback()
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
  db.close()
 def update(self):
  win12=Tk()
  win12.title('UPDATE VALUES IN THE TABLE')
  win12.geometry('650x400')
  win12.configure(background='green')
  lb=Label(win12,text='ENTER THE TABLE NAME:',bg='red')
  lb.place(x=10,y=10)
  self.upte=StringVar()
  self.upda=Entry(win12,textvariable=self.upte)
  self.upda.place(x=300,y=10)
  lb1=Label(win12,text='ENTER THE REFERENCE COLUMN NAME AND THE VALUE:',bg='red')
  lb1.place(x=10,y=70)
  self.upco1=StringVar()
  self.upcod1=Entry(win12,textvariable=self.upco1,width=25)
  self.upcod1.place(x=10,y=90)
  self.upco=StringVar()
  self.upcod=Entry(win12,textvariable=self.upco,width=25)
  self.upcod.place(x=300,y=90)
  lb2=Label(win12,text='ENTER THE COLUMN NAMES WITH SPACES THAT ARE TO BE UPDATED',bg='red')
  lb2.place(x=10,y=120)
  self.ra=StringVar()
  self.rar=Entry(win12,textvariable=self.ra,width=70)
  self.rar.place(x=10,y=170)
  lb3=Label(win12,text='ENTER THE UPDATED VALUES OF THE ABOVE COLUMNS WITH COMMAS',bg='red')
  lb3.place(x=10,y=230)
  self.ama=StringVar()
  self.amad=Entry(win12,textvariable=self.ama,width=70)
  self.amad.place(x=10,y=270)
  btn=Button(win12,text='UPDATE',command=self.upd,padx=30,pady=10)
  btn.place(x=100,y=330)
 def upd(self):
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  t=self.upda.get()
  w=self.upcod.get()
  if not w.isdigit():
    w="'"+w+"'"
  v=self.upcod1.get()
  print(w)
  print(t)
  x=self.rar.get()
  x=x.split()
  y=self.amad.get()
  y=y.split(',')
  s=""""""
  x1='ch'
  sql="""update """+t+""" set """
  for i in range(0,len(x)):
    if i==len(x)-1:
      if type(y[i])==type(x1):
        s=s+x[i]+"="+"'"+y[i]+"'"
      else:
        s=s+x[i]+"="+y[i]
    else:
      if type(y[i])==type(x1):
        s=s+x[i]+"="+"'"+y[i]+"'"+","
      else:
        s=s+x[i]+"="+y[i]+","
  sql=sql+s+" where "+v+"="+w
  print(sql)
  try:
   cursor.execute(sql)
   tkMessageBox.showinfo('NOTIFICATION','UPDATED')
  except:
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
  db.commit()
  db.close()
 def rena(self):
  win11=Tk()
  win11.title('RENAMING WIDGET')
  win11.geometry('315x315')
  win11.configure(background='green')
  lb2=Label(win11,text='ENTER THE TABLE NAME',bg='red')
  lb2.place(x=10,y=15)
  self.tne=StringVar()
  self.tnee=Entry(win11,textvariable=self.tne)
  self.tnee.place(x=10,y=50)
  lb=Label(win11,text='ENTER THE PREVIOUS NAME OF THE COLUMN',bg='red')
  lb.place(x=10,y=90)
  self.z=StringVar()
  self.n=Entry(win11,textvariable=self.z)
  self.n.place(x=10,y=135)
  lb1=Label(win11,text='ENTER THE NEW NAME FOR THE COLUMN',bg='red')
  lb1.place(x=10,y=175)
  self.z1=StringVar()
  self.ze1=Entry(win11,textvariable=self.z1)
  self.ze1.place(x=10,y=215)
  btn=Button(win11,text='RENAME',command=self.marc,padx=10,pady=10)
  btn.place(x=50,y=250)
 def marc(self):
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  t=self.tnee.get()
  sql1="""desc """+t
  try:
   cursor.execute(sql1)
  except:
   db.rollback()
   tkMessageBox.showinfo('ALERT','wrong table name')
  results=cursor.fetchall()
  x=self.n.get()
  y=self.ze1.get()
  for i in results:
    if i[0]==x:
      ma=i[1]
  print(ma)
  sql="""alter table """+t+""" change """+x+""" """+y+""" """+ma
  print(sql)
  try:
   cursor.execute(sql)
   tkMessageBox.showinfo('NOTIFICATION','COLUMN RENAMED :)')
  except:
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
  db.close()
 def infor(self):
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  sql="""SHOW TABLES"""
  cursor.execute(sql)
  results=cursor.fetchall()
  db.close()
  print(results)
  root=Tk()
  root.title('INFORMATION')
  root.geometry('300x500')
  scrollbar=Scrollbar(root)
  scrollbar.pack(side=RIGHT,fill=Y)
  mylist=Listbox(root,yscrollcommand=scrollbar.set)
  for i in range(len(results)):
    mylist.insert(END,results[i][0])
  mylist.pack(side=LEFT,fill=BOTH)
  scrollbar.config(command=mylist.yview)
 def givque(self):
  win8=Tk()
  win8.title('QUERY ENTRY WINDOW')
  win8.configure(background='green')
  win8.geometry('500x500')
  lb=Label(win8,text='ENTER THE QUERY',bg='red')
  lb.config(font=('Courier',25))
  lb.place(x=10,y=10)
  self.gaqe=Text(win8,width=50,height=20)
  self.gaqe.place(x=10,y=65)
  btngiv=Button(win8,text='EXECUTE THE COMMAND',command=self.givquexe,padx=10,pady=10)
  btngiv.place(x=10,y=400)
 def givquexe(self):
  sql=self.gaqe.get('0.0',END)
  print('command: '+sql)
  try:
   db=MySQLdb.connect('localhost','root','pbl123','new')
   cursor=db.cursor()
   cursor.execute(sql)
   db.commit()
   print('executed')
   tkMessageBox.showinfo('NOTIFICATION','EXECUTION SUCCESS')
  except:
   db.rollback()
   tkMessageBox.showinfo('ALERT','AN ERROR OCCURED')
  db.close()
 def instab(self):
  win7=Tk()
  win7.title('INSERT INTO TABLES')
  win7.configure(background='green')
  win7.geometry('500x500')
  lb=Label(win7,text='ENTER THE NAME OF THE TABLE',bg='red')
  lb.place(x=10,y=10)
  self.ins=StringVar()
  self.inst=Entry(win7,textvariable=self.ins)
  self.inst.place(x=10,y=40)
  lb1=Label(win7,text='ENTER THE DATA SEPERATED BY COMMA',bg='red')
  lb1.place(x=10,y=70) 
  self.tak=Text(win7,width=50,height=20)
  self.tak.place(x=10,y=100)
  btn=Button(win7,text='INSERT',command=self.instab1,padx=10,pady=10)
  btn.place(x=50,y=420)
 def instab1(self):
  x=self.inst.get()
  y=self.tak.get(0.0,END)
  print(x)
  print(y)
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  sql="""insert into """+x+""" values("""+y+""")"""
  try:
   cursor.execute(sql)
   db.commit()
   tkMessageBox.showinfo('NOTIFICATION','INSERTED :)')
  except:
   db.rollback()
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
  db.close()
 def drotab(self):
  win6=Tk()
  win6.title('DROP A COLUMN')
  win6.configure(background='green')
  win6.geometry('250x250')
  lb=Label(win6,text='ENTER THE NAME OF THE TABLE',bg='red')
  lb.place(x=10,y=10)
  self.DRO=StringVar()
  self.DROP=Entry(win6,textvariable=self.DRO)
  self.DROP.place(x=10,y=40)
  lb1=Label(win6,text='ENTER THE NAME OF THE COLUMN',bg='red')
  lb1.place(x=10,y=80)
  self.DROCOL=StringVar()
  self.DROPCOLNA=Entry(win6,textvariable=self.DROCOL)
  self.DROPCOLNA.place(x=10,y=120)
  btndrop=Button(win6,text='DROP TABLE',command=self.droptabl,padx=10,pady=10)
  btndrop.place(x=10,y=170)
  btndrop1=Button(win6,text='DROP COLUMN',command=self.droptabl1,padx=10,pady=10)
  btndrop1.place(x=120,y=170)
 def droptabl1(self):
  tabnam=self.DROP.get()
  colnam=self.DROPCOLNA.get()
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  sql="""alter table """+tabnam+""" drop column """+colnam+';'
  print(sql)
  try:
   cursor.execute(sql)
   db.close()
   tkMessageBox.showinfo('NOTIFICATION','COLUMN DROPPED')
  except:
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
 def droptabl(self):
  tabnam=self.DROP.get()
  print(tabnam)
  try:
   db=MySQLdb.connect('localhost','root','pbl123','new')
   cursor=db.cursor()
   sql="""DROP TABLE """+tabnam+""";"""
   print(sql)
   cursor.execute(sql)
   tkMessageBox.showinfo('NOTIFICATION','DROPPED SUCCESSFULLY')
   db.close()
  except:
   tkMessageBox.showinfo('ALERT','ERROR OCCURED')
 def createtable(self):
  win6=Tk()
  win6.title('CREATE A TABLE')
  win6.configure(background='green')
  win6.geometry('800x500')
  lb=Label(win6,text='ENTER THE NAME OF THE TABLE TO CREATE:',bg='yellow')
  lb.place(x=10,y=10)
  self.tn=StringVar()
  self.tabnam=Entry(win6,textvariable=self.tn)
  self.tabnam.place(x=350,y=10)
  lb2=Label(win6,text='ENTER THE COLUMN NAMES AND THEIR CORRESPONDING DATA TYPES IN THE GIVEN TWO DIFFERENT ENTRY BOXES',bg='blue') 
  lb1=Label(win6,text='NOTE:PLEASE GIVE THE SPACES BETWEEN THE COLUMN NAMES AND ALSO BETWEEN THE DATA TYPES',bg='red')
  lb3=Label(win6,text='THE DATA TYPES THAT YOU CAN TYPE ARE: \n  -> CHAR(number of charecters)\n -> INT(no. of numbers)',bg='blue') 
  lb4=Label(win6,text='EXAMPLES ARE: \n 1)CHAR(10)\n2)INT',bg='blue')
  lb5=Label(win6,text='ENTER THE COLUMN NAMES TO CREATE',bg='yellow')
  self.cn=StringVar()
  self.colnam=Entry(win6,textvariable=self.cn,width=85)
  self.colnam.place(x=10,y=250)
  lb6=Label(win6,text='ENTER THE CORRESPONDING DATATYPES FOR YOUR COLUMN NAMES',bg='yellow')
  lb6.place(x=10,y=300)
  self.dt=StringVar()
  self.dattyp=Entry(win6,textvariable=self.dt,width=85)
  self.dattyp.place(x=10,y=320)
  ctab=Button(win6,text='CREATE A TABLE',command=self.creatabl,padx=10,pady=10)
  ctab.place(x=250,y=360)
  lb5.place(x=10,y=230)
  lb4.place(x=300,y=150)
  lb2.place(x=10,y=50)
  lb1.place(x=10,y=100)
  lb3.place(x=10,y=150)
 def creatabl(self):
  nam=self.tabnam.get()
  colnames=self.colnam.get()
  da=self.dattyp.get()
  db=MySQLdb.connect('localhost','root','pbl123','new')
  cursor=db.cursor()
  coln=colnames.split()
  daty=da.split()
  print(coln)
  print(daty)
  s=''
  sql="""CREATE TABLE """+nam+"""("""
  for i in range(0,len(coln)):
    if i==(len(coln)-1):
      s=s+coln[i]+' '+daty[i]
    else:
      s=s+coln[i]+' '+daty[i]+','
  sql=sql+s+')'+';'
  print(sql)
  try:
   cursor.execute(sql)
   tkMessageBox.showinfo('NOTIFICATION','successfully created')
  except:
   tkMessageBox.showinfo('alert','ERROR OCCURED')
  db.close()
 def sp(self):
  r = sr.Recognizer()                                                                                   
  with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
  try:
    engine=pyttsx.init()
    x=r.recognize_google(audio)
    print(x)
    if x.lower()=='hi' or x.lower()=='hello' or x.lower()=='hello verma' or x.lower()=='hey there':
      engine.say('hello')
      engine.say('i am very glad to listen you')
      engine.runAndWait()
    elif x.lower()=='you are my best friend':
      engine.say('you too is my best friend')
    elif x.lower()=='who are you' or x.lower()=='what is your name':
      engine.say('my name is raja nithin')
    elif 'calendar' in x.lower():
      dict1={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
      y=time.ctime(time.time())
      month=dict1[(y[4:7]).lower()]
      year=int(y[20:24])
      cal=calendar.month(year,month)
      win2=Tk()
      win2.title('CALENDAR')
      win2.geometry('300x250')
      win2.configure(background='green')
      lb=Label(win2,text=cal)
      lb.pack()
    elif 'mail' in x.lower():
      self.sendmail()
    elif 'video download' in x.lower():
      win5=Tk()
      win5.title('VIDEO DOWNLOADER')
      win5.geometry('970x250')
      win5.configure(background='blue')
      urlla=Label(win5,text='ENTER THE URL TO DOWNLOAD')
      urlla.config(font=("Courier", 44))
      urlla.place(x=10,y=20)
      self.h=StringVar()
      self.you=Entry(win5,textvariable=self.h,width=100)
      self.you.place(x=10,y=100)
      btndown=Button(win5,text='DOWNLOAD',command=self.videodownl,padx=30,pady=20)
      btndown.place(x=460,y=150)
    elif ('download' in x.lower()) and ('image' in x.lower()):
      win3=Tk()
      win3.title('IMAGE DOWNLOADER')
      win3.geometry('350x200')
      win3.configure(background='green')
      l=Label(win3,text='ENTER THE URL')
      l.place(x=10,y=30)
      self.g=StringVar()
      self.entry=Entry(win3,textvariable=self.g)
      self.entry.place(x=175,y=30)
      downl=Button(win3,text='DOWNLOAD',command=self.downlo)
      downl.place(x=75,y=80)
    elif 'database controller' in x.lower():
      self.dbcontrol()
    elif 'time' in x.lower():
      y=time.ctime(time.time())
      print(y)
      h=int(y[10:13])
      m=int(y[14:16])
      sta='AM'
      if h>12:
        h=h-12
        sta='PM'
        engine1=pyttsx.init()
        engine.say('time is')
        engine1.runAndWait()
      win1=Tk()
      win1.title('TIME NOW')
      win1.geometry('350x150')
      win1.configure(background='blue')
      ti=str(h)+':'+str(m)+' '+sta
      lb=Label(win1,text=ti)
      lb.config(font=("Courier", 44))
      lb.pack()
    else:
      engine.say('could not understand your command')
      engine.runAndWait()
  except sr.UnknownValueError:
    print("Could not understand audio")
  except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
 def videodownl(self):
  url=self.you.get()
  self.you.delete(0,'end')
  print('url:'+url)
  if url=='':
    tkMessageBox.showinfo('ALERT','PLEASE ENTER URL')
  else:
    try:
     print('DOWNLOADING...')
     YouTube(url).streams.first().download()
     tkMessageBox.showinfo('NOTIFICATION','YOUR VIDEO DOWNLOADED SUCCESSFULLY')
    except:
     tkMessageBox.showinfo('SORRY','AN ERROR OCCURED')
     print('download failed or incorrect url')
 def downlo(self):
  print(self.g.get())
  img=str(self.entry.get())
  self.entry.delete(0,'end')
  name_img=img.split('/')
  img_name=name_img[len(name_img)-1]
  print('DOWNLOADING FILE NAME:'+img_name)
  u=urllib.URLopener()
  try:
   f=u.open(img)
   open(img_name,'w').write(f.read())
   print('sucessfully downloaded')
   tkMessageBox.showinfo('NOTICE','IMAGE DOWNLOADED')
  except:
   tkMessageBox.showinfo('SORRY','INVALID URL')
 def vo(self):
  tkMessageBox.showinfo('ASSISTANT EXPLORER','SAY SOMETHING')
  self.nithin()
  r = sr.Recognizer()                                                                                   
  with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
  try:
    x=r.recognize_google(audio)
    print(r.recognize_google(audio))
    #engine.say('ok')
    mixer.init()
    x=x.lower()
    try:
     mixer.music.load('/home/pbl/Desktop/python/'+x+'.mp3')
     mixer.music.play(5)
    except:
     engine.say('wrong name')
  except sr.UnknownValueError:
    engine.say('sorry')
    engine.say('i could not recognise your input')
    engine.say('please try again')
    print("Could not understand audio")
  except sr.RequestError as e:
    engine.say('sorry')
    engine.say('please check your internet connection')
    print("Could not request results; {0}".format(e))
 def nithin(self):
  engine1=pyttsx.init()
  engine1.say('say')
  engine1.say('something')
  engine1.runAndWait()
 def voice(self):
  tkMessageBox.showinfo('ASSISTANT EXPLORER','SAY SOMETHING')
  self.nithin()
  r = sr.Recognizer()                                                                                   
  with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   
  try:
    x=r.recognize_google(audio)
    print(r.recognize_google(audio))
    y="https://www.google.com/search?q="
    y=y+x
    controller=webbrowser.get()
    controller.open(y)
    engine.say('ok')
  except sr.UnknownValueError:
    engine.say('sorry')
    engine.say('i was unable to recognise your input')
    engine.say('please try again')
    print("Could not understand audio")
  except sr.RequestError as e:
    engine.say('sorry')
    engine.say('please check out your internet connection')
    print("Could not request results; {0}".format(e))
 def map(self):
  x='https://www.google.co.in/maps/place/'
  s=self.b.get()
  if s=='':
    tkMessageBox.showinfo('BROWSER','PLEASE ENTER SOMETHING')
  else:
    self.b.set('')
    x=x+s
    controller=webbrowser.get()
    controller.open(x)
 def img(self):
  x='https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1366&bih=662&ei=BOYNWq65PMbcvgTAjImYCw&q='
  s=self.b.get()
  if s=='':
    tkMessageBox.showinfo('BROWSER','PLEASE ENTER SOMETHING')
  else:
    self.b.set('')
    x=x+s
    controller=webbrowser.get()
    controller.open(x)
 def search(self):
  x=self.b.get()
  if x=='':
    tkMessageBox.showinfo('BROWSER','PLEASE ENTER SOMETHING')
  else:
    self.b.set('')
    y="https://www.google.com/search?q="
    y=y+x
    controller=webbrowser.get()
    controller.open(y)
  print('ok') 
 def rewind(self):
  mixer.music.rewind()
 def unpause(self):
  mixer.music.unpause()
 def pause(self):
  mixer.music.pause()
 def stop(self):
  mixer.music.stop()
 def song(self):
     print(self.a.get())
     c=self.a.get()
     b='/home/pbl/Desktop/python/'+str(self.a.get())+'.mp3'
     print(b)
     self.a.set('')
     try:
      self.ni=1
      mixer.init()
      mixer.music.load(b)
      mixer.music.play(10) 
      print('completed')
     except:
      self.ni=0
     finally: 
       if c=='':
         tkMessageBox.showinfo('NOTIFICATION','ENTER THE NAME')
       elif self.ni==0:
         tkMessageBox.showinfo('NOTIFICATION','WRONG NAME')
main()



from Tkinter import *
import time
import pyttsx
from pygame import mixer
import random
import tkMessageBox
class App():
    def __init__(self):
     self.dic={1:'SUBBA REDDY',2:'RAVITEJA',3:'GEETHA PRIYANKA',4:'DEEPTHI CHANDRIKA',5:'USHA RANI',6:'KRISHNA REDDY',7:'BHAVANI AKSHITHA',8:'MADHU PRIYA',9:'VISHWAJA',10:'RAHUL GOEL',11:'S.MOUNIKA',12:'JAI HANUMAN',13:'TH.RUKMANI',14:'SEKHAR SAMAL',15:'Y. DIVYA',16:'ATIYA TANWEER',17:'UMESH THAPA',18:'SWETHA PRIYA',19:'B.SAI SPANDANA',20:'KRISHNA VINEEL',21:'KGV LAKSHMI BUDHA',22:'G. TEJASRI',23:'N. SIRISHA',24:'O. TEJASWI',25:'M. PREMA',26:'M.PRAVALLIKA',27:'AYUSH LAWNIA',28:'N.PUJITHA',29:'CH.CHARISHMA',30:'TV.SOWMYA SRI',31:'K.H.PRIYA DARSINI',32:'S.VEMANI',33:'N.ARUNA SRI',34:'K.SAI SRAVYA',35:'D.SAI SNIGDHA',36:'P.VAISHNAVI',37:'T.AKHIL KRISHNA',38:'P.DEVI PRAVALLIKA',39:'G.SAI SANJANA',40:'B.SRI HARSHA',41:'K.TABITHA',42:'CH.SRI LALITHA POORNIMA',43:'K.NAVEENA REDDY',44:'SAI HARINI',45:'VENKATA ASWINI KUMAR',46:'D.VIJAYA SRI',47:'FAIZA YASEEN',48:'SUDHA RANI',49:'CH.LAKSHMI SRAVANI',50:'D.LIKITHA',51:'N.PHANI DURGA',52:'CH.SAI SAMEERA',53:'R.CHARITHA',54:'G.NIKHIL KRISHNA',55:'M.VENKATESH',
56:'K.DHANA KRUPA',57:'ADITYA SAI SWAROOP',58:'B.MAHESH',59:'N.SANDHYA RANI',60:'Y.KRISHNAVENI',61:'SRI LALITHA AISHWARYA',62:'B.REETHU SANKARI',63:'D.MEENA AMRUTHA',64:'P.HARSITHA',65:'A.CHARISHMA',66:'B.NAVEENA',67:'A.SAI RAHOOL',68:'K.DIVYA',69:'J.VIJAYA SAI',70:'S.SREE LAKSHMI',71:'K.ANUSHA',72:'A.DIVYA SREE',73:'K.SAI CHANDRA REDDY',74:'A.MORIYA SURTHNA',75:'A.MAHATHI',76:'T.NITHEJ',77:'S.SAHITHYA',78:'V.KAVYA KRISHNA',79:'K.CHARITHRA'}
     print self.dic
     self.tag={1:'OKE OKKADU',2:'ANDALA RAMUDU',3:'GOPI GOPIKA GODAVARI ',4:'NAGAVALLI',5:'GANGOTRI',6:'BOBBILI SIMHAM',7:'BAMA MATA BANGARAMATA',8:'PANDEM KODI',9:'MIRAPAKAY',10:'JAI SIMHA',11:'PAISA VASOOL',12:'STATE ROWDY BT ROWDY',13:'BARBIE GIRL',14:'JULAYII',15:'MAHANATI',16:'DARLING',17:'CHILL BULL PANDEY',18:'MIRCHI LANTI AMMAI',19:'BANGARU KODI PETTA',20:'DESAMUDURU',21:'MADHURA MEENAKSHI',22:'MEGHAMALA',23:'SUBBA LACHMIII',24:'CHANDRAMUKHI',25:'CHELIYA',26:'VAYARI BHAMAAA',27:'MAAJNUU',28:'BAPUGARII BOMMA',29:'MISAMMA',30:'VALLUJADAA AHAA VALLUJADAA',31:'TELUGU AMMAYII',32:'GOKULAMLO SITAA',33:'SOUNDARYA LAHARI',34:'PUTTADHI BOMMA',35:'ANDHALA RAKSHASI',36:'ALLARI BULLAMA',37:'PRINCE CHARMING',38:'CHIKNI CHAMELI',39:'CHILAKALURI CHINTAMANI',40:'MR.INNOCENT',41:'KUNDANAPU BOMMA',42:'NIGHTINGALE',43:'JABILAMMA',44:'PANDA',45:'MR.PHOTOGRAPHER',46:'HAHA... HASINI',47:'MEHA BOOBA',48:'NAYAKII',49:'CHINNADANA NIKOSAM',50:'LOVELY',51:'HONEYYY',52:'ATHILOKA SUNDARI',53:'THAT IS MAHALAKSHMI',54:'AAGADU',
55:'ARJUN REDDY',56:'ANDHRA PORI',57:'MANCHI LAKSHANALU UNNA ABBAI(MLA)',58:'STUDENT OF THE YEAR',59:'RAMULAMMA',60:'SATYABAMA',61:'LEADER OF THE FLEET',62:'SURYAKANTHAM',63:'CHOTA DON',64:'TEDDY BEAR',65:'PANCHAKSHARI',66:'CHANDAMAMA',67:'GOVINDUDU ANDHARI VADELE',68:'ANGEL',69:'DUVVADA JAGANADHAM(DJ)',70:'RAMALACHMIII',71:'GURU',72:'KOKILA',73:'AGNATHAVYASII',74:'KANCHUU',75:'BHAGAMATHI',76:'',77:'NENEY RANI NENEY MANTRI',78:'JESSIE',79:'BANGARU KODI PETTA'}
     print len(self.dic)
     self.li=[]
     self.li=random.sample(range(1,80),79)
     print self.li
     self.task=['','LOLLYPOP-DIALOGUE','PICK THINGS','SD','COLECT COINS','FIND THE FILM NAME','PRODUCT SELLING','TUG OF WAR','TIGER RICE PREPARATION','IMITATE ANYONE','GUESS THE THINGS',"EMOJI'S",'ENGLISH TO TELUGU','TELUGU TO ENGLISH','CAT BISCUIT','BAHUBALI SKIT','Z TO A','SIGNATURE MOVEMENTS','SPELLINGS','DIALOGUE','BLACK TICKETS','5 PHOTOSHOOT POSES','EMOVIE NAME WITH HEADSET','PIN ON TAIL','EAT BISCUIT','CONTROVERSY','AMBA TABLE','PLAY CRICKET','TOURIST GUIDE','PICTOGRAPHY','PRANK CALL','THERMOCOL BALLS THROUGH STRAW','INNER VOICE','BIKE FEELINGS','SONG DEDICATION','SCHOOL CHILDREN','PLASTIC CUPS','BALLOONS BLAST','ANIMAL POSTURES','MOVIE NAME''LOLLYPOP-DIALOGUE','PICK THINGS','SD','COLECT COINS','FIND THE FILM NAME','PRODUCT SELLING','TUG OF WAR','TIGER RICE PREPARATION','IMITATE ANYONE','GUESS THE THINGS',"EMOJI'S",'ENGLISH TO TELUGU','TELUGU TO ENGLISH','CAT BISCUIT','BAHUBALI SKIT','Z TO A','SIGNATURE MOVEMENTS','SPELLINGS','DIALOGUE','BLACK TICKETS','5 PHOTOSHOOT POSES','EMOVIE NAME WITH HEADSET','PIN ON TAIL','EAT BISCUIT','CONTROVERSY','AMBA TABLE','PLAY CRICKET','TOURIST GUIDE','PICTOGRAPHY','PRANK CALL','THERMOCOL BALLS THROUGH STRAW','INNER VOICE','BIKE FEELINGS','SONG DEDICATION','SCHOOL CHILDREN','PLASTIC CUPS','BALLOONS BLAST','ANIMAL POSTURES','MOVIE NAME','TOURIST GUIDE','PICTOGRAPHY','PICK THINGS','']
     print len(self.task)
     self.x=0
     self.win=Tk()
     self.win.title('MAIN')
     self.win.geometry('1500x1500')
     self.win.config(background='green')
     canvas=Canvas(self.win)
     canvas.pack(expand=True, fill=BOTH)
     image1=PhotoImage(file="bk.png")
     canvas.img=image1
     canvas.create_image(0, 0, anchor=NW, image=image1)
     canvas.create_window(20,20, anchor=NW)
     img1=PhotoImage(file='back.png')
     btn=Button(self.win,image=img1,command=self.nit,width=600,height=400)
     btn.place(x=400,y=160)
     self.win.mainloop()
    def nit(self):
        self.root = Tk()
        self.root.geometry('1500x1000')
        self.root.config(background='black')
        self.label = Label(self.root,text="",bg='black')
        self.label.pack()
        self.now=0
        self.count=0
        self.update_clock()
    def mus(self):
         try:
          mixer.init()
          x='/home/pbl/Desktop/farewell/'+self.x1.upper()+'.mp3'
          print x
          print 'hello'
          mixer.music.load(x)
          mixer.music.play(1)
         except:
          print 'no song'  
    def newwindow(self):
        #try:
         self.ne=Toplevel()
         self.ne.title('new window')
         self.ne.geometry('1500x1000')
         self.ne.config(background='black')
         self.c=Canvas(self.ne)
         self.c.pack(expand=True, fill=BOTH)
         self.x1=self.dic[self.li[self.x]]
         pic=self.x1+'.png'
         image2=PhotoImage(file=pic)
         image1=PhotoImage(file='bk.png')
         self.c.img=image1
         self.c.create_image(0, 0, anchor=NW, image=image1)
         self.c.create_window(20,20, anchor=NW)
         self.x2=self.tag[self.li[self.x]]
         self.y1=self.task[self.x+1]
         self.x+=1
         print self.x1+'  -  '+self.y1
         print self.x2
         if self.x2=='':
          pass
         else:
          self.x2='('+self.x2+')'
         #l=Label(c,text=self.x1,font=("Courier", 100))
         #l.place(x=10,y=600)
         #rn=self.x1.lower()+'t.png'
         #print rn
         #rajput=PhotoImage(file=rn)
         l=Label(self.c,image=image2)
         l.place(x=10,y=10)
         l1=Button(self.c,text=self.x2,font=("Courier", 30),bg='light blue')
         l1.place(x=600,y=200)
         btn=Button(self.c,text=self.x1,font=("Courier", 50),command=self.displ)
         btn.place(x=10,y=600)
         btn1=Button(self.c,text='stop',command=self.stop)
         btn1.place(x=1000,y=600)
         btn2=Button(self.c,text='close',command=self.close)
         btn2.place(x=1200,y=600)
         self.image2=image2
         #c.rajput=rajput
         engine=pyttsx.init()
         rate = engine.getProperty('rate')
         engine.setProperty('rate', rate-30)
         raj='welcome to '+self.x1.lower()
         print raj
         engine.say(raj) 
         print 'ashish'
         engine.runAndWait()
         self.mus()
         
        #except:
         #tkMessageBox.showinfo('NOTE','ALL MEMBERS COMPLETED')
    def close(self):
         mixer.music.stop()
         self.ne.destroy()
    def stop(self):
         mixer.music.stop()
    def displ(self):
        self.counter=0
        self.dis=Toplevel()
        self.dis.geometry('1500x1000')
        canvas=Canvas(self.dis)
        canvas.pack(expand=True, fill=BOTH)
        #self.canvas.create_image(0, 0, anchor=NW)
        image1=PhotoImage(file="bk.png")
        # keep a link to the image to stop the image being garbage collected
        canvas.img=image1
        canvas.create_image(0, 0, anchor=NW, image=image1)
        canvas.create_window(20,20, anchor=NW)
        btn=Button(canvas,text='close',command=self.closeall)
        btn.place(x=1200,y=600)
       # im=PhotoImage(file='back.png')
       # lab=Label(canvas,image=im,font=("Courier", 20))
        #lab.place(x=1000,y=10)
        self.la=Label(canvas,text='',font=("Courier", 50))
        self.la.place(x=10,y=500)
        #lab1=Label(canvas,text=self.y1,font=("Courier", 40))
        #lab1.place(x=100,y=500)
        #canvas.im=im
        self.taskr()
    def closeall(self):
        self.ne.destroy()
        self.dis.destroy()
    def taskr(self):
        self.counter+=1
        print self.counter
        if self.counter==79:
         self.la.configure(text=self.y1,font=("Courier", 50))
         engine=pyttsx.init()
         rate = engine.getProperty('rate')
         engine.setProperty('rate', rate-60)
         engine.say('your')
         engine.say('task is '+self.y1.lower())
         engine.runAndWait()
         return
        else:
         self.la.configure(text=self.task[self.counter])
         self.root.after(100,self.taskr)
    def update_clock(self):
        self.now += 1
        if self.now==10:
         print 'yes'
         self.now=0
         self.count+=1
         if self.count==1:
          self.root.destroy()
          self.newwindow()
        else:
         self.label.configure(text=self.now,fg='red',font=("Courier", 400))
         self.root.after(100, self.update_clock)

app=App()

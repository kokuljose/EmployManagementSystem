import Tkinter
import tkMessageBox
home=Tkinter.Tk("hello")
from Tkinter import *
home.geometry('1300x900')
home.title("EMPLOYEE MANAGEMENT SYSTEM")
var = IntVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()
fr=open("tx.txt","r")
global spfile
file1=fr.read()
spfile=file1.split()
na=StringVar()
addr=StringVar()
post=StringVar()
bp=StringVar()
mail=StringVar()
phone=StringVar()
degn=StringVar()
id=""
slno=""
repl=StringVar()
fac=StringVar()
fr.close()
l=len(spfile)
def cal():
	global fac
	
	
	filewin = Toplevel(home)
	filewin.title('SALARY CALCULATOR')
	filewin.geometry('300x200+200+125')
	d1=Label(filewin,text="Factor :",font=24).place(x=40,y=50)
	e1=Entry(filewin,textvariable=fac).place(x=150,y=53)
	okbut = Tkinter.Button(filewin, text="                    CALCULATE                      ",command=calc and filewin.quit).place(x=50,y=100)
def dispsal():
	a=""
	fr=open("sal.txt","r")
	file12=fr.read()
	sfile=file12.split()
	ln=len(sfile)
	for i in range (0,ln,2):
		
		a=a+str(sfile[i:i+2])+"\t"
		a=a+"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n"
	tkMessageBox.showinfo("EMPLOYEE SALARY DETAILS",a)	
	


	
def calc():
	global fac
	tem=""
	f=fac.get()
	for i in range (11,l,9):
		
		tem=tem+spfile[i]+"\t"+str(int(spfile[i+3])*int(f))+"\n"
	
	fw=open("sal.txt","w")
	fw.write(tem)
	fw.close()
def addemp():
	global id
	global slno
	global na
	global addr
	global post
	global bp
	global mail
	global phone
	global degn
	a=Toplevel(home)
	a.title("ADD NEW EMPLOYEE")
	a.geometry('550x550+200+125')
	slno=str(len(spfile)/9)
	id=str(int(slno)+100)
	sl1="Slno   :   "+str(slno)
	id1="ID   :   "+str(id)
	de1=Label(a,text=sl1,font=24).place(x=40,y=50)
	de1=Label(a,text=id1,font=24).place(x=40,y=100)
	de1=Label(a,text="Name :",font=24).place(x=40,y=150)
	en1=Entry(a,textvariable=na).place(x=150,y=153)
	de2=Label(a,text="Address :",font=24).place(x=40,y=203)
	en2=Entry(a,textvariable=addr).place(x=150,y=206)
	de6=Label(a,text="Post :",font=24).place(x=40,y=256)
	en6=Entry(a,textvariable=post).place(x=150,y=259)
	de7=Label(a,text="Basic Pay :",font=24).place(x=40,y=310)
	en7=Entry(a,textvariable=bp).place(x=150,y=313)
	de10=Label(a,text="Phone :",font=24).place(x=40,y=360)
	en10=Entry(a,textvariable=phone).place(x=150,y=363)
	de3=Label(a,text="E-mail :",font=24).place(x=40,y=413)
	en3=Entry(a,textvariable=mail).place(x=150,y=416)
	de4=Label(a,text="Designation :",font=24).place(x=40,y=456)
	en4=Entry(a,textvariable=degn).place(x=150,y=459)
	
	but1=Button(a,text="          SAVE THE EMPLOYEE DETAILS        ",font=40,bg="green",command=tofile).place(x=150,y=509)
def tofile():
	global id
	global slno
	global na
	global addr
	global post
	global bp
	global mail
	global phone
	global degn
	r0=slno
	r1=id
	r2=na.get()
	r3=addr.get()
	r4=post.get()
	r5=bp.get()
	r6=phone.get()
	r7=mail.get()
	r8=degn.get()
	filr=open("tx.txt",'r')
	
	file1=filr.read()
	
	filw=open("tx.txt",'w')
	file2=r0+"\t"+r1+"\t"+r2+"\t"+r3+"\t"+r4+"\t"+r5+"\t"+r6+"\t"+r7+"\t"+r8
	file1=file1+file2
	
	filw.write(file1)
	filr.close()
	filw.close()
def selected():
	filewin = Toplevel(home)
	filewin.title('LIST OF EMPLOYEES')
	filewin.geometry('900x500+200+125')
	for i in range (11,l,9):
		
		R1 = Radiobutton(filewin, text=spfile[i], variable=var, value=i,command=dis)
		R1.pack( anchor = W )
def delete():
	filedel = Toplevel(home)
	filedel.title('LIST OF EMPLOYEES')
	filedel.geometry('950x550+100+50')
	

	for i in range (11,l,9):
		R2 = Radiobutton(filedel, text=spfile[i], variable=var1, value=i )
		R2.pack()
	okbut = Tkinter.Button(filedel, text="               OK,REMOVE THE EMPLOY TO TRASH!!!                  ",command=dele and filedel.quit)
	okbut.pack()

def dele():
	
	c=int(var1.get())

	fr=open("tx.txt","r")

	file1=fr.read()
	spfile=file1.split()
	l=len(spfile)
	temp=""
	for i in range(l):
		if(i<(c-2)):
			temp=temp+spfile[i]+"\t"
			if((i+1)%9==0):
				temp=temp+"\n"
		elif(i>(c+6)):
			temp=temp+spfile[i]+"\t"
			if((i+1)%9==0):
				temp=temp+"\n"
		#elif(i==c):
			temp=temp+"\n"
		else:
			continue
	
	fr.close()
	fw=open("tx.txt","w")		
	fw.write(temp)
	
	
	spfile=file1.split()
	fr.close()
	fw.close()
				
def dis():
	te=""
	j=2
	c=int(var.get())
	for i in range(c,c+7):
		te=te+spfile[j]+" :"+spfile[i]+"\n"
		j=j+1
	tkMessageBox.showinfo("EMPLOYEE DETAILS",te)	
	
def updat():
	filewin = Toplevel(home)
	filewin.title('LIST OF EMPLOYEES')
	filewin.geometry('900x500+200+125')
	for i in range (11,l,9):
		
		R1 = Radiobutton(filewin, text=spfile[i], variable=var3, value=i,command=upd)
		R1.pack( anchor = W )
def upd():
	filewin = Toplevel(home)
	filewin.title('LIST OF DETAILS')
	filewin.geometry('900x500+200+125')
	c=int(var3.get())
	for i in range (c,c+9):
		
		R1 = Radiobutton(filewin, text=spfile[i], variable=var2, value=i,command=up)
		R1.pack( anchor = W )
def up():
	global repl
	filewin = Toplevel(home)
	filewin.title('UPDATE')
	filewin.geometry('500x250+200+125')	
	d1=Label(filewin,text="Replace By :",font=24).place(x=40,y=50)
	e1=Entry(filewin,textvariable=repl).place(x=150,y=53)
	okbut = Tkinter.Button(filewin, text="                    UPDATE                      ",command=update).place(x=50,y=100)
def update():
	global repl
	filewin = Toplevel(home)
	filewin.title('UPDATING..')
	filewin.geometry('500x250+200+125')
	fr=open("tx.txt","r")

	file1=fr.read()
	spfile=file1.split()
	l=len(spfile)
	c=int(var3.get())
	d=int(var2.get())
	g=(c*9)+d
	replac=repl.get()
	temp=""

	
	for i in range (l):
		if(i<d):
			temp=temp+spfile[i]+"\t"
			if((i+1)%9==0):
				temp=temp+"\n"
		elif(i==d):
			temp=temp+repl.get()+"\t"
			if((i+1)%9==0):
				temp=temp+"\n"
		elif(i>d):
			temp=temp+spfile[i]+"\t"
			if((i+1)%9==0):
				temp=temp+"\n"	
		
	fr.close()
	fw=open("tx.txt","w")		
	fw.write(temp)
	
	
	spfile=file1.split()
	fr.close()
	fw.close()
	okbut = Tkinter.Button(filewin, text="                    UPDATE AND QUIT                     ",command=filewin.quit).place(x=50,y=50)
def all():
	a=""
	fr=open("tx.txt","r")
	file1=fr.read()
	spfile=file1.split()
	l=len(spfile)
	for i in range (0,l,9):
		#for j in range (i,i+10):
		a=a+str(spfile[i:i+9])+"\t"
		a=a+"---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"+"\n"
	tkMessageBox.showinfo("TOTAL EMPLOYEE DETAILS",a)	
	
def donothing():
	filewin = Toplevel(home)
	button = Button(filewin, text="Do nothing button")
	button.pack()

menubar= Menu(home)
addrmvmenu = Menu(menubar, tearoff=0)
addrmvmenu.add_command(label="Add Employ", command=addemp)
addrmvmenu.add_command(label="Remove Employ", command=delete)
menubar.add_cascade(label="Add/Remove Employ", menu=addrmvmenu)



dispmenu = Menu(menubar, tearoff=0)
dispmenu.add_command(label="All", command=all)
dispmenu.add_command(label="Selected",command=selected)

menubar.add_cascade(label="Display Details", menu=dispmenu)

calmenu=Menu(menubar,tearoff=0)
calmenu.add_command(label="Calculate The Salary",command=cal)
calmenu.add_command(label="Display The Salary",command=dispsal)
menubar.add_cascade(label="Salary",menu=calmenu)


updatemenu = Menu(menubar, tearoff=0)

updatemenu.add_command(label="Personal Details", command=updat)
menubar.add_cascade(label="Update Details", menu=updatemenu)


exitmenu= Menu(menubar,tearoff=0)
exitmenu.add_command(label="Exit", command=home.quit)
menubar.add_cascade(label="Exit", menu=exitmenu, command=home.quit)

home.config(menu=menubar)







home.mainloop()
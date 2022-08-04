from tkinter import *
import tkinter.messagebox as box
L1=[]
L2=[]
    
def loccheck():
    print(entry4.get())
    entryvalue=entry4.get()
    f=open("test2.txt","r")
    while f:
        uni=f.readline()
#        uni=uni.strip()
        if not uni:
            break
        l=uni.split(',')
        uniloc=l[1].strip().lower()
        entryvalue=entryvalue.lower()
        if uniloc==entryvalue:
            L1.append(l)
    f.close()

def coursecheck():
    entryvalue=entry2.get().upper()
   # entry2.delete(0,END)
    #entry2.insert(0,END)
    print(entry2.get)
    f=open("test2.txt","r")
    while f:
        uni=f.readline()
   #     uni=uni.strip()
        if not uni:
            break
        l=uni.split(',')
        courses=l[3].split('-')
        if entryvalue in courses:
            L2.append(l)
#            print(l)
    f.close()

def mainf():
    loccheck()
    coursecheck()
    top = Toplevel(bg='Cyan')
    top.geometry("750x400") 
    top.title("toplevel")
    l3=Label(top,text="\nHello "+entry1.get()+"\n\nThe colleges as per your choice are: \n ",font=("Arial",15),bg="Cyan")
    l3.pack()
    for l in L1:
        if l in L2:
            l2 = Label(top, text = "  ".join(l),font=("Arial",10),bg='Yellow')
            l2.pack()
    
    

window = Tk()
window.title('Course Finder')

frame = Frame(window)
lab1=Label(window,text="WELCOME TO FINDMYUNI",font=("Times New Roman",20),bg="Cyan")
lab1.pack(padx=15,pady=20)
Label1 = Label(window,text = 'Name:',font=("Arial",15))
Label1.pack(padx=15,pady= 5)

entry1 = Entry(window,bd =5)
entry1.pack(padx=15, pady=5)



Label2 = Label(window,text = 'Courses Interested:  ',font=("Arial",15))
Label2.pack(padx = 15,pady=6)

entry2 = Entry(window, bd=5)
entry2.pack(padx = 15,pady=7)


Label4 = Label(window,text = 'Interested location: ',font=("Arial",15))
Label4.pack(padx = 15,pady=6)

entry4 = Entry(window, bd=5)
entry4.pack(padx = 15,pady=7)




btn = Button(frame, text = 'Proceed',font=("Arial",15),command = mainf)


btn.pack(padx =5)
frame.pack(padx=100,pady = 19)

    
window.mainloop()

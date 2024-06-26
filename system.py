from functools import partial
import unittest
import numpy as np
import mysql.connector
from datetime import date, timedelta
from tkinter import *
from PIL import ImageTk , Image , ImageFilter
from tkinter import ttk
from ttkthemes import ThemedTk, ThemedStyle


connection = mysql.connector.connect(host='127.0.0.1', database='db2',
                                         user='newuser',
                                         password='Test@123')

class work:

    def __init__(self,id,name,nofworkers,requirement,priority):
        self.id=id
        self.name=name
        self.status='not started'
        self.nofworkers=nofworkers
        self.requirement=requirement
        self.priority=priority
        self.start_date
    
    def work_status(self,duration):
        self.status='completed'
        self.duration=duration

def addwork(win):
    sub=Toplevel(win)
    sub.geometry("1300x720")
    s=ThemedStyle()
    s.set_theme('equilux')
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    frame=Frame(sub,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")
    
    label=Label(frame,text="Enter the details of the work",background="#44d7eb")
    label.grid(row=0,column=0,columnspan=2)
    label1=Label(frame,text="Enter the id of the work: ",background="#44d7eb")
    label1.grid(row=1,column=0)
    id=StringVar()
    e1=Entry(frame,textvariable=id,width=50)
    e1.grid(row=1,column=1)
    label2=Label(frame,text="Enter the name of the work: ",background="#44d7eb")
    label2.grid(row=2,column=0)
    name=StringVar()
    e2=Entry(frame,textvariable=name,width=50)
    e2.grid(row=2,column=1)
    label3=Label(frame,text="Enter the number of workers required: ",background="#44d7eb")
    label3.grid(row=3,column=0)
    nofworkers=StringVar()
    e3=Entry(frame,textvariable=nofworkers,width=50)
    e3.grid(row=3,column=1)
    # label4=Label(sub,text="Enter the start date: ")
    # label4.grid(row=4,column=0)
    # start_date=StringVar()
    # e4=Entry(sub,textvariable=start_date,width=50)
    # e4.grid(row=4,column=1)
    label5=Label(frame,text='Enter the no. of types of roles required: ',background="#44d7eb")
    label5.grid(row=5,column=0)
    no_of_roles=StringVar()
    e5=Entry(frame,textvariable=no_of_roles,width=50)
    e5.grid(row=5,column=1)
  

    def next_3():
        print(no_of_roles.get())
        worker_role=[0 for row in range(int(no_of_roles.get()))]
        worker_req=[[0 for col in range(3)] for row in range(int(no_of_roles.get()))]
        print(worker_req)
        for i in range(int(no_of_roles.get())):
            var=IntVar()
            sl=Label(frame,text= i+1,background="#44d7eb")
            sl.grid(row=6+i*7,column=0)
            w1=Label(frame,text='Enter the role: ',background="#44d7eb")
            w1.grid(row=6+i*7,column=1)
            worker_role[i]=StringVar()
            ew=Entry(frame,textvariable=worker_role[i],width=50)
            ew.grid(row=6+i*7,column=2)

            def next_1():
                cursor=connection.cursor()
                insert_allotted="""INSERT INTO allotted_workers (id, role, beginner, intermediate, expert,total) VALUES (%s, %s, 0, 0, 0,0)"""
                cursor.execute(insert_allotted, (id.get(),worker_role[i].get()))
                connection.commit()
                print(cursor)
                cursor.close()

                l1=Label(frame,text='Enter required no. of Beginner level workers: ',background="#44d7eb")
                l1.grid(row=7+i*7,column=1)
                worker_req[i][0]=IntVar()
                wr1=Entry(frame,textvariable=worker_req[i][0],width=50)
                wr1.grid(row=7+i*7,column=2)
                l2=Label(frame,text='Enter required no. of Intermediate level workers: ',background="#44d7eb")
                l2.grid(row=8+i*7,column=1)
                worker_req[i][1]=IntVar()
                wr2=Entry(frame,textvariable=worker_req[i][1],width=50)
                wr2.grid(row=8+i*7,column=2)
                l3=Label(frame,text='Enter required no. of Expert level workers: ',background="#44d7eb")
                l3.grid(row=9+i*7,column=1)
                worker_req[i][2]=IntVar()
                wr3=Entry(frame,textvariable=worker_req[i][2],width=50)
                wr3.grid(row=9+i*7,column=2)

                def next_2():
                   
                    insert_record_stmt = """INSERT INTO work_req (id, role, beginner, intermediate, expert) VALUES (%s, %s, %s, %s, %s)"""
                    record_to_insert = (id.get(),worker_role[i].get(),str(worker_req[i][0].get()),str(worker_req[i][1].get()),str(worker_req[i][2].get()))
                    cursor=connection.cursor()
                    cursor.execute(insert_record_stmt, record_to_insert)
                    connection.commit()
                    m=Label(frame,text="Inserted",background="#44d7eb")
                    m.grid(row=11+i*7,column=2)
                    print(cursor)
                    cursor.close()
                    
                    

                next2=Button(frame,text="Next",command=next_2,activebackground="#44d7eb",bg='white')
                next2.grid(row=10+i*7,column=2)
                
                
                


            next1=Button(frame,text="Next",command=next_1,activebackground="#44d7eb",bg='white')
            next1.grid(row=6+i*7,column=3)
            # print(worker_role)
            # print(worker_req[1][0])

            done=Button(frame,text="Done",command=lambda: var.set(1),activebackground="#44d7eb",bg='white')
            done.grid(row=12+i*7,column=2)
            done.wait_variable(var)


        label6=Label(frame,text='Enter the priority: ',background="#44d7eb")
        label6.grid(row=6+int(no_of_roles.get())*7,column=0)
        priority=StringVar()
        e6=Entry(frame,textvariable=priority,width=50)
        e6.grid(row=6+int(no_of_roles.get())*7,column=1)
        

        def process():
            #print(cursor)
            cursor=connection.cursor()
            dur=0
            def_status='not started'
            

            sql = """INSERT INTO works(work_id, work_name, no_of_workers, priority, duration, work_status) VALUES (%s, %s, %s, %s, %s,%s)"""
            #rec=(name, 23, '2023-09-09', 'Mhh', 2000,70)
            rec= (id.get(),name.get(),nofworkers.get(),priority.get(), dur, def_status)


            # sql= """Delete from working where work_name='Jacc'"""  ('Jacc', 23, '2023-09-09', 'Mhh', 2000,70)

            try:
                cursor.execute(sql,rec)
                print("done execution")
                connection.commit()

            except:
                connection.rollback()
                print("error executing")

            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()
            msg=Label(frame,text="Work added successfully",background="#44d7eb")
            msg.grid(row=8+int(no_of_roles.get())*7,column=0,columnspan=2)


        ok=Button(frame,text="OK",command=process,activebackground="#44d7eb",bg='white')
        ok.grid(row=7+int(no_of_roles.get())*7,column=1)

        

        exit=Button(frame,text="Exit",command=win.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=8+int(no_of_roles.get())*7,column=1)


    next3=Button(frame,text='Next',command=next_3,activebackground="#44d7eb",bg='white')
    next3.grid(row=5,column=2)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
    canvas.create_window(650,350,window=frame,anchor=CENTER)
   
    sub.grab_set()
    sub.mainloop()
    # print(no_of_roles.get())

   



def displayallworks(win):
    
    sub=Toplevel(win)
    sub.geometry("1300x720")
    s=ThemedStyle()
    s.set_theme('equilux')
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    frame=Frame(sub,bg='white',bd=3,relief=SOLID,highlightthickness=8)
    
    l=Label(frame,text='Work details ',bg="#44d7eb")
    l.grid(row=0,column=0,columnspan=7)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM works")
    myresult = cursor.fetchall()
    tree=ttk.Treeview( frame,column= ("c1","c2","c3","c4","c5","c6","c7"),show='headings',height=len(myresult))
    tree.column("# 1",anchor=CENTER)
    tree.heading("# 1",text=" ID")
    tree.column("# 2",anchor=CENTER)
    tree.heading("# 2",text="Name")
    tree.column("# 3",anchor=CENTER)
    tree.heading("# 3",text=" No. of workers")
    tree.column("# 4",anchor=CENTER)
    tree.heading("# 4",text="Start Date")
    tree.column("# 5",anchor=CENTER)
    tree.heading("# 5",text="Priority")
    tree.column("# 6",anchor=CENTER)
    tree.heading("# 6",text="Duration")
    tree.column("# 7",anchor=CENTER)
    tree.heading("# 7",text="Status")
    i=1
    for x in myresult:
        tree.insert('','end',text=i, values=x)
        print(x)
        i+=1

    tree.grid(row=1,column=0,columnspan=7)
    cursor.close()
    exit=Button(frame,text='Exit',command=sub.destroy,activebackground="#44d7eb",bg='white')
    exit.grid(row=2,column=0,columnspan=7)
    
    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
    canvas.create_window(800,350,window=frame,anchor=CENTER)
   
    sub.grab_set()
    sub.mainloop()


    

def viewwork(i,win,canvas):
    s=ThemedStyle()
    s.set_theme('equilux')
    frame=Frame(win,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")
    
    #l.grid(row=0,column=0)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM works where work_id="+str(i.get()))
    myresult = cursor.fetchall()

    #if myresult is empty
    if len(myresult)==0:
        #show label
        l4=Label(frame,text='No such work exists')
        l4.configure(fg='black',bg="#44d7eb")
        l4.grid(row=1,column=0,columnspan=6)
        #exit button
        exit=Button(frame,text='Exit',command=frame.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=5,column=0,columnspan=6)
        canvas.create_window(650,350,window=frame,anchor=CENTER)
        return
    
    else:
        l=Label(frame,text='Work details ')
        l.configure(bg="#44d7eb",fg='black')
        l.grid(row=0,column=0,columnspan=6)
        l2=Label(frame,text='Workers Required ')
        l2.configure(fg='black',bg="#44d7eb")
        l2.grid(row=2,column=0,columnspan=6)
        l3=Label(frame,text='Workers Allotted ')
        l3.configure(fg='black',bg="#44d7eb")
        l3.grid(row=4,column=0,columnspan=6)
        tree=ttk.Treeview( frame,column= ("c1","c2","c3","c4","c5","c6","c7"),show='headings',height=len(myresult))
        tree.column("# 1",anchor=CENTER)
        tree.heading("# 1",text=" ID")
        tree.column("# 2",anchor=CENTER)
        tree.heading("# 2",text="Name")
        tree.column("# 3",anchor=CENTER)
        tree.heading("# 3",text=" No. of workers")
        tree.column("# 4",anchor=CENTER)
        tree.heading("# 4",text="Start Date")
        tree.column("# 5",anchor=CENTER)
        tree.heading("# 5",text="Priority")
        tree.column("# 6",anchor=CENTER)
        tree.heading("# 6",text="Duration")
        tree.column("# 7",anchor=CENTER)
        tree.heading("# 7",text="Status")
        j=1

        for x in myresult:
            tree.insert('','end',text=i, values=x)
            print(x)
            j+=1

        tree.grid(row=1,column=0,columnspan=6)

        cursor.execute("SELECT * from work_req where id='"+str(i.get())+"'")
        worker_requirement=cursor.fetchall()
        tree2=ttk.Treeview(frame,column= ("c1","c2","c3","c4","c5"),show='headings',height=len(worker_requirement))
        tree2.column("# 1",anchor=CENTER)
        tree2.heading("# 1",text=" ID")
        tree2.column("# 2",anchor=CENTER)
        tree2.heading("# 2",text="Role")
        tree2.column("# 3",anchor=CENTER)
        tree2.heading("# 3",text=" Beginner")
        tree2.column("# 4",anchor=CENTER)
        tree2.heading("# 4",text="Intermediate")
        tree2.column("# 5",anchor=CENTER)
        tree2.heading("# 5",text="Expert")
        j=1
        for x in worker_requirement:
            tree2.insert('','end',text=i, values=x)
            j+=1

        tree2.grid(row=3,column=0,columnspan=6)
        cursor.execute("SELECT * from allotted_workers where id='"+str(i.get())+"'")
        allotted_workers=cursor.fetchall()
        tree3=ttk.Treeview(frame,column= ("c1","c2","c3","c4","c5"),show='headings',height=len(allotted_workers))
        tree3.column("# 1",anchor=CENTER)
        tree3.heading("# 1",text=" ID")
        tree3.column("# 2",anchor=CENTER)
        tree3.heading("# 2",text="Role")
        tree3.column("# 3",anchor=CENTER)
        tree3.heading("# 3",text=" Beginner")
        tree3.column("# 4",anchor=CENTER)
        tree3.heading("# 4",text="Intermediate")
        tree3.column("# 5",anchor=CENTER)
        tree3.heading("# 5",text="Expert")
        j=1
        for x in allotted_workers:
            tree3.insert('','end',text=i, values=(x[0],x[1],x[2],x[3],x[4]))
            print(x)
            j+=1

        tree3.grid(row=5,column=0,columnspan=6)

        #tree.grid(row=3,column=0,columnspan=6)
        cursor.close()
        exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=6,column=0,columnspan=6)
        #exit.grid(row=4,column=1)
        canvas.create_window(800,350,window=frame,anchor=CENTER)




def editwork(i,win,canvas):
    s=ThemedStyle()
    s.set_theme('equilux')
    frame=Frame(win,bg='white',bd=3,highlightthickness=8,highlightbackground="#44d7eb")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM works where work_id='"+str(i.get())+"'")
    myresult = cursor.fetchall()
    #if myresult is empty
    if len(myresult)==0:
        label=Label(frame,text='No such work exists',bg="#44d7eb")
        label.grid(row=0,column=0)
        exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=1,column=0)
        canvas.create_window(650,350,window=frame,anchor=CENTER)
        return
    for x in myresult:
        print(x)

    cursor.execute("SELECT COLUMN_NAME, ORDINAL_POSITION FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'works' ORDER BY ORDINAL_POSITION")
    myresult = cursor.fetchall()
    
    label1=Label(frame,text='Select the attribute to change',bg="#44d7eb")
    label1.grid(row=0,column=0)
    
    work_index=StringVar()

    for (text,val) in myresult:
        r=Radiobutton(frame,text=text,variable=work_index,value=val)
        r.grid(row=val,column=0,sticky=W)

    new_val=StringVar()
    label2=Label(frame,text='Enter the new value',bg="#44d7eb")
    label2.grid(row=1+len(myresult),column=0)
    e=Entry(frame,textvariable=new_val,width=50)
    e.grid(row=1+len(myresult),column=1)
    
    def process():
        cursor.execute("UPDATE works SET "+str(myresult[int(work_index.get())-1][0])+"='"+str(new_val.get())+"' where work_id="+str(i.get()))
        connection.commit()
        cursor.close()
        msg=Label(frame,text='Updated successfully',bg="#44d7eb")
        msg.grid(row=3+len(myresult),column=1)

    ok=Button(frame,text='OK',command=process,activebackground="#44d7eb",bg='white')
    ok.grid(row=2+len(myresult),column=1)
    exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
    exit.grid(row=4+len(myresult),column=1)

    canvas.create_window(650,350,window=frame,anchor=CENTER)



class worker:
    def __init__(self,id,name,gender,contact_no,role,skill_level):
        self.id=id
        self.name=name
        self.gender=gender
        self.contact_no=contact_no
        self.role=role
        self.skill_level=skill_level
        self.availability=1
        self.nofhours_worked=0
        self.works_completed=[]
        self.last_active_work_date="NULL"
        self.current_work_id="NULL"
        
    def edit_details(self,nofhours_worked,work_completed):
        self.nofhours_worked+=nofhours_worked
        self.works_completed.append(work_completed)

def addworker(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    frame=Frame(sub,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")

    label1=Label(frame,text='Enter the details of the worker',bg="#44d7eb")
    label1.grid(row=0,column=0,columnspan=2)
    label2=Label(frame,text='Enter the id of the worker',bg="#44d7eb")
    label2.grid(row=1,column=0)
    id=StringVar()
    e1=Entry(frame,textvariable=id,width=50)
    e1.grid(row=1,column=1)
    label3=Label(frame,text='Enter the name of the worker',bg="#44d7eb")
    label3.grid(row=2,column=0)
    name=StringVar()
    e2=Entry(frame,textvariable=name,width=50)
    e2.grid(row=2,column=1)
    label4=Label(frame,text='Enter the gender: ',bg="#44d7eb")
    label4.grid(row=3,column=0)
    gender=StringVar()
    e3=Entry(frame,textvariable=gender,width=50)
    e3.grid(row=3,column=1)
    label5=Label(frame,text='Enter the contact number: ',bg="#44d7eb")
    label5.grid(row=4,column=0)
    contact_no=StringVar()
    e4=Entry(frame,textvariable=contact_no,width=50)
    e4.grid(row=4,column=1)
    label6=Label(frame,text='Enter the role: ',bg="#44d7eb")
    label6.grid(row=5,column=0)
    role=StringVar()
    e5=Entry(frame,textvariable=role,width=50)
    e5.grid(row=5,column=1)
    label7=Label(frame,text='Enter the skill level: ',bg="#44d7eb")
    label7.grid(row=6,column=0)
    skill_level=StringVar()
    r1=Radiobutton(frame,text="Beginner",variable=skill_level,value="beginner")
    r1.grid(row=6,column=1,sticky=W)
    r2=Radiobutton(frame,text="Intermediate",variable=skill_level,value="intermediate")
    r2.grid(row=7,column=1,sticky=W)
    r3=Radiobutton(frame,text="Expert",variable=skill_level,value="expert")
    r3.grid(row=8,column=1,sticky=W)
    
    # e6=Entry(frame,textvariable=skill_level,width=50)
    # e6.grid(row=6,column=1)

    def process():
        cursor=connection.cursor()
        insert_record_stmt = """INSERT INTO worker (worker_id, worker_name, gender, contact_no, role, skill_level, availability, no_of_hours_worked,works_completed) VALUES (%s, %s, %s, %s, %s, %s,1,0,' ')"""
        record_to_insert = (id.get(),name.get(),gender.get(),contact_no.get(),role.get(),skill_level.get())
        cursor.execute(insert_record_stmt, record_to_insert)
        connection.commit()
        print(cursor)
        msg=Label(frame,text='Worker added successfully',background="#44d7eb")
        msg.grid(row=9,column=0,columnspan=2)
        cursor.close()


    ok=Button(frame,text='OK',command=process,activebackground="#44d7eb",bg='white')
    ok.grid(row=10,column=0)

    exit=Button(frame,text='Exit',command=sub.destroy,activebackground="#44d7eb",bg='white')
    exit.grid(row=10,column=1)
    
 
    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
    canvas.create_window(650,300,window=frame,anchor=CENTER)
   
    sub.grab_set()
    sub.mainloop()



def displayallworkers(win):
    
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    frame=Frame(sub,bg='white',bd=3,relief=SOLID,highlightthickness=10,highlightbackground="#44d7eb")
    l=Label(frame,text='Worker details',background="#44d7eb")
    l.grid(row=0,column=0,columnspan=6)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM worker")
    myresult = cursor.fetchall()
    tree=ttk.Treeview( frame,
                      column= ("c1","c2","c3","c4","c5","c6"),
                      show='headings',height=len(myresult))
    
    tree.column("# 1",anchor=CENTER)
    tree.heading("# 1",text=" ID")
    tree.column("# 2",anchor=CENTER)
    tree.heading("# 2",text="Name")
    tree.column("# 3",anchor=CENTER)
    tree.heading("# 3",text=" Gender")
    tree.column("# 4",anchor=CENTER)
    tree.heading("# 4",text="Contact No")
    tree.column("# 5",anchor=CENTER)
    tree.heading("# 5",text="Role")
    tree.column("# 6",anchor=CENTER)
    tree.heading("# 6",text="Skill Level")
    for x in myresult:
        tree.insert('','end',text="1", values=(x[0],x[1],x[2],x[3],x[4],x[5]))
        print(x)

    tree2=ttk.Treeview( frame,
                      column= ("c1","c2","c3","c4","c5","c6"),
                      show='headings',height=len(myresult))
    
    tree2.column("# 1",anchor=CENTER)
    tree2.heading("# 1",text="ID")
    tree2.column("# 2",anchor=CENTER)
    tree2.heading("# 2",text="Availability")
    tree2.column("# 3",anchor=CENTER)
    tree2.heading("# 3",text="Current Work ID")
    tree2.column("# 4",anchor=CENTER)
    tree2.heading("# 4",text="Last Active Date")
    tree2.column("# 5",anchor=CENTER)
    tree2.heading("# 5",text="No of hours worked")
    tree2.column("# 6",anchor=CENTER)
    tree2.heading("# 6",text="Works Completed")
    for x in myresult:
        tree2.insert('','end',text="1", values=(x[0],x[6],x[7],x[8],x[9],x[10]))
        print(x)

    tree.grid(row=1,column=0,columnspan=6)
    gap=Label(frame,text="  ",bg='white')
    gap.grid(row=2,column=0)
    tree2.grid(row=3,column=0,columnspan=6)
    cursor.close()
    exit=Button(frame,text='Exit',command=sub.destroy,activebackground="#44d7eb",bg='white')
    exit.grid(row=4,column=0,columnspan=6)
    

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
    canvas.create_window(800,450,window=frame,anchor=CENTER)
   
    sub.grab_set()
    sub.mainloop()


   

def viewworker(i,win,canvas):
    s=ThemedStyle()
    s.set_theme('equilux')
    frame=Frame(win,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")
    
    l=Label(frame,text='Worker details',bg="#44d7eb")
    l.grid(row=0,column=0,columnspan=6)
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM worker where worker_id="+str(i.get()))
    myresult = cursor.fetchall()
    #if myresult is null show label
    if len(myresult)==0:
        label=Label(frame,text='No such worker exists; invalid id',bg="#44d7eb")
        label.grid(row=0,column=0)
        exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=1,column=0)
        canvas.create_window(650,350,window=frame,anchor=CENTER)
        return



    tree=ttk.Treeview( frame,
                      column= ("c1","c2","c3","c4","c5","c6"),
                      show='headings',height=len(myresult))
    
    tree.column("# 1",anchor=CENTER)
    tree.heading("# 1",text=" ID")
    tree.column("# 2",anchor=CENTER)
    tree.heading("# 2",text="Name")
    tree.column("# 3",anchor=CENTER)
    tree.heading("# 3",text=" Gender")
    tree.column("# 4",anchor=CENTER)
    tree.heading("# 4",text="Contact No")
    tree.column("# 5",anchor=CENTER)
    tree.heading("# 5",text="Role")
    tree.column("# 6",anchor=CENTER)
    tree.heading("# 6",text="Skill Level")
    for x in myresult:
        tree.insert('','end',text="1", values=(x[0],x[1],x[2],x[3],x[4],x[5]))
        print(x)

    tree2=ttk.Treeview( frame,
                      column= ("c1","c2","c3","c4","c5","c6"),
                      show='headings',height=len(myresult))
    
    tree2.column("# 1",anchor=CENTER)
    tree2.heading("# 1",text="ID")
    tree2.column("# 2",anchor=CENTER)
    tree2.heading("# 2",text="Availability")
    tree2.column("# 3",anchor=CENTER)
    tree2.heading("# 3",text="Current Work ID")
    tree2.column("# 4",anchor=CENTER)
    tree2.heading("# 4",text="Last Active Date")
    tree2.column("# 5",anchor=CENTER)
    tree2.heading("# 5",text="No of hours worked")
    tree2.column("# 6",anchor=CENTER)
    tree2.heading("# 6",text="Works Completed")
    for x in myresult:
        tree2.insert('','end',text="1", values=(x[0],x[6],x[7],x[8],x[9],x[10]))
        print(x)

    tree.grid(row=3,column=0,columnspan=6)
    tree2.grid(row=5,column=0,columnspan=6)
    
    cursor.close()
    exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
    exit.grid(row=6,column=0,columnspan=6)
    gap=Label(frame,text="    ",bg='white')
    gap.grid(row=4,column=0,columnspan=6)

    canvas.create_window(800,350,window=frame,anchor=CENTER)


def editworker(i,win,canvas):
    s=ThemedStyle()
    s.set_theme('equilux')
    frame=Frame(win,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")
    cursor=connection.cursor()
    cursor.execute("SELECT COLUMN_NAME, ORDINAL_POSITION FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'worker' ORDER BY ORDINAL_POSITION")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

    if len(myresult)==0:
        label=Label(frame,text='No such worker exists; invalid id',bg="#44d7eb")
        label.grid(row=0,column=0)
        exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=1,column=0)
        canvas.create_window(650,350,window=frame,anchor=CENTER)
        return
    
    label1=Label(frame,text='Select the attribute to change: ',bg="#44d7eb")
    label1.grid(row=0,column=0)
    attribute=StringVar()
    for (text,val) in myresult:
        r1=Radiobutton(frame,text=text,variable=attribute,value=val,bg="#44d7eb")
        r1.grid(row=val,column=0,sticky=W)
    label2=Label(frame,text='Enter the new value',bg="#44d7eb")
    label2.grid(row=1+len(myresult),column=0)
    new_val=StringVar()
    e2=Entry(frame,textvariable=new_val,width=50)
    e2.grid(row=1+len(myresult),column=1)

    def process():
        
        cursor.execute("UPDATE worker SET "+str(myresult[int(attribute.get())-1][0])+"='"+str(new_val.get())+"' where worker_id="+str(i.get()))
        connection.commit()
        msg=Label(frame,text='Worker edited successfully',bg="#44d7eb")
        msg.grid(row=3+len(myresult),column=0,columnspan=2)
        cursor.close()


    ok=Button(frame,text='OK',command=process,activebackground="#44d7eb",bg='white')
    ok.grid(row=2+len(myresult),column=0)
    exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
    exit.grid(row=4+len(myresult),column=0)
    canvas.create_window(650,400,window=frame,anchor=CENTER)
    

def deleteworker(i,win,canvas):
    s=ThemedStyle()
    s.set_theme('equilux')
    frame=Frame(win,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")
    cursor=connection.cursor()
    cursor.execute("select * from worker where worker_id='"+str(i.get())+"'")
    myresult = cursor.fetchall()
    if len(myresult)==0:
        label=Label(frame,text='No such worker exists; invalid id',bg="#44d7eb")
        label.grid(row=0,column=0)
        exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white')
        exit.grid(row=1,column=0)
        canvas.create_window(650,350,window=frame,anchor=CENTER)
        return
    cursor.execute("Delete from worker where worker_id='"+str(i.get())+"'")
    connection.commit()
    print(cursor)
    msg=Label(frame,text='Worker deleted successfully',bg="#44d7eb")
    msg.grid(row=0,column=0,columnspan=2)
    exit=Button(frame,text='Exit',command=win.destroy,activebackground="#44d7eb",bg='white',font=('Arial',15,'bold'))
    exit.grid(row=1,column=0,columnspan=2)
    canvas.create_window(650,300,window=frame,anchor=CENTER)
    cursor.close()

        
def assignment_to_workers(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    frame=Frame(sub,bg='white',bd=3,relief=SOLID,highlightthickness=8,highlightbackground="#44d7eb")
    cursor=connection.cursor()
    # cursor.execute("SELECT MAX(priority) FROM works where work_status='not started'")
    # myresult = cursor.fetchall()
    # for x in myresult:
    #     max_priority=x[0]
    #     print(max_priority)
    # cursor.execute("SELECT * FROM works where priority='"+str(max_priority)+"'")
    cursor.execute("SELECT * FROM works where work_status='not started' order by priority DESC")
    myresult = cursor.fetchall()
    connection.commit()
    cursor.close()
    loop_count=0
    ids=list()
    names=list()

    k=0
    j=0
    for x in myresult:
        loop_count=loop_count+1
        print(loop_count)
        cursor=connection.cursor()
        print(x)
        work_id=x[0]
        work_name=x[1]
        cursor.execute("SELECT * FROM work_req WHERE id="+str(work_id))
        myresult = cursor.fetchall()
        possible_to_start=1
        for y in myresult:
            print(y)
            print(y[1])
            print("select count(worker_id) from worker where role='"+str(y[1])+"' and skill_level='beginner' and availability='1'")
            cursor.execute("select count(worker_id) from worker where role='"+str(y[1])+"' and skill_level='beginner' and availability='1'")
            print(cursor)
            res=cursor.fetchall()
            print(res)
            for z in res:
                print(z)
                beginner_count=int(z[0])
                print(beginner_count)
                print(int(y[2]))
            if beginner_count>=int(y[2]):
                cursor.execute("UPDATE allotted_workers SET beginner='"+str(y[2]) +"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                cursor.execute("UPDATE work_req SET beginner='0' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                #alllocation to workers here
                count=int(0)
                cursor.execute("select * FROM worker WHERE last_active_work_date IS NULL and role='"+str(y[1])+"' and skill_level='beginner' and availability='1'")
                result=cursor.fetchall()
                for key in result:
                    if(count<y[2]):
                        cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                        cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                        print(key[0])
                        count=count+1
                        print(count)
                    else: 
                        break   
                while(count<y[2]):
                    cursor.execute("select * FROM worker WHERE last_active_work_date IS NOT NULL and availability='1' and role='"+str(y[1])+"' and skill_level='beginner' ORDER BY last_active_work_date ASC")
                    sorted_result=cursor.fetchall()
                    print(sorted_result)
                    for key in sorted_result:
                        if(count<y[2]):
                            cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                            cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                            print(key[0])
                            count=count+1
                            print(count)

            else:
                cursor.execute("UPDATE allotted_workers SET beginner='"+str(beginner_count) +"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                beginners_needed=int(y[2])- beginner_count
                print(beginners_needed)
                cursor.execute("UPDATE work_req SET beginner='"+ str(beginners_needed)+"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'",)
                #allocation to workers here
                count=int(0)
                cursor.execute("select * FROM worker WHERE last_active_work_date IS NULL and role='"+str(y[1])+"' and skill_level='beginner' and availability='1'")
                result=cursor.fetchall()
                for key in result:
                    if(count<beginner_count):
                        cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                        cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                        print(key[0])
                        count=count+1
                        print(count)
                    else: 
                        break   
                while(count<beginner_count):
                    cursor.execute("select * FROM worker WHERE last_active_work_date IS NOT NULL and availability='1' and role='"+str(y[1])+"' and skill_level='beginner' ORDER BY last_active_work_date ASC")
                    sorted_result=cursor.fetchall()
                    print(sorted_result)
                    for key in sorted_result:
                        if(count<beginner_count):
                            cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                            cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                            print(key[0])
                            count=count+1
                            print(count)


                possible_to_start=0
                print(cursor)

            cursor.execute("select count(worker_id) from worker where role='"+str(y[1])+"' and skill_level='intermediate' and availability=1")
            res=cursor.fetchall()
            for z in res:
                intermediate_count=int(z[0])
                print("inter count is "+str(intermediate_count))
            if intermediate_count>=int(y[3]):
                cursor.execute("UPDATE allotted_workers SET intermediate='"+str(y[3]) +"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                cursor.execute("UPDATE work_req SET intermediate='0' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                #alllocation to workers here
                count=int(0)
                cursor.execute("select * FROM worker WHERE last_active_work_date IS NULL and role='"+str(y[1])+"' and skill_level='intermediate' and availability='1'")
                result=cursor.fetchall()
                for key in result:
                    if(count<y[3]):
                        cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                        cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                        print(key[0])
                        count=count+1
                        print(count)
                    else: 
                        break   
                while(count<y[3]):
                    cursor.execute("select * FROM worker WHERE last_active_work_date IS NOT NULL and availability='1' and role='"+str(y[1])+"' and skill_level='intermediate' ORDER BY last_active_work_date ASC")
                    sorted_result=cursor.fetchall()
                    print(sorted_result)
                    for key in sorted_result:
                        if(count<y[3]):
                            cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                            cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                            print(key[0])
                            count=count+1
                            print(count)
            else:
                print("here")
                cursor.execute("UPDATE allotted_workers SET intermediate='"+str(intermediate_count) +"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                intermediates_needed=int(y[3])- intermediate_count
                print("interim needed" + str(intermediates_needed))
                cursor.execute("UPDATE work_req SET intermediate='"+ str(intermediates_needed)+"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                #allocation to workers here
                count=int(0)
                cursor.execute("select * FROM worker WHERE last_active_work_date IS NULL and role='"+str(y[1])+"' and skill_level='intermediate' and availability='1'")
                result=cursor.fetchall()
                for key in result:
                    if(count<intermediate_count):
                        cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                        cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                        print(key[0])
                        count=count+1
                        print(count)
                    else: 
                        break   
                while(count<intermediate_count):
                    cursor.execute("select * FROM worker WHERE last_active_work_date IS NOT NULL and availability='1' and role='"+str(y[1])+"' and skill_level='intermediate' ORDER BY last_active_work_date ASC")
                    sorted_result=cursor.fetchall()
                    print(sorted_result)
                    for key in sorted_result:
                        if(count<intermediate_count):
                            cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                            cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                            print(key[0])
                            count=count+1
                            print(count)


                possible_to_start=0
                print(cursor)

            cursor.execute("select count(worker_id) from worker where role='"+str(y[1])+"' and skill_level='expert' and availability=1")
            res=cursor.fetchall()
            for z in res:
                expert_count=int(z[0])
            if expert_count>=int(y[4]):
                cursor.execute("UPDATE allotted_workers SET expert='"+str(y[4]) +"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                cursor.execute("UPDATE work_req SET expert='0' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                #alllocation to workers here
                count=int(0)
                cursor.execute("select * FROM worker WHERE last_active_work_date IS NULL and role='"+str(y[1])+"' and skill_level='expert' and availability='1'")
                result=cursor.fetchall()
                for key in result:
                    if(count<y[4]):
                        cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                        cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                        print(key[0])
                        count=count+1
                        print(count)
                    else: 
                        break   
                while(count<y[4]):
                    cursor.execute("select * FROM worker WHERE last_active_work_date IS NOT NULL and availability='1' and role='"+str(y[1])+"' and skill_level='expert' ORDER BY last_active_work_date ASC")
                    sorted_result=cursor.fetchall()
                    print(sorted_result)
                    for key in sorted_result:
                        if(count<y[4]):
                            cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                            cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                            print(key[0])
                            count=count+1
                            print(count)

            else:
                cursor.execute("UPDATE allotted_workers SET expert='"+str(expert_count) +"' WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                experts_needed=int(y[4])- expert_count
                cursor.execute("UPDATE work_req SET expert='"+ str(experts_needed)+"'WHERE id='"+str(work_id) +"' and role='"+str(y[1])+"'")
                #alllocation to workers here
                count=int(0)
                cursor.execute("select * FROM worker WHERE last_active_work_date IS NULL and role='"+str(y[1])+"' and skill_level='expert' and availability='1'")
                result=cursor.fetchall()
                for key in result:
                    if(count<expert_count):
                        cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                        cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                        print(key[0])
                        count=count+1
                        print(count)
                    else: 
                        break   
                while(count<expert_count):
                    cursor.execute("select * FROM worker WHERE last_active_work_date IS NOT NULL and availability='1' and role='"+str(y[1])+"' and skill_level='expert' ORDER BY last_active_work_date ASC")
                    sorted_result=cursor.fetchall()
                    print(sorted_result)
                    for key in sorted_result:
                        if(count<expert_count):
                            cursor.execute("UPDATE worker SET availability='0' where worker_id='"+str(key[0])+"'")
                            cursor.execute("UPDATE worker SET current_work_id='"+str(work_id)+"' where worker_id='"+str(key[0])+"'")
                            print(key[0])
                            count=count+1
                            print(count)


                possible_to_start=0
                print(cursor)


        if possible_to_start==1:
            cursor.execute("UPDATE works SET work_status='in progress' WHERE work_id='"+str(work_id)+"'")
            #enter start date
        
            cursor.execute("UPDATE works SET start_date='"+str(date.today())+ "' WHERE work_id='"+str(work_id)+"'")
            print("Work started")
            ids.append(work_id)
            names.append(work_name)
            
            j+=1
            connection.commit()
            cursor.close()
        else:
            print("Not possible to start work")
            connection.commit()
            cursor.close()

    l2=Label(frame,text=" Work started",bg="#44d7eb",font=('Arial',12,'bold'))
    l2.grid(row=1,column=0,columnspan=5)
    tree1=ttk.Treeview( frame,column= ("c1","c2","c3"),show='headings',height=len(ids))
    tree1.column("# 1",anchor=CENTER)
    tree1.heading("# 1",text=" ID")
    tree1.column("# 2",anchor=CENTER)
    tree1.heading("# 2",text="Name")
    tree1.column("# 3",anchor=CENTER)
    tree1.heading("# 3",text=" Status")
    if len(ids)==0:
        l=Label(frame,text="No works to start",bg="#44d7eb")
        l.grid(row=3,column=0,columnspan=5)
    else:
        for i in range(len(ids)):
            tree1.insert('','end',text=i, values=(ids[i],names[i],'Started'))
   
    tree1.grid(row=2,column=0,columnspan=5)

    cursor=connection.cursor()
    cursor.execute("select * from allotted_workers  where beginner>0 or intermediate>0 or expert>0")
    result=cursor.fetchall()
    connection.commit()
    cursor.close()

    l2=Label(frame,text="Allotted workers",bg="#44d7eb",font=('Arial',12,'bold'))
    l2.grid(row=4,column=0,columnspan=5)
    tree2=ttk.Treeview(frame,column= ("c1","c2","c3","c4","c5"),show='headings',height=len(result))
    tree2.column("# 1",anchor=CENTER)
    tree2.heading("# 1",text=" ID")
    tree2.column("# 2",anchor=CENTER)
    tree2.heading("# 2",text="Role")
    tree2.column("# 3",anchor=CENTER)
    tree2.heading("# 3",text="Beginner")
    tree2.column("# 4",anchor=CENTER)
    tree2.heading("# 4",text="Intermediate")
    tree2.column("# 5",anchor=CENTER)
    tree2.heading("# 5",text="Expert") 
    for x in result:
        tree2.insert('','end',text=k, values=(x[0],x[1],x[2],x[3],x[4]))
        k+=1

    tree2.grid(row=5,column=0,columnspan=5)


    exit=Button(frame,text="Exit",command=sub.destroy,activebackground="#44d7eb",bg='white',bd=2,relief=SOLID,font=('Arial',12,'bold'))
    exit.grid(row=6,column=0,columnspan=5)
    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
    canvas.create_window(650,300,window=frame,anchor=CENTER)
   
    sub.grab_set()
    sub.mainloop()




def mark_completed_work(id,sub,canvas):
    
    
    s=ThemedStyle()
    s.set_theme('equilux')

    frame=Frame(sub,bg='white',bd=3,relief=SOLID,highlightthickness=10,highlightbackground="#44d7eb")
    cursor=connection.cursor()
    cursor.execute("select * from works where work_id='"+str(id.get())+"'")
    result=cursor.fetchall()
    if len(result)==0:
        l2=Label(frame,text="Work not found; invalid work id",fg='black',bg="#44d7eb")
        l2.grid(row=0,column=0)
        canvas.create_window(650,200,window=frame,anchor=CENTER)
        connection.commit()
        cursor.close()
        return
    for x in result:
        print(x)
        print(x[6])
        if x[6]=='completed':
            l2=Label(frame,text="Work already completed",fg='black',bg="#44d7eb")
            l2.grid(row=0,column=0)
            canvas.create_window(650,200,window=frame,anchor=CENTER)
            connection.commit()
            cursor.close()
            return
        else:
            cursor.execute("UPDATE works SET work_status='completed' WHERE work_id='"+str(id.get())+"'")

            #cursor.execute("UPDATE works SET end_date='"+str(date.today())+ "' WHERE work_id='"+str(work_id)+"'")
            #duration
            no_of_days=(date.today()-x[3]).days
            no_of_days=no_of_days+1
            cursor.execute("UPDATE works SET duration='"+str(no_of_days)+ "' WHERE work_id='"+str(id.get())+"'")


            cursor.execute("delete from allotted_workers where id='"+str(id.get())+"'")
            cursor.execute("select * from worker where current_work_id='"+str(id.get())+"'")
            result=cursor.fetchall()
            for y in result:
                cursor.execute("UPDATE worker SET availability='1' where worker_id='"+str(y[0])+"'")
                cursor.execute("UPDATE worker SET current_work_id=NULL where worker_id='"+str(y[0])+"'")
                cursor.execute("UPDATE worker SET last_active_work_date='"+str(date.today())+"' where worker_id='"+str(y[0])+"'")
                #total hours worked
                cursor.execute("UPDATE worker SET no_of_hours_worked='"+str(int(int(y[9])+int(no_of_days*8)))+"' where worker_id='"+str(y[0])+"'")
                #works completed
                if(y[10]==None):
                    cursor.execute("UPDATE worker SET works_completed='"+str(x[1]+" , ")+"' where worker_id='"+str(y[0])+"'")
                else:
                    cursor.execute("UPDATE worker SET works_completed='"+str(str(x[1])+" , "+str(y[10]))+"' where worker_id='"+str(y[0])+"'")
            l3=Label(frame,text="Work completed",fg='black',bg="#44d7eb")
            l3.grid(row=0,column=0)
            canvas.create_window(650,200,window=frame,anchor=CENTER)
            connection.commit()
            cursor.close()
            
            assignment_to_workers(win)
            return
        
    
        
    
    
    

def mark_complete(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    l1=Label(sub,text="Enter work ID",font=('Arial',15,'bold'),fg='black',bg="#44d7eb")
    #l1.grid(row=0,column=0)
    var=IntVar(sub,value=0)
    e1=Entry(sub,textvariable=var,width=50)
    #e1.grid(row=0,column=1)
    ok=Button(sub,text="OK",command=partial(mark_completed_work,var,sub,canvas))
    ok.config(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #ok.grid(row=1,column=1)
    exit=Button(sub,text="Exit",command=sub.destroy)
    exit.config(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #exit.grid(row=3,column=1)
    
    canvas.create_window(400,50,window=l1,anchor=CENTER)
    canvas.create_window(750,50,window=e1,anchor=CENTER)
    canvas.create_window(650,100,window=ok,anchor=CENTER)
    canvas.create_window(650,300,window=exit,anchor=CENTER)


    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
   
    sub.grab_set()
    sub.mainloop()

def edit_worker(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    
    j=Label(sub,text='Enter the worker number:')
    j.config(bg="#44d7eb",fg='black',font=('Arial',15,'bold'))
    #j.grid(row=1,column=0)
    j1=IntVar(sub,value=0)
    j2=Entry(sub,textvariable=j1,width=50)
    #j2.grid(row=1,column=1)
    ok=Button(sub,text='OK',command=partial(editworker,j1,sub,canvas))
    ok.config(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #ok.grid(row=2,column=1)
    
    canvas.create_window(400,50,window=j,anchor=CENTER)
    canvas.create_window(750,50,window=j2,anchor=CENTER)
    canvas.create_window(650,100,window=ok,anchor=CENTER)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
   
    sub.grab_set()
    sub.mainloop()

def delete_worker(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    j=Label(sub,text='Enter the worker ID:')
    j.config(bg="#44d7eb",fg='black',font=('Arial',15,'bold'))
    #j.grid(row=1,column=0)
    j1=IntVar(sub,value=0)
    j2=Entry(sub,textvariable=j1,width=50)
    #j2.grid(row=1,column=1)
    ok=Button(sub,text='OK',command=partial(deleteworker,j1,sub,canvas))
    ok.config(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #ok.grid(row=2,column=1)
    
    canvas.create_window(400,50,window=j,anchor=CENTER)
    canvas.create_window(750,50,window=j2,anchor=CENTER)
    canvas.create_window(650,100,window=ok,anchor=CENTER)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
   
    sub.grab_set()
    sub.mainloop()

def view_worker(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    
    j=Label(sub,text='Enter the worker ID:')
    j.config(bg="#44d7eb",fg='black',font=('Arial',15,'bold'))
    #j.grid(row=1,column=0)
    j1=IntVar(sub,value=0)
    j2=Entry(sub,textvariable=j1,width=50)
    #j2.grid(row=1,column=1)
    ok=Button(sub,text='OK',command=partial(viewworker,j1,sub,canvas))
    ok.config(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #ok.grid(row=2,column=1)
    
    canvas.create_window(400,50,window=j,anchor=CENTER)
    canvas.create_window(750,50,window=j2,anchor=CENTER)
    canvas.create_window(650,100,window=ok,anchor=CENTER)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
   
    sub.grab_set()
    sub.mainloop()

def edit_work(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")
    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)
    
    j=Label(sub,text='Enter the work number:',bg="#44d7eb",fg='black',font=('Arial',15,'bold'))
    #j.grid(row=1,column=0)
    j1=IntVar(sub,value=0)
    j2=Entry(sub,textvariable=j1,width=50)
    #j2.grid(row=1,column=1)
    ok=Button(sub,text='OK',command=partial(editwork,j1,sub,canvas))
    ok.config(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #ok.grid(row=2,column=1)
    
    canvas.create_window(400,50,window=j,anchor=CENTER)
    canvas.create_window(750,50,window=j2,anchor=CENTER)
    canvas.create_window(650,100,window=ok,anchor=CENTER)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
   
    sub.grab_set()
    sub.mainloop()


def view_work(win):
    sub=Toplevel(win)
    s=ThemedStyle()
    s.set_theme('equilux')
   
    sub.geometry("1300x720")

    canvas = Canvas(sub, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    
    j=Label(sub,text='Enter the work ID:')
    j.configure(bg="#44d7eb",fg='black',font=('Arial',15,'bold'))
    #j.grid(row=1,column=0)
    j1=IntVar(sub,value=0)
    j2=Entry(sub,textvariable=j1,width=50)
    #j2.grid(row=1,column=1)
    ok=Button(sub,text='OK',command=partial(viewwork,j1,sub,canvas))
    ok.config(activebackground="#44d7eb",bg='white',fg='black',bd=2,relief=SOLID,font=('Arial',15,'bold'))
    #ok.grid(row=2,column=1)

    canvas.create_window(400,50,window=j,anchor=CENTER)
    canvas.create_window(750,50,window=j2,anchor=CENTER)
    canvas.create_window(650,100,window=ok,anchor=CENTER)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    sub.bind("<Configure>", resize_image)
   
    
    sub.grab_set()
    sub.mainloop()

def worker_menu(sub):
    subw=Toplevel(sub)
    subw.geometry("1300x720")
    s=ThemedStyle()
    s.set_theme('equilux')

    canvas = Canvas(subw, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    add=Button(subw,text="Add a worker",command=partial(addworker,subw))
    add.config(bg="white",fg="black",activebackground="#44d7eb",font=("Arial", 20, "bold"),bd=2,relief=SOLID)
    #add.grid(row=0,column=0)
    edit=Button(subw,text="Edit a worker",command=partial(edit_worker,subw))
    edit.config(bg="white",fg="black",activebackground="#44d7eb",font=("Arial", 20, "bold"),bd=2,relief=SOLID)
    #edit.grid(row=1,column=0)
    delete=Button(subw,text="Delete a worker",command=partial(delete_worker,subw))
    delete.config(bg="white",fg="black",activebackground="#44d7eb",font=("Arial", 20, "bold"),bd=2,relief=SOLID)
    #delete.grid(row=2,column=0)
    view=Button(subw,text="View a worker",command=partial(view_worker,subw))
    view.config(bg="white",fg="black",activebackground="#44d7eb",font=("Arial", 20, "bold"),bd=2,relief=SOLID)
    #view.grid(row=3,column=0)
    display=Button(subw,text="Display all workers",command=partial(displayallworkers,subw))
    display.config(bg="white",fg="black",activebackground="#44d7eb",font=("Arial", 20, "bold"),bd=2,relief=SOLID)
    #display.grid(row=4,column=0)
    exit=Button(subw,text="Exit",command=subw.destroy)
    exit.config(bg="white",fg="black",activebackground="#44d7eb",font=("Arial", 20, "bold"),bd=2,relief=SOLID)
    #exit.grid(row=5,column=0)

    canvas.create_window(650,100,window=add,anchor=CENTER)
    canvas.create_window(650,200,window=edit,anchor=CENTER)
    canvas.create_window(650,300,window=delete,anchor=CENTER)
    canvas.create_window(650,400,window=view,anchor=CENTER)
    canvas.create_window(650,500,window=display,anchor=CENTER)
    canvas.create_window(650,600,window=exit,anchor=CENTER)


    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    subw.bind("<Configure>", resize_image)
   
    
    subw.grab_set()
    subw.mainloop()

def work_menu(sub):
    subw=Toplevel(sub)
    subw.geometry("1300x720")
    s=ThemedStyle()
    s.set_theme('equilux')

    canvas = Canvas(subw, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    add=Button(subw,text="Add a work",command=partial(addwork,subw))
    add.config(bg='white',fg='black',activebackground="#44d7eb",font=('helvetica', 20, 'bold'),bd=2,relief=SOLID)
    #add.grid(row=0,column=0)
    edit=Button(subw,text="Edit a work",command=partial(edit_work,subw))
    edit.config(bg='white',fg='black',activebackground="#44d7eb",font=('helvetica', 20, 'bold'),bd=2,relief=SOLID)
    #edit.grid(row=1,column=0)
    view=Button(subw,text="View a work",command=partial(view_work,subw))
    view.config(bg='white',fg='black',activebackground="#44d7eb",font=('helvetica', 20, 'bold'),bd=2,relief=SOLID)
    #view.grid(row=2,column=0)
    display=Button(subw,text="Display all works",command=partial(displayallworks,subw))
    display.config(bg='white',fg='black',activebackground="#44d7eb",font=('helvetica', 20, 'bold'),bd=2,relief=SOLID)
    #display.grid(row=3,column=0)
    mark=Button(subw,text='Mark a work completed',command=partial(mark_complete,subw))
    mark.config(bg='white',fg='black',activebackground="#44d7eb",font=('helvetica', 20, 'bold'),bd=2,relief=SOLID)
    exit=Button(subw,text="Exit",command=subw.destroy)
    exit.config(bg='white',fg='black',activebackground="#44d7eb",font=('helvetica', 20, 'bold'),bd=2,relief=SOLID)
    #exit.grid(row=4,column=0)

    canvas.create_window(650,150,window=add,anchor=CENTER)
    canvas.create_window(650,250,window=edit,anchor=CENTER)
    canvas.create_window(650,350,window=view,anchor=CENTER)
    canvas.create_window(650,450,window=display,anchor=CENTER)
    canvas.create_window(650,550,window=mark,anchor=CENTER)
    canvas.create_window(650,650,window=exit,anchor=CENTER)

    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    subw.bind("<Configure>", resize_image)
   
    
    subw.grab_set()
    subw.mainloop()
    

def menu(root):
    subwin=Toplevel(root)
    subwin.geometry("1300x720")
    bg = ImageTk.PhotoImage(file ="bg.jpg") 
    s=ThemedStyle()
    s.set_theme('equilux')


    # Create a Canvas
    canvas = Canvas(subwin, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    worker=Button(subwin,text='Worker',command=partial(worker_menu,subwin))
    worker.configure(bg='white',activebackground="#44d7eb",fg='black',bd=2,relief=SOLID,font=('Arial',20,'bold'))
    #worker.pack(side=TOP,expand="true",pady=50)
    #worker.grid(row=0,column=0,sticky=NSEW)
    work=Button(subwin,text='Work',command=partial(work_menu,subwin))
    work.configure(bg='white',fg='black',activebackground="#44d7eb",bd=2,relief=SOLID,font=('Arial',20,'bold'))
    #work.pack(side=TOP,expand="true",pady=60)
    #work.grid(row=1,column=0,sticky=NSEW)
    assign=Button(subwin,text='Worker-work assignment',command=partial(assignment_to_workers,subwin))
    assign.configure(bg='white',fg='black',activebackground="#44d7eb",bd=2,relief=SOLID,font=('Arial',20,'bold'))
    #assign.pack(side=TOP,expand="true",pady=70)
    #assign.grid(row=2,column=0,sticky=NSEW)
    exit=Button(subwin,text="Exit",command=subwin.destroy)
    exit.configure(bg='white',fg='black',activebackground="#44d7eb",bd=2,relief=SOLID,font=('Arial',20,'bold'))
    #exit.pack(side=TOP,expand="true",pady=80)
    #exit.grid(row=3,column=0,sticky=NSEW)
    canvas.create_window(650,150,window=worker,anchor=CENTER)
    canvas.create_window(650,250,window=work,anchor=CENTER)
    canvas.create_window(650,350,window=assign,anchor=CENTER)
    canvas.create_window(650,450,window=exit,anchor=CENTER)

    # Add Image inside the Canvas
    canvas.create_image(0, 0, image=bg, anchor='nw')

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

    
    # Bind the function to configure the parent window
    subwin.bind("<Configure>", resize_image)
   
    
    subwin.grab_set()
    subwin.mainloop()



# def main():
#     win = Tk()

#     # Set the geometry of Tkinter Frame
#     win.geometry("700x450")

#     # Open the Image File
#     #img=Image.open("sakura.jpeg")
#     #bg1=img.filter(ImageFilter.GaussianBlur(radius=20))
#     bg = ImageTk.PhotoImage(file ="sakura.jpeg") 


#     # Create a Canvas
#     canvas = Canvas(win, width=700, height=3500)
#     canvas.pack(fill=BOTH, expand=True)

#     # Add Image inside the Canvas
#     canvas.create_image(0, 0, image=bg, anchor='nw')

#     def resize_image(e):
#         global image, resized, image2 ,image3
#         # open image to resize it
#         image = Image.open("sakura.jpeg")
#         image3=image.filter(ImageFilter.GaussianBlur(radius=7))
#         # resize the image with width and height of root
#         resized = image3.resize((e.width, e.height), Image.ANTIALIAS)

#         image2 = ImageTk.PhotoImage(resized)
#         canvas.create_image(0, 0, image=image2, anchor='nw')

    
#     # Bind the function to configure the parent window
#     win.bind("<Configure>", resize_image)
  
#     home=Label(win, text='Welcome to the Work Management System')
#     home.pack()
#     enter=Button(win, text='Enter', command=partial(menu,win))
#     enter.pack(side=BOTTOM)
#     win.mainloop()

    
    # while True:
    #     print('Enter the choice')
    #     print('1. Add a work')
    #     print('2. Display all works')
    #     print('3. View a work')
    #     print('4. Edit a work')
    #     print('5. Delete a work')
    #     print('6. Add a worker')
    #     print('7. Display all workers')
    #     print('8. View a worker')
    #     print('9. Edit a worker')
    #     print('10. Delete a worker')
    #     print('11. Exit')
    #     choice=int(input('Enter your choice: '))
    #     if choice==1:
    #         addwork()
    #     elif choice==2:
    #         displayallworks()
    #     elif choice==3:
    #         i=int(input('Enter the work number: '))
    #         viewwork(i-1)
    #     elif choice==4:
    #         i=int(input('Enter the work number: '))
    #         editwork(i-1)
    #     elif choice==5:
    #         i=int(input('Enter the work number: '))
    #     elif choice==6:
    #         addworker()
    #     elif choice==7:
    #         displayallworkers()
    #     elif choice==8:
    #         i=input('Enter the role: ')
    #         j=int(input('Enter the worker number: '))
    #         viewworker(i,j)
    #     elif choice==9:
    #         i=input('Enter the role: ')
    #         j=int(input('Enter the worker number: '))
    #         editworker(i,j)
    #     elif choice==10:
    #         i=input('Enter the role: ')
    #         j=int(input('Enter the worker number: '))
    #         deleteworker(i,j)
    #     elif choice==11:
    #         break
    #     else:
    #         print('Invalid choice')
    #     print(' ')

    

# class TestWork(unittest.TestCase):

    # def setUp(self):
    #     self.work1 = work('Task A', 3, date.today() + timedelta(days=7), 'Task A requirements', 10)
    #     self.work2 = work('Task B', 2, date.today() + timedelta(days=3), 'Task B requirements', 5)
    #     self.work3 = work('Task C', 5, date.today() + timedelta(days=10), 'Task C requirements', 15)

    # def test_add_work(self):
    #     addwork()
    #     self.assertEqual(len(works), 1)
    #     self.assertIsInstance(works[0], work)
    
    # def test_display_all_works(self):
    #     displayallworks()
    #     self.assertGreater(len(works), 0)
    
    # def test_view_work(self):
    #     viewwork(1)
    #     self.assertEqual(works[0].name, 'Task A')

    
    
    # def test_edit_work(self):
    #     editwork(4)

    
#class TestWorker(unittest.TestCase):
    # def setUp(self):
    #     self.worker1 = worker('John', '1234567890', 'Programmer', 'Expert')
    #     self.worker2 = worker('Alice', '0987654321', 'Tester', 'Intermediate')
    #     self.worker3 = worker('Bob', '9876543210', 'Analyst', 'Beginner')

    #def test_add_worker(self):
       # mark_completed_work(2)


    
   # def test_display_all_workers(self):
        # workers.append(self.worker1)
        # workers.append(self.worker2)
        # workers.append(self.worker3)
       # displayallworkers()

    
   # def test_view_worker(self):
       # viewworker(1)
    
    # def test_edit_worker(self):
    #     editworker(4)

   # def assignment_to_workers(self):
       # assignment_to_workers()



    
if __name__ == '__main__':
    #unittest.main()
    win =Tk()

    # Set the geometry of Tkinter Frame
    win.geometry("1300x720")
    s=ThemedStyle()
    s.set_theme('equilux')

    # Open the Image File
    #img=Image.open("sakura.jpeg")
    #bg1=img.filter(ImageFilter.GaussianBlur(radius=20))
    bg = ImageTk.PhotoImage(file ="bg.jpg") 


    # Create a Canvas
    canvas = Canvas(win, width=1300, height=720)
    canvas.pack(fill=BOTH, expand=True)

    # Add Image inside the Canvas
    canvas.create_image(0, 0, image=bg, anchor='nw')

    home=Label(win, text='Welcome\n to the\n Work Management System')
    home.configure(fg='black',font=('Noto Sans Arabic', 25, 'bold'),bg='white',bd=3,relief=SOLID)
    #home.pack(side=TOP,expand="true",pady=50)
    
    #home.grid(row=0,column=0,columnspan=10,rowspan=6)
    enter=Button(win, text='Enter', command=partial(menu,win))
    enter.configure(bg="white",activebackground="#44d7eb",fg='black',bd=2,relief=SOLID)
    #enter.pack(side=TOP,expand="true",pady=60)
    canvas.create_window(650,300,window=home,anchor=CENTER)
    # canvas.create_text(650,300, text='Welcome\n to the \nWork Management System',
    #                    anchor=CENTER,fill='black',font=('Noto Sans Arabic', 25, 'bold'),
    #                    justify=CENTER)
    canvas.create_window(650,470,window=enter,anchor=CENTER)
    

    def resize_image(e):
        global image, resized, image2 
        # open image to resize it
        image = Image.open("bg.jpg")
       # image3=image.filter(ImageFilter.GaussianBlur(radius=7))
        # resize the image with width and height of root
        resized = image.resize((e.width, e.height), Image.ANTIALIAS)

        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')

        

    
    # Bind the function to configure the parent window
    win.bind("<Configure>", resize_image)
    
   
    
    
    #enter.grid(row=7,column=3)
    
    win.mainloop()


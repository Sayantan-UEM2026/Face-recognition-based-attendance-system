
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")


        #-----------------Variables----------------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_searchtxt=StringVar()
        self.var_search=StringVar()

        #first
        img=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\srf.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second
        img1=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\ima1.jpg") 
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #second
        img2=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\hkg.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #big image
        #second
        img3=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\moon.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        #Left L F

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\srf.jpg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=120)


        #Department
        #dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        #dep_label.grid(row=0,column=0)
        #dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly")
        #dep_combo["values"]=("Select Department","CSE","CSIT","CSE AIML","ECE","Mechanical","Other")
        #dep_combo.current(0)                      
        #dep_combo.grid(row=0,column=1,padx=2,pady=10)

        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=18)
        dep_combo["values"]=("Select Department","CSE","CSIT","CSE-IOT","CSE-AIML","ECE","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=18)
        course_combo["values"]=("Select Course","Data Structures","OOPS","Database Management Systems","Computer Networks(CN)","AIML","Operating System","Cyber Security","Cloud Computing","Deep Learning")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=18)
        year_combo["values"]=("Select Year","2021","2022","2023","2024","2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=18)
        semester_combo["values"]=("Select Semester","Semester-II","Semester-IV","Semester-VI","Semester-VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=260,width=720,height=300)
        
        #Student ID
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_id,font=("times new roman",13,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student name
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        #class_div_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_div,font=("times new roman",13,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=16)
        div_combo["values"]=("Select Division","A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)


        #roll_no
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)


        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        #gender_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_gender,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=16)
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dob,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #cal = DateEntry(class_student_frame,textvariable=self.var_dob, width=23, year=2019, month=6, day=22, 
         #background='darkblue', foreground='white', borderwidth=2)
        #cal.grid(row=2,column=3,padx=10, pady=10)
      
        # validate_date=self.root.register(self.grad_date)
        # dob_entry.config(validate='key',validatecommand=(validate_date,'%P'))


        
       #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        #email=Label(class_student_frame,text="*ex123@gmail.com",font=("times new roman",6,"bold"),fg="red",bg="white")
        # pswd.grid(row=8,column=1,padx=5,pady=5,sticky=W)
        #email.place(x=150, y=149)


        # validate_email=self.root.register(self.checkemail)
        # email_entry.config(validate='key',validatecommand=(validate_email,'%P'))




        #Phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        #validate_phone=self.root.register(self.checkphone)
        #phone_entry.config(validate='key',validatecommand=(validate_phone,'%P'))
    
   

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_address,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)



        #validate_address=self.root.register(self.checkaddress)
        #address_entry.config(validate='key',validatecommand=(validate_address,'%P'))
    

    

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #validate_Teacher=self.root.register(self.checkTeachername)
        #teacher_entry.config(validate='key',validatecommand=(validate_Teacher,'%P'))

        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
 
        #
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=6,column=1)
        
         #button frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=40)

        save_btn=Button(btn_frame,text="Save",width=17,command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        
        #frame for take photo and update photo
        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",width=35,command=self.generate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


         #Right Frame
        # Right Frame
        right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman",12,"bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        img_right=Image.open(r"C:\Users\ASUS\Desktop\FaceRecognigationSystem\CollageImage\hkg.jpg")
        img_right=img_right.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="Green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=11)
        search_combo["values"]=("Select","Roll")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
    


        search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #Table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        #scroll bar 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        
        self.fetch_data()

#============function details===================
    def add_data(self):

        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)
        else:
            #messagebox.showinfo("Sucessfull","Welcome")
            try:
                conn=mysql.connector.connect(host="......",username="....",password="........",database=".......")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.var_std_id.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
 

                
                                                                                                                ))
                

                conn.commit()
                self.fetch_data()
                conn.close()
                #speak_va('Student Details has been added successfully.')
                messagebox.showinfo("Success","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
                #speak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    
    
######======Fetch data ==============#####
    def fetch_data(self):
        # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
        conn=mysql.connector.connect(host="localhost",username="root",password="India@sayantan04",database="face_recognize")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()
#=================== get cursor ======================#
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content.get("values")

        if data and len(data) >= 14:  # Adjust number based on actual columns
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
        else:
            messagebox.showwarning("Selection Error", "Please select a valid row with complete data.")

#============= Update function =========================

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
       # if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            #speak_va('Alert!!! All fields are required.')
            messagebox.showerror("Error", "All fields Are Required",parent=self.root)

        else:
            try:
                #speak_va("Do you want to Update this Student's Details?")
                Upadate = messagebox.askyesno("Upadate","Do You Want To Update This Student Details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="India@sayantan04",database="face_recognize")
                    # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,phone=%s,Addressl=%s,Teacher=%s,Photosample=%s where Student_id=%s",(

                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                        self.var_course.get(),
                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                        self.var_std_id.get()
                                                                                                                                                                                    ))   
                
                
                else:
                    if not Upadate:
                        return
                #speak_va('Student Details updated successfully.')
                messagebox.showinfo("Success","Student Details updated Successfully.",parent=self.root)                                                                                                                                              
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:   
                #Sspeak_va('An Exception Occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def delete_data(self):
        if self.var_std_id.get()=="":
            # speak_va('Student ID is mandatory')
            messagebox.showerror("Error","Student Id Must be Required",parent=self.root)
        else:
            try:
                #speak_va("Do you want to Delete this Student's Details?")
                delete=messagebox.askyesno("Student Delete Page","Do You Want To Delete This Student Details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="India@sayantan04",database="face_recognize")
                    # conn=mysql.connector.connect(host="localhost",username="root",password="Keshav@123",database="mydata")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                #speak_va('Student Details deleted successfully.')
                messagebox.showinfo("Delete","Student Details Successfully deleted",parent=self.root)

            except Exception as es:
                #speak_va('An exception occurred!')
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    def generate_dataset(self):
    # Validate required fields
        if (self.var_dep.get() == "Select Department" or 
            not self.var_std_name.get() or 
            not self.var_std_id.get()):
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            # Database connection
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="India@sayantan04",
                database="face_recognize"
            )
            my_cursor = conn.cursor()
            student_id = self.var_std_id.get()

            # Check if student exists
            my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=%s", (student_id,))
            if not my_cursor.fetchone():
                my_cursor.execute("""INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                                (student_id, self.var_dep.get(), self.var_course.get(),
                                self.var_year.get(), self.var_semester.get(),
                                self.var_std_name.get(), self.var_div.get(),
                                self.var_roll.get(), self.var_gender.get(),
                                self.var_dob.get(), self.var_email.get(),
                                self.var_phone.get(), self.var_address.get(),
                                self.var_teacher.get(), self.var_radio1.get()))
            else:
                my_cursor.execute("""UPDATE student SET 
                                Dep=%s, course=%s, Year=%s, Semester=%s,
                                Name=%s, Division=%s, Roll=%s, Gender=%s,
                                Dob=%s, Email=%s, phone=%s, Addressl=%s,
                                Teacher=%s, Photosample=%s
                                WHERE Student_id=%s""",
                                (self.var_dep.get(), self.var_course.get(),
                                self.var_year.get(), self.var_semester.get(),
                                self.var_std_name.get(), self.var_div.get(),
                                self.var_roll.get(), self.var_gender.get(),
                                self.var_dob.get(), self.var_email.get(),
                                self.var_phone.get(), self.var_address.get(),
                                self.var_teacher.get(), self.var_radio1.get(),
                                student_id))

            conn.commit()
            self.fetch_data()
            conn.close()

            # Load face detection model
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

            # Initialize camera
            cap = cv2.VideoCapture(0)
            if not cap.isOpened():
                messagebox.showerror("Error", "Could not open camera", parent=self.root)
                return

            img_count = 0
            while img_count < 100:  # Capture 100 images
                ret, frame = cap.read()
                if not ret:
                    continue

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    face_img = frame[y:y+h, x:x+w]
                    face_img = cv2.resize(face_img, (450, 450))
                    face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)

                    filename = f"data/user.{student_id}.{img_count+1}.jpg"
                    cv2.imwrite(filename, face_gray)

                    cv2.putText(face_gray, f"Image: {img_count+1}", (20, 40), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                    cv2.imshow("Capturing Face Samples", face_gray)

                    img_count += 1

                if cv2.waitKey(1) == 27 or cv2.getWindowProperty("Capturing Face Samples", cv2.WND_PROP_VISIBLE) < 1:
                    break

            cap.release()
            cv2.destroyAllWindows()

            messagebox.showinfo("Success", 
                                f"Captured {img_count} images for Student ID {student_id}\n"
                                f"Saved in 'data/' folder.")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}", parent=self.root)
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()
            if 'cap' in locals() and cap.isOpened():
                cap.release()
            cv2.destroyAllWindows()


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()

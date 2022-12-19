from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import datetime
from datetime import datetime
from datetime import timedelta
import webbrowser
from functools import partial



root=tk.Tk()

root.geometry("600x600")
root.title("Library Management System")
root.configure(bg="#d6d6d6")
root.iconbitmap("C:/Users/Dell/Documents/PP")

#creating frame pages
frame1_page=Frame(root,bg="#d6d6d6")
frame2_page=Frame(root,bg="#d6d6d6")
frame3_page=Frame(root,bg="#d6d6d6")

frame1_lib=Frame(root,bg="#d6d6d6")
frame2_lib=Frame(root,bg="#d6d6d6")
frame3_lib=Frame(root,bg="#d6d6d6")
frame4_lib=Frame(root,bg="#d6d6d6")
frame5_lib=Frame(root,bg="#d6d6d6")
#--------

#creating function for showing frames
def show_frame(f):
	f.tkraise()
#------
for i in (frame1_page,frame2_page,frame3_page):
	i.grid(row=0,column=0,sticky='nsew')

for j in (frame1_lib,frame2_lib,frame3_lib,frame4_lib,frame5_lib):
	j.grid(row=0,column=0,sticky='nsew')


#calling the frame function
show_frame(frame1_page)


#frame1 begins-------
#creating function for validating password entry
special_ch=["-","&","%","#","@","~","!","`","^"]
def validation():
	password=password_entry.get()
	msg=''

	if len(password)==0:
		msg='Password can\'t be empty'
	else:
		try:
			if not any (ch in special_ch for ch in password):
				msg='Atleast 1 special character required'
			elif not any (ch.isupper() for ch in password):
				msg='Atleast 1 uppercase letter required'
			elif not any (ch.islower() for ch in password):
				msg='Atleast one lower case letter required'
			elif not any (ch.isdigit() for ch in password):
				msg='Atleast 1 number required'
			else:
				messagebox.showinfo("Success!","Login Successful!") and show_frame(frame2_page)
		except Exception as ep:
			messagebox.showerror("Error",ep)
	messagebox.showinfo("Message",msg)

def validation_1():
	password=password_entry.get()
	msg=''

	if len(password)==0:
		msg='Password can\'t be empty'
	else:
		try:
			if not any (ch in special_ch for ch in password):
				msg='Atleast 1 special character required'
			elif not any (ch.isupper() for ch in password):
				msg='Atleast 1 uppercase letter required'
			elif not any (ch.islower() for ch in password):
				msg='Atleast one lower case letter required'
			elif not any (ch.isdigit() for ch in password):
				msg='Atleast 1 number required'
			else:
				messagebox.showinfo("Success!","Login Successful!") and show_frame(frame1_lib)
		except Exception as ep:
			messagebox.showerror("Error",ep)
	messagebox.showinfo("Message",msg)


#creating sub frames
frame1_page1=Frame(frame1_page,bg="#d6d6d6")
frame1_page1.pack()
frame2_page1=Frame(frame1_page,bg="#d6d6d6")
frame2_page1.pack(pady=30)
frame3_page1=Frame(frame1_page,bg="#d6d6d6")
frame3_page1.pack(pady=30)

#adding an image
canvas=Canvas(frame1_page1,width=600,height=200)
canvas.grid(row=0,column=0)
image=Image.open("login_page.png")
resize_image=image.resize((600,200))
img=ImageTk.PhotoImage(resize_image)
canvas.create_image(20,20,anchor=NW,image=img)
#------

username_label=Label(frame2_page1,text="Username",font=("Times New Roman",15),bg="#d6d6d6")
username_label.grid(row=0,column=0,padx=10,pady=10)

username_entry=Entry(frame2_page1,width=20)
username_entry.grid(row=0,column=1,padx=10,pady=10)

password_label=Label(frame2_page1,text="Password",font=("Times New Roman",15),bg="#d6d6d6")
password_label.grid(row=1,column=0,padx=10,pady=10)


password_entry=Entry(frame2_page1,width=20)
password_entry.grid(row=1,column=1,padx=10,pady=10)


login_button=Button(frame3_page1,text="Login as Admin",bg="red",fg="white",command=validation,width=20)
login_button.grid(row=0,column=0,pady=20)

loginlib_button=Button(frame3_page1,text="Login as Librarian",bg="red",fg="white",command=validation_1,width=20)
loginlib_button.grid(row=1,column=0,pady=20)


#frame 1 ends----

#frame 1 lib begins----
def log_out():
	username_entry.delete(0,END)
	password_entry.delete(0,END)
	messagebox.showinfo("Message","You have been successfully logged out!")
	show_frame(frame1_page)

add_user_button=Button(frame1_lib,text="Add User",bg="red",fg="white",command=lambda:show_frame(frame2_lib),width=20)
add_user_button.pack(pady=20)

issue_book_button=Button(frame1_lib,text="Add Book",bg="red",fg="white",command=lambda:show_frame(frame3_lib),width=20)
issue_book_button.pack(pady=20)

book_return_button=Button(frame1_lib,text="Delete Book",bg="red",fg="white",command=lambda:show_frame(frame4_lib),width=20)
book_return_button.pack(pady=20)

logout_button=Button(frame1_lib,text="Log Out",bg="red",fg="white",command=log_out,width=20)
logout_button.pack(pady=20)


#frame 1 lib ends---

#frame 2 lib begins---
#creating functions
def add_user():
	messagebox.showinfo("User added","User has been added!")
	show_frame(frame1_lib)


#creating sub frames
frame2_lib1=Frame(frame2_lib,bg="#d6d6d6")
frame2_lib1.pack(pady=20)
frame2_lib2=Frame(frame2_lib,bg="#d6d6d6")
frame2_lib2.pack(pady=20)
#---
user_id=Label(frame2_lib1,text="User Id",font=("Times New Roman",15),bg="#d6d6d6")
user_id.grid(row=0,column=0,padx=10,pady=10)

userid_entry=Entry(frame2_lib1,width=20)
userid_entry.grid(row=0,column=1,padx=10,pady=10)

password1=Label(frame2_lib1,text="Password",font=("Times New Roman",15),bg="#d6d6d6")
password1.grid(row=1,column=0,padx=10,pady=10)


password1_entry=Entry(frame2_lib1,width=20)
password1_entry.grid(row=1,column=1,padx=10,pady=10)



name1_label=Label(frame2_lib1,text="Name",font=("Times New Roman",15),bg="#d6d6d6")
name1_label.grid(row=3,column=0,padx=10,pady=10)

name1_entry=Entry(frame2_lib1,width=20)
name1_entry.grid(row=3,column=1,padx=10,pady=10)

mobile_label=Label(frame2_lib1,text="Mobile",font=("Times New Roman",15),bg="#d6d6d6")
mobile_label.grid(row=4,column=0,padx=10,pady=10)

mobile_entry=Entry(frame2_lib1,width=20)
mobile_entry.grid(row=4,column=1,padx=10,pady=10)

branch_label=Label(frame2_lib1,text="Branch",font=("Times New Roman",15),bg="#d6d6d6")
branch_label.grid(row=5,column=0,padx=10,pady=10)

branch_list=["Mumbai","Delhi","Kolkata","Bangalore","Hyderabad"]
branch=StringVar()
branch_option=OptionMenu(frame2_lib1,branch,*branch_list)
branch_option.grid(row=5,column=1,padx=10,pady=10)
branch.set("Select Your Branch")

add_button=Button(frame2_lib2,text="Add User",bg="red",fg="white",command=add_user,width=20)
add_button.pack(pady=20)

close_button=Button(frame2_lib2,text="Close",bg="red",fg="white",command=lambda:show_frame(frame1_lib),width=20)
close_button.pack(pady=20)


#frame 2 lib ends---

#frame 3 lib begins--
#creating functions
def issue_book():
	messagebox.showinfo("Message","Book has been added!")
	show_frame(frame1_lib)

frame3_lib1=Frame(frame3_lib,bg="#d6d6d6")
frame3_lib1.pack(pady=20)
frame3_lib2=Frame(frame3_lib,bg="#d6d6d6")
frame3_lib2.pack(pady=20)

user_id1=Label(frame3_lib1,text="User Id",font=("Times New Roman",15),bg="#d6d6d6")
user_id1.grid(row=0,column=0,padx=10,pady=10)

userid1_entry=Entry(frame3_lib1,width=20)
userid1_entry.grid(row=0,column=1,padx=10,pady=10)

isbn_label=Label(frame3_lib1,text="ISBN Number",font=("Times New Roman",15),bg="#d6d6d6")
isbn_label.grid(row=1,column=0,padx=10,pady=10)

isbn_entry=Entry(frame3_lib1,width=20)
isbn_entry.grid(row=1,column=1,padx=10,pady=10)

book_label=Label(frame3_lib1,text="Book Name",font=("Times New Roman",15),bg="#d6d6d6")
book_label.grid(row=2,column=0,padx=10,pady=10)

bookname_entry=Entry(frame3_lib1,width=20)
bookname_entry.grid(row=2,column=1,padx=10,pady=10)

author_label=Label(frame3_lib1,text="Author",font=("Times New Roman",15),bg="#d6d6d6")
author_label.grid(row=3,column=0,padx=10,pady=10)

author_entry=Entry(frame3_lib1,width=20)
author_entry.grid(row=3,column=1,padx=10,pady=10)

language_label=Label(frame3_lib1,text="Language",font=("Times New Roman",15),bg="#d6d6d6")
language_label.grid(row=4,column=0,padx=10,pady=10)

language_list=["English","Hindi","Gujarati","French","Spanish"]
language=StringVar()
language_option=OptionMenu(frame3_lib1,language,*language_list)
language_option.grid(row=4,column=1,padx=10,pady=10)
language.set("Select a Language")



dateissue1_label=Label(frame3_lib1,text="Date of Issue:",bg="#d6d6d6",font=("Times New Roman",15))
dateissue1_label.grid(row=5,column=0,padx=10,pady=10)
doi1=tk.StringVar()
cal_doi1=DateEntry(frame3_lib1,selectmode='day',textvariable=doi1)
cal_doi1.grid(row=5,column=1,padx=10,pady=10)

issue_button=Button(frame3_lib2,text="Add Book",bg="red",fg="white",command=issue_book,width=20)
issue_button.pack(pady=20)

close_button=Button(frame3_lib2,text="Close",bg="red",fg="white",command=lambda:show_frame(frame1_lib),width=20)
close_button.pack(pady=20)


#frame 3 lib ends---

#frame 4 lib begins----
#creating function
def remove_book():
	messagebox.showinfo("Message","Book has been removed!")
	show_frame(frame1_lib)
#creating sub frames
frame4_lib1=Frame(frame4_lib,bg="#d6d6d6")
frame4_lib1.pack(pady=20)
frame4_lib2=Frame(frame4_lib,bg="#d6d6d6")
frame4_lib2.pack(pady=20)

user_id2=Label(frame4_lib1,text="User Id",font=("Times New Roman",15),bg="#d6d6d6")
user_id2.grid(row=0,column=0,padx=10,pady=10)

userid2_entry=Entry(frame4_lib1,width=20)
userid2_entry.grid(row=0,column=1,padx=10,pady=10)

book1_label=Label(frame4_lib1,text="Book Name",font=("Times New Roman",15),bg="#d6d6d6")
book1_label.grid(row=1,column=0,padx=10,pady=10)

bookname1_entry=Entry(frame4_lib1,width=20)
bookname1_entry.grid(row=1,column=1,padx=10,pady=10)

remove_button=Button(frame4_lib2,text="Remove",bg="red",fg="white",command=remove_book,width=20)
remove_button.pack(pady=20)

close1_button=Button(frame4_lib2,text="Close",bg="red",fg="white",command=lambda:show_frame(frame1_lib),width=20)
close1_button.pack(pady=20)

#frame 4 lib ends---


#frame 2 page begins-----
#creating subframes
frame1_page2=Frame(frame2_page,bg="#d6d6d6")
frame1_page2.pack(pady=30)
frame2_page2=Frame(frame2_page,bg="#d6d6d6")
frame2_page2.pack(pady=30)
frame3_page2=Frame(frame2_page,bg="#d6d6d6")
frame3_page2.pack(pady=30)

#creating function---
def final_display():
	day=int(no_entry.get())
	if day>15:
		t_c=1000+((day-15)*10)
	else:
		t_c=1000
	total_var.set(t_c)
	final_variable=book_option.get()+" "+"has been issued for"+" "+name_entry.get()+" "+"from"+" "+doi.get()+" "+"for"+" "+no_entry.get()+" "+"days"

	file=open("library.txt","w")
	file.write(final_variable)
	file.close()

	

	





#function for displaying receipt in frame 3
def gen_rec():
	display_file=open("library.txt","r")
	file_var.set(display_file.read())
	display_file.close()

#function ends---
#adding image

canvas1=Canvas(frame1_page2,width=600,height=100)
canvas1.grid(row=0,column=0)
image1=Image.open("welcome.png")
resize_image1=image1.resize((600,100))
img1=ImageTk.PhotoImage(resize_image1)
canvas1.create_image(20,20,anchor=NW,image=img1)


name_label=Label(frame2_page2,text="Name",font=("Times New Roman",15),bg="#d6d6d6")
name_label.grid(row=0,column=0,padx=10,pady=10)

name_entry=Entry(frame2_page2,width=20)
name_entry.grid(row=0,column=1,padx=10,pady=10)

email_label=Label(frame2_page2,text="Email",font=("Times New Roman",15),bg="#d6d6d6")
email_label.grid(row=1,column=0,padx=10,pady=10)

email_entry=Entry(frame2_page2,width=20)
email_entry.grid(row=1,column=1,padx=10,pady=10)

genre_label=Label(frame2_page2,text="Genre",bg="#d6d6d6",font=("Times New Roman",15))
genre_label.grid(row=2,column=0,padx=10,pady=10)

genre_list=["Sci-Fi","Comedy","Thriller","Mystery"]

def select_book(e):
	if genre_option.get()=="Sci-Fi":
		book_option.config(value=sci_list)
	elif genre_option.get()=="Comedy":
		book_option.config(value=comedy_list)
	elif genre_option.get()=="Thriller":
		book_option.config(value=thriller_list)
	else:
		book_option.config(value=mystery_list)


genre_option=ttk.Combobox(frame2_page2,value=genre_list)
genre_option.grid(row=2,column=1,padx=10,pady=10)


sci_list=["The War of Worlds","RingWorld","Stranger in a Strange Land","Anathem"]
comedy_list=["Catch-22","Cold Comfort Farm","So Long","One Day at a Time"]
thriller_list=["The Rebecca","You","In Cold Blood","Mrs De Winter","The Firm"]
mystery_list=["Gone Girl","The Postman","Woman in White","Anatomy of a Murder"]

books_label=Label(frame2_page2,text="Select a Book",bg="#d6d6d6",font=("Times New Roman",15))
books_label.grid(row=3,column=0,padx=10,pady=10)
books=StringVar()


#bind combo box
genre_option.bind("<<ComboboxSelected>>",select_book)

book_option=ttk.Combobox(frame2_page2,value=[""])
book_option.grid(row=3,column=1,padx=10,pady=10)

dateissue_label=Label(frame2_page2,text="Date of Issue:",bg="#d6d6d6",font=("Times New Roman",15))
dateissue_label.grid(row=4,column=0,padx=10,pady=10)

def my_upd(*arg):
	label_doi.config(text=doi.get())
	
	

doi=tk.StringVar()
cal_doi=DateEntry(frame2_page2,selectmode='day',textvariable=doi)
cal_doi.grid(row=4,column=1,padx=10,pady=10)

label_doi=tk.Label(frame2_page2,bg="#d6d6d6")
label_doi.grid(row=5,column=2)

doi.trace('w',my_upd)


no_of_days=Label(frame2_page2,text="No of Days",bg="#d6d6d6",font=("Times New Roman",15))
no_of_days.grid(row=5,column=0,padx=10,pady=10)

no_entry=Entry(frame2_page2,width=20)
no_entry.grid(row=5,column=1,padx=10,pady=10)


total_var=IntVar()
total_cost=Label(frame2_page2,text="Total Cost:",bg="#d6d6d6",font=("Times New Roman",15))
total_cost.grid(row=6,column=0,padx=10,pady=10)

total_display=Label(frame2_page2,textvariable=total_var,bg="#d6d6d6",font=("Times New Roman",15))
total_display.grid(row=6,column=1,padx=10,pady=10)

show_cost=Button(frame2_page2,text="Show Cost",bg="red",fg="white",width=20,command=final_display)
show_cost.grid(row=8,column=1,padx=10,pady=10)

generate_button=Button(frame2_page2,text="Generate Receipt",bg="red",fg="white",width=20,command=lambda:(show_frame(frame3_page),gen_rec()))
generate_button.grid(row=8,column=2,padx=10,pady=10)


previous_page=Button(frame2_page2,text="Previous Page",bg="red",fg="white",width=20,command=lambda:show_frame(frame1_page))
previous_page.grid(row=8,column=0,padx=10,pady=10)
#frame 2 ends-----

# creating menus----
menu_widget=Menu(frame2_page)

#defining menu functions
def open_new():
	name_entry.delete(0,END)
	genre_option.delete(0,END)
	book_option.delete(0,END)
	cal_doi.delete(0,END)
	no_entry.delete(0,END)
	total_var.delete(0,END)

def save_menu():

	messagebox.showinfo("Saved","Your details have now been saved in a text file")
	file_variable=book_option.get()+" "+"has been issued for"+" "+name_entry.get()+" "+"from"+" "+doi.get()+" "+"for"+" "+no_entry.get()+" "+"days"

	file_open=open("library.txt","w")
	file_open.write(file_variable)
	file_open.close()

def print_menu():
	messagebox.showwarning("Printer Connected","Your details will now be printed")

def info_menu():
	messagebox.showwarning("Warning","You'll be redirected to another website")
	webbrowser.open_new("https://google.com")





file_menu=Menu(menu_widget)
file_menu.add_command(label="Open New",command=open_new)
file_menu.add_command(label="Save",command=save_menu)
file_menu.add_command(label="Print",command=print_menu)
file_menu.add_command(label="Exit Window",command=root.destroy)
menu_widget.add_cascade(label="File",menu=file_menu)

help_menu=Menu(menu_widget)
help_menu.add_command(label="Info",command=info_menu)
menu_widget.add_cascade(label="Help",menu=help_menu)


root.config(menu=menu_widget)
#menus end----

#frame 3 begins-----
#creating sub frames
frame1_page3=Frame(frame3_page,bg="#d6d6d6")
frame1_page3.pack(pady=20)
frame2_page3=Frame(frame3_page,bg="#d6d6d6")
frame2_page3.pack(pady=20)
frame3_page3=Frame(frame3_page,bg="#d6d6d6")
frame3_page3.pack(pady=20)
frame4_page3=Frame(frame3_page,bg="#d6d6d6")
frame4_page3.pack(pady=20)

#inserting image
canvas2=Canvas(frame1_page3,width=600,height=100)
canvas2.grid(row=0,column=0)
image2=Image.open("invoice.png")
resize_image2=image2.resize((600,100))
img2=ImageTk.PhotoImage(resize_image2)
canvas2.create_image(20,20,anchor=NW,image=img2)

'''
username_display=Label(frame2_page3,text="Username",bg="#d6d6d6",font=("Times New Roman",15))
username_display.grid(row=0,column=1,padx=5,pady=5)

name_display=Label(frame2_page3,text="Name",bg="#d6d6d6",font=("Times New Roman",15))
name_display.grid(row=0,column=1,padx=5,pady=5)

book_name=Label(frame2_page3,text="Book Name",bg="#d6d6d6",font=("Times New Roman",15))
book_name.grid(row=0,column=2,padx=5,pady=5)

date_of_issue=Label(frame2_page3,text="Date of Issue",bg="#d6d6d6",font=("Times New Roman",15))
date_of_issue.grid(row=0,column=3,padx=5,pady=5)

date_of_return=Label(frame2_page3,text="Date of Return",bg="#d6d6d6",font=("Times New Roman",15))
date_of_return.grid(row=0,column=4,padx=5,pady=5)

totalcost_display=Label(frame2_page3,text="Total Cost",bg="#d6d6d6",font=("Times New Roman",15))
totalcost_display.grid(row=0,column=5,padx=5,pady=5)

username_var=StringVar()
u_display=Label(frame2_page3,textvariable=username_var,bg="#d6d6d6",font=("Times New Roman",12))
u_display.grid(row=1,column=0,padx=5,pady=5)

name_var=StringVar()
n_display=Label(frame2_page3,textvariable=name_var,bg="#d6d6d6",font=("Times New Roman",12))
n_display.grid(row=1,column=1,padx=5,pady=5)

book_var=StringVar()
book_display=Label(frame2_page3,textvariable=book_var,bg="#d6d6d6",font=("Times New Roman",12))
book_display.grid(row=1,column=2,padx=5,pady=5)

doi_var=StringVar()
doi_display=Label(frame2_page3,textvariable=doi_var,bg="#d6d6d6",font=("Times New Roman",12))
doi_display.grid(row=1,column=3,padx=5,pady=5)

dor_var=StringVar()
dor_display=Label(frame2_page3,textvariable=dor_var,bg="#d6d6d6",font=("Times New Roman",12))
dor_display.grid(row=1,column=4,padx=5,pady=5)

cost_var=StringVar()
cost_display=Label(frame2_page3,textvariable=cost_var,bg="#d6d6d6",font=("Times New Roman",12))
cost_display.grid(row=1,column=5,padx=5,pady=5)
'''

file_var=StringVar()
file_display=Label(frame3_page3,textvariable=file_var,font=("Times New Roman",15),bg="#d6d6d6")
file_display.pack()

generate_button=Button(frame4_page3,text="Logout",bg="red",fg="white",width=20,command=log_out)
generate_button.grid(row=8,column=2,padx=10,pady=10)




#frame 3 ends-----



#running the app
root.mainloop()



#C:\Users\Dell\Documents\PP
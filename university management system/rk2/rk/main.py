from ast import If, Pass
from  tkinter import *
from  tkinter import ttk
from  views import *
from tkinter import messagebox
import os
import hashlib
import pandas as pd
 
os.chdir(r'''C:\Users\kaush\OneDrive\Desktop\fsss finale\rk2\rk''')
co0="#D2B48C"
co2="#8B5A2B"

window = Tk()
window.title("")
window.geometry('1050x600')
window.configure(background=co0)
window.resizable(width=FALSE,height=False)



frame_up=Frame(window,width=1500,height=80,bg=co2)
frame_up.grid(row=0,column=0,padx=0,pady=1)

frame_down=Frame(window,width=1300,height=250,bg=co0)
frame_down.grid(row=1,column=0,padx=0,pady=1)

frame_table=Frame(window,width=3000,height=700,bg=co0)
frame_table.grid(row=2,column=0,columnspan=2,padx=0,pady=1,sticky=NW)


def show():
    global tree

    listheader = ['NAME', 'BRANCH', 'SEM','USN','ADHAR NUMBER']

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    #tree head
    tree.heading(0, text=' NAME', anchor=NW)
    tree.heading(1, text=' BRANCH', anchor=NW)
    tree.heading(2, text='SEM', anchor=NW)
    tree.heading(3, text='USN', anchor=NW)
    tree.heading(4, text='ADHAR CARD NUMBER', anchor=NW)
    # tree  columns
    tree.column(0, width=200, anchor='nw')
    tree.column(1, width=200, anchor='nw')
    tree.column(2, width=200, anchor='nw')
    tree.column(3, width=200, anchor='nw')

    tree.column(4,width=200,anchor='nw')

    for item in demo_list:
        tree.insert('','end',values=item)

show()

def insert():
    NAME = e_NAME.get()
    BRANCH= e_BRANCH.get()
    SEM= e_SEM.get()
    USN= e_USN.get()
    PASS=hashlib.sha256(str.encode( e_PASS.get())).hexdigest()
    DOL="$"
    data = [NAME, BRANCH, SEM,USN,str(PASS),DOL]

    if NAME == '' or BRANCH== '' or SEM == '' or USN == '' or PASS=='':
        messagebox.showwarning('data', 'Please fill in all fields')
    
    else:
        add(data)
        messagebox.showinfo('data', 'data added successfully')

        e_NAME.delete(0, 'end')
        e_BRANCH.delete(0, 'end')
        e_SEM.delete(0, 'end')
        e_USN.delete(0, 'end')
        e_PASS.delete(0,'end')

        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
      

        NAME = str(tree_list[0])
        BRANCH = str(tree_list[1])
        SEM = str(tree_list[2])
        USN = str(tree_list[3])
        PASS=str(tree_list[4])
        e_NAME.insert(0, NAME)
        e_BRANCH.insert(0, BRANCH)
        e_SEM.insert(0, SEM)
        e_USN.insert(0, USN)
        e_PASS.insert(0,PASS)

        def confirm():
            new_NAME = e_NAME.get()
            new_BRANCH = e_BRANCH.get()
            new_SEM = e_SEM.get()
            new_USN = e_USN.get()
            new_PASS=e_PASS.get()
            data = [new_USN, new_NAME, new_BRANCH, new_SEM,new_USN,new_PASS]

            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_NAME.delete(0, 'end')
            e_BRANCH.delete(0, 'end')
            e_SEM.delete(0, 'end')
            e_USN.delete(0, 'end')
            e_PASS.delete(0,'end')
            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()

            show()
            
        b_confirm =  Button(frame_down, text="Confirm", width=10, height=1, bg=co2, fg = co0, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x = 290, y = 110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table to update')
       
def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_USN = str(tree_list[3])

        remove(tree_USN)

        messagebox.showinfo('Success', 'Data has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()
        show()

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table to delete')



def to_search():
    USN= e_search.get()

    data = search(USN)
    messagebox.showinfo('Sucess', 'Data  Found')

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)
        
    e_search.delete(0, 'end')
    


  
#frame_up widgets

app_name=Label(frame_up,text="UNIVERSITY MANAGEMENT SYSTEM",height=1,font=('Verdana 17 bold'),bg=co2,fg=co0)
app_name.place(x=5,y=5)

#frame down widgets
l_NAME=Label(frame_down,text="NAME *",width=40,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_NAME.place(x=10,y=20)
e_NAME=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_NAME.place(x=80,y=20)

l_BRANCH=Label(frame_down,text="BRANCH *",width=40,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_BRANCH.place(x=10,y=50)
e_BRANCH=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_BRANCH.place(x=80,y=50)

l_SEM=Label(frame_down,text="SEM *",width=40,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_SEM.place(x=10,y=80)
e_SEM=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_SEM.place(x=80,y=80)

l_USN=Label(frame_down,text="USN *",width=40,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_USN.place(x=10,y=110)
e_USN=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_USN.place(x=80,y=110)

l_PASS=Label(frame_down,text="ADHAR NO*",width=50,height=1,font=('Ivy 10'),bg=co0,anchor=NW)
l_PASS.place(x=5,y=140)
e_PASS=Entry(frame_down,width=25,justify='left',highlightthickness=1,relief="solid")
e_PASS.place(x=80,y=140)

b_search=Button(frame_down,text="Search",height=1,bg=co2,fg=co0,font=('Ivy 8 bold'),command=to_search)
b_search.place(x=290,y=20)
e_search=Entry(frame_down,width=40,justify='left',font=('Ivy',11),highlightthickness=1,relief="solid")
e_search.place(x=347,y=20)

b_view = Button(frame_down, text="View", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'))
b_view.place(x=290, y=50)

b_add = Button(frame_down, text="Add", width=40, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'),command=insert)
b_add.place(x=400, y=50)

b_update = Button(frame_down, text="Update", width=40, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'),command=to_update)
b_update.place(x=400, y=80)

b_delete = Button(frame_down, text="Delete", width=40, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'),command=to_remove)
b_delete.place(x=400, y=110)




window.mainloop()
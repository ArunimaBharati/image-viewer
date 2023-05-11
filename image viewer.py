from tkinter import*

root=Tk()
root.title="IMAGE VIEWER"
root.geometry("500x500")
root.config(bg="black")

button_open=Button(root,text="OPEN IMAGE",bg="lightpink")
button_open.place(relx=0.5,rely=0.2,anchor=CENTER)

label_image=Label(root,bg="lightpink",highlightthickness=5,borderwidth=2,relief=RAISED)
label_image.place(relx=0.5,rely=0.5,anchor=CENTER)

button_open=Button(root,text="OPEN IMAGE",bg="lightpink")
button_open.place(relx=0.5,rely=0.7,anchor=CENTER)

label_credits=Label(root,text="Created by Arunima Bharati")
label_credits.place(relx=0.5,rely=0.85,anchor=CENTER)

root.mainloop()
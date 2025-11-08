from tkinter import *


# ---------------PASSWORD GENERATOR -------------#
# ------------------SAVE PASSWORD------------------#
#---------------------UI SETUP --------------------#
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx = 10,pady = 10,bg="black")
canvas = Canvas(width=1000,height=1000,bg="black")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(500,400,image=logo_img)
canvas.pack()



window.mainloop()
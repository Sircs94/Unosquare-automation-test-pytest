from tkinter import *
root = Tk()
root.title("Angelica ")
root.resizable(1,1)
root.iconbitmap("Kanna_Anime.ico")
root.config(width=400, height=300)
miFrame = Frame(root)
miFrame.pack(side=BOTTOM)
miFrame.config(width=100,height=100)
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")

miFrame = Frame(root)
miFrame.pack(side=TOP)
miFrame.config(width=100,height=100)
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")

miFrame = Frame(root)
miFrame.pack(side=LEFT)
miFrame.config(width=100,height=100)
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")

miFrame = Frame(root)
miFrame.pack(side=RIGHT)
miFrame.config(width=100,height=100)
miFrame.config(cursor="pirate")
miFrame.config(bg="red")
miFrame.config(bd="20")
miFrame.config(relief="ridge")

root.config(cursor="boat")
root.config(bg="blue")
root.config(bd="65")
root.config(relief="sunken")




root.mainloop()
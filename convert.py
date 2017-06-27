from tkinter import *
root = Tk()
root.title('Перенос проекта')
root.geometry('800x600')
path = Label(root, text='Путь: ')
path.place(x = 20, y = 30, width=120, height=25)
msg = Message(root, bg = 'white', fg='black',width=600)
msg.place(x = 10, y = 80, width=780, height=400)
root.mainloop()
from tkinter import *
def choiceDir():
	print('0')
def startConvert():
	print('1')

root = Tk()
root.title('Перенос проекта')
root.geometry('800x600')
root.configure(background='gray93')
path = Label(root, text='Путь: ', bg = 'gray93')
path.place(x = 20, y = 30, width=120, height=25)
msg = Message(root, bg = 'white', fg='black',width=600)
msg.place(x = 10, y = 80, width=780, height=400)
butChoiceDir = Button(root,text ='Выбрать папку', command = choiceDir)
butChoiceDir.place(x = 295, y = 500, width=100, height=25)
butStartConvert = Button(root,text ='Начать перенос', command = startConvert)
butStartConvert.place(x = 405, y = 500, width=100, height=25)
root.mainloop()
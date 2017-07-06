from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import os
from datetime import datetime
import shutil
pathDir=''
def choiceDir():
        global pathDir
        pathDir = askdirectory()        
        pathLabel['text'] = 'Путь: ' +  pathDir
        if fileList.size() > 0:
                fileList.delete(0,END)
        files = os.listdir(pathDir)
        cpp = filter(lambda x: x.endswith('.cpp'), files)
        print(cpp)
        for file in cpp:
                fileList.insert(END,file)
        
        return pathDir

def startConvert():
        backUpDir = pathDir +"/BackUp/" + datetime.strftime(datetime.now(),"%Y.%m.%d")
        if not os.path.exists(backUpDir):
                os.makedirs(backUpDir)
                if fileList.size() > 0:
                        items = fileList.get(0,END)
                for item in items:
                        copyFrom = pathDir + "/" + item
                        copyTo = backUpDir + "/" + item
                        shutil.copy(copyFrom,copyTo)
        else:
                messagebox.showerror("Ошибка!!!","Существует другая резервная копия!")
                

root = Tk()
root.title('Перенос проекта')
root.geometry('800x600')
root.configure(background='gray93')

pathLabel = Label(root,anchor=W, text='Путь: ', bg = 'gray93')
pathLabel.place(x = 20, y = 30, width=400, height=25)

fileList = Listbox(root, bg = 'white', fg='black',width=600)
fileList.place(x = 10, y = 80, width=780, height=400)

butChoiceDir = Button(root,text ='Выбрать папку', command = choiceDir)
butChoiceDir.place(x = 295, y = 500, width=100, height=25)

butStartConvert = Button(root,text ='Начать перенос', command = startConvert)
butStartConvert.place(x = 405, y = 500, width=100, height=25)

root.mainloop()

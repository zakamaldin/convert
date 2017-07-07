from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import os
from datetime import datetime
import shutil
import re
pathDir=''
regex = r'Application->MessageBox[AW]?\("(.+)","(.+)",MB_OK\);'
subst = r'Application->MessageBox(L"\1",L"\2",MB_OK);'
def choiceDir():
        global pathDir
        pathDir = askdirectory()        
        pathLabel['text'] = 'Путь: ' +  pathDir
        if fileList.size() > 0:
                fileList.delete(0,END)
        files = os.listdir(pathDir)
        cpp = filter(lambda x: x.endswith('.cpp'), files)
        for file in cpp:
                fileList.insert(END,file)
        
        return pathDir

def startConvert():
        backUpDir = pathDir +"/BackUp/" + datetime.strftime(datetime.now(),"%Y.%m.%d")
        if not os.path.exists(backUpDir):
                os.makedirs(backUpDir)
                if fileList.size() > 0:
                        items = fileList.get(0,END)
                for index, item in enumerate(items):
                        statusLabel['text'] = 'Копирование: ' +  item
                        copyFrom = pathDir + "/" + item
                        copyTo = backUpDir + "/" + item
                        shutil.copy(copyFrom,copyTo)
                        currFile = open(copyFrom,"r")
                        currLine = currFile.read()
                        currFile.close()
                        print(currLine)
                        print("\n\n\n")                               
                        result = re.sub(regex,subst, currLine,0)
                        print(result)
                        currFile = open(copyFrom,"w")
                        currFile.write(result)
                        currFile.close()
                        fileList.itemconfig(index,fg="green")
                messagebox.showinfo("Успех!!!","Перенос успешно завершен!")
        else:
                messagebox.showerror("Ошибка!!!","Существует другая резервная копия!")
                

root = Tk()
root.title('Перенос проекта')
root.geometry('450x600')
root.configure(background='gray93')
root.resizable(width = False, height = False)

pathLabel = Label(root, anchor = W, text = 'Путь: ', bg = 'gray93')
pathLabel.place(x = 20, y = 30, width = 400, height = 25)
statusLabel = Label(root,text ='', bg = 'gray93')
statusLabel.place(x = 20, y = 550, width=400, height=25)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

fileList = Listbox(root, yscrollcommand = scrollbar.set, bg = 'white', fg = 'black',width = 600)
fileList.place(x = 10, y = 80, width = 415, height = 400)

scrollbar.config(command = fileList.yview)

butChoiceDir = Button(root,text ='Выбрать папку', command = choiceDir)
butChoiceDir.place(x = 120, y = 500, width=100, height=25)

butStartConvert = Button(root,text ='Начать перенос', command = startConvert)
butStartConvert.place(x = 230, y = 500, width=100, height=25)

root.mainloop()

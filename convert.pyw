from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
import os
from datetime import datetime
import shutil
import re
include = ('.cpp','.h')
exclude = ('pngdib.h','ddraw.h','fft.h','png.h','pngconf.h','Rtapi.h','zconf.h','zlib.h')
pathDir=''
regex = [ r'Application->MessageBox[AW]?\("(.+)",[\s]?"(.+)",[\s]?(.+)\);',
          r'WINAPI WinMain\(HINSTANCE, HINSTANCE, LPSTR, int\)',
          r'(swap\(.+\));',
          r'<algorith\.h>',
          r'([C|c]hart\.h)',
          r'([S|s]eries\.h)',
          r'([T|t]eengine\.h)',
          r'([T|t]ee[P|p]rocs\.h)',
          r'vcl\\registry\.hpp',
          r'fopen\(([^"].+),[\s]*(.+)\);',
          r'fopen\((".+"),[\s]*(.+)\);',
          r'sprintf\((.+),[\s]*(".+"),(.+)\);',
          r'strcat\((.+),([\s]*".+")\);',
          r'char (file_name)',
          r'LPCSTR',
          r'char szBitmap\[\] = "ALL";',
          r'OutputDebugString\((.+)\);'
          r'_lopen\(szBitmap,',
          r'char buffer[1];',
          r'#include <Psock\.hpp>',
          r'TPowersock \*Powersock1;'
        ]
substr = [
          r'Application->MessageBox(L"\1",L"\2",\3);',
          r'WINAPI wWinMain(HINSTANCE, HINSTANCE, LPWSTR, int)',
          r'std::\1;',
          r'<utility>',
          r'VCLTee.\1',
          r'VCLTee.\1',
          r'VCLTee.\1',
          r'VCLTee.\1',
          r'registry.hpp',
          r'_wfopen(\1,L\2);',
          r'_wfopen(L\1,L\2);',
          r'wsprintf(\1,L\2,\3);',
          r'wcscat(\1,L\2);',
          r'wchar_t \1',
          r'LPCWSTR',
          r'wchar_t szBitmap[] = L"ALL";',
          r'OutputDebugString(L\1);',
          r'_lopen((LPCSTR)szBitmap',
          r'wchar_t buffer[1];',
          r'',
          r''
         ]

def choiceDir():
        global pathDir
        pathDir = askdirectory()        
        pathLabel['text'] = 'Путь: ' +  pathDir
        if fileList.size() > 0:
                fileList.delete(0,END)
        files = os.listdir(pathDir)
        cpp = filter(lambda x: x.endswith(include) and not x.endswith(exclude), files)
        for file in cpp:
                fileList.insert(END,file) 

def startConvert():
        backUpDir = pathDir +"/BackUp/" + datetime.strftime(datetime.now(),"%Y.%m.%d")
        if not os.path.exists(backUpDir):
                os.makedirs(backUpDir)
                copyFrom = ""
                copyTo = ""
                if fileList.size() > 0:
                        items = fileList.get(0,END)
                for index, item in enumerate(items):
                        copyFrom = pathDir + "/" + item
                        copyTo = backUpDir + "/" + item
                        shutil.copy(copyFrom,copyTo)
                        currFile = open(copyFrom,"r")
                        result   = currFile.read()
                        currFile.close()
                        for rg,subst in zip(regex, substr):
                                result = re.sub(rg,subst, result,0)
                        if result:
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

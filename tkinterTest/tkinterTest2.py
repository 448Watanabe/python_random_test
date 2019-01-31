#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkMessageBox


root = Tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")


#
# チェックボックスのチェック状況を取得する
#
def check(event):
    global Val1
    global Val2
    global Val3

    text = ""

    if Val1.get() == True:
        text += "項目1はチェックされています\n"
    else:
        text += "項目1はチェックされていません\n"

    if Val2.get() == True:
        text += "項目2はチェックされています\n"
    else:
        text += "項目2はチェックされていません\n"

    if Val3.get() == True:
        text += "項目3はチェックされています\n"
    else:
        text += "項目3はチェックされていません\n"

    tkMessageBox.showinfo('info',text)


#
# チェックボックスの各項目の初期値
#
Val1 = Tkinter.BooleanVar()
Val2 = Tkinter.BooleanVar()
Val3 = Tkinter.BooleanVar()

Val1.set(False)
Val2.set(True)
Val3.set(False)

CheckBox1 = Tkinter.Checkbutton(text=u"項目1", variable=Val1)
CheckBox1.pack()

CheckBox2 = Tkinter.Checkbutton(text=u"項目2", variable=Val2)
CheckBox2.pack()

CheckBox3 = Tkinter.Checkbutton(text=u"項目3", variable=Val3)
CheckBox3.pack()


button1 = Tkinter.Button(root, text=u'チェックの取得',width=30)
button1.bind("<Button-1>",check)
button1.pack()

root.mainloop()
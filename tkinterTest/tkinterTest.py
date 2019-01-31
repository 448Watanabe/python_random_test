# coding: utf-8

from tkinter import *

"""
参照)
http://www.narinarissu.net/entry/20170903/1504443427
"""

def timer():
   time = int(buff.get())
   if time > 0:
       frame.after(1000, timer)
       time -= 1
       buff.set(str(time))

# フレームの初期化
frame = Tk()

# カウントダウンする時間を設定
buff = StringVar()
buff.set('10')


# 文字列を表示するエントリーを表示
entry  = Entry(frame, textvariable = buff)
# 表示する場所を指定
entry.pack(side='left')

# スタートボタンを作成
button = Button(frame, text = 'START', command = timer)
# 表示する場所を指定
button.pack(side='right')

frame.mainloop()
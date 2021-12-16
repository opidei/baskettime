import time
import tkinter
import tkinter.messagebox
from pynput import keyboard
from tkinter import *
# from PyQt5.QtWidgets import QApplication, QWidget
import ctypes

root = Tk()


def submit(tinker):
    host_name=host_input.get()
    guest_name=guest_input.get()
    if host_name=='' or guest_name=='':
        okqqq()
        return
    host_input.grid_forget()
    guest_input.grid_forget()
    host_label.grid_forget()
    guest_label.grid_forget()
    submit.grid_forget()
    create_match(host_name,)

def create_match(host_name,guest_name):
    host_name

def okqqq():
    # 弹出对话框
    result = tkinter.messagebox.askokcancel(title='提示框', message='请填写比赛队队名！')
    print(result)


root.title('篮球赛计时软件')
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
w=screenwidth
h=screenheight
x=0
y=0
host_label=Label(root,text="主队名称：")
host_label.grid(row=0)
host_input=Entry(root)
host_input.grid(row=0,column=1)
guest_label=Label(root,text="客队名称：")
guest_label.grid(row=1)
guest_input=Entry(root)
guest_input.grid(row=1,column=1)
submit = Button(root, text=u"确定", command=submit)
submit.grid(row=2)
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
root.configure(bg='black')
root.overrideredirect(True)
# root.attributes('-topmost', True)

root.mainloop()

quarte = 1
q_time = 10
b_time = 240
second = 0
trans = True

def resize():
    pass

def reset():
    global q_time
    global b_time
    pass

#
# def start():
#     global quarte,q_time,b_time,trans,second
#     print('10:00')
#     while q_time >= 0 and b_time > 0 and quarte < 5:
#         if not trans:
#             print(trans)
#             time.sleep(1)
#             second -= 1
#             if second < 0:
#                 second = 59
#                 q_time -= 1
#             if q_time>=0:
#                 if second < 10:
#                     out = f'0{q_time}:0{second}'
#                 else:
#                     out = f'0{q_time}:{second}'
#                 print(out)
#             else:
#                 if q_time < 0 and quarte <= 1:
#                     quarte += 1
#                     player = ctypes.windll.kernel32
#                     player.Beep(2000, 3000)
#                     print(quarte)
#                 if quarte > 2:
#                     player = ctypes.windll.kernel32
#                     player.Beep(1000, 5000)
#
#
# def pause():
#     global trans
#     trans=True
#     print(trans)


print('10:00')


def start():
    while 1:
        with keyboard.Events() as events:
            if not trans and q_time >= 0 and b_time > 0 and quarte < 5:

                time.sleep(0.8)
                second -= 1
                if second < 0:
                    second = 59
                    q_time -= 1
                if q_time >= 0:
                    if second < 10:
                        out = f'0{q_time}:0{second}'
                    else:
                        out = f'0{q_time}:{second}'
                    print(out)
                else:
                    if q_time < 0 and quarte <= 1:
                        quarte += 1
                        player = ctypes.windll.kernel32
                        player.Beep(2000, 3000)
                        print(quarte)
                    if quarte > 2:
                        player = ctypes.windll.kernel32
                        player.Beep(1000, 5000)
            event = events.get(1.0)
            if event is None:
                pass
            else:
                if event.key==keyboard.Key.f1:
                    trans=False
import time
import threading
import tkinter
import tkinter.messagebox
from pynput import keyboard
from tkinter import *
# from PyQt5.QtWidgets import QApplication, QWidget
import ctypes
start=False
def listen(event):
    global start
    print(123)
    if event.char=='s':
        start=True
    if event.char=='t':
        start=False
    print(repr(event.char))


def test_key():
    with keyboard.Events() as events:
        keys = events.get()
        print(keys.key)
        if (keys.key == "'a'"):
            print(1234)
        # if first:
        #     pass
        # if not pause and q_time >= 0 and b_time > 0 and quarte < 5:
        #     start_time = time.time()
        #     second -= 1
        #     b_time -= 1
        #     if second < 0:
        #         second = 59
        #         q_time -= 1
        #     if q_time >= 0:
        #         if second < 10:
        #             out = f'0{q_time}:0{second}'
        #         else:
        #             out = f'0{q_time}:{second}'
        #         # self.create_time(quarte, out, b_time)
        #         # self.window.mainloop()
        #     else:
        #         pass
        #         # if q_time < 0 and quarte <= 1:
        #         #     quarte += 1
        #         #     player = ctypes.windll.kernel32
        #         #     player.Beep(2000, 3000)
        #         #     print(quarte)
        #         # if quarte > 2:
        #         #     player = ctypes.windll.kernel32
        #         #     player.Beep(1000, 5000)
        #     end_time = time.time()
        #     wait = end_time - start_time
        #     time.sleep(1 - wait)
        # event = events.get()
        # if event is None:
        #     pass
        # else:
        #     if event.key == keyboard.Key.f1:
        #         print(12313)
        #         time.sleep(1)
        #         pause = False
        #     if event.key == keyboard.Key.esc:
        #         break


class myGUI():
    def __init__(self,window):
        self.window=window

    def setinit(self):
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        w = screenwidth
        h = screenheight
        x = 0
        y = 0
        self.frame=Frame(self.window)
        self.frame.grid()
        self.host_label = Label(self.frame, text="主队名称：")
        self.host_label.grid(row=0)
        self.host_input = Entry(self.frame)
        self.host_input.grid(row=0, column=1)
        self.guest_label = Label(self.frame, text="客队名称：")
        self.guest_label.grid(row=1)
        self.guest_input = Entry(self.frame)
        self.guest_input.grid(row=1, column=1)
        self.submit = Button(self.frame, text=u"确定", command=self.submit)
        self.submit.grid(row=2)
        self.window.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.window.configure(bg='black')
        # self.window.overrideredirect(True)

        self.window.mainloop()
        self.window.after(1, test_key)

    def submit(self):
        host_name = self.host_input.get()
        guest_name = self.guest_input.get()
        if host_name == '' or guest_name == '':
            self.okqqq(message='请填写比赛队队名！')
            return
        self.host_input.grid_forget()
        self.guest_input.grid_forget()
        self.host_label.grid_forget()
        self.guest_label.grid_forget()
        self.submit.grid_forget()
        self.create_match(host_name, guest_name)

    def create_match(self,host_name, guest_name):
        self.host_show_label = Label(self.frame, text=host_name, bg='black', fg='yellow', font=("微软雅黑", 48, "bold"))
        self.host_show_label.grid(row=0,column=1)
        self.vs_show_label = Label(self.frame, text=' VS  ', bg='black', fg='red', font=("微软雅黑", 48, "bold", "italic"))
        self.vs_show_label.grid(row=0, column=2)
        self.guest_show_label = Label(self.frame, text=guest_name, bg='black', fg='yellow', font=("微软雅黑", 48, "bold"))
        self.guest_show_label.grid(row=0, column=3)
        self.create_time()
        self.create_score()
        self.frame.focus_set()
        self.frame.bind("<Key>",listen)


    def create_time(self,quarte=1, total_time='10:00', attack_time=24):
        self.quarte_label= Label(self.window, text='第'+str(quarte)+'节', bg='black', fg='red', font=("微软雅黑", 24, "bold"))
        self.quarte_label.grid(row=1,column=2)
        self.total_label= Label(self.window, text=total_time, bg='black', fg='green', font=("微软雅黑", 24, "bold"))
        self.total_label.grid(row=2, column=2)
        self.attack_label = Label(self.window, text=str(attack_time), bg='black', fg='red', font=("微软雅黑", 32, "bold"))
        self.attack_label.grid(row=3, column=2)
    def create_score(self,host=0, guest=0):
        self.host_score_label = Label(self.window, text=str(host), bg='black', fg='red', font=("微软雅黑", 60, "bold"))
        self.host_score_label.grid(row=2, column=1)
        self.guest_host_label = Label(self.window, text=str(guest), bg='black', fg='red', font=("微软雅黑", 60, "bold"))
        self.guest_host_label.grid(row=2, column=3)


    def okqqq(self,title='提示框',message=''):
        # 弹出对话框
        result = tkinter.messagebox.askokcancel(title=title, message=message)
        print(result)

    def listen(event):
        print(repr(event.char))
        quarte = 1
        q_time = 10
        b_time = 24
        second = 0
        pause = True
        first = True
        while True:
            with keyboard.Events() as events:
                if first:
                    pass
                if not pause and q_time >= 0 and b_time > 0 and quarte < 5:
                    start_time = time.time()
                    second -= 1
                    b_time -= 1
                    if second < 0:
                        second = 59
                        q_time -= 1
                    if q_time >= 0:
                        if second < 10:
                            out = f'0{q_time}:0{second}'
                        else:
                            out = f'0{q_time}:{second}'
                        # self.create_time(quarte, out, b_time)
                        # self.window.mainloop()
                    else:
                        pass
                        # if q_time < 0 and quarte <= 1:
                        #     quarte += 1
                        #     player = ctypes.windll.kernel32
                        #     player.Beep(2000, 3000)
                        #     print(quarte)
                        # if quarte > 2:
                        #     player = ctypes.windll.kernel32
                        #     player.Beep(1000, 5000)
                    end_time = time.time()
                    wait = end_time - start_time
                    time.sleep(1 - wait)
                event = events.get()
                if event is None:
                    pass
                else:
                    if event.key == keyboard.Key.f1:
                        print(12313)
                        time.sleep(1)
                        pause = False
                    if event.key == keyboard.Key.esc:
                        break

    def reset(self):
        pass


root = Tk()
mywindow=myGUI(root)
mywindow.setinit()



# quarte = 1
# q_time = 10
# b_time = 240
# second = 0
# trans = True


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



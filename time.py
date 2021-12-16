import time
from pynput import keyboard
from tkinter import *
import ctypes

root=Tk()
root.title('ZTJ')
screenwidth=root.winfo_screenwidth()
screenheight=root.winfo_screenheight()
w=screenwidth
h=screenheight
x=0
y=0
root.geometry("%dx%d+%d+%d"%(w,h,x,y))
root.configure(bg='gray')
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
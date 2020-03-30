import tkinter
import pygame
import os

def play():
    pygame.mixer.init()
    pygame.mixer.music.load(r'E:\YUNPAN\(www.50yin.com)音阙诗听 - 霜降.flac')
    pygame.mixer.music.set_volume(5)
    pygame.mixer.music.play(-1, 0)


windows = tkinter.Tk()
windows.title('嘿嘿城市薪资')
windows.geometry('400x400')
label = tkinter.Label(windows, text='找工作啦!请顺次点击以下四个按钮!', font=("黑体", 15))
label.pack()
button1 = tkinter.Button(windows, text='爬取数据', bd=10)
button1.pack(side=tkinter.TOP)
button3 = tkinter.Button(windows, text='数据处理1', bd=10)
button3.pack(side=tkinter.TOP)
button2 = tkinter.Button(windows, text='数据处理2', bd=10)
button2.pack(side=tkinter.TOP)
button5 = tkinter.Button(windows, text='获得坐标', bd=10)
button5.pack(side=tkinter.TOP)
button6 = tkinter.Button(windows, text='显示HOT-MAP', bd=15)
button6.pack(side=tkinter.TOP)
quit_button = tkinter.Button(windows, text="退出", command=windows.quit, bd=8)
quit_button.pack(side=tkinter.BOTTOM)
button4 = tkinter.Button(windows, text='帮助必点', bd=10)
button4.pack(side=tkinter.BOTTOM)

mainmenu = tkinter.Menu(windows)
menuStart = tkinter.Menu(mainmenu)
mainmenu.add_cascade(label="开始", menu=menuStart)
menuStart.add_command(label='播放', command=play)
menuStart.add_separator()    # 添加一条分隔线
menuStart.add_command(label='Exit', command=windows.quit)
windows.config(menu=mainmenu)


windows.mainloop()

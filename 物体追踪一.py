# -*- coding: utf-8 -*-
import cv2
import numpy as np
from tkinter import *
from tkinter import messagebox
color_high=0
color_low=0
a=1
'''视像部分'''
cap=cv2.VideoCapture(0)
while(1):
    if a==1:
        def message_tk():
            if messagebox.askokcancel('消息框','选择好颜色了吗？\n 记得按\'q\'键返回窝')==True:
                global a
                a=2
                root.destroy()
        def closeone():
            quit()
        def orange_color():
            global color_high
            global color_low
            color_high=20
            color_low=0
            message_tk()
        def yellow_color():
            global color_high
            global color_low
            color_high=38
            color_low=22
            message_tk()
        def green_color():
            global color_high
            global color_low
            color_high=75
            color_low=38
            message_tk()
        def blue_color():
            global color_high
            global color_low
            color_high=130
            color_low=75
            message_tk()
        def violet_color():
            global color_high
            global color_low
            color_high=160
            color_low=130
            message_tk()
        def red_color():
            global color_high
            global color_low
            color_high=179
            color_low=160
            message_tk()
        root=Tk() #初始化Tk
        root.title("图像颜色")
        root.geometry('500x500')
        label=Label(root,text="选你喜欢的颜色")#创建一个label标签
        label.pack()#显示label标签
        label1=Label(root,width=1).pack()
        Button(root,text='橙色',width=19,height=2,bg="orange",command=orange_color).pack()#创建橙色按钮
        label2=Label(root,width=1).pack()
        Button(root,text='黄色',width=19,height=2,bg="Yellow",command=yellow_color).pack()#创建黄色按钮
        label3=Label(root,width=1).pack()
        Button(root,text='绿色',width=19,height=2,bg="green",command=green_color).pack() #创建绿色按钮
        label4=Label(root,width=1).pack()
        Button(root,text='蓝色',width=19,height=2,bg="orange",command=blue_color).pack()#创建蓝色按钮
        label5=Label(root,width=1).pack()
        Button(root,text='紫色',width=19,height=2,bg="Violet",command=violet_color).pack()#创建紫色按钮
        label6=Label(root,width=1).pack()
        Button(root,text='红色',width=19,height=2,bg="Red",command=red_color).pack()#创建红色按钮
        label7=Label(root,width=1).pack()
        Button(root,text='退出',width=19,height=2,bg="white",command=closeone).pack()#创建退出按钮
        root.mainloop()#进入消息循环
        print(color_high)
        print(color_low)
# 获取每一帧
    if a==2:
        ret,frame=cap.read()
    # 转换到 HSV
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # 设定蓝色的阈值
        lower_blue=np.array([color_low,50,50])
        print(lower_blue)
        upper_blue=np.array([color_high,255,255])
        print(upper_blue)
    # 根据阈值构建掩模
        mask=cv2.inRange(hsv,lower_blue,upper_blue)
    # 对原图像和掩模进行位运算
        res=cv2.bitwise_and(frame,frame,mask=mask)
    # 显示图像
        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k=cv2.waitKey(5)&0xFF
        #关闭窗口
        if k==ord('q'):
            cv2.destroyAllWindows()
            a=1




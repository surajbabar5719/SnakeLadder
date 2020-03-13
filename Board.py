# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 10:14:27 2020

@author: admin
"""

import os
os.chdir('E:/business1')
import Player1
import time
from Dice1 import *
from tkinter import *
images=[]
class Board:
    def __init__(self,number):
        gui=Tk()
        self.sti=0
        gui.configure(background="white")
        gui.title("Business Game")
        no=0
        num=[]
        nrow=[]
        ncol=[]
        ii=0
        jj=91
        rw=9
        while no<99:
            for i in range(0,10):
                if jj!=100:
                    jk="0"+str(jj)
                    cl=jj%10
                    if cl==0:
                        cl=10
                else:
                    jk=jj
                    cl=10
                
                imgw1=PhotoImage(file="E:/business1/imagedata\snakeboard\image_part_"+str(jk)+".png")
                l1=Label(gui,text=str(no),image=imgw1,height=47,width=47)
                l1.grid(row=rw,column=cl)
                num.append(no)
                l1.imgw1=imgw1
                images.append(imgw1)
                nrow.append(rw)
                ncol.append(cl)
                jj+=1
                no+=1
            jj-=11
            rw-=1
            for i in range(0,10):
                jk="0"+str(jj)
                cl=jj%10
                if cl==0:
                    cl=10
                if jj<10:
                    jk="00"+str(jj)
                imgw1=PhotoImage(file="E:/business1/imagedata\snakeboard\image_part_"+str(jk)+".png")
                l1=Label(gui,text=str(no),image=imgw1,height=47,width=47)
                l1.grid(row=rw,column=cl)
                num.append(no)
                l1.imgw1=imgw1
                images.append(imgw1)
                nrow.append(rw)
                ncol.append(cl)
                jj-=1
                no+=1
            jj-=9
            rw-=1
        img1=PhotoImage(file="imagedata\image_part_00"+str(1)+".png")
        #img2=PhotoImage(file="imagedata\image_part_00"+str(1)+".png")
        images.append(img1)
        lb1=Label(gui,image=img1,borderwidth=2,relief="solid",height=70,width=70)
        lb1.grid(row=11,column=11)
        #lb2=Label(gui,image=img1,height=70,width=70,borderwidth=2,relief="solid")
        #lb2.grid(row=11,column=12)
        lb1.img1=img1
        #lb2.img2=img2
        
        #imgp=[]
        lbp=[]
        """
        =PhotoImage(file="imagedata/0.png")
        imgb=PhotoImage(file="imagedata/1.png")
        
        lbred=Label(gui,image=imgr)
        lbred.grid(row=nrow[0],column=ncol[0])
        lbblue=Label(gui,image=imgb)
        lbblue.grid(row=nrow[0],column=ncol[0])
        lbred.imgr=imgr
        lbblue.imgb=imgb
        """
        numberOfPlayers=int(input())
        Players=[]
        
        for i in range(0,numberOfPlayers):
            Players.append(Player1.Player())
            imgpq=PhotoImage(file="imagedata/"+str(i)+".png")
            lbp.append(Label(gui,image=imgpq))
            lbp[i].imgpq=imgpq
            lbp[i].grid(row=nrow[0],column=ncol[0])
        def pch(d):
            ip=Players[self.sti].getPosition()
            Players[self.sti].changePosition(d)
            while ip>Players[self.sti].getPosition():
                lbp[self.sti].grid(row=nrow[ip],column=ncol[ip])
                ip-=1
                gui.update()
                time.sleep(0.1)
            while ip<=Players[self.sti].getPosition():    
                lbp[self.sti].grid(row=nrow[ip],column=ncol[ip])
                ip+=1
                gui.update()
                time.sleep(0.1)
            gui.update()
            self.sti+=1
            if d==6:
                self.sti-=1
            if self.sti==numberOfPlayers:
                self.sti=0
            return 0
        def dic():
            d=dice()
            img1=PhotoImage(file="imagedata\image_part_00"+str(d)+".png")
            #img2=PhotoImage(file="imagedata\image_part_00"+str(n)+".png")
            lb1=Label(gui,image=img1,height=70,width=70,borderwidth=2,relief="solid")
            lb1.img1=img1
            lb1.grid(row=11,column=11)
            #lb2=Label(gui,image=img2,height=70,width=70,borderwidth=2,relief="solid")
            #lb2.grid(row=11,column=12)
            #lb2.img2=img2
            gui.update()
            if Players[0].getPosition()==99:
                lb1=Label(gui,text="RED WIN",borderwidth=2,relief="solid")
                lb1.grid(row=13,column=12)
            else:
                if Players[1].getPosition()==99:
                    lb1=Label(gui,text="RED WIN",borderwidth=2,relief="solid")
                    lb1.grid(row=13,column=12)
                else:
                    pch(d)
        b1=Button(gui,text="Roll Dice",command=dic)
        b1.grid(row=12,column=12)
        print(num)
        print(nrow)
        print(ncol)
if __name__=="__main__":
    brd=Board(2)
    mainloop()
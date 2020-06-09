#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 04:14:49 2019

@author: bvegetas
"""
preset='Retlatisäxäs7.csv'
preset='RetlatTöötuarä.csv'
disk='/media/bvegetas/亂數天下/'
oäkp=6

#import pygame as pg
import time as tm
import numpy as np
import threading
import vjvo as jv
import os,sys
import numba as nb
import pydub as pd
from pydub.playback import play 
import subprocess
'''
def play(segment):
    pdplay(segment)
'''

event=threading.Event()





logistic=False  #Sexäspas Logistic Regression ejosa?
a=sorted(os.listdir(disk+'/Glossõri/'))
path=disk+'/Glossõri/'+a[0]
a=a[1:len(a)]
rndpool=jv.vjvo(path,acc=oäkp,logistic=logistic)
nrp=len(rndpool)
while nrp<1e6:
    path=disk+'/Glossõri/'+a[0]
    a=a[1:len(a)]
    rndpool=np.r_[rndpool,jv.vjvo(path,acc=oäkp)]
    nrp=len(rndpool)

#pg.mixer.init()
#beep1000=pg.mixer.Sound('1000hz.wav')
#beep800=pg.mixer.Sound('800hz.wav')
beep1000=pd.AudioSegment.from_wav('1000hz.wav')
beep800=pd.AudioSegment.from_wav('800hz.wav')

'''
for i in range(3):
    beep1000.play()
    tm.sleep(1)
beep800.play()
'''
print('Selamat datang di Jam Kekacauan!')
gaywegä=float(input('Berapa lama Anda akan retlat? (dalam detik)'))
tbl=np.loadtxt(preset,str,'#','\t')
tagä=tbl[:,0]
xm=tbl[:,1].astype(float)
alpha=tbl[:,2].astype(float)

tlist=[]
wlist=[]
gay=0
spanduk=True
k=0
while(spanduk):
    for i in range(len(tagä)):
        tlist.append(tagä[i])
        wlist.append(np.exp((alpha[i]*np.log(xm[i])-np.log(rndpool[k]))/alpha[i]))
        k+=1
        gay+=wlist[-1]
        if gay>gaywegä:
            wlist[-1]-=(gay-gaywegä)
            spanduk=False
            break
tagä=np.vstack(tlist).reshape(-1)
wegä=np.vstack(wlist).reshape(-1)
jv.ljvo(path,rndpool[k:],acc=oäkp)
#wegä*=0.01   

#@nb.jit(forceobj=True)#20,nogil=True)
def main(tagä,wegä):    
    dytuuwegä=tm.time()
    for i in range(len(tagä)):
        flag3=True
        flag2=True
        flag1=True
        while True:
            töl=tm.time();
            w=dytuuwegä+wegä[i]-töl
            print('\r'+tagä[i]+', %.2f dtk, %d/%d\t\t'%(w,i+1,len(wegä)),end='',flush=True)
            if w<=3 and flag3:
                #beep1000.play()
                play(beep1000)
                flag3=False
            if w<=2 and flag2:
                #beep1000.play()
                play(beep1000)
                flag2=False
            if w<=1 and flag1:
                #beep1000.play()
                play(beep1000)
                flag1=False
            if w<=0:
                #beep800.play()
                play(beep800)
                break
            tm.sleep(0.23)
            #event.wait(0.23)
        dytuuwegä+=wegä[i]

main(tagä,wegä)
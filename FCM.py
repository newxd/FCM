import numpy as np
import cv2
import random


def fcm(img,c,alpha):
    #c:cluster numbers
    #alpha: parameter as terminate conditon
    [row,column]=img.shape
    n=img.size
    U=[]
    for i in range(c):
        temp=[]
        for j in range(n):
            temp.append(random.random())
        U.append(temp)
    U=np.array(U,dtype=float)
    # intial U funcion
    Un=U.copy()
    V=getV(img,U)
    ''''for i in range(n):
        for j in range(c):
            x=0.0
            for k in range(c):
                x+=((img[i]-V[j])**2/((img[i]-V[k])**2))
            Un[j][i]=1/x'''''
    for i in range(row):
        for j in range(column):
            for k in range(c):
                x=0.0
                for l in range(c):
                    x+=((img[i][j]-V[k])**2/((img[i][j]-V[l])**2))
                Un[k][i*column+j]=1.0/x


    t=1
    while(np.sum(np.sum(np.abs(U-Un)))>alpha):
        V=getV(img,Un)
        U=Un.copy()
        Un=getU(img,V)
        print t,np.sum(np.sum(np.abs(U-Un)))
        t+=1
    #

    #different colors for each cluster
    color=np.linspace(0,255,c)
    for i in range(row):
        for j in range(column):
            l=np.argsort(Un[:,i*column+j])
            img[i][j]=color[l[-1]]

    return img

def getV(img,U):
    #compute cluster V function
    n=img.size
    [row,colum]=img.shape
    V=[]
    for i in range(len(U)):
        a=np.sum(U[i])
        b=0.0
        for j in range(row):
            for k in range(colum):

                b+=((U[i][j*colum+k])**2*img[j][k])
        V.append(b/a)
    return V

def getU(img,V):
    #compute U function
    c=len(V)
    [row,column]=img.shape
    n=img.size
    Un=np.zeros([c,n])
    for i in range(row):
        for j in range(column):
            for k in range(c):
                x = 0.0
                for l in range(c):
                    x += ((img[i][j] - V[k]) ** 2 / ((img[i][j] - V[l]) ** 2))
                Un[k][i * column + j] = 1.0 / x
    return Un


def Img_Fcm(img,alpha):
    out=fcm(img,2,alpha)
    cv2.imshow('FCM', out)
    cv2.waitKey(0)
if __name__ == '__main__':
    img=cv2.imread('dataset/H332.bmp',0)
    Img_Fcm(img,0.1)







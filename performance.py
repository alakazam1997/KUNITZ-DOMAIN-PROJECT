#!/usr/bin/env python 

import sys 

import numpy as np 

 

def get_preds(fname): 

    preds=[] 

    fh=open(fname) 

    for line in fh: 

        v=line.rstrip().split() 

        preds.append([v[0],float(v[1]),int(v[2])]) 

    return preds 

 

def get_cm(preds,th=0.001): 

    cm=np.zeros((2,2)) 

    n=len(preds) 

    for k in range(n): 

        j=0 

        i=preds[k][2] 

        if preds[k][1]<=th: j=1 

        cm[i,j]=cm[i,j]+1 

    return cm 

 

def get_acc(cm): 

    return (cm[0,0]+cm[1,1])/np.sum(cm) 

 

def get_mcc(cm): 

    tp=cm[1,1] 

    tn=cm[0,0] 

    fn=cm[1,0] 

    fp=cm[0,1] 

    d=((tp+fp)*(tp+fn)*(tn+fn)*(tn+fp)) 

    mcc = (tp*tn-fp*fn)/np.sqrt(d) 

    return mcc 

 

if __name__ == '__main__': 

    fname=sys.argv[1] 

    th=float(sys.argv[2]) 

    preds=get_preds(fname) 

    cm=get_cm(preds,th) 

    q2=get_acc(cm) 

    mcc=get_mcc(cm) 

    print ('TH:',th,'Q2:',q2,'MCC:',mcc) 


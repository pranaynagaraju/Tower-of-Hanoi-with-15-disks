from array import *
import string
import sys
t1=array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]);
t2=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
t3=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
n=15;
x1=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
x2=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
x3=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
d1=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
d2=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
d3=array('i',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]);
k1=[];
k2=[];
k3=[];
ol=[];
co=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0];
c=0;
count=0;
final=0
p=0;
p1=0;
initial=0;

def hanoi(x1,x2,x3):
  check=0;
  check1=0;
  check2=0;
  print(x1,"parent")
  print(x2,"parent")
  print(x3,"parent")
  print(ol,"open list")
  print(co,"close list")
  for i in range(0,n):
    if(x1[i]!=0):
      k=x1[i];
      for j in range (0,n):
        if(x2[j]==0):
          if(j==(n-1)):
            x2[j]=k;
            x1[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            update(x1,x2,x3)
            x1[i]=k;
            x2[j]=0;
            check=1;
            break;
          elif(k<x2[j+1]):
            x2[j]=k;
            x1[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            update(x1,x2,x3)
            x2[j]=0;
            x1[i]=k;



            check=1;
            break;
        
      for i1 in range (0,n):
        if(x3[i1]==0):
          if(i1==(n-1)):
            x3[i1]=k;
            x1[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1


            
            update(x1,x2,x3)
            x3[i1]=0;
            x1[i]=k;



            check=1;
            break;
          elif(k<x3[i1+1]):

            x3[i1]=k;
            x1[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            update(x1,x2,x3)
            x3[i1]=0;
            x1[i]=k;



            check=1;
            break;
    if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
       print(x1)
       print(x2)
       print(x3,"ANSWER")
       sys.exit();
       final=1
       
    if(check==1):

      break;
  for i in range(0,n):
    if(x2[i]!=0):
      k=x2[i];
      for j in range (0,n):
        if(x1[j]==0):
          if(j==(n-1)):
            x1[j]=k;
            x2[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            check1=1;
            update(x1,x2,x3)
            x1[j]=0
            x2[i]=k      

            check1=1;
            break;
          elif(k<x1[j+1]):
            x1[j]=k;
            x2[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            check1=1;
            update(x1,x2,x3)
            x2[i]=k;
            x1[j]=0;


            check1=1;
            break;
    
      for i1 in range (0,n):

        if(x3[i1]==0):
          if(i1==(n-1)):
            x3[i1]=k;
            x2[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1

            update(x1,x2,x3)
            x3[i1]=0;
            x2[i]=k;


            check1=1;
            break;
          elif(k<x3[i1+1]):

            x3[i1]=k;
            x2[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
              sys.exit();

            check1=1;

            update(x1,x2,x3)
            x3[i1]=0;
            x2[i]=k;



            check1=1;
            break;
    if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
       print(x1)
       print(x2)
       print(x3,"ANSWER")
       sys.exit();
       final=1          
    if(check1==1):
      break;
  for i in range(0,n):

    if(x3[i]!=0):
      k=x3[i];
      for j in range (0,n):
        if(x1[j]==0):
 
          if(j==(n-1)):
            x1[j]=k;
            x3[i]=0;
            check2=1;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
              update(x1,x2,x3)
            x1[j]=0;
            x3[i]=k;
            break;
          elif(k<x1[j+1]):
            x1[j]=k;
            x3[i]=0;
            check2=1;

            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1


            update(x1,x2,x3)
            x1[j]=0;
            x3[i]=k;


            break;
    
      for i1 in range (0,n):
        if(x2[i1]==0):

          if(i1==(n-1)):

            x2[i1]=k;
            x3[i]=0;
            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            check2=1;
            update(x1,x2,x3)
            x2[i1]=0;
            x3[i]=k;
            
            break;
          elif(k<x2[i1+1]):
            x2[i1]=k;
            x3[i]=0;

            if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1

            check2=1;
            update(x1,x2,x3)
            x2[i1]=0;
            x3[i]=k;
            break;
          
    if(check2==1):

      break;
    if(x3==array('i',[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])):
       print(x1)
       print(x2)
       print(x3,"ANSWER")
       sys.exit();
       final=1

    
def update(x1,x2,x3):
  print(x1,"child");
  print(x2,"child");
  print(x3,"child");
  print("          ");
  ol.append(x1[0]);
  ol.append(x1[1]);
  ol.append(x1[2]);
  ol.append(x1[3]);
  ol.append(x1[4]);
  ol.append(x1[5]);
  ol.append(x1[6]);
  ol.append(x1[7]);
  ol.append(x1[8]);
  ol.append(x1[9]);
  ol.append(x1[10]);
  ol.append(x1[11]);
  ol.append(x1[12]);
  ol.append(x1[13]);
  ol.append(x1[14]);
  
  ol.append(x2[0]);
  ol.append(x2[1]);
  ol.append(x2[2]);
  ol.append(x2[3]);
  ol.append(x2[4]);
  ol.append(x2[5]);
  ol.append(x2[6]);
  ol.append(x2[7]);
  ol.append(x2[8]);
  ol.append(x2[9]);
  ol.append(x2[10]);
  ol.append(x2[11]);
  ol.append(x2[12]);
  ol.append(x2[13]);
  ol.append(x2[14]);
  
  ol.append(x3[0]);
  ol.append(x3[1]);
  ol.append(x3[2]);
  ol.append(x3[3]);
  ol.append(x3[4]);
  ol.append(x3[5]);
  ol.append(x3[6]);
  ol.append(x3[7]);
  ol.append(x3[8]);
  ol.append(x3[9]);
  ol.append(x3[10]);
  ol.append(x3[11]);
  ol.append(x3[12]);
  ol.append(x3[13]);
  ol.append(x3[14]);
hanoi(t1,t2,t3);

def fun():


    while(len(ol)!=0):
 
      for k in range (0,15):
        x1[k]=ol.pop(0)

      for k in range (0,15):
        x2[k]=ol.pop(0)
      for k in range (0,15):
        x3[k]=ol.pop(0)


      p=0
      intial=0;

      count=0;
      final=0
      com=len(co)
      com=com-9


      while(1==1):


        initial=count;

        if(x1[0]==co[count] and x1[1]==co[count+1] and x1[2]==co[count+2] and x1[3]==co[count+3] and x1[4]==co[count+4] and x1[5]==co[count+5] and x1[6]==co[count+6] and x1[7]==co[count+7] and x1[8]==co[count+8] and x1[9]==co[count+9] and x1[10]==co[count+10] and x1[11]==co[count+11] and x1[12]==co[count+12] and x1[13]==co[count+13] and x1[14]==co[count+14]):
          count=count+15;

          if(x2[0]==co[count] and x2[1]==co[count+1] and x2[2]==co[count+2] and x2[3]==co[count+3] and x2[4]==co[count+4] and x2[5]==co[count+5] and x2[6]==co[count+6] and x2[7]==co[count+7] and x2[8]==co[count+8] and x2[9]==co[count+9] and x2[10]==co[count+10] and x2[11]==co[count+11] and x2[12]==co[count+12] and x2[13]==co[count+13] and x2[14]==co[count+14]):
            count=count+15;

            if(x3[0]==co[count] and x3[1]==co[count+1] and x3[2]==co[count+2] and x3[3]==co[count+3] and x3[4]==co[count+4] and x3[5]==co[count+5] and x3[6]==co[count+6] and x3[7]==co[count+7] and x3[8]==co[count+8] and x3[9]==co[count+9] and x3[10]==co[count+10] and x3[11]==co[count+11] and x3[12]==co[count+12] and x3[13]==co[count+13] and x3[14]==co[count+14]):

              if(len(ol)!=0):

                    fun();
                    
              else:
                  print("exitttttttttttt")
                  sys.exit();
              
            
            else:
              if(count==len(co)-1 or count+46>len(co)-1):
                  break;

              count=initial+45


          else:
            if(count==len(co)-1 or count+46>len(co)-1):
              break;

            count=initial+45;



        else:
          if(count==len(co)-1 or count+46>len(co)-1):
              break;
          count=initial+45

      if(p==0):
          co.append(x1[0]);
          co.append(x1[1]);
          co.append(x1[2]);
          co.append(x1[3]);
          co.append(x1[4]);
          co.append(x1[5]);
          co.append(x1[6]);
          co.append(x1[7]);
          co.append(x1[8]);
          co.append(x1[9]);
          co.append(x1[10]);
          co.append(x1[11]);
          co.append(x1[12]);
          co.append(x1[13]);
          co.append(x1[14]);
          co.append(x2[0]);
          co.append(x2[1]);
          co.append(x2[2]);
          co.append(x2[3]);
          co.append(x2[4]);
          co.append(x2[5]);
          co.append(x2[6]);
          co.append(x2[7]);
          co.append(x2[8]);
          co.append(x2[9]);
          co.append(x2[10]);
          co.append(x2[11]);
          co.append(x2[12]);
          co.append(x2[13]);
          co.append(x2[14]);
          co.append(x3[0]);
          co.append(x3[1]);
          co.append(x3[2]);
          co.append(x3[3]);
          co.append(x3[4]);
          co.append(x3[5]);
          co.append(x3[6]);
          co.append(x3[7]);
          co.append(x3[8]);
          co.append(x3[9]);
          co.append(x3[10]);
          co.append(x3[11]);
          co.append(x3[12]);
          co.append(x3[13]);
          co.append(x3[14]);
            
        
      if(p==0):
        hanoi(x1,x2,x3)
while(len(ol)!=0):


    for k in range (0,15):
        x1[k]=ol.pop(0)

    for k in range (0,15):
        x2[k]=ol.pop(0)
    for k in range (0,15):
        x3[k]=ol.pop(0)
    count=0
    p=0
    intial=0;

    count=0;
    final=0
    com=len(co)
    com=com-9

    while(1==1):
      initial=count;
      if(x1[0]==co[count] and x1[1]==co[count+1] and x1[2]==co[count+2] and x1[3]==co[count+3] and x1[4]==co[count+4] and x1[5]==co[count+5] and x1[6]==co[count+6] and x1[7]==co[count+7] and x1[8]==co[count+8] and x1[9]==co[count+9] and x1[10]==co[count+10] and x1[11]==co[count+11] and x1[12]==co[count+12] and x1[13]==co[count+13] and x1[14]==co[count+14]):
        count=count+15;

        if(x2[0]==co[count] and x2[1]==co[count+1] and x2[2]==co[count+2] and x2[3]==co[count+3] and x2[4]==co[count+4] and x2[5]==co[count+5] and x2[6]==co[count+6] and x2[7]==co[count+7] and x2[8]==co[count+8] and x2[9]==co[count+9] and x2[10]==co[count+10] and x2[11]==co[count+11] and x2[12]==co[count+12] and x2[13]==co[count+13] and x2[14]==co[count+14]):
          count=count+15;

          if(x3[0]==co[count] and x3[1]==co[count+1] and x3[2]==co[count+2] and x3[3]==co[count+3] and x3[4]==co[count+4] and x3[5]==co[count+5] and x3[6]==co[count+6] and x3[7]==co[count+7] and x3[8]==co[count+8] and x3[9]==co[count+9] and x3[10]==co[count+10] and x3[11]==co[count+11] and x3[12]==co[count+12] and x3[13]==co[count+13] and x3[14]==co[count+14]):

            if(len(ol)!=0):

                fun();
                  
            else:
                print("exitttttttttttt")
                sys.exit();
              
            
          else:
            if(count==len(co)-1 or count+46>len(co)-1):
                break;

            count=initial+45


        else:
          if(count==len(co)-1 or count+46>len(co)-1):
            break;
 
          count=initial+45;



      else:
        if(count==len(co)-1 or count+46>len(co)-1):
            break;

        count=initial+45


    if(p==0):
      co.append(x1[0]);
      co.append(x1[1]);
      co.append(x1[2]);
      co.append(x1[3]);
      co.append(x1[4]);
      co.append(x1[5]);
      co.append(x1[6]);
      co.append(x1[7]);
      co.append(x1[8]);
      co.append(x1[9]);
      co.append(x1[10]);
      co.append(x1[11]);
      co.append(x1[12]);
      co.append(x1[13]);
      co.append(x1[14]);
      co.append(x2[0]);
      co.append(x2[1]);
      co.append(x2[2]);
      co.append(x2[3]);
      co.append(x2[4]);
      co.append(x2[5]);
      co.append(x2[6]);
      co.append(x2[7]);
      co.append(x2[8]);
      co.append(x2[9]);
      co.append(x2[10]);
      co.append(x2[11]);
      co.append(x2[12]);
      co.append(x2[13]);
      co.append(x2[14]);
      co.append(x3[0]);
      co.append(x3[1]);
      co.append(x3[2]);
      co.append(x3[3]);
      co.append(x3[4]);
      co.append(x3[5]);
      co.append(x3[6]);
      co.append(x3[7]);
      co.append(x3[8]);
      co.append(x3[9]);
      co.append(x3[10]);
      co.append(x3[11]);
      co.append(x3[12]);
      co.append(x3[13]);
      co.append(x3[14]);
            
        
    if(p==0):
      hanoi(x1,x2,x3)



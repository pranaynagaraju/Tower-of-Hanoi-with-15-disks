from array import *
import string
import sys
t1=array('i',[1,2,3]);
t2=array('i',[0,0,0]);
t3=array('i',[0,0,0]);
n=3;
x1=array('i',[0,0,0]);
x2=array('i',[0,0,0]);
x3=array('i',[0,0,0]);
d1=array('i',[0,0,0]);
d2=array('i',[0,0,0]);
d3=array('i',[0,0,0]);
k1=[];
k2=[];
k3=[];
ol=[];
co=[0,0,0,0,0,0,0,0,0,1,2,3,0,0,0,0,0,0];
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
            if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
    if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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
    if(x3==array('i',[1,2,3])):
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
            if(x3==array('i',[1,2,3])):
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

            if(x3==array('i',[1,2,3])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            x1[j]=k;
            x3[i]=0;
            check2=1;

            update(x1,x2,x3)
            x1[j]=0;
            x3[i]=k;


            break;
    
      for i1 in range (0,n):
        if(x2[i1]==0):

          if(i1==(n-1)):

            x2[i1]=k;
            x3[i]=0;
            if(x3==array('i',[1,2,3])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1

            update(x1,x2,x3)
            x2[i1]=0;
            x3[i]=k;
            check2=1;
            break;
          elif(k<x2[i1+1]):


            if(x3==array('i',[1,2,3])):
              print(x1)
              print(x2)
              print(x3,"ANSWER")
              sys.exit();
              final=1
            x2[i1]=k;
            x3[i]=0;
            check2=1;
            update(x1,x2,x3)
            x2[i1]=0;
            x3[i]=k;

            break;
    if(x3==array('i',[1,2,3])):
       print(x1)
       print(x2)
       print(x3,"ANSWER")
       sys.exit();
       final=1
    if(check2==1):

      break;
    
def update(x1,x2,x3):
  print(x1,"child");
  print(x2,"child");
  print(x3,"child");
  print("          ");
  ol.append(x1[0]);
  ol.append(x1[1]);
  ol.append(x1[2]);
  ol.append(x2[0]);
  ol.append(x2[1]);
  ol.append(x2[2]);
  ol.append(x3[0]);
  ol.append(x3[1]);
  ol.append(x3[2]);
hanoi(t1,t2,t3);

def fun():


    while(len(ol)!=0):
      for k in range (0,3):
        x1[k]=ol.pop(0)

      for k in range (0,3):
        x2[k]=ol.pop(0)
      for k in range (0,3):
        x3[k]=ol.pop(0)


      p=0
      intial=0;

      count=0;
      final=0
      com=len(co)
      com=com-9


      while(1==1):

        initial=count;

        if(x1[0]==co[count] and x1[1]==co[count+1] and x1[2]==co[count+2]):
          count=count+3;

          if(x2[0]==co[count] and x2[1]==co[count+1] and x2[2]==co[count+2]):
            count=count+3;

            if(x3[0]==co[count] and x3[1]==co[count+1] and x3[2]==co[count+2]):

              if(len(ol)!=0):

                    fun();
                    
              else:
                  print("exitttttttttttt")
                  sys.exit();
              
            
            else:
              if(count==len(co)-1 or count+10>len(co)-1):
                  break;

              count=initial+9


          else:
            if(count==len(co)-1 or count+10>len(co)-1):
              break;

            count=initial+9;



        else:
          if(count==len(co)-1 or count+10>len(co)-1):
              break;
          count=initial+9

      if(p==0):
          co.append(x1[0]);
          co.append(x1[1]);
          co.append(x1[2]);
          co.append(x2[0]);
          co.append(x2[1]);
          co.append(x2[2]);
          co.append(x3[0]);
          co.append(x3[1]);
          co.append(x3[2]);
            
        
      if(p==0):
        hanoi(x1,x2,x3)
while(len(ol)!=0):

    for k in range (0,3):
        x1[k]=ol.pop(0)

    for k in range (0,3):
        x2[k]=ol.pop(0)
    for k in range (0,3):
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
      if(x1[0]==co[count] and x1[1]==co[count+1] and x1[2]==co[count+2]):
        count=count+3;

        if(x2[0]==co[count] and x2[1]==co[count+1] and x2[2]==co[count+2]):
          count=count+3;

          if(x3[0]==co[count] and x3[1]==co[count+1] and x3[2]==co[count+2]):

            if(len(ol)!=0):

                fun();
                  
            else:
                print("exitttttttttttt")
                sys.exit();
              
            
          else:
            if(count==len(co)-1 or count+10>len(co)-1):
                break;

            count=initial+9


        else:
          if(count==len(co)-1 or count+10>len(co)-1):
            break;
 
          count=initial+9;



      else:
        if(count==len(co)-1 or count+10>len(co)-1):
            break;

        count=initial+9


    if(p==0):
        co.append(x1[0]);
        co.append(x1[1]);
        co.append(x1[2]);
        co.append(x2[0]);
        co.append(x2[1]);
        co.append(x2[2]);
        co.append(x3[0]);
        co.append(x3[1]);
        co.append(x3[2]);
            
        
    if(p==0):
      hanoi(x1,x2,x3)



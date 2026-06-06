def inp():
  n=int(input("Enter number of subjects:"))
  m=[]
  mm=[]

  if n<=0:
    print("Invalid number")
    return None,None
  
  for i in range(n):
       s=float(input(f"Enter marks of subject {i+1}:"))
       
       mi=float(input(f"Enter maximum marks of subject{i+1}:"))
       
       
       if s<0:
        print("Invalid Obtained Marks")
        return None,None
       if mi<=0:
        print("Invalid maximum marks")
        return None,None
       if s>mi:
        print("Invalid")
        return None,None
       m.append(s)
       mm.append(mi)


  return m,mm
  
  
 
def tot(m,mm):
  to=tm=0
 
  for s in m:
    to=to+s
    
  for mi in mm:
    tm=tm+mi
  
  return to,tm 

def per(t,tm):
  return (t/tm)*100

def sub_per(m,mm):
  sp=[]

  for i in range(len(m)):
    sp.append((m[i]/mm[i])*100)
  return sp

def grd(p):
    if p >= 90:
        return "A+"
    elif p >= 80:
        return "A"
    elif p >= 70:
        return "B"
    elif p >= 60:
        return "C"
    elif p >= 50:
        return "D"
    else:
        return "F"

def mxp(sp):
  h=sp[0]
  for s in sp:
    if s>h:
      h=s
  return h
def mnp(sp):
  l=sp[0]
  for s in sp:
    if s<l:
      l=s
  return l
def out(t,tm,p,g,h,l):
  print("\n"*2)
  print("="*14,end="")
  print("RESULT",end="")
  print("="*14,end='\n'*2)
  print(f"Total Obtained            :{t}")
  print(f"Total maximum marks       :{tm}")
  print(f"Percentage                :{p:.2f}%")
  print(f"Grade                     :{g}")
  print(f"Highest Subject Percentage:{h:.2f}%")
  print(f'Lowest Subject Percentage :{l:.2f}%')

def main():
  m,mm=inp()
  if m is None:
    return 
  t,tm=tot(m,mm)
  sp=sub_per(m,mm)
  p=per(t,tm)
  g=grd(p)
  h=mxp(sp)
  l=mnp(sp)
  out(t,tm,p,g,h,l)
  

if __name__=="__main__":
  main()
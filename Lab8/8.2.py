import math
ax = float(input('ax='))
ay = float(input('ay='))
bx = float(input('bx='))
by = float(input('by='))
cx = float(input('cx='))
cy = float(input('cy='))
def pl (ax,ay,bx,by,cx,cy):
  a = math.sqrt(((bx - ax)**2)+(by- ay)**2)
  b = math.sqrt(((cx - ax)**2)+(cy- ay)**2)
  c = math.sqrt(((bx - cx)**2)+(by- cy)**2)
  p = (a+b+c)/2
  s = math.sqrt(p*(p-a)*(p-b)*(p-c))
  return s
def in_tr(ax,ay,bx,by,cx,cy,x,y):
    s_tr1= pl(ax,ay,bx,by,cx,cy)
    s_tr2 = pl(ax,ay,bx,by,x,y)+pl(ax,ay,cx,cy,x,y)+pl(bx,by,cx,cy,x,y)
    
    if  abs(s_tr1 - s_tr2 )<0.0001:
     return True 
    else:
     return False
kx = float(input('kx='))
ky = float(input('ky='))
px = float(input('px='))
py = float(input('py='))
dx = float(input('dx='))
dy = float(input('dy='))
if in_tr(ax,ay,bx,by,cx,cy,kx,ky) and in_tr(ax,ay,bx,by,cx,cy,px,py) and in_tr(ax,ay,bx,by,cx,cy,dx,dy):
   print("Трикутник KPD лежить в трикутнику ABC ")
else:
    print("Трикутник KPD  не лежить в трикутнику ABC ")
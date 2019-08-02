class Bunny:
  def __init__(self, x=0, y=0, face='n'):
    self.x=x
    self.y=y
    self.face=face
    self.path=[(0,0)]
    self.twice=[]

  def position(self):
    print self.x, self.y
  
  def breadcrumb(self,step,coor,op):
    for s in range (0,step):
      if coor=='x' and op=='add':
        self.x+=1
      elif coor=='y' and op=='add':
        self.y+=1
      elif coor=='x' and op=='sub':
        self.x-=1
      elif coor=='y' and op=='sub':
        self.y-=1
      if (self.x,self.y) in self.path:
        self.twice.append((self.x,self.y))
      self.path.append((self.x,self.y))

  def navigate(self,d):
    #do something
    if 'R' in d:
      step=int(d.lstrip('R'))
      if self.face=='n':
        self.face='e'
        self.breadcrumb(step,'x','add')
      elif self.face=='e':
        self.face='s'
        self.breadcrumb(step,'y','sub')
      elif self.face=='s':
        self.face='w'
        self.breadcrumb(step,'x','sub')
      elif self.face=='w':
        self.face='n'
        self.breadcrumb(step,'y','add')
    else:
      step=int(d.lstrip('L'))
      if self.face=='n':
        self.face='w'
        self.breadcrumb(step,'x','sub')
      elif self.face=='e':
        self.face='n'
        self.breadcrumb(step,'y','add')
      elif self.face=='s':
        self.face='e'
        self.breadcrumb(step,'x','add')
      elif self.face=='w':
        self.face='s'
        self.breadcrumb(step,'y','sub')
      
inputroute = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3"

#inputroute = "R2, R2, R2"
#inputroute = "R1, R1, R1, R1"
#inputroute = "R5, L5, R5, R3"
#inputroute = "R2, L3"
#inputroute = "R8, R4, R4, R8"
arr = inputroute.split(', ')
b = Bunny()
for d in arr:
  b.navigate(d)

#b.position()

#print b.path
#print "Visited blocks:", abs(b.twice[0])+abs(b.twice[1])
print "Visited coord:", abs(b.twice[0][0]) + abs(b.twice[0][1])
print "Blocks away:",abs(b.x)+abs(b.y)

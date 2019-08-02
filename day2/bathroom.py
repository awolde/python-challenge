class keycode:
  def __init__(self, startposition=5):
    self.startposition=[1,1]
    self.keycodes=[[1,2,3],[4,5,6],[7,8,9]]
    self.part2keycodes=[[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,'A','B','C',0],[0, 0, 'D',0,0]]
    self.part2lp=[2,0]
    self.part2cp=[2,0]
    self.lastposition=[1,1] #start at 5
    self.currentposition=[1,1] #location of 5 in the 2d array
    self.savedkeycodes=[]

  def savekeycode(self):
    self.savedkeycodes.append(self.keycodes[self.currentposition[0]][self.currentposition[1]]) 
    print "saved keys:",self.savedkeycodes

  def part2savekey(self):
    self.savedkeycodes.append(self.part2keycodes[self.part2cp[0]][self.part2cp[1]])
    print "saved keys:",self.savedkeycodes

  def navigate(self,direction,limit):
    #do something
#    print direction
    if 'D' in direction:
      if self.lastposition[0]+1 <= limit:
#      print "yes"
        self.currentposition[0] = self.lastposition[0]+1
    elif 'R' in direction:
      if self.lastposition[1]+1 <= limit:
        self.currentposition[1] = self.lastposition[1]+1
    elif 'U' in direction:
      if self.lastposition[0]-1 >= 0:
        self.currentposition[0] = self.lastposition[0]-1
    elif 'L' in direction:
      if self.lastposition[1]-1 >= 0:
        self.currentposition[1] = self.lastposition[1]-1
    self.lastposition=self.currentposition

  def part2nav (self,direction,limit):
    #do something
#    print direction
    if 'D' in direction:
      if self.part2lp[0]+1 <= limit:
        if self.part2keycodes[self.part2cp[0]+1][self.part2cp[1]] != 0:
          self.part2cp[0] = self.part2lp[0]+1
    elif 'R' in direction:
      if self.part2lp[1]+1 <= limit:
        if self.part2keycodes[self.part2cp[0]][self.part2cp[1]+1] !=0:
          self.part2cp[1] = self.part2lp[1]+1
    elif 'U' in direction:
      if self.part2cp[0]-1 >= 0:
        if self.part2keycodes[self.part2cp[0]-1][self.part2cp[1]] != 0:
          #print self.part2keycodes[self.part2cp[0]-1][self.part2cp[1]]
          self.part2cp[0] = self.part2lp[0]-1
    elif 'L' in direction:
      if self.part2lp[1]-1 >= 0:
        if self.part2keycodes[self.part2cp[0]][self.part2cp[1]-1] !=0:
          self.part2cp[1] = self.part2lp[1]-1
    self.part2lp=self.part2cp

instruction = '''
ULL
RRDDD
LURDL
UUUUD'''


arr = [y for y in (x.strip() for x in instruction.splitlines()) if y]

k = keycode()
c = keycode()
for x in range(0,len(arr)):
  line=list(arr[x])
  for y in range(0,len(line)):
    k.part2nav(line[y],4)
    c.navigate(line[y],2)
  k.part2savekey()
  c.savekeycode()

print k.savedkeycodes
print c.savedkeycodes
  

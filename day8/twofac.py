def colrotate ():
  print "do soemthing here"
  
def displayScreen(arr,x,y):
  for i in range(x):
    print arr[x][:-1]
    #print ""
  
def rect(arr,a,b):
  for x in range(b):
    for y in range(a):
      arr[x][y] = '#'
  return arr
  
screen = [['.' for x in range(10)] for y in range(6)]
#print rect (screen, 3,4)
displayScreen(rect (screen, 3,4), 5, 10)
#print screen

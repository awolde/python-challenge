def isTriangle(line):
  maxside=max(line)
  line.remove(maxside)
  if sum(line) <= maxside:
    return False
  else:
    return True

inputs = '''
  427  323  608
  613  402  520
  725  312  215'''

arr = [y for y in (x.strip() for x in inputs.splitlines()) if y]
print arr
line=[]
tri=0
for c in range(0, len(arr), 3):
  value=c
  for count in range(0,3):
  #this assumes the input lines are multiples of 3
    for i in range(0,3):
      line.append(int(arr[c].split()[count]))
      c+=1
    c=value
    print line
    if isTriangle(line):
      tri+=1
    line=[]
print tri

triangles=0
for x in range(0, len(arr)):
  line=map(int,arr[x].split())
  if isTriangle(line):
    triangles+=1

print triangles

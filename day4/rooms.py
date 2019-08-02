def matcher(checksum,line):
  for x in range(0,len(checksum)):
    for y in range(0,len(line)):
      s=line[y]
      c=checksum[x]
      if s==c:
        while line[y]==s and len(line)>0:
          line.pop(y)
          if len(line)==0:
            break
        break
      else:
        #print "not a real room"
        return False
  return True

f = open('input')
inputs = str(f.readlines())
f.close()
inputs = '''
qzmt-zixmtkozy-ivhz-343[fffdd]
dfcxsqhwzs-qzoggwtwsr-qvcqczohs-fsoqeiwgwhwcb-714[lgtfc]
ojk-nzxmzo-xviyt-xjvodib-omvdidib-265[iodvx]
wbhsfbohwcboz-qobrm-zcuwghwqg-298[bwhoc]
shoewudys-tou-ixyffydw-478[uszty]'''
#print type(sample_inputs)
arr = [y for y in (x.strip() for x in inputs.splitlines()) if y]
sectors=0

def rotate(char, val):
  return chr(ord(char)+val)

for i in range(0,len(arr)):
  line = arr[i].split('-')
#print line
  last = line.pop().rstrip(']').split('[')
  checksum = last[-1]
  sector = last[0]
  joinedstr=''.join(map(str, line))
  sortd_line=sorted(sorted(joinedstr),key=sorted(joinedstr).count,reverse=True)
  checksum=list(checksum)
  #print checksum
  if matcher(checksum,sortd_line):
    sectors+=int(sector)

print sectors

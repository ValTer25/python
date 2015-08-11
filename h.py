raw = raw_input('Enter number ')
print type(raw)
try:
 ival = int(raw)
except:
 ival = -1
if ival > 0:
 print 'OK'
else:
 print 'Error'
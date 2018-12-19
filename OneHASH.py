import base64
import binascii
import getpass

pwd = getpass.getpass('Insert your password:')


#(This line will show passowd being typed) 
#pwd = raw_input("Password: ")


#String Conversion for future logic 
pwds = str(pwd)


#base64 Encoding input
y = base64.b64encode(pwds)
pwdl = len(pwd)

#caracters as list 
char_list = ([pwd[i:i+1] for i in range(0, len(pwd), 1)])

char='aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789#%+=?'
def intpw(x):
   val=0
   pwl = pwdl
   for n in range(0,pwdl):
           val+=char.find(x[n])*(37**(pwdl-n))
   if (val%8)==7:
           val+=37**256
   return val

s = intpw([pwd[i:i+1] for i in range(0, len(pwd), 1) * pwdl])
u = str(s)
#each character as list 
oii = '%x' % intpw([pwd[i:i+1] for i in range(0, len(pwd), 1) * pwdl])
#Base64 Encoding
de = base64.b64encode(u)

#Output
print 'Raw:', '%x' % intpw([pwd[i:i+1] for i in range(0, len(pwd), 1) * pwdl])
print 'Base64:', de 	

########################################################
#DB outputs
#print(([oii[i:i+1] for i in range(0, len(oii), 1)]))
#print(([pwd[i:i+1] for i in range(0, len(pwd), 1)]))

########################################################

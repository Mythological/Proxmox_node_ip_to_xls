
from pyproxmox import *
import xlwt
import getpass

ip_addr = raw_input("Proxmox's host or IP:")
login = raw_input("login:")
realm = raw_input("Realm[pam]:") or "pam"
passw = getpass.getpass("Password:")


a = prox_auth(ip_addr,login + '@' + realm ,passw)

b = pyproxmox(a)

a2 = b.getClusterStatus()
a3 = a2[u'data']

for i in a3:
    print i.get(u'name')
    print i.get(u'ip')

workbook = xlwt.Workbook() 
sheet = workbook.add_sheet("Sheet1", cell_overwrite_ok=True)

count = 0
count2 = 0
for i in a3:
    sheet.write(count, 0, i.get(u'name'))
    sheet.write(count2, 1, i.get(u'ip'))
    count += 1
    count2 += 1

workbook.save("my3.xls")


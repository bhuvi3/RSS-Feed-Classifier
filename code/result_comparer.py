fh2 = open('../result/categorized_comapred.csv')
lines = fh2.readlines()
fh2.close()

rc = 0
tc = 0
for a in lines:
    a = a[:-1]
    tok = a.split(',')
    n = tok[1]
    p = tok[2]
    tc = tc + 1
    if n == p:
        rc = rc + 1

match = float(rc)/tc * 100
print "total feeds: ",tc
print "total matched feeds: ",rc
print "percentage match: ",match
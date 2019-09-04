
fsort = open("tblastx_HitTable_sorted.txt", 'r')
fth = open("tblastx_HitTable_THlisted_trimAB.txt", 'r')
fw = open("tblastx_HitTable_sorted_trimAB.txt", 'w')

rsort = fsort.readline()  #一行目の目次の読み飛ばし
rth = fth.readline()
fw.write(rsort) #目次の書き出し

count = 0

for rth in fth:
    rth_spl = rth.split('\t')
    for rsort in fsort:
        rsort_spl = rsort.split('\t')
        if rth_spl[0] in rsort_spl[0]:
            fw.write(rsort)
            count += 1
    if count == 0:
        print("THlisted_trimAB.txt の中に sorted.txt に無いIDがあります\n")
    count = 0
    fsort.seek(0)

fsort.close()
fth.close()
fw.close()

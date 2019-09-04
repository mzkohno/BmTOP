
f = open("tblastx_HitTable_sorted_trimABC.txt", 'r')
fw = open("tblastx_HitTable_THlisted_trimABC.txt", 'w')

r = f.readline()  #一行目の目次の読み飛ばし
fw.write(r) #目次の書き出し

r = f.readline()
r0 = r
r0_spl = r0.split('\t')



for r in f:
    r_spl = r.split('\t')
    if r0_spl[0] != r_spl[0]:
        fw.write(r0)
        r0 = r
        r0_spl = r0.split('\t')

fw.write(r0)


f.close()
fw.close()

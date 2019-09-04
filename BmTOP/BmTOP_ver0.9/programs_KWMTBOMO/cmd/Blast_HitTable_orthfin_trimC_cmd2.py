

f = open("tblastx_HitTable_sorted_trimAB.txt", 'r')
fthr = open("BHTOF_threshold_指定表.txt", 'r')
fwr = open("tblastx_HitTable_sorted_trimABC_REMOVED.txt", 'w')
fwe = open("tblastx_HitTable_sorted_trimABC.txt", 'w')

r = f.readline()  #一行目の目次の読み飛ばし
fwr.write(r) #目次の書き出し
fwe.write(r) #目次の書き出し

r = f.readline()
r0 = r
r0_spl = r0.split('\t')


#しきい値のダウンロード
count = 0

for rthr in fthr:
    count += 1
    if count == 14:
        thr = float(rthr)
    elif count == 18:
        thr0 = float(rthr)


#実際の処理
swit = 1

for r in f:
    r_spl = r.split('\t')
    if r0_spl[0] == r_spl[0]:
        # Second hit以降の処理
        if swit == 2:
            fwr.write(r0)
        elif swit == 0:
            fwe.write(r0)
        # Top hitの処理
        elif float(r0_spl[5]) != 0.0:
            if (float(r0_spl[5]) / float(r_spl[5])) >= thr:
                fwr.write(r0)
                swit += 1
            elif (float(r0_spl[5]) / float(r_spl[5])) < thr:
                fwe.write(r0)
                swit -= 1
        elif float(r0_spl[5]) == 0.0:
            if float(r_spl[5]) < thr0:
                fwr.write(r0)
                swit += 1
            elif float(r_spl[5]) >= thr0:
                fwe.write(r0)
                swit -= 1
        else:
            print("ERROR\n")
    else:
        # 次のTrinity IDに移る
        if swit == 2:
            fwr.write(r0)
            swit = 1
        elif swit == 0:
            fwe.write(r0)
            swit = 1
        else:
            fwe.write(r0)
    r0 = r
    r0_spl = r0.split('\t')

#最後の行の処理
if swit == 2:
    fwr.write(r0)
    swit = 1
elif swit == 0:
    fwe.write(r0)
    swit = 1
else:
    fwe.write(r0)


f.close()
fwr.close()
fwe.close()

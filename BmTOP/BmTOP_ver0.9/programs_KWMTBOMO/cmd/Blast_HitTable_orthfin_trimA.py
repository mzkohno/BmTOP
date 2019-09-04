print("\nプログラム「TrimA」を実行します\n")

ft = open("tblastx_HitTable_THlisted.txt", "r")
fsq = open("tblastx_HitTable_sorted.txt", "r")
fsd = open("tblastx_HitTable_sorted.txt", "r")
ftw = open("tblastx_HitTable_THlisted_trimA.txt", "w")

rsq = fsq.readline()  #一行目の目次の読み飛ばし
rsd = fsd.readline()
rt = ft.readline()
ftw.write(rsq)#目次の書き出し


count = 0
swit = 0

rt = ft.readline()    #Top hit listの値一行目の取得
rt_spl = rt.split('\t')

for rsq in fsq:
    rsq_spl = rsq.split('\t')
    if rt_spl[0] == rsq_spl[0]:
        if swit >= 1:
            continue
        for rsd in fsd:
            rsd_spl = rsd.split('\t')
            if rsq_spl[1] == rsd_spl[1]:
                count += 1
            if count >= 2:
                swit += 1
                break
        count = 0
        fsd.seek(0)
    elif rt_spl[0] != rsq_spl[0]:
        if swit == 0:
            ftw.write(rt)
            rt = ft.readline()
            rt_spl = rt.split('\t')
        else:
            rt = ft.readline()
            rt_spl = rt.split('\t')
            swit = 0
        for rsd in fsd:
            rsd_spl = rsd.split('\t')
            if rsq_spl[1] == rsd_spl[1]:
                count += 1
            if count >= 2:
                swit += 1
                break
        count = 0
        fsd.seek(0)
 
#最後の行の処理
if swit == 0:
    ftw.write(rt)


ft.close()
fsq.close()
fsd.close()
ftw.close()

print("プログラム「TrimA」が正常に完了しました\n")


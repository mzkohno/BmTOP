print("\nプログラム「TrimB」を実行します\n")

f = open("tblastx_HitTable_THlisted_trimA.txt", "r")
fthr = open("BHTOF_threshold_指定表.txt", "r")
fw = open("tblastx_HitTable_THlisted_trimAB.txt", "w")

r = f.readline()  #一行目の目次の読み飛ばし
fw.write(r) #目次の書き出し

#しきい値のダウンロード
count = 0

for rthr in fthr:
    count += 1
    if count == 6:
        thre = float(rthr)
    elif count == 10:
        thrs = float(rthr)

#しきい値との比較
for r in f:
    r_spl = r.split('\t')
    if float(r_spl[5]) <= thre:
        if float(r_spl[6]) >= thrs:
            fw.write(r)

f.close()
fthr.close()
fw.close()

print("プログラム「TrimB」が正常に完了しました\n")

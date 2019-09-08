# sorted listがTHlistを利用して作られることを利用したアルゴリズム
print("\nプログラム「TrimA」を実行します\n")

ft = open("tblastx_HitTable_THlisted.txt", "r")
fs = open("tblastx_HitTable_sorted.txt", "r")
ftw = open("tblastx_HitTable_THlisted_trimA.txt", "w")

rs = fs.readline()  #一行目の目次の読み飛ばし
rt = ft.readline()    #一行目の目次の読み飛ばし
ftw.write(rt)#目次の書き出し


count = 0
swit = 0


for rt in ft:
    rt_spl = rt.split('\t')
    for rs in fs:
        rs_spl = rs.split('\t')
        if rt_spl[1] == rs_spl[1]:
            count += 1
        if count >= 2:
            swit += 1
            break
    if swit == 0:
        ftw.write(rt)
    count = 0
    swit = 0
    fs.seek(0)


ft.close()
fs.close()
ftw.close()

print("プログラム「TrimA」が正常に完了しました\n")


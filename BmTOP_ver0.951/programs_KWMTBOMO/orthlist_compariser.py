# 任意の2つのTop hit list (orthlist)を比較する
# AにあるのにBにないID(OnlyA_ID.txt)。
# BにあるのにAにないID(OnlyB_ID.txt)。
# 両方にあるID(Both_having_ID.txt)。
## ※Aが持っているうち、Bも持っているもの。

# ※Blast_HitTable_orthfin.outによって出力されたファイルを利用する


while True:
    print('\n比較に用いるファイル名を2つ記入してください')
    print('※ テキストファイル限定(.txt)。')
    #目次がないと一行目の解析がされないバグが生じる
    filename1 = input("filename1: tblastx_HitTable_THlisted_trimABC_orthlist_")
    if '.txt' in filename1:
        filename2 = input("filename2: tblastx_HitTable_THlisted_trimABC_orthlist_")
        if '.txt' in filename2:
            break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')


fA = open("tblastx_HitTable_THlisted_trimABC_orthlist_"+ filename1, 'r')
# 例: Sensitive(ThresholdB80C80)
fB = open("tblastx_HitTable_THlisted_trimABC_orthlist_"+ filename2, 'r')
# 例: Rough(ThresholdB20C20)
# ※事前にファイル名を変えておくこと

fwA = open("Only"+ filename1.rstrip(".txt") +"_ID.txt", 'w')	#出力用ファイル
fwB = open("Only"+ filename2.rstrip(".txt") +"_ID.txt", 'w')	#出力用ファイル
fwAB = open("Both_"+filename1.rstrip(".txt") + "&" + filename2.rstrip(".txt") +"_ID.txt", 'w')	#出力用ファイル

countM = 0


rA = fA.readline() #一行目の目次の読み飛ばし
fwA.write(rA) #目次の出力
fwB.write(rA)
fwAB.write(rA)

#AからBを解析
for rA in fA:
    rA_spl = rA.split('\t')
    for rB in fB:
        rB_spl = rB.split('\t')
        if rA == rB:
            fwAB.write(rA)
            countM += 1
        if countM >=2:
            print("\nERROR: 同じIDが2つ以上存在する\n")
    if countM == 0:
        fwA.write(rA)
    countM = 0
    fB.seek(0)

#BからAを解析
fA.seek(0)
rB = fB.readline() #一行目の目次の読み飛ばし

for rB in fB:
    rB_spl = rB.split('\t')
    for rA in fA:
        rA_spl = rA.split('\t')
        if rB == rA:
            countM += 1
        if countM >=2:
            print("\nERROR: 同じIDが2つ以上存在する\n")
    if countM == 0:
        fwB.write(rB)
    countM = 0
    fA.seek(0)

fA.close()
fB.close()
fwA.close()
fwB.close()
fwAB.close()

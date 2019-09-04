### 「任意のファイル」のKWMTBOMO_IDが記載されたカラムを利用して、
### 「任意のファイル」と比較し、
### 	出力1. クエリーの項目のうち、比較対象に存在する項目のみを抽出したファイル
###      i.e. query && 比較対象
### 	出力2. クエリーの項目のうち、比較対象に存在しない項目のみを抽出したファイル
###      i.e. query && !(query && 比較対象)
# 2019.3.7 BmCorTable_compariser_withorthlist_cmd2.pyをマイナーチェンジして作成した
# 2019.7.1 KWMTBOMO_orthlistCompariser.pyをさらに改変
# BmCorTable_compariser_withorthlistでできることは本プログラムでも実行可能

import sys

"""
print("\n\n")
print("「KWMTBOMO_IDが、特定カラムに存在するTable」2つを比較する")
print("	出力1. クエリーの項目のうち、カイコ単一遺伝子リストに存在する項目のみを抽出したファイル（ファイル名_BmSG）\n i.e. query && カイコ単一遺伝子リスト")
print("	出力2. クエリーの項目のうち、カイコ単一遺伝子リストに存在しない項目のみを抽出したファイル（ファイル名_notBmSG）\n i.e. query && !(query && カイコ単一遺伝子リスト)")
print("※ BmSG: Bombyx mori Single Gene")
print("\n\n")
"""

countM = 0
try:
    fdb = open("BmSingleGeneList.txt", 'r') #比較対象ファイル
except FileNotFoundError:
    print("BmSingleGeneList.txtファイルがありません\n")
    sys.exit()
fq = open("tblastx_HitTable_THlisted_trimABC.txt", 'r')    #クエリー用ファイル
fw = open("tblastx_HitTable_THlisted_trimABC_BmSG.txt", 'w')
fw3 = open("tblastx_HitTable_THlisted_trimABC_notBmSG.txt", 'w')


rq = fq.readline()  #一行目の目次の読み飛ばし
rdb = fdb.readline()
fw.write(rq) #目次の書き出し
fw3.write(rq)

for rq in fq:
    rq_spl = rq.split('\t')
    for rdb in fdb:
        rdb_spl = rdb.split('\t')
        if rq_spl[1] in rdb_spl[0]: #カイコ単一遺伝子リストは、KWMTBOMO_IDをカラム0に記入すること！！
            fw.write(rq)
            countM += 1
            break
    if countM == 0:
        fw3.write(rq)
    countM = 0
    fdb.seek(0)

fdb.close()
fq.close()
fw.close()
fw3.close()



### 以下、「_THlist_BmSG.txt」から「_sorted_BmSG.txt」を出力するスクリプト ###

fsort = open("tblastx_HitTable_sorted_trimABC.txt", 'r')
fth = open("tblastx_HitTable_THlisted_trimABC_BmSG.txt", 'r')
fw = open("tblastx_HitTable_sorted_trimABC_BmSG.txt", 'w')
"""
fnth = open("tblastx_HitTable_THlisted_trimABC_notBmSG.txt", 'r')
fnw = open("tblastx_HitTable_sorted_trimABC_notBmSG.txt", 'w')
"""

rsort = fsort.readline()  #一行目の目次の読み飛ばし
rsort_spl = rsort.split('\t') #一周目のrsort_spl[0]創出のため
rth = fth.readline()
fw.write(rsort) #目次の書き出し
"""
rnth = fnth.readline()
fnw.write(rsort)
"""

swit = 0

# BmSG
for rth in fth:
    rth_spl = rth.split('\t')
    if rth_spl[0] in rsort_spl[0]: #一周目はrsort_spl[0]は目次項目（Trinity_ID）なので、同じにはならないはず
        fw.write(rsort)
        swit += 1
    for rsort in fsort:
        rsort_spl = rsort.split('\t')
        if rth_spl[0] in rsort_spl[0]:
            fw.write(rsort)
            swit += 1
        elif swit >= 1:
            break
    swit = 0
    # IDは上から順に並んでいる前提なので、ここでf.seek(0)は行わない
    # sortedはTHlistedから創出されているので、これらのIDの並びが異なることはない。だからf.seek(0)はなしでOK

"""
# notBmSG(時間がかかるので、やらない)
for rnth in fnth:
    rnth_spl = rnth.split('\t')
    if rnth_spl[0] in rsort_spl[0]: #一周目はrsort_spl[0]は目次項目（Trinity_ID）なので、同じにはならないはず
        fnw.write(rsort)
        swit += 1
    for rsort in fsort:
        rsort_spl = rsort.split('\t')
        if rnth_spl[0] in rsort_spl[0]:
            fnw.write(rsort)
            swit += 1
        elif swit >= 1:
            break
    swit = 0
"""

fsort.close()
fth.close()
fw.close()
"""
fnth.close()
fnw.close()
"""

###

print("プログラム「ListCompariser_vsBmSG」が正常に完了しました\n\n\n")

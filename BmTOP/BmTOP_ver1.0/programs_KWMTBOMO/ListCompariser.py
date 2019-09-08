### 「任意のファイル」のGeneModel or contig_IDが記載されたカラムを利用して、
### 「任意のファイル」と比較し、
### 	出力1. クエリーの項目のうち、比較対象に存在する項目のみを抽出したファイル
###      i.e. query && 比較対象
### 	出力2. クエリーの項目のうち、比較対象に存在しない項目のみを抽出したファイル
###      i.e. query && !(query && 比較対象)
# 2019.3.7 BmCorTable_compariser_withorthlist_cmd2.pyをマイナーチェンジして作成した
# 2019.7.1 KWMTBOMO_orthlistCompariser.pyをさらに改変
# BmCorTable_compariser_withorthlistでできることは本プログラムでも実行可能


print("\n" + "#" * 60)
print("「GeneModel or contig IDが、特定カラムに存在するTable」2つを比較する")
print("	出力1. クエリーの項目のうち、比較対象に存在する項目のみを抽出したファイル（ファイル名_both）\n i.e. query && 比較対象")
print("	出力2. クエリーの項目のうち、比較対象に存在しない項目のみを抽出したファイル（ファイル名_qonly）\n i.e. query && !(query && 比較対象)")
print("#" * 60 + "\n")


while True:
    print('\nクエリー用ファイル名を記入してください')
    print('※ テキストファイル限定(.txt)')
    filename_fq = input("filename: ")
    if '.txt' in filename_fq:
        break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')

precount = 0	#precount変数の宣言
while precount == 0:
    print('\nクエリーファイルの、KWMTBOMOナンバーが記入されているカラム番号を記入してください')  #例: 2
    print('(一番左のカラムを0として、0, 1, 2......と数える)')
    columnq_inp = input("column#: ")
    if len(columnq_inp) == 0:
        continue
    columnq = int(columnq_inp)
    precount += 1

while True:
    print('\n比較対象のファイル名を記入してください')
    print('※ テキストファイル限定(.txt)')
    filename_fdb = input("filename: ")
    if '.txt' in filename_fdb:
        break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')

precount = 0	#precount変数の宣言2
while precount == 0:
    print('\n比較対象ファイルの、KWMTBOMOナンバーが記入されているカラム番号を記入してください')  #例: 2
    print('(一番左のカラムを0として、0, 1, 2......と数える)')
    columndb_inp = input("column#: ")
    if len(columndb_inp) == 0:
        continue
    columndb = int(columndb_inp)
    precount += 1

while True:
    print('\n出力用ファイル名を記入してください')
    print('※ テキストファイル限定(.txt)')
    filename_w = input("filename: ")
    if '.txt' in filename_w:
        break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')


countM = 0
fq = open(filename_fq, 'r')    #クエリー用ファイル（例: BmCorTable_Misof.txt）
fdb = open(filename_fdb, 'r') #比較対象ファイル
fw = open(filename_w.rstrip('.txt') + "_both.txt", 'w')
fw3 = open(filename_w.rstrip('.txt') + "_qonly.txt", 'w') #qonly == query only


rq = fq.readline()  #一行目の目次の読み飛ばし
rdb = fdb.readline()
fw.write(rq) #目次の書き出し
fw3.write(rq)

for rq in fq:
    rq_spl = rq.split('\t')
    for rdb in fdb:
        rdb_spl = rdb.split('\t')
        if rq_spl[columnq] in rdb_spl[columndb]:
            fw.write(rq)
            countM += 1
    if countM == 0:
        fw3.write(rq)
    elif countM >= 2:
        print("※クエリーの" + rp + "が、比較対象に" + countM + "個存在しています\n")
    countM = 0
    fdb.seek(0)

fdb.close()
fq.close()
fw.close()
fw3.close()

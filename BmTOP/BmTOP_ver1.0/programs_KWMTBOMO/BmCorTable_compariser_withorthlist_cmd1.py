### 「BmCorTable_extracter.py処理で得られた出力ファイル」を利用して、
### 「tblastx_HitTable_THlisted_trimABC_orthlist.txt」の結果と比較し、
### 	出力1. KWMTBOMO_ID or BGIBMGA_IDが共通する項目のみを抽出したファイルを作成する
### 	出力2. orthlistに項目を追加したファイルを作成する


print("\n" + "#" * 80)
print("「BmCorTable_preparator.py処理で得られた出力ファイル」を利用して、")
print("「tblastx_HitTable_THlisted_trimABC_orthlist.txt」の結果と比較し、")
print("	出力1. KWMTBOMO_IDが共通する項目のみを抽出したファイルを作成する")
print("	出力2. orthlistに項目を追加したファイルを作成する")
print("#" * 80 + "\n")


while True:
    print('\nクエリー用ファイル名を記入してください')
    print("例: BmCorTable_Misof.txt")
    print('※ テキストファイル限定')
    filename_f = input("filename: ")
    if '.txt' in filename_f:
        break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')


while True:
    print('\n出力用ファイル名を記入してください')
    print("例: ..._orthlist_onlyMisof.txt, ..._orthlist_Misof.txt, ..._orthlist_notMisof.txt")
    print('※ テキストファイル限定')
    filename_w = input("filename_1: tblastx_HitTable_THlisted_trimABC_orthlist_")
    if '.txt' in filename_w:
        break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')


print('\n出力ファイルに追加する項目名を記入してください')
print("例: Misof2014")
itemname = input("item: ")



countM = 0
countM2 = 0
k = 0
f = open("tblastx_HitTable_THlisted_trimABC_orthlist.txt", 'r') #比較して出力するためのファイル
fM = open(filename_f, 'r')    #クエリー用ファイル（例: BmCorTable_Misof.txt）
fw = open("tblastx_HitTable_THlisted_trimABC_orthlist_only" + filename_w, 'w')	#出力用ファイル（例: tblastx_......_orthlist_onlyMisof.txt）
fw2 = open("tblastx_HitTable_THlisted_trimABC_orthlist_" + filename_w, 'w')	#出力用ファイル（例: tblastx_......_orthlist_Misof.txt）
fw3 = open("tblastx_HitTable_THlisted_trimABC_orthlist_not" + filename_w, 'w')	#出力用ファイル（例: tblastx_......_orthlist_notMisof.txt）


rM = fM.readline()  #一行目の目次の読み飛ばし
r = f.readline()
fw.write(r) #目次の書き出し
fw3.write(r)
fw2.write(r.strip("\n") + "\t" + itemname + "\t" + 'count' + "\n")

for r in f:
    r_spl = r.split('\t')
    for k in range(1):
        if 'BGIBMGA' in r_spl[1]:
            i = 0
            j = 2
        elif 'KWMTBOMO' in r_spl[1]:
            i = 2
            j = 0
        else:
            print('error')
            f.close()
            fM.close()
            fw.close()
            fw2.close()
            quit()
    for rM in fM:
        rM_spl = rM.split('\t')
        if rM_spl[i] == r_spl[1]:
            countK = str(countM + 1)
            fw.write(r)
            fw2.write(r.strip("\n") + "\t" + rM_spl[j] + "\t" + countK + "\n")
            countM += 1
    if countM == 0:
        fw3.write(r)
        fw2.write(r.strip("\n") + "\tN\t0\n")
    countM = 0
    fM.seek(0)


f.close()
fM.close()
fw.close()
fw2.close()
fw3.close()



fadd = open("tblastx_HitTable_THlisted_trimABC_orthlist_" + filename_w, 'r')
faddw = open("tblastx_HitTable_THlisted_trimABC_orthlist_single_only" + filename_w, 'w')
faddw2 = open("tblastx_HitTable_THlisted_trimABC_orthlist_single_" + filename_w, 'w')

radd = fadd.readline()
faddw.write(radd)
faddw2.write(radd)

for radd in fadd:
    radd_spl = radd.split('\t')
    raddint = int(radd_spl[8])
    if raddint < 1:
        faddw2.write(radd)
    elif raddint >= 1:
        faddw.write(radd)
        faddw2.write(radd)

fadd.close()
faddw.close()
faddw2.close()

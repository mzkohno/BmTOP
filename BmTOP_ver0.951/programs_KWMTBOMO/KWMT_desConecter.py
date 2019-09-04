## KWMTBOMO基準で、どんなファイルにもアノテーション情報を付与できるように設計したプログラム
## 'KWMTBOMO.desc.txtをソースファイルとして使用

precount = 0

while True:
    print('\nKWMTBOMO description dataを追加したいファイル名を記入してください')
    print('※ テキストファイル限定')
    filename = input("filename: ")
    if '.txt' in filename:
        break
    print('\n拡張子「.txt」を含んだ正しい名前で入力してください')

while precount == 0:
    print('\nKWMTBOMOナンバーが記入されているカラム番号を記入してください')
    print('(一番左のカラムを0として、0, 1, 2......と数える)')
    column_inp = input("column#: ")
    if len(column_inp) == 0:
        continue
    column = int(column_inp)
    precount += 1


f = open(filename, 'r')
fKWMT = open('KWMTBOMO.desc.txt', 'r')
w = open(filename.rstrip('.txt') + '_desc.txt', 'w')

# 目次飛ばし
rKWMT = fKWMT.readline()
# 目次作成
r = f.readline()
w.write(r.strip("\n") + '\tBLAST (UniRef)\tKWMTBOMO_length(bp)\n')

if len(rKWMT) == 0 or len(r) == 0:
    print('\nカレントディレクトリに指定ファイルが存在するか確認してください\n')
    f.close()
    fKWMT.close()
    w.close()
    quit()


for r in f:
    r_spl = r.split('\t')
    for rKWMT in fKWMT:
        rKWMT_spl = rKWMT.split('\t')
        if len(rKWMT_spl[0]) == 0:
            continue
        if rKWMT_spl[1] == r_spl[column]:
            rk = '\t' + rKWMT_spl[3]
            rKWMT = fKWMT.readline()
            rKWMT_spl = rKWMT.split('\t')
            w.write(r.strip("\n") + rk + '\t' + rKWMT_spl[1].strip(' bp') + '\n')
            break
    if len(rKWMT) == 0:
        w.write(r.strip("\n") + 'ND\tND\n')
    fKWMT.seek(0)

f.close()
fKWMT.close()
w.close()

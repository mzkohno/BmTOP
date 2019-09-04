# Blast_HitTable_lister_noIso_qSB.py
# (noIso = nothing isoforms)
# isoformを考えないTop Hit lister かつ 全BLAST結果のlister
# ...Trinity_IDには使用不可
### さらに、カイコGeneModelをクエリーにした場合向けの解析法!!!
### （出力結果をorthfinにそのまま使うと、多分バグる）

f = open("tblastx_HitTable.txt", 'r')
fgff3 = open("KWMTBOMO.gff3.txt", 'r')
w = open('tblastx_HitTable_THlisted.txt', 'w')
w2 = open('tblastx_HitTable_sorted.txt', 'w')

counter = 0
error = 0

# 一行目の目次。項目を変えた場合、ここも書き換える！！
w.write("Trinity_ID\tSB_ID\tSB_chr\tSB_start\tSB_end\tevalue\tbitscore\n")
w2.write("Trinity_ID\tSB_ID\tSB_chr\tSB_start\tSB_end\tevalue\tbitscore\n")

print("\n\n以下の項目を「tblastx_HitTable_THlisted.txt」と\n\
「tblastx_HitTable_sorted.txt」に出力します\n\n\
Trinity_ID\nSB_ID\nSB_chr\nSB_start\nSB_end\nevalue\nbitscore\n")


#TopHitlister

# 一行目のDL
rref = f.readline()
rref_spl = rref.split('\t')
#gff3DL
for rgff3 in fgff3:
    rgff3_spl = rgff3.split('\t')
    if rref_spl[0] in rgff3_spl[8]: ### ★ここをrref_spl[1]から[0]にして、クエリー側を参照している
        counter += 1
        break
if counter == 0:
    print("gff3ファイルエラー0\n")
    error += 1
counter = 0
fgff3.seek(0)
#

for r in f:
    r_spl = r.split('\t')
    if not(rref_spl[0] in r_spl[0]):
        w.write(rref_spl[0] +'\t'+ rref_spl[1] +'\t'+ rgff3_spl[0] +'\t'+\
         rgff3_spl[3] +'\t'+ rgff3_spl[4] +'\t'+ rref_spl[10] +'\t'+ rref_spl[11])
        rref = r
        rref_spl = rref.split('\t')
        # gff3DL
        for rgff3 in fgff3:
            rgff3_spl = rgff3.split('\t')
            if rref_spl[0] in rgff3_spl[8]: ### ★
                counter += 1
                break
        if counter == 0:
            print("gff3ファイルエラー1\n")
            error += 1
            break
        counter = 0
        fgff3.seek(0)
        #
#最後の行
w.write(rref_spl[0] +'\t'+ rref_spl[1] +'\t'+ rgff3_spl[0] +'\t'+\
rgff3_spl[3] +'\t'+ rgff3_spl[4] +'\t'+ rref_spl[10] +'\t'+ rref_spl[11])
f.seek(0)
w.close()


#lister(_sorted出力)

# 一行目のDL
rref = f.readline()
rref_spl = rref.split('\t')
#gff3DL
for rgff3 in fgff3:
    rgff3_spl = rgff3.split('\t')
    if rref_spl[0] in rgff3_spl[8]: # ★
        counter += 1
        break
if counter == 0:
    print("gff3ファイルエラー2\n")
    error += 1
counter = 0
fgff3.seek(0)
#
for r in f:
    r_spl = r.split('\t')
    if not(rref_spl[0] in r_spl[0]) or not(rref_spl[1] in r_spl[1]):
        w2.write(rref_spl[0] +'\t'+ rref_spl[1] +'\t'+ rgff3_spl[0] +'\t'+\
         rgff3_spl[3] +'\t'+ rgff3_spl[4] +'\t'+ rref_spl[10] +'\t'+ rref_spl[11])
        rref = r
        rref_spl = rref.split('\t')
        # gff3DL
        for rgff3 in fgff3:
            rgff3_spl = rgff3.split('\t')
            if rref_spl[0] in rgff3_spl[8]: # ★
                counter += 1
                break
        if counter == 0:
            print("gff3ファイルエラー3\n")
            error += 1
            break
        counter = 0
        fgff3.seek(0)
        #
#最後の行
w2.write(rref_spl[0] +'\t'+ rref_spl[1] +'\t'+ rgff3_spl[0] +'\t'+\
 rgff3_spl[3] +'\t'+ rgff3_spl[4] +'\t'+ rref_spl[10] +'\t'+ rref_spl[11])

w2.close()
f.close()
fgff3.close()

print("Blast_HitTable_lister_noIso.pyが完了しました\n")

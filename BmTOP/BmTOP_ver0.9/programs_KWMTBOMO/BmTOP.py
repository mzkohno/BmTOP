class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m' #白またはグレー
    END = '\033[0m'
    BOLD = '\038[1m' #なぜかうまくいかない
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m' #塗りつぶし
    REVERCE = '\033[07m'

import subprocess
import sys
import os

print(pycolor.BLUE + "\n"+ "-"*60 + "\n" + pycolor.END)
print(pycolor.BLUE + "本アプリケーションには、python3とblast+(NCBI)を使用します\n\
事前にDLをお願いいたします\n\n" + pycolor.END)

print(pycolor.BLUE + "本アプリケーションでは、下記のファイル群を使用します\n\
workspaceディレクトリ(カレントディレクトリ)にすべて用意してください\n\n\
[BmTOP]\n\
・KWMTBOMO.gff3.txt......Silkbase_HPよりDL(Bomo_gene_models.gff3をrename)\n\
・BHTOF_threshold_指定表.txt......各種thresholdを指定する\n\
-Trinity.fasta(assembled_data)から解析する場合\n\
 ・Trinity.fasta\n\
 ・KWMTBOMO.nucl.fa......Silkbase_HPよりDL(Bomo_gene_models.nucl.faをrename)\n\
 ・Blastコマンド指定表.txt\n\
-blast_HitTable(blast結果表)を用いる場合\n\
 ・tblastx_HitTable.txt......*ファイル名を左記にご変更ください\n\n\
[KWMT_desConecter]\n\
・KWMTBOMO_IDの記入があるファイル\n\
・KWMTBOMO.desc.txt......Silkbase_HPのLibrary_Informationを参考に作成\n\
[orthlist_compariser]\n\
・比較に用いる2つのtblastx_HitTable_THlisted_trimABC_orthlist_[任意].txtファイル\n" + pycolor.END)

print(pycolor.BLUE + "\n\n*1 BmTOPは、「Trinityによるde novo assembled dataをqueryに、\n\
カイコGeneModels(2017)をblast+(NCBI)で解析したBLAST_Hit_Table」\n\
を対象として構築されております\n\n\
それ以外のTableを解析に用いますと、想定外の挙動をとる恐れがありますのでご注意ください" + pycolor.END)

print(pycolor.BLUE + "\n\n*2 本アプリケーションはlinux環境向けです\n\
Windowsでは仮想OSやWSLでの実行をお勧めいたします\n" + pycolor.END)

print(pycolor.BLUE + "-"*60 +"\n\n" + pycolor.END)

print(pycolor.GREEN + "BmTOP:Bombyx mori Tool for Ortholog Picker\n\n" + "[menu]\n" + pycolor.END)
print(pycolor.GREEN + "1:BmTOP\n\
2:BmTOP(16条件のオルソログ探索)\n\
3:BmTOP_noIso(Trinity_data以外の解析用:Isoformを考えない解析)\n\
4:BmTOP_noIso(Isoformを考えない16条件のオルソログ探索)\n\
5:KWMT_desConecter\n\
6:KWMT_orthlistCompariser\n\
7:exit\n\n" + pycolor.END)

while 1:
    precom = input("command: ")
    if precom.isdecimal() != True:
        print("数字を入力してください\n\n")
        continue
    if precom == "1":
        break
    elif precom == "2":
        break
    elif precom == "3":
        break
    elif precom == "4":
        break
    elif precom == "5":
        break
    elif precom == "6":
        break
    elif precom == "7":
        print("BmTOPを実行しませんでした\n\n")
        sys.exit()
    else:
        print("数字を入力してください\n\n")
        continue

com = int(precom)


count = 0
mbdswit = 0

if com >= 1 and com <= 4:
    print(pycolor.GREEN + "\n############################################################\n\n\
BmTOPを実行します\n" + pycolor.END)
    print(pycolor.GREEN + "解析に用いるデータタイプを選択してください\n\n" + pycolor.END)
    #カレントディレクトリにTrinity.fastaとKWMTBOMO.nucl.faがあるか判定
    Tri_isfile = os.path.isfile("./Trinity.fasta")
    KWMT_isfile = os.path.isfile("./KWMTBOMO.nucl.fa")
    #カレントディレクトリにKWMTBOMO.nucl.fa.nhrがあるか判定
    mdb_isfile = os.path.isfile("./KWMTBOMO.nucl.fa.nhr")
    #カレントディレクトリにtblastx_HitTable.txtがあるか判定
    bTH_isfile = os.path.isfile("./tblastx_HitTable.txt")
    if Tri_isfile == True and KWMT_isfile == True:
        print(pycolor.GREEN + "A:カイコGeneModelsのデータベース化とtblastx解析が必要\n" + pycolor.END)
        print(pycolor.GREEN + "B:カイコGeneModelsのデータベース化とblastn解析が必要\n" + pycolor.END)
    else:
        print(pycolor.WHITE + "A:カイコGeneModelsのデータベース化とtblastx解析が必要\n" + pycolor.END)
        print(pycolor.WHITE + "B:カイコGeneModelsのデータベース化とblastn解析が必要\n" + pycolor.END)
    if mdb_isfile == True and Tri_isfile == True and KWMT_isfile == True:
        print(pycolor.GREEN + "C:tblastx解析が必要\n" + pycolor.END)
        print(pycolor.GREEN + "D:blastn解析が必要\n" + pycolor.END)
    else:
        print(pycolor.WHITE + "C:tblastx解析が必要\n" + pycolor.END)
        print(pycolor.WHITE + "D:blastn解析が必要\n" + pycolor.END)
    if bTH_isfile == True:
        print(pycolor.GREEN + "E:blast済(tblastx_HitTable.txt準備済)\n" + pycolor.END)
    else:
        print(pycolor.WHITE + "E:blast済(tblastx_HitTable.txt準備済)\n" + pycolor.END)
    print(pycolor.GREEN + "F:exit\n\n" + pycolor.END)
    while 1:
        blast = input("command: ")
        if (blast == "E" and bTH_isfile == True):
            break
        elif blast == "F":
            print("BmTOPを実行しませんでした\n\n")
            sys.exit()
        if (blast == "D" or blast == "C" or blast == "B" or blast == "A"):
            #blast用コマンドファイルの読みこみ
            cmdfile = open("Blastコマンド指定表.txt", "r")
            for allcmd in cmdfile:
                count += 1
                if count == 2:
                    mbdcmd = allcmd
                elif count == 5:
                    bncmd = allcmd
                elif count == 8:
                    tbxcmd = allcmd
            cmdfile.close()
        # makeblastdbの判定（データベース化の有無）
        if ((blast == "A" or blast == "B") and Tri_isfile == True and KWMT_isfile == True):
            subprocess.call(mbdcmd.split())
            mbdswit += 1
        # blastn or tblastx (※出力ファイル名はすべてtblastx_HitTable.txt)
        if ((blast == "B" or blast == "D") and (mdb_isfile == True or mbdswit == 1)):
            print("\nblastn解析中です")
            subprocess.call(bncmd.split())
            print("\nblastn解析が終了しました\n")
            break
        elif ((blast == "A" or blast == "C") and (mdb_isfile == True or mbdswit == 1)):
            print("\ntblastx解析中です")
            subprocess.call(tbxcmd.split())
            print("\ntblastx解析が終了しました\n")            
            break
        print("有効なコマンドを入力してください(英語は大文字)\n")
    # THlister and lister
    if com >=1 and com <= 2:
        subprocess.call(["../programs_KWMTBOMO/Blast_HitTable_THlister.out"])
        subprocess.call(["../programs_KWMTBOMO/Blast_HitTable_lister.out"])
    elif com >= 3 and com <= 4:
        subprocess.call(["python3", "../programs_KWMTBOMO/Blast_HitTable_lister_noIso.py"])
    # orthfin
    if com == 1 or com == 3:
        subprocess.call(["python3", "../programs_KWMTBOMO/Blast_HitTable_orthfin.py"])
    elif com == 2 or com == 4:
        subprocess.call(["python3", "../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimA.py"])
        subprocess.call(["python3", "../programs_KWMTBOMO/Blast_HitTable_orthfin_trimBC_allcond.py"])
    print(pycolor.GREEN + "\n\n############################################################\n\n\
BmTOPが正常に完了しました\n\n" + pycolor.END)


elif com == 5:
    print(pycolor.GREEN + "\n############################################################\n\n\
KWMT_desConecterを実行します\n" + pycolor.END)
    subprocess.call(["python3", "../programs_KWMTBOMO/KWMT_desConecter.py"])
    print(pycolor.GREEN + "\n\n############################################################\n\n\
KWMT_desConecterが正常に完了しました\n\n" + pycolor.END)


elif com == 6:
    print(pycolor.GREEN + "\n############################################################\n\n\
KWMT_orthlistCompariserを実行します\n" + pycolor.END)
    subprocess.call(["python3", "../programs_KWMTBOMO/KWMT_orthlistCompariser.py"])
    print(pycolor.GREEN + "\n\n############################################################\n\n\
KWMT_orthlistCompariserが正常に完了しました\n\n" + pycolor.END)


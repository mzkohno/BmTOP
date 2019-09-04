# ※workspaceで実行する

# ※下記ファイルをworkspaceに用意する
## 「BHTOF_threshold_指定表.txt」
## 「tblastx_HitTable_sorted.txt」
## 「tblastx_HitTable_THlisted_trimA.txt」

# ※「score」と「TopHitのe-valueが0の場合のSecond_Hitの最高値」は
## 事前に決めて、指定表に記述しておく

# やること: B20C20-B80C80の全条件を実行し、ファイルを作成して振り分ける

import subprocess

print("\n「Blast_HitTable_orthfin.out」のプログラムTrimB, TrimC を、\n")
print("B20,40,60,80、C20,40,60,80の全条件で実行します\n")

listB = [1e-20, 1e-40, 1e-60, 1e-80]
listC = [1e-20, 1e-40, 1e-60, 1e-80]

countmv = 0

for B in listB:
    titleB = "B" + str(B)
    countmv = 0
    for C in listC:
        titleC = "C" + str(C)
        #
        print(titleB + titleC + "での処理を実行中\n")
        # 「BHTOF_threshold_指定表.txt」の作成
        ###################################
        fBmTOP = open("BHTOF_threshold_指定表.txt", "r")
        fBmTOPw = open("BHTOF_threshold_指定表_copy.txt", "w")

        countBmTOP = 0

        for rBmTOP in fBmTOP:
            countBmTOP += 1
            if countBmTOP == 6:
                fBmTOPw.write(str(B) + "\n")
            elif countBmTOP == 14:
                fBmTOPw.write(str(C) + "\n")
            else:
                fBmTOPw.write(rBmTOP)

        fBmTOP.close()
        fBmTOPw.close()

        cmdBmTOP = "mv -f BHTOF_threshold_指定表_copy.txt BHTOF_threshold_指定表.txt"
        subprocess.call(cmdBmTOP.split())
        ###################################
        #
        #実行
        if countmv == 0:
            cmd = "python3 ../programs_KWMTBOMO/Blast_HitTable_orthfin_trimBC.py"
            subprocess.call(cmd.split())
        else:
            cmd = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimC_cmd23.py"
            subprocess.call(cmd.split())
        ### vsBmSG ###
        subprocess.call(["python3", "../programs_KWMTBOMO/cmd/ListCompariser_vsBmSG.py"])
        ### 最終結果を_orthlist.txtに出力する ###
        subprocess.call(["python3", "../programs_KWMTBOMO/BmTOP_mkorthlist.py"])
        #
        # ディレクトリの作成、移動
        subprocess.call(["mkdir", titleB + titleC])
        #
        if countmv == 3:
            subprocess.call(["mv", "tblastx_HitTable_THlisted_trimAB.txt", "./" + titleB + titleC])
        else:
            subprocess.call(["cp", "tblastx_HitTable_THlisted_trimAB.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_THlisted_trimABC.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_THlisted_trimABC_BmSG.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_THlisted_trimABC_notBmSG.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_THlisted_trimABC_orthlist.txt", "./" + titleB + titleC])
        if countmv == 3:
            subprocess.call(["mv", "tblastx_HitTable_sorted_trimAB.txt", "./" + titleB + titleC])
        else:
            subprocess.call(["cp", "tblastx_HitTable_sorted_trimAB.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_sorted_trimABC.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_sorted_trimABC_REMOVED.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_sorted_trimABC_BmSG.txt", "./" + titleB + titleC])
        subprocess.call(["mv", "tblastx_HitTable_sorted_trimABC_orthlist.txt", "./" + titleB + titleC])
        subprocess.call(["cp", "BHTOF_threshold_指定表.txt", "./" + titleB + titleC])
        countmv += 1

print("「Blast_HitTable_orthfin.out」プログラムTrimB, TrimC が全条件で正常に完了しました\n")

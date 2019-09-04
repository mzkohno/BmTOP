import subprocess
import sys
import os
import shutil

#現在実行中のプログラムの所在地(パス)を確認
#print("\nBmTOP.pyのパス: ")
BmTOP_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
# 以下デバッグ用スクリプト
#print(BmTOP_dir)
#subprocess.call(["python3", BmTOP_dir + "/zhello.py"])

# 実行中プログラムのディレクトリから、workspaceにカレントディレクトリを移動
os.chdir(BmTOP_dir)
current_dir = os.chdir("../workspace")
#print("カレントディレクトリ: \n" + os.getcwd())

print("BmTOP (Bombyx mori Tool for Ortholog Picker)\nversion 0.9")

mark = 0
res = 0

#移動するディレクトリのevalueリスト
x = [20,40,60,80]
y = [20,40,60,80]

while mark == 0:
    subprocess.call(["python3", "../programs_KWMTBOMO/BmTOP.py"])
    while 1:
        if (os.path.exists("../result/data" + str(res)) == False):
            os.mkdir("../result/data" + str(res))
            os.chmod("../result/data" + str(res), 0o777)
            break
        else:
            res += 1
        if res > 999:
            print("resultファイル作成エラー\n(data1000以上のディレクトリは作れない設定にしてます)\n")
            sys.exit()
    if os.path.exists("./tblastx_HitTable_THlisted.txt") == True:
        shutil.move('./tblastx_HitTable_THlisted.txt', "../result/data" + str(res) + "/tblastx_HitTable_THlisted.txt")
        if os.path.exists("./tblastx_HitTable_THlisted_trimA.txt") == True:
            shutil.move('./tblastx_HitTable_THlisted_trimA.txt', "../result/data" + str(res) + "/tblastx_HitTable_THlisted_trimA.txt")
            if os.path.exists("./tblastx_HitTable_THlisted_trimAB.txt") == True:
                shutil.move('./tblastx_HitTable_THlisted_trimAB.txt', "../result/data" + str(res) + "/tblastx_HitTable_THlisted_trimAB.txt")
            if os.path.exists("./tblastx_HitTable_THlisted_trimABC.txt") == True:
                shutil.move('./tblastx_HitTable_THlisted_trimABC.txt', "../result/data" + str(res) + "/tblastx_HitTable_THlisted_trimABC.txt")
            if os.path.exists("./tblastx_HitTable_THlisted_trimABC_orthlist.txt") == True:
                shutil.move('./tblastx_HitTable_THlisted_trimABC_orthlist.txt', "../result/data" + str(res) + "/tblastx_HitTable_THlisted_trimABC_orthlist.txt")
    if os.path.exists("./tblastx_HitTable_sorted.txt") == True:
        shutil.move('./tblastx_HitTable_sorted.txt', "../result/data" + str(res) + "/tblastx_HitTable_sorted.txt")
        if os.path.exists("./tblastx_HitTable_sorted_trimAB.txt") == True:
            shutil.move('./tblastx_HitTable_sorted_trimAB.txt', "../result/data" + str(res) + "/tblastx_HitTable_sorted_trimAB.txt")
            if os.path.exists("./tblastx_HitTable_sorted_trimABC.txt") == True:
                shutil.move('./tblastx_HitTable_sorted_trimABC.txt', "../result/data" + str(res) + "/tblastx_HitTable_sorted_trimABC.txt")
            if os.path.exists("./tblastx_HitTable_sorted_trimABC_REMOVED.txt") == True:
                shutil.move('./tblastx_HitTable_sorted_trimABC_REMOVED.txt', "../result/data" + str(res) + "/tblastx_HitTable_sorted_trimABC_REMOVED.txt")
            if os.path.exists("./tblastx_HitTable_sorted_trimABC_orthlist.txt") == True:
                shutil.move('./tblastx_HitTable_sorted_trimABC_orthlist.txt', "../result/data" + str(res) + "/tblastx_HitTable_sorted_trimABC_orthlist.txt")
    # ディレクトリの移動
    for xeval in x:
        for yeval in y:
            if os.path.exists('./B1e-' + str(xeval) + 'C1e-' + str(yeval)) == True:
                os.chmod('./B1e-' + str(xeval) + 'C1e-' + str(yeval), 0o777)
                shutil.move('./B1e-' + str(xeval) + 'C1e-' + str(yeval), "../result/data" + str(res))
    # KWMT_desConecter.pyとKWMT_orthlistCompariser.pyの結果はworkspaceに出力される
    # 作成したディレクトリが空かどうか確認して、空なら下記を出力する
    if not os.listdir("../result/data" + str(res)):
        f = open('comment.txt', 'w')
        f.write("この解析結果はworkspaceに出力されています\n(exitをえらんだ場合は結果はありません)")
        f.close
        shutil.move('./comment.txt', "../result/data" + str(res) + "/comment.txt")
    print("結果は/result/data" + str(res) + "ディレクトリに収納しました\n\n")
    while 1:
        print("続けて解析を行いますか？\n")
        rep = input("1:はい 2:いいえ ")
        if rep == "1":
            res = 0
            break
        elif rep == "2":
            mark += 1
            break
        else:
            print("無効なコマンドです\n\n")


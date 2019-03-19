import subprocess


while True:
	print("\n\n比較に用いるファイルを以下から選択してください\n")
	print("\n  1. BmCorTable_(任意).txt\t2. その他(KWMTBOMOのカラムを指定して比較)\n\n")
	chose = input("数字を打ち込んでEnterを押してください: ")
	if (chose == "1" or chose == "2"):
		break
	print("\n\n想定外のコマンドです\n")

if chose == "1":
	cmd1 = "python3 ../programs_KWMTBOMO/BmCorTable_compariser_withorthlist_cmd1.py"
	subprocess.call(cmd1.split())
elif chose == "2":
	cmd2 = "python3 ../programs_KWMTBOMO/BmCorTable_compariser_withorthlist_cmd2.py"
	subprocess.call(cmd2.split())
else:
	print("\nerror\n")

print("\nプログラムが正常に完了しました\n")

import subprocess

print("\nプログラム「TrimC」を実行します\n")

cmd1 = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimC_cmd1.py"
subprocess.call(cmd1.split())

cmd2 = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimC_cmd2.py"
subprocess.call(cmd2.split())

cmd3 = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimC_cmd3.py"
subprocess.call(cmd3.split())

'''
# 20190701 以下を除外
fs = open("tblastx_HitTable_sorted_trimABC.txt", "r")
ft = open("tblastx_HitTable_THlisted_trimABC.txt", "r")
fsw = open("tblastx_HitTable_sorted_trimABC_orthlist.txt", "w")
ftw = open("tblastx_HitTable_THlisted_trimABC_orthlist.txt", "w")

for rs in fs:
    fsw.write(rs)

for rt in ft:
    ftw.write(rt)


fs.close()
ft.close()
fsw.close()
ftw.close()
'''

print("プログラム「TrimC」が正常に完了しました\n")


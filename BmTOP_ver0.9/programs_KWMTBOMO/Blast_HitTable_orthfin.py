import subprocess

print("\n「Blast_HitTable_orthfin.py」を実行します\n")

cmdA = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimA.py"
subprocess.call(cmdA.split())

cmdB = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimB.py"
subprocess.call(cmdB.split())

cmdC = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimC.py"
subprocess.call(cmdC.split())

print("「Blast_HitTable_orthfin.out」が正常に完了しました\n")

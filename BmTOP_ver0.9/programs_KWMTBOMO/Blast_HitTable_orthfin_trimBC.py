import subprocess

print("\n「Blast_HitTable_orthfin.out」のうち、\n")
print("プログラムTrimB, TrimC のみを実行します\n")

cmdB = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimB.py"
subprocess.call(cmdB.split())

cmdC = "python3 ../programs_KWMTBOMO/cmd/Blast_HitTable_orthfin_trimC.py"
subprocess.call(cmdC.split())

print("「Blast_HitTable_orthfin.out」プログラムTrimB, TrimC が正常に完了しました\n")

import os

### 最終結果を_orthlist.txtに出力する ###
if os.path.exists("./tblastx_HitTable_sorted_trimABC_BmSG.txt") == True:
    fsfin = open("tblastx_HitTable_sorted_trimABC_BmSG.txt", "r")
    ftfin = open("tblastx_HitTable_THlisted_trimABC_BmSG.txt", "r")
    fswfin = open("tblastx_HitTable_sorted_trimABC_orthlist.txt", "w")
    ftwfin = open("tblastx_HitTable_THlisted_trimABC_orthlist.txt", "w")
else:
    fsfin = open("tblastx_HitTable_sorted_trimABC.txt", "r")
    ftfin = open("tblastx_HitTable_THlisted_trimABC.txt", "r")
    fswfin = open("tblastx_HitTable_sorted_trimABC_orthlist.txt", "w")
    ftwfin = open("tblastx_HitTable_THlisted_trimABC_orthlist.txt", "w")

for rsfin in fsfin:
    fswfin.write(rsfin)

for rtfin in ftfin:
    ftwfin.write(rtfin)

fsfin.close()
ftfin.close()
fswfin.close()
ftwfin.close()
###

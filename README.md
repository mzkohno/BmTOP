BmTOP (Bombyx mori Tool for Ortholog Picker)
version 0.9

------------------------------------------------------------

本アプリケーションには、python3とblast+(NCBI)を使用します
事前にDLをお願いいたします


本アプリケーションでは、下記のファイル群を使用します
workspaceディレクトリ(カレントディレクトリ)にすべて用意してください

[BmTOP]
・KWMTBOMO.gff3.txt......Silkbase_HPよりDL(Bomo_gene_models.gff3の一行目を削除し、rename)
・BHTOF_threshold_指定表.txt......各種thresholdを指定する
-Trinity.fasta(assembled_data)から解析する場合
 ・Trinity.fasta
 ・KWMTBOMO.nucl.fa......Silkbase_HPよりDL(Bomo_gene_models.nucl.faをrename)
 ・Blastコマンド指定表.txt
-blast_HitTable(blast結果表)を用いる場合
 ・tblastx_HitTable.txt......*ファイル名を左記にご変更ください

[KWMT_desConecter]
・KWMTBOMO_IDの記入があるファイル
・KWMTBOMO.desc.txt......Silkbase_HPのLibrary_Informationを参考に作成
[orthlist_compariser]
・比較に用いる2つのtblastx_HitTable_THlisted_trimABC_orthlist_[任意].txtファイル



*1 BmTOPは、「Trinityによるde novo assembled dataをqueryに、
カイコGeneModels(2017)をblast+(NCBI)で解析したBLAST_Hit_Table」
を対象として構築されております

それ以外のTableを解析に用いますと、想定外の挙動をとる恐れがありますのでご注意ください


*2 本アプリケーションはlinux環境向けです
Windowsでは仮想OSやWSLでの実行をお勧めいたします

------------------------------------------------------------


[使い方]
0.環境構築を行う（ファイル「環境構築_最初に行うこと」参照）

1.BmTOPディレクトリ内の、BmTOPアイコンをダブルクリックして起動

2.立ち上がる端末の指示に従って入力を行う

※ディレクトリの並びを変えると、アプリが正常に動作しなくなるので注意！！


[結果]
解析結果はresultのdataディレクトリ群に一部を除いて保存されます
  -blastデータベースならびにblast結果はworkspaceに出力されます
  -KWMT_desConecterとKWMT_orthlistCompariserの結果もworkspaceに出力されます


[バージョンアップ情報]
2019.03.08
ver0.9
アプリケーションとしての体裁を整えた
Blast_HitTable_lister_noIso.pyのバグを修正

2019.03.20
GitHubにupload


[製作者情報]
2019.03.20
岩手大学連合農学研究科
応用昆虫学研究室
大野 瑞紀

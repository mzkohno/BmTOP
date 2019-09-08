BmTOP (Bombyx mori tool for ortholog pick-upper)
version 1.0

------------------------------------------------------------

本アプリケーションには、python3とblast+(NCBI)を使用します
事前にDLをお願いいたします


本アプリケーションでは、事前にファイルを用意する必要があります
「readme_FilePrep」に記載のあるファイルをすべて、
workspaceディレクトリ(カレントディレクトリ)に用意してください


*1 BmTOPは、「Trinityによるde novo assembled dataをqueryに、
カイコGeneModels(2017)をblast+(NCBI)で解析したBLAST_Hit_Table」
を対象として構築されております
それ以外のTableを解析に用いる場合、形式を合わせる必要があります


*2 本アプリケーションはlinux環境向けです
Windowsでは仮想OSやWSLでの実行をお勧めいたします

------------------------------------------------------------


[使い方]
0.環境構築を行う（ファイル「環境構築_最初に行うこと」参照）

1.BmTOPディレクトリ内の、BmTOPアイコンをダブルクリックして起動

2.立ち上がる端末の指示に従って入力を行う


[結果]
解析結果はresultのdataディレクトリ群に一部を除いて保存されます
  -blastデータベースならびにblast結果はworkspaceに出力されます
  -KWMT_desConecterとKWMT_orthlistCompariserの結果もworkspaceに出力されます


[defaultからの解析条件変更]
・threshold 1 の変更
  「Blastコマンド指定表.txt」を書き換える(blastのコマンドが書いてあります)
・thresholds 2, 3 の変更
  「BHTOF_threshold_指定表.txt」を書き換える
※どちらも余計な情報やメモ書きはしないこと。ファイル中に予想外の記入があるとエラーを吐きます。


[開発者情報]
2019.09.08
岩手大学連合農学研究科
応用昆虫学研究室
大野 瑞紀
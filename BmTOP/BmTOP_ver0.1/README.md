<font size="10">
  <p> BmTOP: Bombyx mori Tool for Ortholog Picker </p>
  <p>※このプログラムを使用する際は、BmTOPディレクトリをまるごと取得して、<p>
  <p> 位置関係を変えずにworkspaceをカレントディレクトリとしてご使用ください</p>
  <br>
  <br>
</font>
<font size="5">
<p> [BmTOPの使い方---BLASTからオルソログリスト作成まで---]</p>
<br>
<p> "tBLASTx"	※これはBmOFTK関係ない</p>
<p> 1. makeblastでBLAST用データベースを用意する</p>	
<p> コマンド	makeblastdb -in ./XXXXXX.nucl.fa -dbtype nucl -parse_seqids</p>
<p>	（XXXXXXはサンプルによって変える）</p>
<br>
<p> 2. Trinity.fastaをクエリーに、tblastxを下記コマンドでかける	</p>
<p> コマンド	tblastx -query Trinity.fasta -db XXXXXX.nucl.fa -evalue 1e-10 -outfmt "6" -out tblastx_HitTable_e10.txt</p>
<p>	（XXXXXXはサンプルによって変える）</p>
<br>
<br>
<p> "オルソログ探索"	</p>
<p> 3. ディレクトリ「workspace」にBLAST結果をコピーする（ファイル名は「tblastx_HitTable.txt」に変更する）	</p>
<br>
<p> 4. workspaceに、「BHTOF_threshold_指定表.txt」「KWMTBOMO.gff3.txt」「tblastx_HitTable.txt」が入っていることを確認	</p>
<br>
<p> 5. workspaceに移動し、下記をコマンドラインで実行	</p>
<p> コマンド1	../programs_KWMTBOMO/Blast_HitTable_THlister.out</p>
<p> コマンド2	../programs_KWMTBOMO/Blast_HitTable_lister.out</p>
<p> コマンド3	../programs_KWMTBOMO/Blast_HitTable_orthfin.out</p>
<p> ※コマンド3を行う前に「BHTOF_threshold_指定表.txt」を書き換えて、処理のthresholdを任意に指定すること	</p>
<br>
<p> 出力ファイル:	</p>
<p> 「tblastx_HitTable_THlisted_trimABC_orthlist.txt」がorthologだと思われるTranscriptのTopHitList	</p>
<p> 「tblastx_HitTable_sorted_trimABC_orthlist.txt」がselected_Transcriptの総BLAST結果List	</p>
<br>
<br>
<p> [BmTOPの使い方---他Tableとの比較---]</p>
<br>
<p> 1. 比較したいTableの拡張子を「.txt」とする。KWMTBOMOの書かれているカラムを確認しておく	</p>
<p> ※KWMTBOMOのIDが書かれたカラムさえあれば、どんなTableでも比較可能	</p>
<br>
<p> 2. workspaceに移動し、「 (任意).txt」と「tblastx_HitTable_THlisted_trimABC_orthlist.txt」をカレントディレクトリに用意した状態で、下記をコマンドラインを実行</p>	
<p> コマンド	python3 ../programs_KWMTBOMO/BmCorTable_compariser_withorthlist.py</p>
<br>
<p>	出力ファイル:</p>
<p>	「tblastx_HitTable_THlisted_trimABC_orthlist_only(コマンドラインで決定).txt」</p>
<p>	「tblastx_HitTable_THlisted_trimABC_orthlist_(コマンドラインで決定).txt」</p>
<p>	「tblastx_HitTable_THlisted_trimABC_orthlist_not(コマンドラインで決定).txt」</p>
<p>	「tblastx_HitTable_THlisted_trimABC_orthlist_single_(コマンドラインで決定).txt」</p>
<p>	「tblastx_HitTable_THlisted_trimABC_orthlist_single_only(コマンドラインで決定).txt」</p>
</font>

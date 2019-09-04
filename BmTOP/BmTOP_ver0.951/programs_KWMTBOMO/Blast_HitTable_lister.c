/* もしtblastx_HitTable_THlisted.txtの中に、tblastx_HitTable.txtに無い項目が含まれていた場合、
   その無い項目のところで、出力が終わる */


#include <stdio.h>
#include <string.h>

char * TrimSB(char *str2);


int main(void) {

  /* 変数宣言 */
FILE *fpR, *fpSB, *fpTH, *fpw;
int i = 0, error1 = 0, printswitch = 0, THcount = 0, iii = 0;
char lineR[100], lineL[100], lineSB[120], lineSC[120]; // メモリは多めにとった(長さに差があったので)
char lineTH[100];  // THlisted収納用
char k1_ID_a[26], base_ID_a[26];
char k2_SBID_a[20], TH_ID[26];
// 各文字列のサイズは、Trinity.fasta(HSS様に委託)のIDと
// 「KWMTBOMO.gff3」のデータに依存
// ※読み込みファイルを変える場合は、サイズに注意！！


  /* 仮1の宣言 */
char k1_ID[26], k1_SBID[26];  /* k = kari(仮), 上から順番に並んでいる */
double k1_Ident;
int k1_Alnlen, k1_mismatch, k1_gap, k1_Qstart, k1_Qend, k1_Sstart, k1_Send;
double k1_evalue, k1_bitscore;
  /* 出力用変数1 */
char base_ID[26], base_SBID[26];  /* k = kari(仮), 上から順番に並んでいる */
double base_Ident;
int base_Alnlen, base_mismatch, base_gap, base_Qstart, base_Qend, base_Sstart, base_Send;
double base_evalue, base_bitscore;

  /* 仮2の宣言 */
char k2_chr[13], k2_type[25], k2_SBID[70]; /* 順不同 */
int k2_start, k2_end;
float k2_float;
char k2_1, k2_2, k2_3;
  /* 出力用変数2 */
char SB_chr[13], SB_type[25], SB_SBID[70]; /* 順不同 */
int SB_start, SB_end;
float SB_float;
char SB_1, SB_2, SB_3;



/* 処理者にファイルの準備をさせるならここ */



/* 各種ファイルのオープン */
  if(!(fpR = fopen("tblastx_HitTable.txt", "r"))){
     printf("\n「tblastx_HitTable.txt」ファイルが存在しません\n\n");
     return 1;
  }

  if(!(fpSB = fopen("KWMTBOMO.gff3.txt", "r"))){
     printf("\n「KWMTBOMO.gff3.txt」ファイルが存在しません\n\n");
     fclose(fpR);
     return 1;
  }

  if(!(fpTH = fopen("tblastx_HitTable_THlisted.txt", "r"))){
     printf("\n「tblastx_HitTable_THlisted.txt」ファイルが存在しません\n\n");
     fclose(fpR);
     fclose(fpSB);
     return 1;
  }

  if(!(fpw = fopen("tblastx_HitTable_sorted.txt", "w"))){
     printf("\n書き込みファイルのオープンに失敗しました\n\n");
     fclose(fpR);
     fclose(fpSB);
     fclose(fpTH);
     return 1;
  }

//* 最初の目次。項目を変えた場合、ここも書き換える！！ *//
fprintf(fpw, "Trinity_ID\tSB_ID\tSB_chr\tSB_start\tSB_end\tevalue\tbitscore\n");

printf("\n\n以下の項目を「tblastx_HitTable_sorted.txt」に出力します\n\nTrinity_ID\nSB_ID\nSB_chr\nSB_start\nSB_end\nevalue\nbitscore\n\n");


// 一行目(値)の処理(必ず出力する)
fgets(lineTH, 100, fpTH);  // 目次の読み飛ばし
fgets(lineTH, 100, fpTH);  // 「THlist一行入力」
sscanf(lineTH, "%s", TH_ID);  // THlistedからIDのみを抜き出す


while(1){ // TopHitResultのIDと一致するまで繰り返す <開始位置の確定>
  fgets(lineR, 100, fpR);  // BLAST_HitTableデータから一行目のDL
  if(lineR == NULL){  // 無限ループエラー対策
    printf("「tblastx_HitTable.txt」ファイルが読み込めません\n\n");
    fclose(fpR);  fclose(fpSB);  fclose(fpTH); fclose(fpw);
    return 1;
  }
  strcpy(lineL, lineR);  // lineRは借り置きなので、出力用配列はlineLへコピーしておく
  sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
    base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
     &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
     &base_evalue, &base_bitscore);

  if(strcmp(TH_ID, base_ID) == 0){
    break;
  }
}


   /* ★アノテーション用スクリプト(一行目base用) */
   while(1){
     if(fgets(lineSB, 120, fpSB) == NULL){     /* エラーチェック */
       error1++;
       printf("SKWMTBOMO.gff3.txtのエラー\n\n");
       break;}

     else if(lineSB[0] != 'B'){
       continue;
     }  // IDがBから始まらない場合、スキップ

     strcpy(lineSC, lineSB);   // lineSBをlineSCで保持

     sscanf(lineSB, "%s %c %s %d %d %f %c %c %s",
       k2_chr, &k2_1, k2_type, &k2_start, &k2_end,
       &k2_float, &k2_2, &k2_3, k2_SBID);

     // 両方のIDに”ID=”をつけて、strcmpで比較可能にする作業
     strcpy(k2_SBID_a, k2_SBID);
     TrimSB(k2_SBID_a);
     char base_SBIDwith[30] = "ID=";
     strcat(base_SBIDwith, base_SBID);

     // strcmpで比較
     if(strcmp(base_SBIDwith, k2_SBID_a) == 0){   /* SBのIDが一致した際に、SBの情報を代入する */
       sscanf(lineSC, "%s %c %s %d %d %f %c %c %s",
         SB_chr, &SB_1, SB_type, &SB_start, &SB_end,
         &SB_float, &SB_2, &SB_3, SB_SBID);
       break;
     }
   }
     rewind(fpSB);
     printswitch++;


     if(error1 == 1){    /* SKWMTBOMO.gff3.txtにエラーが生じた際の出力 */
       fprintf(fpw, "%s\t%s\terror\n", base_ID, base_SBID);
       error1 = 0;
       printswitch = 0;
     }


     else if(printswitch == 1){
       //* 出力（出力項目を変更したい場合、ここのfprintf()を変更する!！） *//
       fprintf(fpw, "%s\t%s\t%s\t%d\t%d\t%lg\t%lf\n",
         base_ID, base_SBID, SB_chr, SB_start,
         SB_end, base_evalue, base_bitscore);
       error1 = 0;
       printswitch = 0;
     }

// 今どこを処理しているのかの可視化
iii++;
printf("\n＊＊＊現在の処理状況＊＊＊\n");


// 二行目の値〜最後の値までの処理（すべてk1を出力する）
  while(fgets(lineR, 100, fpR) != NULL){  // HitTableの抜き出し
    sscanf(lineR, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
      k1_ID, k1_SBID, &k1_Ident, &k1_Alnlen, &k1_mismatch,
       &k1_gap, &k1_Qstart, &k1_Qend, &k1_Sstart, &k1_Send,
       &k1_evalue, &k1_bitscore);

  label:	// goto文のラベル

    /* THlistとk1のIDが同じものの処理(baseとk1のSBIDが違うもののみ出力) */
    if(strcmp(TH_ID, k1_ID) == 0){  // THlistとHitTableのIDが同じ &&
      // HitTableのSBIDが一行前と違う(参考表2) || THcountがONになっている(参考表3, THlist移動済)
      if((strcmp(base_SBID, k1_SBID) != 0) || (THcount == 1)){

        /* ★アノテーション用スクリプト */
        while(1){
          if(fgets(lineSB, 120, fpSB) == NULL){     /* エラーチェック */
            error1++;
            printf("SKWMTBOMO.gff3.txtのエラー\n\n");
            break;}

          else if(lineSB[0] != 'B')  // IDがBから始まらない場合、スキップ
            continue;

          strcpy(lineSC, lineSB);   // lineSBをlineSCで保持

          sscanf(lineSB, "%s %c %s %d %d %f %c %c %s",
            k2_chr, &k2_1, k2_type, &k2_start, &k2_end,
            &k2_float, &k2_2, &k2_3, k2_SBID);

          // 両方のIDに”ID=”をつけて、strcmpで比較可能にする作業
          strcpy(k2_SBID_a, k2_SBID);
          TrimSB(k2_SBID_a);
          char k1_SBIDwith[30] = "ID=";
          strcat(k1_SBIDwith, k1_SBID);

          // strcmpで比較
          if(strcmp(k1_SBIDwith, k2_SBID_a) == 0){   /* SBのIDが一致した際に、SBの情報を代入する */
            sscanf(lineSC, "%s %c %s %d %d %f %c %c %s",
              SB_chr, &SB_1, SB_type, &SB_start, &SB_end,
              &SB_float, &SB_2, &SB_3, SB_SBID);
            break;
          }
        }
        rewind(fpSB);
        printswitch++;
        THcount = 0;
      }
    }
    // THlistとHitTableのIDが同じ && baseとk1のSBIDも同じもの(参考表1)は無視して次の行へ


    else{  // THlistとHitTableのIDが違う(isoform参考表3 or 別のID参考表4)
      if(THcount == 0){
        fgets(lineTH, 100, fpTH);  // THlistedを次の行へ移動させる
        sscanf(lineTH, "%s", TH_ID);  // THlistedからIDのみを抜き出す
        THcount = 1;
	// ここで「次の一周だけ」、fgets(lineR, 100, fpR)無しでループしたいので、苦肉の策でgoto文法を使用
	goto label;
      }
  }  // THlistedを一行動かしたら、次の周からはIDが一致するまでループさせる(参考表3-2)







    if(error1 == 1){    /* SKWMTBOMO.gff3.txtにエラーが生じた際の出力 */
      error1 = 0;
      printswitch = 0;
      strcpy(lineL, lineR);  // base配列の変更（必須）
      sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
        base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
        &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
        &base_evalue, &base_bitscore);
    }


    else if(printswitch == 1){
      // 今どこを処理しているのかの可視化
      iii++;
      if(iii % 100 == 0){
        printf("%d行目出力中......\n", iii);
      }
      //* 出力（出力項目を変更したい場合、ここのfprintf()を変更する!！） *//
      fprintf(fpw, "%s\t%s\t%s\t%d\t%d\t%lg\t%lf\n",
        k1_ID, k1_SBID, SB_chr, SB_start,
        SB_end, k1_evalue, k1_bitscore);
      error1 = 0;
      printswitch = 0;
      strcpy(lineL, lineR);  // base配列の変更（必須）
      sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
        base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
        &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
        &base_evalue, &base_bitscore);
    }

  }





fclose(fpR);
fclose(fpSB);
fclose(fpTH);
fclose(fpw);

printf("\nプログラムが正常に完了しました\n\n");

  return 0;
}




/* str2の文字列の前後を切り落とす関数 */
// 元の配列も切れるので(ポインタで参照しているため)、注意
char * TrimSB(char *str2){
    char *sb;

    /* アドレスの代入 */
    sb = str2;

    /* str2ポインタを任意の数進める */
    for(int i = 0; i <= 15; i++)		/* ここの数(i <= n)で切り出す文字数(後部)を決める！！ */
    	*str2++;
    *str2++ = '\0';    // 後部の切り落とし


    return sb;

}

#include <stdio.h>
#include <string.h>

char * TrimTrin(char *str1);

char * TrimSB(char *str2);


int main(void) {

  /* 変数宣言 */
FILE *fpR, *fpSB, *fpw;
int i = 0, error1 = 0, printswitch = 0;
char lineR[100], lineL[100], lineSB[120], lineSC[120]; // メモリは多めにとった(長さに差があったので)
char check;
char k1_ID_a[26], base_ID_a[26];
char k2_SBID_a[20];
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

/* 処理者にファイルの準備をさせる */
/*

 printf("\n\nカレントディレクトリに「tblastx_HitTable.txt」と\n「KWMTBOMO.gff3」を準備してください\n");
printf("\nOK?\tOK[z]\tquit[q]\n\n");

scanf("%c", &check);

while(1){
  if(check == 'z')
    break;
  else if(check == 'q')
    return 1;
}

*/

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

  if(!(fpw = fopen("tblastx_HitTable_THlisted.txt", "w"))){
     printf("\n書き込みファイルのオープンに失敗しました\n\n");
     fclose(fpR);
     fclose(fpSB);
     return 1;
  }

//* 一行目の目次。項目を変えた場合、ここも書き換える！！ *//
fprintf(fpw, "Trinity_ID\tSB_ID\tSB_chr\tSB_start\tSB_end\tevalue\tbitscore\n");

printf("\n\n以下の項目を「tblastx_HitTable_THlisted.txt」に出力します\n\nTrinity_ID\nSB_ID\nSB_chr\nSB_start\nSB_end\nevalue\nbitscore\n\n");




while(fgets(lineR, 100, fpR) != NULL){
  sscanf(lineR, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
    k1_ID, k1_SBID, &k1_Ident, &k1_Alnlen, &k1_mismatch,
     &k1_gap, &k1_Qstart, &k1_Qend, &k1_Sstart, &k1_Send,
     &k1_evalue, &k1_bitscore);

  i++;
  /* 一周目の一行目はすべてbaseシリーズに代入 */
  if(i <= 1){
    strcpy(lineL, lineR);  // lineRは借り置きなので、出力用配列をlineLへコピーしておく
    sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
      base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
      &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
      &base_evalue, &base_bitscore);
    }



  /* 2周目以降はbaseと比較する */
  else{
    // Trimtrin前に文字列を保存
    strcpy(base_ID_a, base_ID); strcpy(k1_ID_a, k1_ID);
    TrimTrin(base_ID_a); TrimTrin(k1_ID_a);


    if(strcmp(base_ID_a, k1_ID_a) == 0){   /* ID_cX_gXまでを比較して、同じだったもの(参考表2-4,6,8,9) */

      if(strcmp(base_ID, k1_ID) != 0){   /* isoformの場合の判定(参考表2-4,6,8,9) */
        if(base_evalue > k1_evalue){  /* isoformのほうがevalue高かった場合、baseを変更(参考表2,9:k1をbaseに代入) */
          strcpy(lineL, lineR);  // 出力用配列の変更
          sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
            base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
            &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
            &base_evalue, &base_bitscore);
        }
                                    /* isoformのevalueがbase以下なら、処理なし(参考表3,4,6,8) */

      }
      /* else 全く同じIDの場合、処理なし(参考表にはないけど、実際はある(SBIDだけ違う場合)) */
    }


    else{    /* _cX_gXまでのIDが違った場合（全く異なるクエリー）（参考表1,5,7:baseの出力、k1のbaseへの代入） */
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
    }




      if(error1 == 1){    /* SKWMTBOMO.gff3.txtにエラーが生じた際の出力 */
        fprintf(fpw, "%s\t%s\terror\n", base_ID, base_SBID);
        error1 = 0;
        printswitch = 0;
        strcpy(lineL, lineR);  // 出力用配列の変更（必須）
        sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
          base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
          &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
          &base_evalue, &base_bitscore);
      }


      else if(printswitch == 1){
        //* 出力（出力項目を変更したい場合、ここのfprintf()を変更する!！） *//
        fprintf(fpw, "%s\t%s\t%s\t%d\t%d\t%lg\t%lf\n",
          base_ID, base_SBID, SB_chr, SB_start,
          SB_end, base_evalue, base_bitscore);
        error1 = 0;
        printswitch = 0;
        strcpy(lineL, lineR);  // 出力用配列の変更（必須）
        sscanf(lineL, "%s %s %lf %d %d %d %d %d %d %d %lg %lf",
          base_ID, base_SBID, &base_Ident, &base_Alnlen, &base_mismatch,
          &base_gap, &base_Qstart, &base_Qend, &base_Sstart, &base_Send,
          &base_evalue, &base_bitscore);
      }

        i = 1;
      }
    }





/* ★比較対象のない、一番最後のアノテーション用スクリプト（参考表10:baseの出力） */
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


    // ※最後は出力用配列の変更は必要ない
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



fclose(fpR);
fclose(fpSB);
fclose(fpw);

printf("\nプログラムが正常に完了しました\n\n");

  return 0;
}





/* str1の文字列を前から任意の数切り出す関数 */
// 元の配列も切れるので(ポインタで参照しているため)、strcpyで保存しておくこと
char * TrimTrin(char *str1){
    char *top;

// 作業的には、(1)でポインタを代入(*topが*str1と同じアドレスを示すようにする)し、
//　(2)(3)で*topの参照先にNULLを付与する(*str1を動かして代入する)
   /* (1) 返り値用に先頭アドレスを保持しておく */
    top = str1;

   /* (2) str1ポインタを任意の数進める */
    for(int i = 0; i <= 18; i++)		/* ここの数(i <= n)で切り出す文字数を決める！！ */
    	*str1++;

   /* (3) str1の進んだ先のポインタにNULLを付与する */
    *str1++ = '\0';

    return top;
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
    *str2++ = '\0';    //　後部の切り落とし


    return sb;

}

#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(void){

//* 変数宣言 *//
// [A]の変数
FILE *fpRsAs, *fpRsAq, *fpTHAq, *fpwA;
int switA, switA2 = 0, switA3 = 0, switAw = 0, switAkari = 0, countA = 0;
char lineRsAs[100], lineRsAq[100], lineTHAq[100], lineTHAqF[100]; // メモリは多めにとった(長さに差があったので)
char AS_ID[26], AQ_ID[26], AS_SBID[20], AQ_SBID[20], ATH_ID[26], ATH_SBID[20];

// [B]の変数
FILE *fpTHB, *fprefBC, *fpwB;
char lineTHB[100], linerefBC[30];
double thr_eval, thr_score, thr_evalgap, thr_evalgap0;
int iB;

char BID[26], BSBID[20], Bchr[13];
int Bs, Be;
double Beval, Bscore;

// [C]の変数
FILE *fpTHC, *fpCk, *fpwC;
char lineCk[100], lineC1[100], lineTHC[100];
int countC = 0, switC = 0;

char C1ID[26], C1SBID[20], C1chr[13];
int C1s, C1e;
double C1eval, C1score;

char CkID[26], CkSBID[20], Ckchr[13];
int Cks, Cke;
double Ckeval, Ckscore;

char THCID[26], THCSBID[20], THCchr[13];
int THCs, THCe;
double THCeval, THCscore;

// [Final_result]の変数
FILE *fpTrim, *fpsort, *fpwFinTH, *fpwFin;
char lineTrim[100], linesort[100], linek[100];
char TrimID[26], sortID[26];
int countFin = 0;

//　以下を除外 2019.1.3
//////////////////////////////////////////////////////////////////////////////////
// [A]クエリーを選択させる
//printf("\n「BLAST結果のspecificityチェック」のクエリーはどちらを使いますか？\n\n");
//printf("[tblastx_HitTable_THlisted.txt] = 1\n[tblastx_HitTable_sorted.txt] = 2\n");

//while(switA != 1 && switA != 2){
//  scanf("%d", &switA);
//  if(switA == 1)
//    printf("\n「tblastx_HitTable_THlisted.txt」をクエリーに解析します\n\n\n");
//  else if(switA == 2)
//    printf("\n「tblastx_HitTable_sorted.txt」をクエリーに解析します\n\n\n");
//  else
//    printf("もう一度おねがいします\n");
//}
///////////////////////////////////////////////////////////////////////////////////

switA = 2
// フツーはsortedしかクエリーに使わないため、switAを2で固定した

///////////////////////////////////////////////////////////////////////////
// A.「BLAST結果のspecificity check」 //
// クエリー以外のBLAST結果全てを検索し、Hitしたらスルー、Hitしなかったら出力する //
///////////////////////////////////////////////////////////////////////////


/*
[A]2018.7.16
最後のTopHitlistの行が、_TrimAファイルに出力されないバグあり
*/


/* 各種ファイルのオープン */
// sortedファイルを、サブジェクト用とクエリー用の２つ開く
// tblastx_HitTable_sorted.txt
if(!(fpRsAs = fopen("tblastx_HitTable_sorted.txt", "r"))){
    printf("\n「tblastx_HitTable_sorted.txt」ファイルが存在しません\n\n");
    return 1; // データベース用
 }

if(!(fpRsAq = fopen("tblastx_HitTable_sorted.txt", "r"))){
     printf("\n「tblastx_HitTable_sorted.txt」ファイルが存在しません\n\n");
     fclose(fpRsAs);
     return 1; // クエリー用
  }

// クエリー用のTHlistedファイルを開く
// tblastx_HitTable_THlisted.txt or tblastx_HitTable_THlisted_trimC.txt
if(!(fpTHAq = fopen("tblastx_HitTable_THlisted.txt", "r"))){
  printf("\n「tblastx_HitTable_THlisted.txt」ファイルが存在しません\n\n");
  fclose(fpRsAs); fclose(fpRsAq);
  return 1; // クエリー用
}

// 書き込みファイルを開く(tblastx_HitTable_trimA.txt)
if(!(fpwA = fopen("tblastx_HitTable_THlisted_trimA.txt", "w"))){
    printf("\n書き込みファイルのオープンに失敗しました\n\n");
    fclose(fpRsAs); fclose(fpRsAq); fclose(fpTHAq);
    return 1;
 }


// 一行目の目次を出力
fgets(lineRsAs, 100, fpRsAs);
if(lineRsAs == NULL){  // エラー対策
  printf("「tblastx_HitTable_sorted.txt」ファイルが読み込めません\n\n");
  fclose(fpRsAs);  fclose(fpRsAq);  fclose(fpTHAq); fclose(fpwA);
  return 1;
}
fprintf(fpwA, "%s", lineRsAs);

fgets(lineRsAq, 100, fpRsAq); // 目次の分、一行進めておく
fgets(lineTHAq, 100, fpTHAq); // 目次の分、一行進めておく



// [tblastx_HitTable_THlisted.txt]をクエリーに解析
if(switA == 1){
 while(fgets(lineTHAq, 100, fpTHAq) != NULL){
  sscanf(lineTHAq, "%s %s", AQ_ID, AQ_SBID);

  fgets(lineRsAs, 100, fpRsAs); // 目次とばし用

  while(countA <= 1){
    if(fgets(lineRsAs, 100, fpRsAs) == NULL)
      break;
    sscanf(lineRsAs, "%s %s", AS_ID, AS_SBID);
    if(strcmp(AS_SBID, AQ_SBID) == 0){
      countA++;}
  }
  if(countA <= 1){
    fprintf(fpwA, "%s", lineTHAq);
  }
  rewind(fpRsAs);
  countA = 0;
 }
}



// [tblastx_HitTable_sorted.txt]をクエリーに解析
else if(switA == 2){

  while(fgets(lineTHAq, 100, fpTHAq) != NULL){
   sscanf(lineTHAq, "%s %s", ATH_ID, ATH_SBID);
   strcpy(lineTHAqF, lineTHAq); // 最後の行の出力用

   if(switA3 == 1){
     switA3 = 0;
     goto labelA; //lineRsAqのfgets回避用
   }

     while(fgets(lineRsAq, 100, fpRsAq) != NULL){
       sscanf(lineRsAq, "%s %s", AQ_ID, AQ_SBID);

       if((switAw >= 1 || switA2 >= 1) && strcmp(ATH_ID, AQ_ID) != 0){ // 出力
         if(switAw >= 1 && switA2 == 0){
           fprintf(fpwA, "%s", lineTHAq);
         }
         switAw = 0;  switA2 = 0; switA3 = 1;
         break;
       }

       if(switA2 >= 1){ // すでにオルソログではないとわかったIDの検索を省く、省力用スクリプト
         continue;
       }


       labelA:


       if(strcmp(ATH_ID, AQ_ID) == 0){

        while(fgets(lineRsAs, 100, fpRsAs) != NULL){
         sscanf(lineRsAs, "%s %s", AS_ID, AS_SBID);
         if(strcmp(AS_SBID, AQ_SBID) == 0){
           countA++;}
         if(countA >= 2){
          switA2++;
          break;}
        }

        if(countA <= 1){
         switAw++;
        }

        rewind(fpRsAs);
        countA = 0;
       }

     }
  }

    if(switAw >= 1 && switA2 == 0){ // 最後の行の出力用
      fprintf(fpwA, "%s", lineTHAqF);
    }


}

printf("[A]「BLAST結果のspecificityチェック」が正常に完了しました\n\n\n");

fclose(fpRsAs);  fclose(fpRsAq);  fclose(fpTHAq); fclose(fpwA);



///////////////////////////////////////////////////////////////////////////
// B.「各項目による足切り」 //
// e-valueとscore(他に項目があれば追加可能)が指定値より低いものを除外する //
///////////////////////////////////////////////////////////////////////////

/* 各種ファイルのオープン */
// クエリー用のTHlistedファイルを開く
// tblastx_HitTable_THlisted.txt or tblastx_HitTable_THlisted_trimA.txt
if(!(fpTHB = fopen("tblastx_HitTable_THlisted_trimA.txt", "r"))){
  printf("\n「tblastx_HitTable_THlisted_trimA.txt」ファイルが存在しません\n\n");
  return 1; // 読み込み用
}

// BHTOF(BLAST_HitTable_orthologs_finderの略)_threshold_指定表.txtを開く
// *これは[C]にも使う*
if(!(fprefBC = fopen("BHTOF_threshold_指定表.txt", "r"))){
  printf("\n「BHTOF_threshold_指定表.txt」ファイルが存在しません\n\n");
  fclose(fpTHB);
  return 1; // 読み込み用
}

// tblastx_HitTable_THlisted.txt or tblastx_HitTable_THlisted_trimAB.txt
if(!(fpwB = fopen("tblastx_HitTable_THlisted_trimAB.txt", "w"))){
  printf("\n「tblastx_HitTable_THlisted_trimAB.txt」ファイルが存在しません\n\n");
  fclose(fpTHB);  fclose(fprefBC);
  return 1; // 書き出し用
}



// 各種thresholdの読み込み
// まずタイトル下へのポインタ移動
for(iB = 0; iB < 2; iB++){
  fgets(linerefBC, 30, fprefBC);
}

// [B]
// evalueの読み込み
for(iB = 0; iB < 4; iB++){
  fgets(linerefBC, 30, fprefBC);
}
thr_eval = strtod(linerefBC, NULL);
printf("e-value最高値 = %lg\n", thr_eval); // thresholdの掲示


// scoreの読み込み
for(iB = 0; iB < 4; iB++){
  fgets(linerefBC, 30, fprefBC);
}
thr_score = strtod(linerefBC, NULL);
printf("score最低値 = %lf\n", thr_score); // thresholdの掲示

// XXXXXの読み込み
// *[B]の項目を増やしたい場合、ここに追加する！！


// [C]
// evalue_gapの最高値
for(iB = 0; iB < 4; iB++){
  fgets(linerefBC, 30, fprefBC);
}
thr_evalgap = strtod(linerefBC, NULL);


// TopHitのe-valueが0.0の場合のSecond_Hitの最高値
for(iB = 0; iB < 4; iB++){
  fgets(linerefBC, 60, fprefBC);
}
thr_evalgap0 = strtod(linerefBC, NULL);


// reference取り終わったら、早めに閉じちゃう
fclose(fprefBC);



// タイトルの入力と出力
fgets(lineTHB, 100, fpTHB);
fprintf(fpwB, "%s", lineTHB);

// 各項目による足切りと出力
while(fgets(lineTHB, 100, fpTHB) != 0){

  sscanf(lineTHB, "%s %s %s %d %d %lg %lf",
  BID, BSBID, Bchr, &Bs, &Be, &Beval, &Bscore);

  if(Beval <= thr_eval){ // e-valueのチェック
    if(Bscore >= thr_score){  // scoreのチェック
      fprintf(fpwB, "%s", lineTHB);
    }
  }
}

printf("\n[B]「各項目による足切り」が正常に完了しました\n\n\n");

fclose(fpTHB);  fclose(fpwB);



///////////////////////////////////////////////////////////////////////////
// C.「Top HitとSecond Hitのe-value比較」 //
// TopHitのevalueとsecond hitのevalueが一致〜近い値のものを排除 //
// if((TopHit / second hit <= 1e-10) != NULL) //
///////////////////////////////////////////////////////////////////////////


// thresholdがうまく入力できているかの確認
if(!(thr_evalgap >= 0)){
  printf("「BHTOF_threshold_指定表.txt」から、e-value_gapの値が正常にダウンロードできていません\n\n");
  return 1;
}
printf("e-value_gapの最高値 = %lg\n", thr_evalgap);  // evalue_gapの掲示

if(!(thr_evalgap0 >= 0)){
  printf("「BHTOF_threshold_指定表.txt」から、e-value_gap0の値が正常にダウンロードできていません\n\n");
  return 1;
}
printf("TopHitのe-valueが0.0の場合のSecond_Hitの最高値 = %lg\n", thr_evalgap0);


// ファイルの読み込み
// tblastx_HitTable_THlisted_trimB.txt or tblastx_HitTable_THlisted_trimAB.txt
if(!(fpTHC = fopen("tblastx_HitTable_THlisted_trimAB.txt", "r"))){
  printf("\n「tblastx_HitTable_THlisted_trimAB.txt」ファイルが存在しません\n\n");
  return 1; // 検索用
}

// sortedファイルを開く
// tblastx_HitTable_sorted.txt
if(!(fpCk = fopen("tblastx_HitTable_sorted.txt", "r"))){
    printf("\n「tblastx_HitTable_sorted.txt」ファイルが存在しません\n\n");
    fclose(fpTHC);
    return 1; // TopHitとSecondHitのe-value比較用
 }

// 書き出しTopHitTableファイル
if(!(fpwC = fopen("tblastx_HitTable_THlisted_trimABC.txt", "w"))){
  printf("\n書き込みファイルのオープンに失敗しました\n\n");
  fclose(fpTHC); fclose(fpCk);
  return 1; // 検索用
}

// 一行目の目次読み込みと書き出し
fgets(lineTHC, 100, fpTHC);
 fprintf(fpwC, "%s", lineTHC); // THlistedのtrimABCへの目次出力
fgets(lineCk, 100, fpCk); // sortedファイルも1行進めておく

// 出力用ループ
while(fgets(lineTHC, 100, fpTHC) != 0){
  sscanf(lineTHC, "%s %s %s %d %d %lg %lf",
  THCID, THCSBID, THCchr, &THCs, &THCe, &THCeval, &THCscore);

  if(switC == 1){ // 「前の行で」TopHitの次の行が別の遺伝子だった場合(TopHitのみだった場合)
    if((strcmp(THCID, CkID) == 0) && (strcmp(THCSBID, CkSBID) == 0)
        && (THCeval == Ckeval) && (THCscore == Ckscore)){ // その別の遺伝子がTopHitlistにリストアップされている場合
      strcpy(lineC1, lineCk); // C1にCkを代入
      sscanf(lineCk, "%s", C1ID);
      countC++; // countCをONにして(1行目に指定して)、次の行と比較する
    }
    switC = 0;
  }

  while(1){
    if(fgets(lineCk, 100, fpCk) == 0){  // 最後の行用の出力スクリプト
      if(countC == 1){
        fprintf(fpwC, "%s", lineTHC);
      }
      break;
    }
    sscanf(lineCk, "%s %s %s %d %d %lg %lf",
    CkID, CkSBID, Ckchr, &Cks, &Cke, &Ckeval, &Ckscore);

    if(countC == 1){ // TopHitの次の行の処理
      if(strcmp(C1ID, CkID) != 0){ // TopHitの次の行が別の遺伝子だった場合(TopHitのみだった場合)
        fprintf(fpwC, "%s", lineTHC); // ＜出力＞
        switC++;
      }
      else if(C1eval == Ckeval){ // TopHitとSecondHitが同値の場合、出力しない
        break;}
      else if(C1eval == 0){ // TopHitのe-value(C1)が0だった場合
        if(Ckeval >= thr_evalgap0){ // SecondHitのe-valueがthreshold以上だった場合
          fprintf(fpwC, "%s", lineTHC);} // ＜出力＞ (それ以外は一番下でbreakされる)
      }
      else if(((C1eval / Ckeval) < thr_evalgap)){ // TopHitとSecondHitのevalueの差がthr_evalより小さく、同じではない場合
        fprintf(fpwC, "%s", lineTHC); // ＜出力＞
      }
      break;
    }

    else if((strcmp(THCID, CkID) == 0) && (strcmp(THCSBID, CkSBID) == 0)
        && (THCeval == Ckeval) && (THCscore == Ckscore)){ // TopHitlistにCkの行がリストアップされている場合
      strcpy(lineC1, lineCk); // C1にCkを代入
      sscanf(lineC1, "%s %s %s %d %d %lg %lf",
      C1ID, C1SBID, C1chr, &C1s, &C1e, &C1eval, &C1score);
      countC++;
    }
  }

  countC = 0;
}


printf("\n[C]「Top_HitとSecond_Hitのe-value比較」が正常に完了しました\n\n\n");

fclose(fpTHC); fclose(fpCk); fclose(fpwC);



///////////////////////////////////////////////////////////////////////////
// 「最終結果の出力」 //
// tblastx_HitTable_THlisted_trim***_orthlist.txt (trim***のコピー)//
// tblastx_HitTable_sorted_trim***_orthlist.txt (trimmed THlistを利用して出力)//
///////////////////////////////////////////////////////////////////////////


// ファイルの読み込み
// tblastx_HitTable_THlisted_trimABC.txt or tblastx_HitTable_THlisted_trimBCA.txt
if(!(fpTrim = fopen("tblastx_HitTable_THlisted_trimABC.txt", "r"))){
  printf("\n「tblastx_HitTable_THlisted_trimABC.txt」ファイルが存在しません\n\n");
  return 1;
}

// sortedファイルを開く
// tblastx_HitTable_sorted.txt
if(!(fpsort = fopen("tblastx_HitTable_sorted.txt", "r"))){
    printf("\n「tblastx_HitTable_sorted.txt」ファイルが存在しません\n\n");
    fclose(fpTrim);
    return 1;
 }

// ファイルの書き出し
// ABCの順序は場合による
 if(!(fpwFinTH = fopen("tblastx_HitTable_THlisted_trimABC_orthlist.txt", "w"))){
   printf("\n書き込みファイルのオープンに失敗しました\n\n");
   fclose(fpTrim);  fclose(fpsort);
   return 1;
 }

 // ABCの順序は場合による
 if(!(fpwFin = fopen("tblastx_HitTable_sorted_trimABC_orthlist.txt", "w"))){
   printf("\n書き込みファイルのオープンに失敗しました\n\n");
   fclose(fpTrim);  fclose(fpsort);  fclose(fpwFinTH);
   return 1;
 }


// 一行目の目次読み込みと書き出し
fgets(lineTrim, 100, fpTrim);
 fprintf(fpwFinTH, "%s", lineTrim);
fgets(linesort, 100, fpsort);
 fprintf(fpwFin, "%s", linesort);


while(fgets(lineTrim, 100, fpTrim) != 0){

  if(strcmp(linek, lineTrim) == 0){ // linek(sortを代入したもの)とlineTrimが同じ場合
    fprintf(fpwFin, "%s", linek);
    countFin++;
  } // sorted_trimABC_orthlistへの書き出しその2

  fprintf(fpwFinTH, "%s", lineTrim); // THlisted_trimABC_orthlistへの書き出し
  sscanf(lineTrim, "%s", TrimID);

  while(fgets(linesort, 100, fpsort) != 0){
    sscanf(linesort, "%s", sortID);
    if(strcmp(TrimID, sortID) == 0){
      fprintf(fpwFin, "%s", linesort); // sorted_trimABC_orthlistへの書き出し
      countFin++;
    }
    else if(countFin >= 1){ // 前の行がlineTrimとlinesortが同じで、次の行が違う場合
      strcpy(linek, linesort); // linekにlinesortを一時的に代入
      break;
    }
  }
  countFin = 0;
}


printf("\n「最終結果の出力」が正常に完了しました\n\n");

printf("\nすべての工程が正常に完了しました\n\n\n");

fclose(fpTrim);  fclose(fpsort);  fclose(fpwFinTH);  fclose(fpwFin);


return 0;
}

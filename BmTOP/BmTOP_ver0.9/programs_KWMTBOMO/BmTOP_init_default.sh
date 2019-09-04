# 最初に下記のパスを書き換えること!!
#   パスは、絶対パスでないとダメ
#   *相対パスだとシンボリックリンクからアクセスできない

#デバック時のスクリプト
#gnome-terminal -e "sh -c 'python3 [ここに絶対パスを記入]/BmTOP_path.py;exec bash'"

#実装時のスクリプト
gnome-terminal -e "python3 [ここに絶対パスを記入]/BmTOP_path.py"

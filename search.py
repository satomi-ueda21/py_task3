import pandas as pd
import eel
import os

### デスクトップアプリ作成課題
def kimetsu_search(word, file_path, file_name):
    # 検索対象取得
    new_file_path = os.path.join(file_path, file_name) + ".csv"
    new_file = str(file_name + ".csv")
    #ファイルの保存場所と名前を指定する。何も指定がなければ既存のcsv読み込み。
    if file_path != "" and file_name != "":
        #ディレクトリが存在しない場合作成
        os.makedirs(file_path, exist_ok=True)
        #ファイルが存在しない場合作成
        if not os.path.exists(new_file_path):
            with open(new_file_path, 'w'):
                pass
        df=pd.read_csv(new_file_path)
    elif file_path != "" and file_name == "":
        if not os.path.exists(new_file):
            with open(new_file, "w"):
                pass
        df=pd.read_csv("./{}".format(new_file))
    elif file_path == "" and file_name != "":

    else:
        df=pd.read_csv("./source.csv")

    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はいます".format(word))
        eel.view_log_js("『{}』はいます".format(word))
        val = True
    else:
        print("『{}』はいません".format(word))
        eel.view_log_js("『{}』はいません".format(word))
        eel.view_log_js("『{}』を追加します".format(word))
        val = False
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)

    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    if file_path != "" and file_name != "":
        df.to_csv(new_file_path, encoding="utf_8-sig")
    elif file_path != "" and file_name == "":
        df.to_csv("./{}".format(new_file), encoding="utf_8-sig")
    elif file_path == "" and file_name != "":
        df.to_csv("{}/source.csv".format(file_path),encoding="utf_8-sig")
    else:
        df.to_csv("./source.csv", encoding="utf_8-sig")
    print(source)



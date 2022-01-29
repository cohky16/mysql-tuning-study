# coding:utf-8
import random

# 苗字と名前のリストから名前を生成
def randomName():
    myouji = ["田中", "鈴木", "佐藤", "高橋"]
    namae = ["太郎", "二郎", "三郎", "花子"]
    return random.choice(myouji) + random.choice(namae)

# 0~10の乱数を生成
def randomAge():
    return random.randint(0, 10)

# 出力するファイル名
OUTPUT_FILE = "testData.sql"

# 登録するデータ件数
RECORD_COUNT = 150000

# 実行するSQLコマンド文字列
sqlCommands = ""

# 使用するデータベースを指定(今回はtest_database)
sqlCommands += "USE test_database;\n"


sqlCommands += "INSERT INTO users(name, age) VALUES "

# 登録するデータの数だけINSERT文を生成
for i in range(RECORD_COUNT):

    # 登録するランダムなデータの生成
    name = randomName()
    age  = randomAge()

    if i + 1 == RECORD_COUNT:
        sqlCommands += "('{}', '{}');"\
                    .format(name, age)
    else:
        sqlCommands += "('{}', '{}'),"\
                    .format(name, age)

# 生成したSQLコマンドをファイルに書き出す
f = open(OUTPUT_FILE, 'w')
f.write(sqlCommands)
f.close()
# 從迷宮裡逃走吧
## 動機
你是一位勇者，因為不小心被大魔王抓進了迷宮裡，趕快逃出來打敗大魔王吧!
## 功能：
執行app.py後即可開始遊玩，使用wasd控制腳色移動
## 軟體
flask
python
## 執行過程
需確定ubuntu系統裡有沒有安裝了Python，使用以下命令確認：python3 --version

如果你的系統沒有安裝，可以使用以下命令安裝：
sudo apt-get update
sudo apt-get install python3

在虛擬環境中安裝 Flask。使用以下命令：pip install Flask

新增一個資料夾，ex:game。將app.py檔案放進去，在新增的資料夾裡再新增一個templates資料夾，將index.html及play.html兩個檔案丟進去。

開啟Terminal，cd到game資料夾，使用以下命令開始遊戲:python3 app.py。

在瀏覽器打開這個網址:http://127.0.0.1:5000/選擇迷宮地圖

回到Terminal開始遊戲，使用wasd進行移動，走到p即通關。

使用ctrl+c退出flask。
## 心得回饋&遇到的困難
1.原本是想要以nginx代理到網頁上，但我花了很久時間沒有搞定要怎麼用，所以最後改用了flask

2.使用了flask後不知道怎麼把遊戲運行在網頁上，只能運行在Terminal上，只有選擇地圖，及顯示遊戲結束是在網頁上。'

3.時間不足
## 參考資料
flask:https://devs.tw/post/448



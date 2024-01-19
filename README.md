# MazeGame
需確定ubuntu系統裡有沒有安裝了Python，使用以下命令確認：python3 --version
如果你的系統沒有安裝，可以使用以下命令安裝：
sudo apt-get update
sudo apt-get install python3
在虛擬環境中安裝 Flask。使用以下命令：pip install Flask
新增一個資料夾，ex:game。將app.py檔案放進去，在新增的資料夾裡再新增一個templates資料夾，將index.html及play.html兩個檔案丟進去。
開啟Terminal，cd到game資料夾，使用以下命令開始遊戲:python3 app.py。
在瀏覽器打開這個網址:http://127.0.0.1:5000/，選擇迷宮地圖
回到Terminal開始遊戲，使用wasd進行移動，走到p即通關。
使用ctrl+c退出flask。

# 100万行のエクセルデータを秒で集計する

## 手順はこちら

## 必要なプログラムをダウンロード
任意のディレクトリへ移動して
```
git clone https://github.com/yasmatt/python_excel_automation
```

### ライブラリーのインストール
必要なファイルはこの処理で全てインストールされます
```
pip install -U pipenv
pipenv install
```

### 100万行のデータを生成
終わるまでに数分かかります  
作成されるファイルは毎回異なる値が入力されます
```
cd million_records
pipenv run python main.py
```


### JupyterLabを起動
新しいターミナルを開いて下記コマンドを実行
```
pipenv run jupyter lab
```

### JupyterLabへアクセス
- URLが表示されるのでそれをコピペし、ウェブブラウザーからアクセス

### 集計処理を行う
- アクセスした、JupyterLabのスクリプトの各行で`Shift + Return` を押し、最後の行まで同じ処理をおこなう  

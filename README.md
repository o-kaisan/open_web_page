# WEBページ 自動起動ツール

## 概要
yamlファイルに定義したURLを自動で開くプログラム

## 前提
- python導入済み
  - 3.10環境では動作する
- windows環境のみ

## 準備
- pythonの仮想環境を準備
    ```bash
    python -m venv venv
    ```

- 仮想環境に入った状態でパッケージのインストール
    ```
    # 仮想環境に入る
    .\venv\Scripts\activate

    # パッケージをインストール
    python -m pip install -r requirement.txt
    ```

## 使い方
### 設定ファイルを編集する
```yaml
settings:
    # 開きたいブラウザのpathを指定する
    # 初期値はchromeで開く設定
  - browser_path: C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
    # 開きたいurlを指定する(複数可)
    # 追加する場合は以下のような形で並列に並べる
  - urls:
    - https://www.google.com/
    - https://www.yahoo.co.jp/
```

### アプリの実行
powershellやcmdで以下を実行
```bash
openWebPage.bat
```
※ショートカットに定義すると便利

## ショートカット設定手順
1. エクスプローラーで「openWebPage.bat」を右クリック
2. 「ショートカットを作成」をクリックすると「openWebPage.bat - ショートカット」が作成される
3. 「openWebPage.bat - ショートカット」をデスクトップにコピーする
4. デスクトップにコピーした「openWebPage.bat - ショートカット」を右クリックし、「プロパティ」をクリック
5. ショートカット キー(K)にプログラムを呼び出すキーを入力
6. OKで閉じる
7. 入力したショートカットキーで実行できるかを確認
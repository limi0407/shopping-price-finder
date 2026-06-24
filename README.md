# Shopping Price Finder

ネットショッピング商品の価格を比較しやすくするための個人用ツールです。  
現在は、商品名を入力すると Amazon・楽天市場・Yahoo!ショッピングの検索URLを簡単に生成できます。

## できること

- 商品名を入力して、各ショッピングサイトの検索URLを生成する
- Streamlitベースの簡単なWeb UIで操作する
- そのまま各サイトで商品を探しやすくする

## 目的

欲しい商品の価格を複数サイトで比較しやすくすることを目的としています。

## 現在の機能

- [x] 商品名入力
- [x] Amazon検索URL生成
- [x] 楽天市場検索URL生成
- [x] Yahoo!ショッピング検索URL生成

## 今後の予定

- [ ] 検索履歴保存
- [ ] お気に入り登録
- [ ] 最安値比較
- [ ] 商品URL貼り付け対応
- [ ] 価格履歴グラフ
- [ ] 画像検索
- [ ] Amazon・楽天・Yahoo以外のショップ対応

## 必要環境

- Python 3.10 以上
- pip
- インターネット接続

## セットアップ

1. Python をインストールする
2. このリポジトリをクローンまたはダウンロードする
3. プロジェクトフォルダに移動する
4. 仮想環境を作成する

### Windows の例

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### macOS / Linux の例

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> Windows で `python` が見つからない場合は、Python のインストールパスを直接指定してください。  
> 例: `& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe"`

## 起動方法

### 通常の起動

```bash
python -m streamlit run app.py
```

### Windows で Python パス指定が必要な場合

```powershell
& "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe" -m streamlit run app.py
```

起動後はブラウザで `http://localhost:8501` を開いてください。

## プロジェクト構成

- `app.py` : Streamlit アプリ本体
- `requirements.txt` : Python の依存関係
- `README.md` : プロジェクト説明

## Git 基本コマンド

### 状態確認

```bash
git status
```

### 変更を追加

```bash
git add .
```

### コミット

```bash
git commit -m "メッセージ"
```

### GitHub へ反映

```bash
git push
```

## 作業履歴

### 2026-06-24

- Python 導入
- Streamlit 導入
- 初回アプリ作成
- README 整備

## Git 設定

```bash
git config --global user.name "SAO"
git config --global user.email "291765915+limi0407@users.noreply.github.com"
```
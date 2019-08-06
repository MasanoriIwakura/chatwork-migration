# chatwork-migration

Chatwork API を使用して全メッセージを抽出し、コンソールに出力する

## 使用方法

1. pipenv 環境を準備
1. `pipenv install`で必要なモジュールを追加
1. プロジェクト直下に`.env`ファイルを作成し、Chatwork の API キーを記載する (記載方法は`.env.sample`参考)
1. `python main.py`で実行

## 注意点

API の仕様で直近１００件までしか取得できません・・・

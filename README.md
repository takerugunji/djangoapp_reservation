# djangoapp_reservation

# 概要
宿泊予約サイトです。
スタッフブログを参考に会員登録して宿泊予約をしてみよう！

# 機能・使用技術一覧
- 技術一覧
  - 言語/フレームワーク
    - Python3.7.3
    - Django2.2.4 
  - データベース
    - PostgreSQL10.10
  - 開発環境
    - Docker
    - docker-compose
    - Webアプリケーション(Django)・Webサーバ(Nginx)・APサーバ(Gunicorn)・Database(PostgreSQL)
- 機能一覧
  - ページネーション
  - カレンダー機能(django-bootstrap-datepicker-plus

# 工夫したこと
  - Docker
    - docker-compose
      よく使うコマンドはMakefileにまとめた。

# 苦労したこと
  - Django
    - DB関連
      最初DefaultのUserでアプリを作成しており、後からCustom Userをmigrateしようとしたらうまくいかず、showmigrationsでmigration履歴を確認したり、-fakeコマンドを使ってmigrationし直したりしましたがうまくいかず、結局いろいろ試した結果０からmakemigrationsし直すのがベストだと気付き、やり直したらうまくいった。

# これからすること
- ウェブサイト
  - メール送信確認
  - コード整理
  - テスト機能追加
  - UI整理

- AWS
  - AWS環境構築
  - デプロイ(Docker + Django)

- Circle CI
  - 

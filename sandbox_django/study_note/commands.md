# 実行したコマンドとまとめ

`python3 manage.py runserver` 鯖を起動する

`python3 manage.py startapp {arg}` {arg} というアプリケーションを作成する。

`python3 manage.py migrate` DBの生成を行う。（初期設定）

`python3 manage.py makemigrations polls` migrationで新規作成を行いました的な旨を伝える

`python3 manage.py sqlmigrate polls 0001`

`python3 manage.py shell` shellでdjangoを起動してみる
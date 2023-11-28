# ubuntu20 22で確認
# kick.shを作成し、これを全て貼り付け
# server_name 54.237.217.167;の部分をグローバルIPに書き換え
# source ./kick.shで実行
# djangoのsettings.pyのallowshostを直す→とりあえず['*']にする
# sudo systemctl restart gunicorn
# 以上で構築完了
# publicリポジトリを作ってクローンURLを変えれば他のプロジェクトもいける
# その場合はライブラリには注意

#!/bin/bash

# Djangoのインストール
sudo apt-get update
sudo apt-get install -y python3-pip
sudo pip3 install Django==4.0
sudo pip3 install pillow


# Gunicornのインストール
sudo apt-get install -y gunicorn

# nginxのインストール
sudo apt-get install -y nginx

# Djangoプロジェクトのクローン
git clone https://github.com/high-bridge-bot/PythonFramework.git

# Djangoプロジェクトの作業ディレクトリに移動
cd boadproject/boadproject

# Gunicorn設定ファイルの作成
sudo bash -c 'cat > /etc/systemd/system/gunicorn.service << EOL
[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/boadproject/boadproject
ExecStart=/usr/bin/gunicorn --workers 3 --bind 0.0.0.0:8000 boadproject.wsgi:application

[Install]
WantedBy=multi-user.target
EOL'

# Gunicorn起動
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

# nginx設定ファイルの編集
sudo bash -c 'cat > /etc/nginx/sites-available/boadproject << EOL
server {
    listen 80;
    server_name 100.26.45.198;

    location / {
        proxy_pass http://0.0.0.0:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}
EOL'

# nginx設定ファイルのシンボリックリンク作成
sudo ln -s /etc/nginx/sites-available/boadproject /etc/nginx/sites-enabled/

# nginx再起動
sudo service nginx restart


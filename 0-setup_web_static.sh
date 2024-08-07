#!/usr/bin/env bash
# Sets aup a web server for deployment of web statics

apt-get update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
	listen	80 default_server;
	listen	[::]:80 default_server;
	root	/var/www/html;
	index	index.html index.htm;

	location /hbnb_static {
	    try_files \$uri \$uri/ =404;
	    alias /data/web_static/current/;
	    index 0-index.html index.html index.htm;
	    add_header X-Served-By $HOSTNAME;
	}

	location /redirect_me {
	    return 301 https://cuberule.com;
	}

	error_page 404 /404.html;
	location /404 {
	    root /var/www/html;
	    internal;
	}

	location / {
	    add_header X-Served-By $HOSTNAME;
}
}
" > /etc/nginx/sites-available/default

service nginx restart
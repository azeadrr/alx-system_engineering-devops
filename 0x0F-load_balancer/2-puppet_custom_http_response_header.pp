#!/usr/bin/env bash
#puppet custom http response header

exec {'custom HTTP':
    command  => 'apt-get -y update;
    sudo sed -i "50i\\t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;
	apt-get install -y nginx;
    service nginx restart',
    provider => shell
}

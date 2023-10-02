#!/usr/bin/env bash
#puppet custom http response header

exec { 'HTTP header':
    command  => 'apt-get -y update;
    apt-get install -y nginx;
    sudo sed -i "50i\\t\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;
    service nginx restart',
    provider => shell
}

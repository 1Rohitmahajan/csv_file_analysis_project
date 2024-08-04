
#!/usr/bin/bash

sudo systemctl daemon-reload
sudo rm -f /etc/nginx/sites-enabled/default

sudo cp /home/ubuntu/csv_file_analysis_project/nginx/nginx.conf /etc/nginx/sites-available/csv_file_analysis_project
sudo ln -s /etc/nginx/sites-available/csv_file_analysis_project /etc/nginx/sites-enabled/
#sudo ln -s /etc/nginx/sites-available/csv_file_analysis_project /etc/nginx/sites-enabled
#sudo nginx -t
sudo gpasswd -a www-data ubuntu
sudo systemctl restart nginx


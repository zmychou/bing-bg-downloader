systemctl --user disable downloader.service
systemctl --user disable downloader.timer
systemctl --user stop downloader.timer

rm ~/.config/systemd/user/downloader.service
rm ~/.config/systemd/user/downloader.timer
rm -rf ~/.config/systemd/user/basic.target.wants

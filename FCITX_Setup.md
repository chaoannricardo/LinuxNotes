# FCITX Set up (Fedora KDE)

# Procedures
* Install following packages via dnf
 * fcitx
 * fcitx-chewing
 * kcm-fcitx
* remove ~/.config/fcitx/ if exist.
* set up /etc/environment and ~/.xprofile via following lines
export XIM=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XIM_PROGRAM=fcitx
export XMODIFIERS=@im=fcitx
fcitx &
* imsettings-switch fcitx

# Some Other FCITX Commands
* fcitx-diagnose



# Reference
* https://apap918.wordpress.com/2017/12/26/%E6%96%BCfedora-27%E5%AE%89%E8%A3%9D%E4%B8%AD%E6%96%87%E8%BC%B8%E5%85%A5%E6%B3%95/
* https://fcitx-im.org/wiki/Install_(Fedora)
* https://h.mc4.us/2018/10/09/autostart-fcitx-and-enable-chewing/
* https://yuyueshihaoren.github.io/tutorial/2020/06/12/Installing-Fcitx-on-Fedora-KDE-Plasma-32.html

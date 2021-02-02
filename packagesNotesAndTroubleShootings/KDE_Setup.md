# KDE Set up

* **Mouse**
    
    * Reference: https://superuser.com/questions/1426077/how-to-enable-and-disable-double-click-mouse-options-in-kde
    
    * vim ~/.config/kdeglobals
    
      ```
      ...
      [KDE]
      ...
      SingleClick=false
      ...
      ```
    
      
    
* **Screenshot**

  * Reference: https://forum.kde.org/viewtopic.php?f=19&t=140137
  * enter Settings > Shortcuts > Custom Shortcuts
  * create new custom group ie "Spectacle": Edit > New Group
  * and create new custom shortcut(s): Edit > New > Global Shortcut > Command/URL
  * fill the name ie "PrintScreen Clipboard Rectangular"
  * Trigger: Ctrl+Shift+Print
  * Command/URL: spectacle -bcr
  * Apply

* **Animation**

    * Disable all animation effect of KDE from system settings.

* **Desktop Entry**

    * More information about creating desktop entry: https://developer.gnome.org/integration-guide/stable/desktop-files.html.en

    ```
    nano /home/$USER/.local/share/applications/typora.desktop
    ```

    ```
    [Desktop Entry]
    Categories=IDE;
    Comment[en_US]=MarkDown Editor
    Comment=MarkDown Editor
    Exec=/opt/Typora/bin/Typora-linux-x64/Typora
    GenericName[en_US]=
    GenericName=
    Icon=/opt/Typora/typora-icon.png
    MimeType=
    Name[en_US]=Typora
    Name=Typora
    Path=~/
    StartupNotify=true
    Terminal=false
    TerminalOptions=
    Type=Application
    X-DBUS-ServiceName=
    X-DBUS-StartupType=
    X-KDE-SubstituteUID=false
    X-KDE-Username=
    ```

    



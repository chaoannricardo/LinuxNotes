# Mono develop Troubleshooting



```
Debugger operation failed
ApplicationName='/usr/lib/gnome-terminal/gnome-terminal-server', CommandLine='--app-id mono.develop.id1f71c1c4cede406e9ae6cc55355f30e2', CurrentDirectory='', Native error= Cannot find the specified file
```

* https://stackoverflow.com/questions/59336129/error-when-trying-to-run-code-in-monodevelop

Also had this same error. This happens because `/usr/lib/gnome-terminal/gnome-terminal-server` is actually `/usr/libexec/gnome-terminal-server`, and MonoDevelop is still using the old path.

The way I fixed it was to create the `/usr/lib/gnome-terminal` directory and adding a symbolic link with `sudo ln -s /usr/libexec/gnome-terminal-server` inside `/usr/lib/gnome-terminal`.
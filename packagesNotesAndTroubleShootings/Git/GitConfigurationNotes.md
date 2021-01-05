# Git Configuration Notes

* **Git** Installation inside Ubuntu

```shell
# install git service
sudo apt-get install git git-core git-gui git-doc git-svn git-cvs gitweb gitk git-email git-daemon-run git-el
```

<br>

* **GitHub** setup inside Ubuntu.

**SSH key set-up for GitHub**

**Reference:** https://wiki.paparazziuav.org/wiki/Github_manual_for_Ubuntu

**Step 1**

```shell
cd ~/.ssh
```

When the terminal displays: ""bash: cd: ./.ssh:No such file or  directory" you should generate a public/private rsa ket pair, continue  with step 2.  If the terminal changes to ~/.ssh directory, continue with step 3.

**Step 2**

```shell
ssh-keygen -t rsa -C "your_email@youremail.com"
```

After hitting Enter, the terminal will say: 'Generating  public/private rsa ket pair. Enter file in which to save the  key(/Home/ubuntu/.ssh/id_rsa):' please press only enter and the terminal will ask to enter a passphrase. Enter a suitable passphrase which is > 4 characters. If this is done, please continue with step 4.

**Step 3**

(Follow this step only if your terminal changed to "~/.ssh") 
 You  already have some SSH-keys, following commands will backup (in folder  "key_backup") and remove the keys. Type in your terminal: 

```shell
mkdir key_backup
cd id_rsa* key backup
rm id_rsa*
```

**Step 4**

```shell
vim id_rsa.pub
```

Ubuntu will open a file, copy it's entire content:

1.  Open the github site and login.
2.  Go to "Account Settings" (in the upper right corner from your page).
3.  Click: "SSH Keys"
4.  Click: "Add another public key" 
5.  Paste the copied content into the "key field" and press "Add key" 

**Step 5**

```shell
ssh-add
```

**GitHub log-in configuration**

```shell
# Github service setup
ssh -T git@github.com
# GitHub configuration
git config --global user.name "user_name"
git config --global user.email "email_id"
```



**GIt Cache set-up**

**Reference:** https://help.github.com/en/github/using-git/caching-your-github-password-in-git

```shell
git config --global credential.helper cache
# Set git to use the credential memory cache

git config --global credential.helper 'cache --timeout=3600'
# Set the cache to timeout after 1 hour (setting is in seconds)
```
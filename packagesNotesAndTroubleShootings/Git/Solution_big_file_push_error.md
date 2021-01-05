https://stackoverflow.com/questions/19573031/cant-push-to-github-because-of-large-file-which-i-already-deleted



I found [squashing](https://gist.github.com/patik/b8a9dc5cd356f9f6f980) more useful than `filter-branch`. I did the following:

1. Locally delete large files.
2. Commit the local deletes.
3. Soft reset back X number of commits (for me it was 3): `git reset --soft HEAD~3`.
4. Then recommit all the changes together (AKA squash) `git commit -m "New message for the combined commit"`
5. Push squashed commit.

***Special case\*** (from user @lituo): If above doesn't work, then you may have this case. Commit 1 included the large file and Commit 1's push failed due to large file error. Commit 2 removed the large file by `git rm --cached [file_name]` but Commit 2's push still failed. You can follow the same steps above but instead of using `HEAD~3`, use `HEAD~2`.
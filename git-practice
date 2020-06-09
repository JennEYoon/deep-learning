# Github history edit 2, commands only  

### Change the date of last commit to an arbitrary date

GIT_COMMITTER_DATE="Mar 19, 2020 10:00 AM EST" git commit --amend --no-edit --date "Mar 19, 2020 10:00 AM EST" 
 
GIT_COMMITTER_DATE="Dec 23, 2019 1:01 PM EST" git commit --amend --no-edit --date "Dec 23, 2019 1:01 PM EST" 

### Change the date of an arbitrary commit to an arbitrary or current date

Rebase to before said commit and stop for amendment:  
  ```bash
  git rebase /<commit-hash>^ -i  (Copy commit long-hash number)  
  Replace **pick** with **e** (edit) on the line with that commit (the first one)  
  quit the editor (ESC followed by :wq in VIM)  
  ```

Either:
>GIT_COMMITTER_DATE="$(date)" git commit --amend --no-edit --date "$(date)"  
>GIT_COMMITTER_DATE="Mon 20 Aug 2018 20:19:19 BST" git commit --amend --no-edit --date "Mon 20 Aug 2018 20:19:19 BST"  

See here for more information around rebasing and editing in git:  
Split an existing git commit. https://codewithhugo.com/split-an-existing-git-commit/  

## Also works with <feature> branch.  
Commit added to feature branch.  Commit date changed.   
Push to GitHub "origin feature".  Then merge branch to master on GitHub.   


## git history change - force remote to match local history.  

You are looking for **git push -f origin branch-name**.

See my other stack overflow answer on how git force pushing works here.

>You force pushed, meaning you overwrote the changes on a remote. 
Your computer can't fix it; however, if there is another computer with 
a local copy before you force pushed, 
you can force push from that computer and overwrite your force push.

>Git's push --force is destructive because it unconditionally overwrites 
the remote repository with whatever you have locally, possibly overwriting 
any changes that a team member has pushed in the meantime. - Atlaissan Git Resource


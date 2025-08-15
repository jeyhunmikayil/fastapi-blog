git init
Initializes a new Git repository in the current directory.

git clone <repository_url>
Creates a copy of an existing repository from a remote source.

git status
Shows the state of the working directory and staging area.

git add <file> / git add .
Adds changes from the working directory to the staging area.

git commit -m "message"
Records staged changes in the repository with a descriptive message.

git log
Shows the commit history.

git diff
Displays differences between working directory and staging area or between commits.

git branch
Lists, creates, or deletes branches.

git checkout <branch_name>
Switches to a specified branch or commit.

git merge <branch_name>
Combines changes from the specified branch into the current branch.

git pull
Fetches and integrates changes from a remote repository into the current branch.

git push
Uploads local branch commits to the remote repository.

git fetch
Downloads objects and refs from another repository without merging.

git remote -v
Shows the URLs of remote repositories.

git reset --hard <commit_hash>
Resets the current branch to the specified commit, discarding all changes.

git revert <commit_hash>
Creates a new commit that undoes changes from a previous commit.

git stash
Temporarily stores changes in the working directory that are not yet ready to commit.

git stash pop
Restores the most recently stashed changes.

git tag
Lists or creates tags for specific commits.

git config
Configures user information, preferences, and behaviors for Git.
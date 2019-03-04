## If you want to contribute you need to do:

Make sure that the Python >= 3.7.2 was installed.

1. Fork this project to your github account
2. Clone your fork to your computer
3. Change to the directory of the project 
4. Add this repo `git@github.com:tiagocordeiro/mulhergorila-website.git` as an upstream remote repo
5. Install dependencies with Pipenv
6. Run `pipenv shell` to activate virtualenv 
7. Create a .env with a copy of contrib/env-sample
8. Make migrations
9. Make sure that the code agrees with the PEP8 recommendations
10. Make sure that the test will pass with codecov coverage

### These steps as a code:

```console
git clone [address to your remote fork repo]
cd mulhergorila-website 
git remote add upstream git@github.com:tiagocordeiro/mulhergorila-website.git
pipenv sync --dev
pipenv shell
cp contrib/env-sample .env
python manage.py migrate
pycodestyle .
pyflakes .
coverage run manage.py test -v 2
```

## Feature Branch

_Feature Branch_ is the workflow in place. In this process, you need to create a new branch with the number of the Issue
existing in the main repository. Feature is described on a issue tracker which generates a number for it. This number is
used as branch's name. Then you create a PR with finished code and refer the issue's number to automatically close it
which will map requisite to code changes. Thus you assign at least a team mate as reviwer and code is rebased after 
discussion.

### How to implement Feature Branch on the project?

1. Go to the project directory
2. Activate the virtualenv
3. Make the fetch of the upstream repository
4. Make the rebase of the upstream to master branch
5. Create a new branch with the number of the Issue
6. You should work to implement the task of the Issue
7. Add the files changed to the stage of local repository
8. Make a commit with a expressive message about what you did
9. Make the push to your repository fork
10. Make the Pull Request to the main repository
11. Mark at least teammate to review your code
12. Wait that your PR will be reviewed and merged on to the master of the main repository

### Some of the before steps expressed in code:

```console
~/$ cd mulhergorila-website
~/mulhergorila-website (master)/$ pienv shell
(venv) ~/mulhergorila-website (master)/$ git fetch upstream 
(venv) ~/mulhergorila-website (master)/$ git rebase upstream master
(venv) ~/mulhergorila-website (master)/$ git checkout -b [issue's number]
```
... now work to implement the task of the issue ...

```console
(venv) ~/mulhergorila-website (master)/$ git add .
(venv) ~/mulhergorila-website (master)/$ git commit -m 'A message that expose what do you do'
(venv) ~/mulhergorila-website (master)/$ git push origin master
```

The steps 10 - 12 must do on Github.
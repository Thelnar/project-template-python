[![Windows platform](https://img.shields.io/badge/platform-windows--64-orange.svg)](https://www.microsoft.com/en-us/)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/20.04/)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://docs.python.org/3/whatsnew/3.11.html)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-BSD--3-yellow.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![License](https://img.shields.io/badge/license-Apache--2.0-yellow.svg)](https://opensource.org/license/apache-2-0)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://opensource.org/license/mit)

## Running locally
This project uses [pixi](https://pixi.sh/latest/) to manage its environment.

Pros:
- code environment specified in [pyproject.toml](pyproject.toml)
- packages fetched using conda from [conda-forge](https://conda-forge.org/)
- creation and automatic checking/updating of a [lockfile](pixi.lock)

Cons:
- another tool

## Updating the template in your project
From user Cereal on [Stack Overflow](https://stackoverflow.com/a/69563752):
> [!NOTE]
> If you want to merge changes from a template into your project, > you're going to need to fetch all of the missing commits from the > template, and apply them to your own repo.
> 
> To do this, you're going to need to know the exact commit ID that you templated from, and you're going to need to know the commit ID of your first commit.
> ```
> ORIGINAL_COMMIT_ID=<commit id from original repo you templated from>
> YOUR_FIRST_COMMIT=<first commit id in your repo>
> YOUR_BRANCH=master
> ```
> Next you're going to need add the template as a remote, and fetch it.
> ```
> git remote add upstream git@github.com:whatever/foo.git
> git fetch upstream
> ```
> And finally, you need to rebase all of the commits you're missing onto your branch
> ```
> git rebase --onto ORIGINAL_COMMIT_ID YOUR_FIRST_COMMIT YOUR_BRANCH
> ```
> What this is doing it basically creating a branch off of ORIGINAL_COMMIT_ID, then manually applying all of the commits on your original branch, onto this new branch.
> 
> This leaves you with what you would have had, if you had forked.
> 
> From here, you can `git merge upstream/master` just as if you had forked.
> 
> Once you've completed your merge, you'll need to use `git push --force` to push all of the changes up to the remote. If you're working with a team, you'll need to coordinate with everyone when doing this, as you're changing the history of the repo.
> 
> Note: It's important to note that this is only going to apply to one branch. If you have multiple feature branches, you'll need to perform the same steps to each one.
> 
-- https://stackoverflow.com/a/69563752

## Contributing
Check out [Contributing](CONTRIBUTING.md)!
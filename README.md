[![Windows platform](https://img.shields.io/badge/platform-windows--64-orange.svg)](https://www.microsoft.com/en-us/)
[![Linux platform](https://img.shields.io/badge/platform-linux--64-orange.svg)](https://releases.ubuntu.com/20.04/)
[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://docs.python.org/3/whatsnew/3.11.html)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/license-BSD--3-yellow.svg)](https://opensource.org/licenses/BSD-3-Clause)

## Running locally
This project uses [pixi](https://pixi.sh/latest/) to manage its environment.

Pros:
- code environment specified in [pyproject.toml](pyproject.toml)
- packages fetched using conda from [conda-forge](https://conda-forge.org/)
- creation and automatic checking/updating of a [lockfile](pixi.lock)

Cons:
- another tool

## Contributing
Guidelines:
- contributions should be made in branches named for the feature being implemented
- commits should be signed
- PRs should be resolved by squash and merge
```sh
> pixi shell
> pre-commit install
> git checkout -b "foobar-support"
> echo "foo" > "bar.txt"
> git add .
> git commit -sam "foo in bar"
> git push --set-upstream origin main
```
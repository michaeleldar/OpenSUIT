# OpenSUIT

An open source alternative to [SUIT](https://github.com/PPPDUD/SUIT/). Find out a [Scratch](https://scratch.mit.edu) user ID or username from the command line.

## Download

Download OpenSUIT from the releases tab and make sure you have [Python 3.7](https://python.org/downloads/) or higher installed.

## Usage

Run `python3 opensuit.py`. You can specify the username or ID as an argument, like `python3 opensuit.py -u griffpatch`.

OpenSUIT also caches user data by default by putting responses in `suit_cache.json`. You can disable this behavior by adding `--no-cache`.

You can find more information about arguments with `python3 opensuit.py --help`.

## Output

`{username}: {ID}`
e.g `griffpatch: 1882674`

## Programmatic usage

```python
import opensuit

out = opensuit.fetch("griffpatch", no_cache=False)
# no_cache defaults to True

print(out)
```

Output:

```text
{'Error': False, 'ID': '1882674', 'Username': 'griffpatch'}
```

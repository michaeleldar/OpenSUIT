# OpenSUIT
## An open soure alternative to SUIT. 
## Find out a scratch user's ID or Username.

## Download
Download opensuit from the releases tab and make sure you have python 3.7 or higher installed.

## Usage
Run `python3 opensuit.py`.
You can also specify the username or ID as an argument, like `python3 opensuit.py griffpatch`

## Output
`{username}: {ID}`
e.g `griffpatch: 1882674`

## You can also use opensuit like a python library. Example:
```
import opensuit
out = opensuit.fetch("griffpatch")
print(out)
```
Output:
```
griffpatch: 1882674
```
Note: Caching is not yet implemented

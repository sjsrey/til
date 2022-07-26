# Confirming in a shell script

On zsh I have the `cp` and `rm` commands prompt my in the event they will do some damage by overwriting or deleting an existing file.
This has saved me on many occassions.

However, when building out shell scripts, this can cause a complication that I'm not around to do the confirmation.

For example, I have a shell script that updates my daily reading list by copying files from one local directory to another prior to updating the git repository:

The original command was:
```
cp -r ~/Documents/Reading/* ~/Documents/r/reading/
```

The solution for automatic confirmation is:

```
yes | cp -r ~/Documents/Reading/* ~/Documents/r/reading/
```

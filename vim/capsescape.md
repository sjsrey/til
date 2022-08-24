# Remapping CapsLock to be Control and Escape


It looks like I can remap CapsLock to serve as both a Control key and Escape.

Using System Preferences under Ubuntu, go to Keyboard Layout -> Options -> Ctrl Key and check `Caps Lock` as `Ctrl` 

Then, install **xcape** with 
`sudo apt install xcape`

and in a terminal:
```
xcape -e 'Ctrl_L=Escape'`
```

A single press generates Escape, using the same key together with a second key as in `C-t` gets me Control-t.

My left pinky is a happy camper.

[Source](https://askubuntu.com/questions/177824/remapping-caps-lock-to-control-and-escape-not-the-usual-way).




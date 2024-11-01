# One-shot sticky keys on X11

With my [emacs-pinky](https://www.reddit.com/r/emacs/comments/44c0ed/emacs_pinky/) starting to make its presence known, I looked into a mitigation strategy.

Sticky keys allow for my modifier keys to be, well, modified so that a single press starts a key chord.

For example, to write and upper case `A`, normally this is done with the chord `S-a` where `S` represents the shift key, and the shift key is held down while I press `a`.

If the shift key becomes a sticky key, I know have two single chords `S` `a` to get the upper case `A`. No longer do I need to keep the modifier key pressed.

To get this working in the current session so I can test it out:
```
xkbset sticky -twokey -latchlock
xkbset mousekeys
```

Once, I'm happy, I can make this permanent by adding those lines to my `.xprofile` so that next time I reboot, they are set.


Source: https://drets.github.io/posts/keyboard-adjustments.html

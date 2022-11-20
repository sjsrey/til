# Enabling tap to click on i3

On the [dev one](https://hpdevone.com/) I decided to give [i3](https://i3wm.org/) a go. One thing that didn't work out of the box under i3 was tap-to-click. 
This had been working under Gnome on this machine. The fix is to first add the `90-touchpad.conf` file:
```
sudo mkdir -p /etc/X11/xorg.conf.d && sudo tee <<'EOF' /etc/X11/xorg.conf.d/90-touchpad.conf 1> /dev/null
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
EndSection

```
and then log out, and log back in.

Original source: <https://cravencode.com/post/essentials/enable-tap-to-click-in-i3wm/>

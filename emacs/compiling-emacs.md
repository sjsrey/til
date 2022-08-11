# Compiling Emacs 28.1

Setting up a new box today, the version of emacs in the repository was a bit too old. 
So, I struck out looking for a guide to install a more recent version from source. 
I lucked out:

```
#!/bin/bash

sudo apt install build-essential texinfo libx11-dev libxpm-dev libjpeg-dev libpng-dev libgif-dev libtiff-dev libgtk2.0-dev libncurses-dev libgnutls28-dev

wget http://ftp.gnu.org/gnu/emacs/emacs-28.1.tar.gz
tar xvzf emacs-28.1.tar.gz

cd emacs-28.1
./configure
make
sudo make install
```

[Source](https://gist.github.com/ivan-loh/9eab9770c937f8a0a555252fa9c65c8d)


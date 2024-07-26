# SSH + Git

I work on different machines each day, different rooms of our house, at the
office, on the road.

Keeping things in sync is a bit of a challenge, as I go all heterodox and work
mainly on Linux but keep a few macs around for good measure. Using syncthing has
been pretty solid Linux-Linux but Linux-Mac is not as much joy.

The other workflow I want to support is working on a project in git where I have
a bunch of feature branches. These are in various WIP states and I don't want to
push them up to my github account, and then pull them down on the other
machines, just yet as I want to get them far enough along and clean up the
commits before making them publically available.

So the solution I have is to not worry about using syncthing to handle this, but
rather, using ssh+git:


## Setting up on a client I want to add to my portfolio of machines that I work on

1. clone the repo
2. let that code go stale as I work on the project elsewhere
3. `git remote add machine1 ssh://user@machine1:/path/to/repo`
4. `git fetch machine1`


Then those two machines can be kept in sync. Manually, for sure, but I like this
setup.



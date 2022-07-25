# Large File Storage in Git

Nice [tutorial](https://www.youtube.com/watch?v=4WftZfn9L_I) on setting this up.

This is helpful for reproducible research where you have large data files as part of the project (I'm looking at you parquet) but don't want these taking up space in the repo.


After cloning a repo that has been migrated using lfs, the host has to have lfs installed.

The local large file will simply be a pointer, not the actual file.
To get the actual file downloaded, do `git lfs pull` in the clone.


[Source](https://stackoverflow.com/questions/65363299/git-clone-lfs-files-not-fully-downloading)

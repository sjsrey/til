# Finding files that changed today

```
#!/bin/bash

# List all the files in ~/Documents that have changed in the last day
# Ignore files with .git in their path

find ~/Documents -type f -mtime -1 | grep -v ".git"
```

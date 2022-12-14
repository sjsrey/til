# Removing duplicate agenda items

Sometimes when using `org-agenda` the listing can include duplicates of the same item.
The culprit is that the org file that has that subtree has multiple entries in `org-agenda-files`.

The solution is to open the particular org file that is associated with the duplicate agenda items and then

```
org-remove-file
```

Check if this removes the duplicates. If it does, add the removed file back in the list with
```
org-agenda-file-to-front
```
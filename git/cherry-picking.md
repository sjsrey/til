# Cherry picking a commit from one branch to another branch


Today I was working an a branch `docker` for an on-going research paper, where that branch is building out the replication infrastructure for the paper. In doing so, I made some commits that I realized should go back to `main` so my collaborators had them as we continue on the research.

My question to my self was how to get a single commit from the `docker` branch back into the `main` branch, without brining along the other commits in `docker` that are works-in-progress?

Cherry picking to the rescue:

```
# On branch docker
git add <file>
git commit -m "Fixed issue #562" // Note commit-id
git checkout main
git cherry-pick <commit-id>
git push origin main
```




[Source](https://stackoverflow.com/questions/42467062/commit-a-single-file-to-another-branch)

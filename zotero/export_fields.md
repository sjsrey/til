# Controlling which fields export in Zotero

We are using [shared groups](https://www.zotero.org/support/groups) for collaboration on papers.
This has been working great, as we have zotero setup to export the group anytime there is a change, with the export going to the bibtex file in the paper repos on an author's machine. Zotero syncing makes the changes from one author's machine propagate to the local machines of all other collaborators.

Having the bibtex file in git would result in conflicts,  however, as the `file` field for each entry would be different depending upon the collaborator who most recently updated the group on zotero.


The solution is to use [better-bibtex](https://retorque.re/zotero-better-bibtex/installation/preferences/export/#fields-to-omit-from-export-comma-separated) to specify which fields to exclude when exporting:

![image](https://user-images.githubusercontent.com/118042/181065456-298cab6f-6957-4fc4-9148-f9f414e98268.png)


Now the bibtex file that is updated when the group changes no longer contains the `file` field.

# Forward sync from Emacs to pdf

Using Emacs to edit LaTeX files, I typically use backwards-sync, to read the pdf and `C-1` on a particular point in the pdf to have emacs jump to that line in the source file. This is a great way to do editing.

Less often, it can be useful to go the other route.
That is, you are in the tex file and want the pdf to sync to align with the position of the point.

To do so, when in the buffer the key binding is:
`C-c C-v`
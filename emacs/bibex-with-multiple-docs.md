# BibTex with a multiple file document 

 When collaborating on an article, I like to use multiple documents with a main document that uses `\input{results}` so that each author can work on one section in parallel and minimize conflicts.
 
 To set this up to work with reftex and bibtex, each of the documents (other than the main) need to have the following included:
 ```
%%% Local Variables: 
%%% mode: latex
%%% TeX-master: "main"
%%% End: 
 ```
 
 If for some reason, when attempting to add cites to a document, if there is a warning about no valid bibliography, the fix is to make sure you have that above snippet in the file , and then force a reread of the configuration data with:
 `C-c C-n`.
 
 [Source](https://tex.stackexchange.com/questions/195002/how-to-use-reftex-in-multiple-files)

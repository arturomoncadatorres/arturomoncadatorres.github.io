---
title: 'Using jphysicsB.bst with Titles in LaTeX'
date: 2013-07-04T05:56:08+01:00
author: Arturo
layout: post
permalink: /using-jphysicsb-bst-with-titles-in-latex/
categories:
  - Tutorials
tags:
  - jphysicsB
  - latex
  - technical document
  - thesis
  - writing
  - paper
---
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/latex.png"/>
</figure>

Recently, I was working on a paper submission. Being a huge fan of it, I used LaTeX for the manuscript preparation. The journal's guidelines for submission indicate that [LaTeX Harvard Alphabetic Style](http://www.ctan.org/tex-archive/macros/latex/contrib/harvard/){: target="_blank"} must be used together with the BibTeX style file [`jphysicsB.bst`](http://ctan.mackichan.com/macros/latex/contrib/harvard/jphysicsB.bst){: target="_blank"}. The guidelines also instruct that references must include the title of the article/book/etc. However, the `jphysicsB` style does not print it (this is not an error, that is the way it is supposed to work). How to solve this?

<!--more-->

Apparently this is a frequently encountered problem. After a couple of hours spent, I finally found [Michael Shell's answer in a thread](https://groups.google.com/d/msg/comp.text.tex/dbnqrDHEJso/xVC6r69FG0cJ){: target="_blank"}. It turns out that the original `jphysicsB.bst` requires some minor tweaking. I could tell you exactly what lines to change, but to make things easier for you, you can download the modified and working style file here:

* [**jphysicsB_withTitles.bst**](../multimedia/files/jphysicsB_withTitles.bst)


Remember to update your LaTeX file (i.e., change the bibliography style to `\bibliographystyle{jphysicsB_withTitles}`, assuming you place the `.bst` file in the same directory where your LaTeX file is).

Please note that the file is provided as it is. Use it under your own responsibility. Full credit goes to Michael Shell for his solution. I am only making his answer easier to find and share!

----------
If you have any comments, questions or feedback, leave them in the comments below [or drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres){: target="_blank"}. Moreover, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

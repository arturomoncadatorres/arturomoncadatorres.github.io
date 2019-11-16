---
title: 'Installing LaTeX'
date: 2014-05-08T01:06:27+01:00
author: Arturo
layout: post
permalink: /installing-latex/
categories:
  - Tutorial
  - Writing
tags:
  - latex
  - technical document
  - thesis
---
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/latex.png"/>
</figure>
Recently, quite a few friends have been finishing their degrees and preparing their final theses. A very common struggle was the actual procedure of writing the thesis document. I don't mean sitting down and writing the content (which is already quite challenging itself), but to manage big amounts of text, figures, and (specially) references efficiently. Being such a big fan of LaTeX myself, I always recommend it. However, setting up everything for the first time might not be very intuitive for everyone, since it requires a few steps. Therefore, I decided to write this small guide on how to setup LaTeX in your computer for the first time.

<!--more-->

I would like to point that this guide was done for Windows. Although I am currently using Windows 8, it should work for older versions as well. I have never owned a Mac, therefore I can't provide any guidance on that side, sorry.

## 1. Download a LaTeX distribution.

First, you will need to download and install LaTeX itself. The most popular distribution is open-source [MiKTeX](http://miktex.org/){: target="_blank"} for a variety of reasons: it is quite stable, it is well maintained (and therefore receives continuous updates), and it has an integrated package manager (which, as you will see, comes quite handy).

This is quite straight forward. Just go to [MiKTeX's Download Page](http://miktex.org/download){: target="_blank"} and select the most appropriate version for you. You will probably want to download the Basic MiKTeX, just be careful to choose the correct Windows version (32- or 64-bit).

Once you have the executable file, open it and let the installation wizard take charge. Pay attention to where you are installing MiKTeX, since you will need this information later. You will also have the chance to configure a couple of parameters, such as page size and how to install missing packages (I recommend to choose the option "Install packages on the fly", which will install missing packages automatically from the internet later on).

## 2. Download an appropriate text editor (WinEdt).

The next step is to get an adequate text editor. Technically, you could write and edit all your `.tex` files with something as simple as good old Notepad. However, it is nice to have some additional LaTeX-oriented features. I tried a couple of editors myself, but the one that I am sticking with and that really recommend is [WinEdt](http://winedt.com/){: target="_blank"}. It is a powerful and versatile text editor for Windows that has been specifically designed and configured to integrate with LaTeX. Given how much I recommend WinEdt, the rest of this guide is focused on it.

Once more, installation is quite easy. Just go to [WinEdt's download page](http://winedt.com/download.html){: target="_blank"} and select the most recent version. Again, be careful to choose the correct Windows version (32- or 64-bit). Afterwards, once you have the executable file, open it and let the installation wizard take charge.

It is important to mention that WinEdt has a trial period during which you can use it for free. However, once this period is over, an annoying reminder to buy a license will keep popping randomly. Even if this is not a problem for you (and if you intend to use WinEdt in a regular basis), I seriously recommend buying a license for it. It is a great piece of software. Furthermore, [prices are not out of this world](http://winedt.com/registration.html){: target="_blank"}, even having the option of student prices.

## 3. Configure WinEdt.

This is the only step that might be a little bit tricky. You need to configure WinEdt and point it to where MiKTeX's files are. To do so, go to **Options → Execution Modes**. There, go to the **TeX System** tab and insert the root path of your TeX distribution in the **TeX Root** field (that is why it was important to note that path from step 1).  Then, press **Apply** and you will see how WinEdt retrieves all the relevant information for the rest of the fields automatically. Be sure that the checkbox **Maintain MiKTeX as Administrator** is ticked. The press **OK** and restart WinEdt.

## 4. Try it.

With these steps, you are ready to go to write your first LaTeX document. Create a new `.tex` file in WinEdt and write (i.e., copy/paste) the following:

{% highlight latex %}
\begin{document}

\title{My First \LaTeX{} Document}
\author{Violet Baudelaire}
\maketitle

\begin{abstract}
The objective of this document is to test my \LaTeX{} installation.
\end{abstract}

\section{Introduction}
This is my first \LaTeX{} document. Isn't it exciting?

\end{document}
{% endhighlight %}


Afterwards, hit `F9` in your keyboard. This will produce a bunch of files in the same directory where your original .tex file is located. Don't pay too much attention to these. For now, it is just good to know that among those files, you will find the PDF version of your document. Additionally, it will be displayed on your screen.

That's it. It wasn't so hard, right? I recommend you take a look at ["The Not So Short Introduction to LaTeX"](http://tobi.oetiker.ch/lshort/lshort.pdf){: target="_blank"}, by Tobias Oetiker. It is a true jewel. If you have any additional thoughts, suggestions, or questions, please write them on the comments below.

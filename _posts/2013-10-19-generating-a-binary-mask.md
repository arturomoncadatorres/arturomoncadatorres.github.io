---
title: 'Generating a Binary Mask'
date: 2013-10-19T15:55:50+01:00
author: Arturo
layout: post
permalink: /generating-a-binary-mask/
categories:
  - MATLAB
tags:
  - binary mask
  - digital image processing
  - matlab
---
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/matlab.png"/>
</figure>

When working with images, selecting a specific region of an image to work with is quite common. Therefore I made a script that allows you to generate a mask with one or more regions of interest (ROIs). The shape of the ROIs can be rectangular, elliptic, (irregular) polygon, or free-hand drawn.

<figure class="aligncenter">
	<img width="600" src="../multimedia/images/lena_mask.png"/>
  <figcaption>Original Lena, generated mask, and masked Lena.</figcaption>
</figure>

<!--more-->

You can find the scripts in my [GitHub repository](https://github.com/arturomoncadatorres/generating-binary-mask){: target="_blank"}, which includes the classic image of Lena to use it in the demo. I suggest play with it in order to understand how it works. The scripts include plenty of comments in which I tried to explain each of the steps as clear as possible.

----------
If you have any questions, comments, or feedback, please [open a discussion](https://github.com/arturomoncadatorres/generating-binary-mask/discussions){: target="_blank"}. If there is a problem with the code (e.g., mistake), please [open an issue](https://github.com/arturomoncadatorres/generating-binary-mask/issues){: target="_blank"}. You can always drop me a line on Twitter [(@amoncadatorres)](https://twitter.com/amoncadatorres){: target="_blank"}. Lastly, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

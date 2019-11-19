---
title: 'Generating a Binary Mask'
date: 2013-10-18T15:55:50+01:00
author: Arturo
layout: post
permalink: /generating-a-binary-mask/
categories:
  - MATLAB
tags:
  - binary mask
  - digital image processing
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

You can find the script in [MATLAB's File Exchange](http://www.mathworks.com/matlabcentral/fileexchange/43864-generate-mask){: target="_blank"}. The submission includes a demo, which I suggest you try in order to understand how it works. The script includes plenty of comments in which I tried to explain as clear as possible each of the steps. If you still have questions about it or, even better, suggestions for its improvement, please leave a comment either here or in the submission's page.

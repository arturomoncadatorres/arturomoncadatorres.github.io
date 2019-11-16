---
title: 'ECG IIR Notch Filtering Using Transient Suppression'
date: 2014-08-03T15:59:08+01:00
author: Arturo
layout: post
permalink: /ecg-iir-notch-filtering-using-transient-suppression/
categories:
  - MATLAB
  - DSP
tags:
  - digital signal processing
  - ecg
  - filter
  - iir
  - notch
---
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/matlab.png"/>
</figure>

Recently, I was going through my undergraduate lecture notes. Putting aside the frustration of realizing how much have I forgotten, I stumbled upon an exercise which I found interesting. The task consisted in implementing the algorithm proposed by Pei and Tseng, which uses vector projection to minimize the problem of transient values when applying an IIR notch filter to an ECG signal.

<!--more-->

A complete, detailed explanation of it can be found in

> Pei, Soo-Chang, and Chien-Cheng Tseng. ["Elimination of AC interference in electrocardiogram using IIR notch filter with transient suppression"](http://ieeexplore.ieee.org/xpl/articleDetails.jsp?tp=&arnumber=469385){: target="_blank"}. Biomedical Engineering, IEEE Transactions on 42.11 (1995): 1128-1132.

I went through the code I wrote back then and was not very proud of what I found: it was inefficient, poorly structured, and it didn't use many of the advantages that MATLAB offers. In my defense, I was just learning how to program in MATLAB back then, but still... Thus, I decided to rewrite nicely and share it for educational purposes. Please note that my only contribution is the implementation of the algorithm in MATLAB. Full credit for the algorithm itself goes to the authors of the paper (if you use it, don't forget to give proper credit!).

<figure class="aligncenter">
	<img width="500" src="../multimedia/images/ecg_transient_suppression.png"/>
  <figcaption>Top: original ECG signal with AC interference noise. Middle: filtered ECG signal using a typical IIR notch filter. Bottom: filtered ECG signal using an IIR notch filter with the proposed transient suppression technique.</figcaption>
</figure>

You can find the submission in [MATLAB's File Exchange](http://www.mathworks.com/matlabcentral/fileexchange/47441-ecg-iir-notch-filtering-with-transient-suppression){: target="_blank"}, which includes sample ECG data (as a `.mat` file) as well as a demo, which I suggest you to try in order to understand how it works. The scripts include plenty of comments in which I tried to explain each of the steps as clear as possible. If you still have questions about the implementation or, even better, suggestions for its improvement, please leave a comment either here or in the submission's page.

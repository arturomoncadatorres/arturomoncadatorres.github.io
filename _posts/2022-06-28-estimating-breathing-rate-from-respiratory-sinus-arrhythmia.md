---
title: Estimating Breathing Rate from Respiratory Sinus Arrhythmia
date: 2022-06-28-01T01:18:30+01:00
author: Arturo
layout: post
description: Implementation of the methods used to calculate (average) respiratory rate from heart rate variability as shown by Schafer and Kratky (2008).
permalink: /estimating-breathing-rate-from-respiratory-sinus-arrhythmia/
mood: speechless
categories:
  - DSP
  - Python
tags:
  - biomedical engineering
  - breathing rate
  - digital signal processing
  - ecg
  - python
  - wearables
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/python.png"/>
</figure>

As a Biomedical Engineer, I've always been fascinated by working with physiological signals. It amazes much how much stuff we can measure on the human body and what we can learn from it. Lately, I've been missing working with such data. To scratch that itch, I have been busy with a side project focused on estimating the respiratory rate from the heart rate variability signal (measured from single-lead ECG), as shown in the work by [Schäfer and Kratky (2008)](https://link.springer.com/article/10.1007/s10439-007-9428-1){: target="_blank"}.

<figure class="aligncenter">
	<img width="600" src="../multimedia/gifs/respiration_animation.gif"/>
  <figcaption>GIF for display purposes only. You can find the code for generating it [here](https://github.com/arturomoncadatorres/breathing-rate-rsa/blob/main/multimedia/make_gif.py){: target="_blank"}. Original lung GIF by [PresenterMedia](https://www.presentermedia.com/powerpoint-animation/human-lungs-pa-pid-3795){: target="_blank"}</figcaption>
</figure>

<!--more-->

In their paper, they compare different methods ranging from frequency analysis to autocorrelation and counting methods. I have implemented these methods in Python, including some plots to better show what they are doing. If you are interested, you can find the [GitHub repository right here](https://github.com/arturomoncadatorres/breathing-rate-rsa){: target="_blank"}

I am not done with the whole thing and I hope to keep on working on this type of (fun) projects in the near future. If you have any questions, feedback, or find any bugs, let me know!

----------
If you have any questions, comments, or feedback, please [open a discussion](https://github.com/arturomoncadatorres/breathing-rate-rsa/discussions){: target="_blank"}. If there is a problem with the code (e.g., mistake), please [open an issue](https://github.com/arturomoncadatorres/breathing-rate-rsa/issues){: target="_blank"}. You can always drop me a line on Twitter [(@amoncadatorres)](https://twitter.com/amoncadatorres){: target="_blank"}. Lastly, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

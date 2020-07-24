---
title: Leveraging Cookiecutter to Publish Python Packages
date: 2020-07-24-01T01:19:22+01:00
author: Arturo
layout: post
description: Leveraging Cookiecutter to simplify the process of publishing your Python packages
permalink: leveraging-cookiecutter-to-publish-python-packages/
mood: speechless
categories:
  - Cookiecutter
  - Python
tags:
  - cookiecutter
  - github
  - pip
  - python
  - pyup
  - sphinx
  - travis
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/python.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/cookiecutter.png"/>
</figure>

I started working on my first Python package (which is far from ready, but I will definitely post about it when I have a version worth sharing). When trying to find resources of how to publish it to make it available for the community, I felt a bit overwhelmed. The setup for it to work properly involves a lot of individual files. These need to be in the right structure with the right content. As you can imagine, this is very prone to errors.

<!--more-->

Enter [Cookiecutter](https://github.com/cookiecutter/cookiecutter){: target="_blank"}. Cookiecutter is a tool that allows you to very easily create projects from templates. This way, you can find a template of your liking and use it as a boilerplate for the development of your package. This is huge, since (as you may know) DevOps knowledge is not precisely a strong suit for Data Scientists.

![Cookiecutter](https://raw.githubusercontent.com/cookiecutter/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png)

The most popular Cookiecutter for Python packages (and with good reason) is the one created by [audreyr](https://github.com/audreyr/cookiecutter-pypackage/){: target="_blank"}. The resulting project has some terrific out-of-the-box features, such as [Travis CI](https://travis-ci.org/){: target="_blank"} integration, [Sphinx](https://www.sphinx-doc.org/en/master/){: target="_blank"} documentation ready to be imported into [Read the Docs](https://readthedocs.org/){: target="_blank"}, and auto release to [PyPI](https://pypi.org/){: target="_blank"}.

However, I felt it was lacking a couple of things that I would like for a Data Science package. Therefore, I decided to fork it and tune it to my needs. In the process, I took the liberty to add a few quality-of-life improvements, which resulted in the following features:

* Updated requirements to more recent versions
* Concentrated original documentation into the project's README
* Added a `data` directory (together with its corresponding README)
* Added an `examples` directory
* Updated the generated project's README from .rst to .md
* Changed the generated project's default documentation style from Alabaster to Sphinx-rtd-theme (much nicer)
* Added issue templates for bugs reports, documentation improvements, feature suggestions, and others.
* More to come!

You can [**find my Cookiecutter template for a Python (Data Science) package here**](https://github.com/arturomoncadatorres/cookiecutter-pypackage/){: target="_blank"}. In the same repository, you will find both a Quickstart and a Tutorial to get you up and running in no time.

I hope to keep on working and improving this Cookiecutter. On the meantime, if you have suggestions for its improvement, [file a new issue in Github](https://github.com/arturomoncadatorres/cookiecutter-pypackage/issues){: target="_blank"} [or drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres){: target="_blank"}.

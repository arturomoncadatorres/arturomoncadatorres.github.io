---
title: Creating a Shareable Bokeh Dashboard with Binder
date: 2019-08-25T17:53:30+01:00
author: Arturo
layout: post
permalink: /creating-a-shareable-bokeh-dashboard-with-binder/
mood: speechless
categories:
  - Python
  - Tutorials
tags:
  - binder
  - bokeh
  - data visualization
  - github
  - interactive
  - pokemon
  - python
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/bokeh.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/binder.png"/>
</figure>

Recently, I finished a personal project in which [I analyzed the results of the "Who is your favorite Pokemon" survey](https://github.com/arturomoncadatorres/favorite-pokemon){: target="_blank"}. After that, I wanted to generate a more interactive visualization in which the user could choose a specific Pokemon and see its results. After pondering different options, I decided to do so in [Bokeh](https://bokeh.pydata.org/en/latest/index.html){: target="_blank"} because of a few reasons. First of all, you can generate your visualizations using Python only. Furthermore, it is very easy to incorporate [Bokeh in Jupyter notebooks](https://bokeh.pydata.org/en/latest/docs/user_guide/notebook.html){: target="_blank"}, which is great to generate a first version of the prototype. Lastly, a few colleagues of mine have used it for their projects at work and have been very happy with it.

<!--more-->

However, I wanted to be able to share the Bokeh app with the general public, preferably through a single URL, due to easiness. This is where things started to get a bit tricky. [Bokeh's documentation states a few options](https://bokeh.pydata.org/en/latest/docs/user_guide/server.html){: target=_"blank"} to do so, but they aren't very straightforward, since they require setting up a hosting system on a server. After some googling, I came across [a post by Jacob Deppen](https://deppen8.github.io/posts/2018/09/shareable-dashboard/){: target="_blank"}, where he described my exact same situation. He suggested doing so using Binder.

[Binder](https://mybinder.org/){: target="_binder"} is an (open source) web service that takes a Github repository and creates a shareable, interactive, reproducible environment in the cloud. This is a perfect solution for what I wanted to achieve. It even has a small tutorial that explains [how to deploy a Bokeh app](https://github.com/binder-examples/bokeh){: target="_blank"}. Unfortunately, I had a few issues to get everything up and running. After more days than I care to admit working on this (and with the help of some great people), I got it working. Therefore, in this post I want to give a more detailed tutorial on how to do so.

## 1. Create a (new) repository with the proper structure
First, to make things easier for us, we need to create a new (Github) repository that will be exclusively dedicated to the interactive visualization. It needs to have the following structure:

{%highlight text %}
README.md (optional)

LICENSE (optional)

.gitignore (optional)

bokeh-app
|----main.py

.binder
|----bokehserverextension.py
|----environment.yml
|----postBuild
{%endhighlight%}

## 2. Prepare the files
The files in the `bokeh-app` directory are the files required for your app to run.

* `main.py`  
This file will contain the code of your Bokeh app.
* Furthermore, here you can have additional files, different directories where your data are located, where your outputs are saved, etc.

The files in the `binder` directory are needed to deploy your app in Binder.

* `bokehserverextension.py`
This file should have the following content:

{% highlight python %}
from subprocess import Popen

def load_jupyter_server_extension(nbapp):
"""serve the bokeh-app directory with bokeh server"""
Popen(["bokeh", "serve", "bokeh-app", "--allow-websocket-origin=*"])
{% endhighlight %}

* `environment.yml`
 In this file, you should define the dependencies of your app (e.g., `numpy`, `pandas`, etc.). It should have at least the following:

{% highlight text %}
dependencies:
  - bokeh
  - pip
  - pip:
    - nbserverproxy
    - jupyter-server-proxy
{% endhighlight %}

* `postBuild`  
 This file should have the following content:

{% highlight text %}
# Enable nbserverproxy
jupyter serverextension enable --sys-prefix nbserverproxy

# Install the bokeh server extension so that Bokeh launches at startup
mv .binder/bokehserverextension.py ${NB_PYTHON_PREFIX}/lib/python*/site-packages/

# Enable Bokeh extension
jupyter serverextension enable --sys-prefix bokehserverextension
{% endhighlight %}

## 3. Commit and push your repository to Github
Pretty straightforward.

## 4. Launch Binder
Lastly, you will actually launch Binder. It is very simple, but you need to be careful to get it right. Go to [`https://mybinder.org/`](https://mybinder.org/){: target="_blank"}, where you will see the following panel:

<figure class="aligncenter">
	<img width="600" src="../multimedia/images/binder_panel.png"/>
</figure>

In **A**, paste the link to your repository. I prefer working with Github, but you can also use other types of repositories (e.g., GitLab). If you do, _make sure you change it in the corresponding drop-down menu_.

In **B**, paste the ID of a specific branch, tag, or commit that you wish. This is optional. If you aren't doing anything fancy and want to generate a link for the master branch of your latest commit, you can leave it empty

In **C**, write `/proxy/5006/bokeh-app`. Also, _make sure to change from File to URL_.

The first time you run it, it will take long, since Binder will create the image for your app. If everything went right, it will open a tab in your favorite navigator with you app running. You can use that link to share your app. Good job!

## Bonus: Troubleshooting, tips & tricks
* When building your Binder, be sure to show the console. You could see potentially useful information about errors there.
* If you make a change in your app, you will need to push it to your repository and do step 4 again.
* Be careful of your dependencies! You might need to define more dependencies than you think. Debugging your environment might be useful (more on that below)
* Watch out for your paths! If you are using paths for certain files (e.g., read data files), make sure to define them relative to where `main.py` is (credit to [`@jdkent`](https://github.com/jdkent){: target="_blank"}).
* Debugging. This one can be a real life-saver. To debug your app, create a Python environment from the `environment.yml` file. Then, run `bokeh serve bokeh-app` _at the top level_ of your repository (and not within the `bokeh-app` directory), since that is where Binder is running Bokeh. Then, look at the errors that pop in the terminal (credit to [`@jdkent`](https://github.com/jdkent){: target="_blank"}).

## Closing remarks
Big shout out to [`@betatim`](https://github.com/betatim){: target="_blank"} for helping me start with the deployment of my app in Binder. Huge shout out to [`@jdkent`](https://github.com/jdkent){: target="_blank"} for taking time of his busy graduate student life to help me debug my app.

You can actually see my [Bokeh app in action here](https://mybinder.org/v2/gh/arturomoncadatorres/favorite-pokemon-interactive/16eebda4779dd6dc52fcdc4c2181b291fbb5a270?urlpath=%2Fproxy%2F5006%2Fbokeh-app){: target="_blank"} (be patient, it can take a while to load). Furthermore, you can also take a look at its [corresponding Github repository here](https://github.com/arturomoncadatorres/favorite-pokemon-interactive){: target="_blank"}.

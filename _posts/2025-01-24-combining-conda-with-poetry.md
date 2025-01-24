---
title: Combining Conda with Poetry for Environment and Package Management (in Windows)
date: 2025-01-24T00:00:01+01:00
author: Arturo
layout: post
description: How to configure Conda and Poetry to work together for environment and (Python) package management
permalink: /combining-conda-with-poetry/
mood: speechless
categories:
  - Data Science
  - Python
tags:
  - conda
  - data-science
  - poetry
  - windows
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/python.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/conda.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/poetry.png"/>
</figure>

Recently, I was working in a (Python) project that was completely set up using [Poetry](https://python-poetry.org/){: target="_blank"}. Up to now, I hadn't had the 
opportunity (or the need) to try it out, so this seemed like a good learning opportunity.

Except for a few caveats[1], Poetry has been very simple and straightforward to use. However, it still has [some disadvantages compared to `conda`](https://www.geeksforgeeks.org/conda-vs-poetry-in-python/){: target="_blank"}
(my go-to solution for environment and package management), namely:

1. Poetry only supports Python projects. Sure, I work mostly with Python, but what will happen when I need to use or combine a different framework?
1. Poetry relies on `venv` for virtual environments, which has given me a lot of headaches in the past (and one of the main reasons why I switched to `conda`).

But what if you could combine the best of both worlds? For instance: creating an environment with `conda` and letting Poetry do all the Python package management?
That sounds great!

<figure class="aligncenter">
	<img width="600" src="../multimedia/images/conda_poetry/conda_poetry.png"/>
</figure>

I was looking for a step-by-step guide of how to configure them for Windows. Although I found [one](https://michhar.github.io/2023-07-poetry-with-conda/){: target="_blank"} or [two](https://felix11h.github.io/notes/ops/poetry.html){: target="_blank"}, 
I still needed to do some tinkering myself. In this post, I would like to share how I configured `conda` and Poetry to work together. Hopefully this will save you some time and makes things smoother, should you decide to have this setup yourself.

<!--more-->

## 0. Install `conda`
I assume that you have already [installed `conda`](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html){: target="_blank"} in your machine (which comes with `pip`). 
By the way, this setup also works for [`miniforge`](https://github.com/conda-forge/miniforge){: target="_blank"}, which is what I actually use.

## 1. Install `pipx`
In your `conda` terminal, install [`pipx`](https://pipx.pypa.io/stable/){: target="_blank"} **on your `base` environment**
(I know, I know, usually you shouldn't mess up with your `base` environment, but this is how I managed to make things work):

```shell
pip install pipx
```

## 2. Install Poetry
Poetry provides a few [installation options](https://python-poetry.org/docs/#installation){: target="_blank"}. To narrow it down, do the following.

**While still being in your `base` environment**, do:

```shell
pipx install poetry
```

Note that as [Poetry's documentation](https://python-poetry.org/docs/#installation) states, do **not** install Poetry in the environment of your project!

After that, you will (probably) get a warning message regarding paths. Save yourself the issue of changing this manually, and just do:

```shell
pipx ensurepath
```

You can check if Poetry was installed correctly by going to a Windows shell and doing:

```shell
poetry --version
```

## 3. Configure Poetry
Now you just need to configure Poetry. On a Windows shell, do:

```shell
poetry config virtualenvs.path "path_to_your_conda_envs"
```

Replace `path_to_your_conda_envs` with the actual Windows path where `conda` stores your environments (don't forget the quotation marks `" "`). 
If you don't know said path (as it is always the case with me), you can find out with the command `conda info --envs`.

Then, type:

```shell
poetry config virtualenvs.create false
```

which allows to keep the environment management up to you (and `conda`), therefore using Poetry only for package (and dependency) management.

## 4. Make sure everything works
Lastly, let's see that everything is working. Close the previous `conda` terminal, open a new one and do:

```shell
poetry --version
```

You can now use Poetry for installing new packages, for instance:

```shell
poetry add mkdocs-git-revision-date-localized-plugin
```

(It is a weirdly specific example, but that's the package that I needed at the moment).

That's it! So far, this configuration has worked quite good for me. Apparently, there are other options that also look very promising,
such as using [`Pixi`](https://pixi.sh/latest/){: target="_blank"} (as suggested [here](https://stackoverflow.com/a/71110028/948768){: target="_blank"}) 
or [`uv`](https://docs.astral.sh/uv/){: target="_blank"} (which claims to be [extremely fast](https://github.com/astral-sh/uv/blob/main/BENCHMARKS.md){: target="_blank"}). 
I hope I have the chance to take a look at them in the future.

[1]: For example, [`install` ](https://python-poetry.org/docs/cli/#install){: target="_blank"} installs *all* dependencies of a project's `pyproject.toml`; if you want to install a package, you need to use [`add`](https://python-poetry.org/docs/cli/#add){: target="_blank"}.

----------
If you have any comments, questions or feedback, leave them in the comments below [or drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres){: target="_blank"}.
Moreover, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

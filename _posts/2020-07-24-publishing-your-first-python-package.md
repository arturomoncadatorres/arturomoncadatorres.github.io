---
title: Publishing Your First Python Package
date: 2019-07-24-01T01:18:38+01:00
author: Arturo
layout: post
description: Publishing your first Python package as a Data Scientist
permalink: /publishing-your-first-python-package/
mood: speechless
categories:
  - Python
  - Github
tags:
  - cookiecutter
  - travis
  - pip
  - python
  - sphinx
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/python.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/github.png"/>
</figure>

I started working on my first Python package (which is far from ready, but I will definitely post about it when I have a version worth sharing). When trying to find resources of how to publish it to make it available for the community, I felt a bit overwhelmed. Most of the tutorials assumed at least some basic DevOps knowledge. As you may know, that is usually not a strong suit for Data Scientists. Therefore, I decided to compile my experience in this post, hopefully making it easier for other people like me.

<!--more-->

Before we start, I need to say that this post is based on [Audrey Roy Greenfeld's tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html#step-3-create-a-github-repo). Here, I will expand upon it and provide additional tips that made my experience much smoother.

### 0. Pre-requisites
* Have a [GitHub account](https://github.com/). For this tutorial, we will use `github_username` as an example.
* Have a [ReadTheDocs account](https://readthedocs.org/)
* Have a [PyPI (Python Package Index) account](https://pypi.org/)
* Have a [PyUp account](https://pyup.io/) (which will be linked to your GitHub account)

### 1. Setup your environment
First, we need to create a virtual environment in which we will be working on the package development. You can do so using your preferred tool. Personally, I like [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands). Be sure to activate your created environment.

#### Enter Cookiecutter
As you have probably seen in other projects, creating a package requires configuring a lot of files to be in a very specific structure. This can be prone to errors, specially if this is your first time.

Enter [Cookiecutter](https://github.com/cookiecutter/cookiecutter). Cookiecutter is the key tool that will make this process much easier. In short, it allows you to easily create a project based on pre-existing cookiecutters (i.e., templates).

You need to install Cookiecutter in your environment, which you can do using conda:

```bash
conda config --add channels conda-forge
conda install cookiecutter
```

or using pip:

```bash
pip install cookiecutter
```

### 2. Generate package files
Now, we will actually generate the files. For this tutorial, we will use [audreyr's Cookiecutter for PyPackage](https://github.com/audreyr/cookiecutter-pypackage).

In your prompt, move to the directory where your project will live. Once there, type:

```bash
cookiecutter https://github.com/audreyr/cookiecutter-pypackage.git
```

A series of prompts will ask you about the characteristics of your project. At the time of writing, these are:

* `full_name` <br>
Your full name.

* `email` <br>
Your email address.

* `github_username` <br>
Your GitHub username (`github_username` in our example).

* `project_name` <br>
The name of the package. This is used in documentation, so spaces and special characters are ok. For now, we will use `Cool Package` as an example.

* `project_slug` <br>
This is the *namespace* of your Python package. This should be Python import-friendly. Typically, it is the [slugified](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django) version (i.e., human-readable, unique identifier) of `project_name`. Therefore, in our case this would be `cool-package`.

* `project_short_description` <br>
A short description (preferably one sentence) of your package's purpose.

* `pypi_username` <br>
Your PyPI username.

* `version` <br>
The starting version number of the package. If this is the package's first iteration, I recommend sticking to `0.1.0`.

* `use_pytest` <br>
Whether to use [`pytest`](https://docs.pytest.org/en/latest/) (a framework for code testing).

* `use_pypi_deployment_with_travis` <br>
Whether to use PyPI deployment with [Travis CI (continuous integration](https://travis-ci.org/), a framework for automatically building and testing code changes, providing you with feedback almost immediately).

* `add_pyup_badge` <br>
Whether to include a [`PyUp` badge](https://github.com/pyupio/pyup) (a service for tracking and updating your dependencies). We will assume you chose so as well for the rest of the tutorial (step 7).

* `command_line_interface` <br>
Whether to create a console script using Click. Console script entry point will match the `project_slug`. Possible options are `Click`, `Argparse`, and `No command-line interface` <br>
(*I'm still figuring what these are used for*).

* `create_author_file` <br>
Whether to create an authors file. I recommend you do.

* `open_source_license`
Choosing a license for your project is important. Possible options are
  * 1. MIT License
  * 2. BSD license
  * 3. ISC license
  * 4. Apache Software License 2.0
  * 5. GNU General Public License v3
  * 6. Not open source

  If you are unsure of which license would be better for your project, take a look at [`choosealicense.com`](https://choosealicense.com/)


### 3. Put files under version control in GitHub
Next, we need to put our newly-created files under version control using GitHub. Go to GitHub and create a new repository. Make sure that the repository's name matches that defined `project_slug`.

Make sure that you have [configured your SSH key properly](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account). Now, in your project's directory, open a Git Bash and type:

```
git init
git remote add origin git@github.com/github_username/cool-package.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

### 4. Install requirements
Now, we need to install the new project's local development requirements. We can do so by typing:

```bash
pip install -r requirements_dev.txt
```

*TODO: I will probably change this configuration later. I would prefer having requirement files organized a little bit more neatly.*

### 5. Configure Travis CI
Afterwards, we will configure [Travis CI](https://travis-ci.org/). First, we need to do so online. Just login with your GitHub credentials, click on your profile picture and go to settings. In the section "Legacy Services Integration", you will see all your (public) repositories (the first time it might take a few minutes, be patient). Simply turn on the switch of your repository of interest.

Next, we need to configure Travis locally. To do so, we need Ruby. Check if you have it installed already by typing in the console

```
ruby -v
```

If you have it already, you will see the current version of Ruby. If not, follow the [instructions here](https://www.ruby-lang.org/en/documentation/installation/). Afterwards, install Travis by typing

```
gem install travis
```

Check if the installation was successful by typing

```
travis version
```

Finally, we need to encrypt our PyPI password in the Travis configuration. Moreover, we also need to automate deployment on PyPI when pushing a new tag to the master branch. To do this, we need to type in the console

```
travis encrypt password --add deploy.password
```

You will get asked if you want to rewrite the contents of `.travis.yml`. Say yes. After that, commit and push this change to GitHub

```
git add .travis.yml
git commit -m "Updated .travis.yml"
git push -u origin master
```

### 6. Configure ReadTheDocs
Login to [ReadTheDocs](https://readthedocs.org/). Click on your profile picture, which will bring you to your dashboard. Here, you can choose to import a project. Select your package repository and follow the instructions.

One important thing. Do notice that the package documentation uses [Sphinx](https://www.sphinx-doc.org/en/master/), which relies on `.rst` (reStructureText) files. This format is different from (your probably familiar) `.md` (Markdown) files. While you might be tempted to switch to Markdown, [it is not advisable](https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/). For technical documentation, it is well worth investing some time in learning how to work with `.rst` files.

#### 6.1 Change ReadTheDocs Theme [optional]

After this, you will have a page with your documentation in `https://cool-package.readthedocs.io/en/latest/`. It will use the Alabaster template, which in my opinion isn't very visually appealing. I much more prefer the `sphinx_rtd_theme`. Fortunately, it is very easy to change it, as described [here](https://sphinx-rtd-theme.readthedocs.io/en/stable/). In short:

* Install the theme using `pip`
```
pip install sphinx-rtd-theme
```

* Go to your project's `docs` directory and open the `conf.py` file in your preferred (Python) editor.

* In there, make the following changes:

```python
# At the top, import the theme.
import sphinx_rtd_theme

...

# Add the `sphinx_rtd_theme` item to the `extensions list` (leave the rest unchanged)
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx_rtd_theme']

...

# Lastly, change the `html_theme` value to
html_theme = "sphinx_rtd_theme"
```
* Build your documentation again. You should see the new changes. Ahh, so much nicer!

You can also very easily change several [configuration options](https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html). However, we will stick to the defaults for now.


### 7. Configure PyUp
PyUp is a handy tool that takes care of updating your dependencies automatically. To configure it, login to [PyUp](https://pyup.io/) using your GitHub credentials. Then, click on the button `+ Add Repo` and select your `cool-package` repository. Confirm the dialogue. After that, your PyUp badge in your `README` will be updated automatically.

If you originally chose not to have a PyUp badge (Step 2) and you changed your mind, you can add it very easily. Just add the following lines in your `README` wherever you want the badge to show (probably at the top:

```
.. image:: https://pyup.io/repos/github/github_username/cool-package/shield.svg
        :target: https://pyup.io/repos/github/github_username/cool-package/
        :alt: Updates
```

### 8. Release on (Test)PyPI
As you might have guessed, the last step is to actually release your package to PyPI. If you are unsure, you can always try releasing it first on [TestPyPI](https://test.pypi.org/). This is a good place to use as a sandbox.

*TODO: I will update this section once I have some hands on experience with the actual release. On the meantime, you can check some other [tutorials online](https://dev.to/wangonya/publishing-your-python-packages-on-testpypi-before-publishing-on-pypi-2gb2).*

<!--
To create releases, type in Console

```bash
bump2version patch
git push --tags
```

This will result in:
cool-package 0.1.1 showing up in your GitHub tags/releases page
cool-package 0.1.1 getting released on PyPI
You can also replace patch with minor or major.
-->
----------

That's it. This should kickstart you in developing your own Python package. In the future (once I have a better idea of what am I doing), I might fork and tweak [audreyr's original  Cookiecutter template](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html#step-3-create-a-github-repo) to my personal liking and needs. However, it is more than enough to get you started.

If you still have questions about the implementation or, even better, suggestions for its improvement, please leave a comment here or [file a new issue in Github](https://github.com/arturomoncadatorres/arturomoncadatorres.github.io/issues){: target="_blank"}. I will do my best to try to reply to you.

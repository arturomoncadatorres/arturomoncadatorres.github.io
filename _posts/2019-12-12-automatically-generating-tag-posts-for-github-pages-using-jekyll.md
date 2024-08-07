---
title: Automatically Generating Tag Posts for GitHub Pages using Jekyll
date: 2019-12-12-01T01:03:30+01:00
author: Arturo
layout: post
description: How to automatically generate tag posts for a Jekyll-based GitHub Pages site
permalink: /automatically-generating-tag-posts-for-github-pages-using-jekyll/
mood: speechless
categories:
  - Github Pages
  - Jekyll
tags:
  - github-pages
  - jekyll
  - python
  - website
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/github.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/jekyll.png"/>
</figure>

Recently, I migrated my personal website from Wordpress to [GitHub Pages](https://pages.github.com/){: target="_blank"} using [Jekyll](https://jekyllrb.com/){: target="_blank"}. After some trial and error, I managed to have everything up and running. However, Jekyll tagging (i.e., generating the pages that contain a collection of posts filtered by a tag) requires additional plugins which are [not supported by GitHub Pages](https://help.github.com/en/github/working-with-github-pages/about-github-pages-and-jekyll#plugins){: target="_blank"}. Long Qian wrote a [fantastic tutorial](https://longqian.me/2017/02/09/github-jekyll-tag/){: target="_blank"} on how to implement this functionality with a Python script. Unfortunately, this still requires running the script, adding the files to the staging area, committing them, and pushing them to GitHub. That's a lot of steps for every time that I want to add a new tag. Not only is it prone to errors, but let's be honest: ain't nobody got time for that.

<!--more-->

Therefore, I automated the whole process. I adapted Long's solution and embedded it in a more comprehensive script, [`update_tags.py`](https://github.com/arturomoncadatorres/arturomoncadatorres.github.io/blob/master/update_tags.py){: target="_blank"}. Now, I let [GitPython](https://gitpython.readthedocs.io/en/stable/){: target="_blank"} handle the Git part (make sure you [installed it](https://gitpython.readthedocs.io/en/stable/intro.html#installing-gitpython){: target="_blank"} beforehand). This way, after I finished updating/creating a post with new tags (and pushing those files to GitHub), I can run `update_tags` and let it do the rest: fish the tags used across all posts, create the corresponding posts, and commit and push these changes to GitHub in a single go. To keep things tidy, I recommend running this script when having a clean working space (nothing to commit/push).

Please note that Long's original script reads the tags from posts that are formatted as follows:

{%highlight text %}
---
layout: post
title: Jekyll Tags on Github Pages
description: Github Pages with Jekyll are cool!
tags: blog github-page jekyll
---
{%endhighlight%}

I adapted the script to read tags from posts that are formatted differently:

{%highlight text %}
---
layout: post
title: Jekyll Tags on GitHub Pages
description: GitHub Pages with Jekyll are cool!
tags:
  - blog
  - github-page
  - jekyll
---
{%endhighlight%}

You can find all the files of my website in my [GitHub repository](https://github.com/arturomoncadatorres/arturomoncadatorres.github.io){: target="_blank"}.

*Update*: Nicholas Pachulski came up with a workaround that automates the process (a bit) using a gem. You can check it out [here](https://pachulski.me/jekyll-blog-post-tags-and-github-pages). I haven't tried out myself, but it looks promising!

----------
If you have any comments, questions or feedback, leave them in the comments below [or drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres){: target="_blank"}. Moreover, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

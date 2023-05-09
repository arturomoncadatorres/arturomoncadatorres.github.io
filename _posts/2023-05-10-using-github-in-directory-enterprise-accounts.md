---
title: Using `.github` in Enterprise Accounts
date: 2023-05-10T00:00:01+01:00
author: Arturo
layout: post
description: How to configure the folder .github for (enterprise) GitHub organizations
permalink: /using-github-in-directory-enterprise-accounts/
mood: speechless
categories:
  - Github
tags:
  - github
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/github.png"/>
</figure>

Among GitHub's many cool features, you can create default "[community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file){: target="_blank"}" (e.g., `CODE_OF_CONDUCT.md`, `FUNDING.yml`, etc.) for all your repositories.

<figure class="aligncenter">
	<img width="300" src="../multimedia/images/github/invertocat.png"/>
</figure>

If you are working on repositories from your personal account, you can create a `.github` repository where you can place the corresponding files. Then, new repositories that you create will use these same files (unless you create community health files for each of them, in which case these will override the defaults). However, when working on an enterprise [organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations){: target="_blank"}, there are a couple of considerations that you need to take into account to get this up and running.

<!--more-->

## 1. `.github`-ception [^1]
When working on an enterprise organization, you need to create a `.github` repository. Additionally, you need to create *another* `.github` directory inside it and *there* is where you need to put all your community health files.

{%highlight text %}

.github
├─── .github
|    └─── Community health files
|
└─── ...
{%endhighlight%}

Apparently, this is a [known issue](https://github.com/orgs/community/discussions/22451#discussioncomment-3236785){: target="_blank"}. Unfortunately, this hasn't been clarified in the official documentation (at least at the moment of writing of this post).


## 2. `.github` needs to be public
This is an important one. For this to work, the `.github` repository needs to be public. If you are working on an enterprise organization, you need to *be extra careful* about this, since more often than not, enterprise repositories need to be internal only. Make sure that you double check if you are allowed to have public repositories (even if only for template purposes).

The latter in particular could be a problem when implementing such functionality. Fortunately, there are workarounds. In my case, we added the community health files as part of the [Cookiecutter template](https://github.com/cookiecutter/cookiecutter){: target="_blank"} that we use for new repositories. So far, this has worked pretty well.

I hope this helps and saves you some precious minutes when googling why is it that your enterprise `.github` functionality is not working.


[^1] I know that this isn't the proper definition of something inception, but it is catchy subtitle.

----------
If you have any comments, questions or feedback, leave them in the comments below [or drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres){: target="_blank"}. Moreover, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

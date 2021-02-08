---
title: Adding LDraw Models to Bricklink Studio
date: 2020-12-20-01T01:20:22+01:00
author: Arturo
layout: post
description: Small guide on how to add LDraw models (.dat files) to use as parts in Bricklink Studio
permalink: adding-ldraw-models-to-bricklink-studio/
mood: speechless
categories:
  - Bricklink Studio
  - LEGO
tags:
  - bricklink-studio
  - ldraw
  - lego
---

<figure class="alignleft">
	<img width="32" src="../multimedia/icons/lego.png"/>
</figure>
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/studio.png"/>
</figure>

Recently, I started getting into LEGO again. More interestingly, I started experimenting with [Bricklink Studio](https://www.bricklink.com/v3/studio/download.page){: target="_blank"} (or Studio, in short), a great CAD tool for creating your own (virtual) models brick by brick. One of its best features is the wide variety of parts at your disposal. However, every now and then you can come across a part or two that aren't registered in Studio's catalogue, but that exist already as a model. This is especially true if you are using parts from very old sets. Fortunately, there is a way to add them and make them available for your creations.

<!--more-->

## 1. Find your missing part
[LDraw](https://www.ldraw.org/) is "an open standard for LEGO CAD programs that allow the user to create virtual LEGO models and scenes". It hosts an extensive library of LEGO parts.

Go to [LDraw's Part List](https://www.ldraw.org/cgi-bin/ptlist.cgi){: target="_blank"} and look for your missing part. Finding a specific part can be challenging. The way I usually do it is to look for the inventory of the set to which your part belongs to (for instance, using [Brickset inventories](https://brickset.com/inventories){: target="_blank"}). There, you can find your part's element number, design number, and description. You can use these as search terms in LDraw's Part List.

## 2. Get the part's model ID.
Once you found your part, go to its `Details` page. Here, you will find some important information. At this point, we are interested in the ID of its model file. You will find it at the top, in a green box with a `.dat` extension. Take note of this (and don't close the part's LDraw page yet).

## 3. Check the part's `.dat` file
Go to Studio's part directory. If you accepted the default path during Studio's installation, you will find it in `C:\Program Files\Studio 2.0\ldraw\parts`. Here, you will find a list of all the models used by Studio. Search for the file corresponding to your part. If you cannot find it, go to step 3.1. If the file exists, go to step 4.

### 3.1 Add your part's `.dat` file
Go back to the part's LDraw page and click on `Download` (on top of the green box). Save the `.dat` file on Studio's parts directory.

## 4. Make the model available to Studio
At this point, we are sure that the model exists. It is just a matter of telling Studio about it. To do so, we need to add the part's information to the file `StudioPartDefinition2.txt`, which you can find in `C:\Program Files\Studio 2.0\data`. This is an important file, so before proceeding, I recommend you create a copy of it for safekeeping, in case you mess something up.

Open `StudioPartDefinition2.txt` with your favorite text editor (I prefer using [Notepad++](https://notepad-plus-plus.org/){: target="_blank"}). You will see it is a tab-separated table containing the information of all the parts available to Studio.

Now, this is the tricky part. We need to manually add the missing part information here. There are several fields that need to be filled in:

* `Studio ItemNo`
* `BaseStudioItemNo`
* `BL ItemNo`
* `BL ItemKey`
* `LDraw ItemNo`
* `LDD ItemNo`
* `Description`
* `isPerfectForCulling`
* `BLCatalogIndex`
* `BLCatalogSubIndex`
* `EasyModeIndex`
* `IsAssembly? flexible type`
* `IsDecorated`
* `XPCatalogIndex`
* `XPCatalogSubIndex`

To be honest, I don't know what all of them mean. My recommendation is to look for a similar part to the one you are trying to add (as you did before) and search it in this file by its `.dat` name. Copy its corresponding line and paste it as the first row of the table. Then, adapt it as necessary. The most important fields that you need to change are `LDraw ItemNo` (which corresponds to the part's model ID + `.dat` extension) and `Description` (the text that you will see in Studio for that part). Moreover, be sure that `Studio ItemNo`, `BaseStudioItemNo`, and `BL ItemNo` are unique in the file as well (you can probably use the part's model ID for these fields as well, but double check to be sure).

## 5. Wrap things up
Lastly, save your changes. If you had Studio open, close it and open it again so that it loads the updated part catalogue. Now, if you look for your part within Studio, you should be able to see it and use it in your model as any other part.

I read in a few (old) posts that modifying `StudioPartDefinition2.txt` can make Studio's Patcher to act weird. However, so far I haven't had any issues. Moreover, I am not sure if when a new update of Studio is released (which usually comes with new parts), `StudioPartDefinition2.txt` appends the new data or if it is completely overwritten. What I am trying to say is... please use this method at your own risk ;) .

That's it! Hopefully this will save you many hours of googling.

----------
If you have any comments, questions or feedback, leave them in the comments below [or drop me a line on Twitter (@amoncadatorres)](http://www.twitter.com/amoncadatorres){: target="_blank"}. Moreover, if you found this useful, fun, or just want to show your appreciation, you can always [buy me a cookie](https://www.buymeacoffee.com/amoncadatorres){: target="_blank"}. Cheers!

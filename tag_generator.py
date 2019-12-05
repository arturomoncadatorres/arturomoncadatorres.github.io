#!/usr/bin/env python

'''
tag_generator.py
Copyright 2017 Long Qian
Contact: lqian8@jhu.edu
This script creates tags for your Jekyll blog hosted by Github page.
No plugins required.
See https://longqian.me/2017/02/09/github-jekyll-tag/

Updated 2019-12-05
Arturo Moncada-Torres
arturomoncadatorres@gmail.com
Adapted script to process .md files with tags in format
tags:
    - tag1
    - tag2
    ...
Notice that for this to work properly, tags must be the last element of the
Markdown header.
'''

#%% Preliminaries.
import glob
import os


#%% Define paths.
post_dir = '_posts/'
tag_dir = 'tag/'


#%% Get tags.

# Get Markdown posts files.
filenames = glob.glob(post_dir + '*md')

# Loop through all files.
total_tags = []
for filename in filenames:
    f = open(filename, 'r', encoding='utf8')
    crawl = False
    tag_lines_coming = False
    for line in f:
        current_line = line.strip()
        if crawl:
            if current_line == 'tags:':
                tag_lines_coming = True
                continue
            
        # If --- delimiter is found, start crawling.
        if current_line == '---':
            if not crawl:
                crawl = True
            else:
                crawl = False
                break
            
        # If we are in the actual tag lines (that is, tag_lines_coming is
        # True and we aren't in the tags: line), extract them.
        if tag_lines_coming and (current_line != 'tags:'):
            total_tags.append(current_line.strip('- '))
    f.close()
    
# Make tags unique in a set.
total_tags = set(total_tags)


#%% Create individual tag posts.
old_tags = glob.glob(tag_dir + '*.md')
for tag in old_tags:
    os.remove(tag)
    
if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

for tag in total_tags:
    tag_filename = tag_dir + tag + '.md'
    f = open(tag_filename, 'a')
    write_str = '---\nlayout: tag_page\ntitle: \"Tag: ' + tag + '\"\ntag: ' + tag + '\nrobots: noindex\n---\n'
    f.write(write_str)
    f.close()
print("Tags generated, count", total_tags.__len__())
# Instructions
The intention of this Markdown document is to state a few quick steps for several use cases related to creating and updating a website hosted in Github pages using Jekyll. It is not intended to serve as a complete tutorial.


## Installation
1. As mentioned in the official [Jekyll documentation](https://jekyllrb.com/docs/installation/windows/), first install a Ruby+Devkit version from [RubyInstaller Downloads](https://rubyinstaller.org/downloads/). Use the default options for installation.
0. Open a new command prompt (in admin mode) and install Jekyll and Bundler using `gem install jekyll bundler`
0. Check if Jekyll was installed properly using `jekyll -v`. You should see as an output something like `jekyll 4.0.0`
0. Perform a bundle update typing `bundle update`
0. Navigate to the directory where your website files will be located (e.g., `C:\Users\website\`) and install Github Pages typing `gem install github-pages` *or* copy and paste the files from a template.
0. The `Gemfile` should have the following content

```
gem "github-pages", group: :jekyll_plugins

# Plugins go here.
group :jekyll_plugins do
    gem "jekyll-paginate", "~> 1.1.0"
    gem 'wdm', '>= 0.1.0'
end
```
If you are using a template, you might have to adjust them appropriately. For instance, the `Gemfile` of the template I used looks like this:

```
source "https://rubygems.org"
ruby RUBY_VERSION

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
#gem "jekyll", "4.0.0"

# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`
# (or `gem update github-pages` if you used a gem instead of a bundle).
gem "github-pages", group: :jekyll_plugins

# If you have any plugins, put them here!
group :jekyll_plugins do
    gem "jekyll-paginate", "~> 1.1.0"
    gem 'wdm', '>= 0.1.0'
end
```
Notice that since I am using Github Pages, I commented the line `gem "jekyll", "4.0.0"` and uncommented the line `gem "github-pages", group: :jekyll_plugins`.


## Updating the website

1. Navigate to the directory where your website files are located (e.g., `C:\Users\website\`)

**Locally**
2. Type `bundle exec jekyll serve`. This will launch a local server at `http://localhost:4000/`. Here, you will see the changes that you make to the website (locally).

**Online**
3. If you are happy with the changes, just push them to Github
- `git add ...`
- `git commit -m "Commit message"`
- `git push -u origin master`


## Setting up a computer for updating an existing website
1. As mentioned in the official [Jekyll documentation](https://jekyllrb.com/docs/installation/windows/), first install a Ruby+Devkit version from [RubyInstaller Downloads](https://rubyinstaller.org/downloads/). Use the default options for installation.
0. Open a new command prompt (in admin mode) and install Jekyll and Bundler using `gem install jekyll bundler`
0. Check if Jekyll was installed properly using `jekyll -v`. You should see as an output something like `jekyll 4.0.0`
0. Install the bundler using `gem install bundler` and `bundler install`

## Tips, tricks, and troubleshooting
- The `_site` files are in  the `.gitignore` because they are generated every time that the site is updated. Once in Github Pages, these files are generated based on the web content. There is really no need to push them at all.
- To change the code (color) theme:
  - Go to https://jwarby.github.io/jekyll-pygments-themes/languages/python.html
  - Choose a theme
  - Got to `assets/partials/_syntax.scss` and replace the content with that of the chosen theme
  - Additionally, add the line `.highlight {background: #fff; border: 1px solid $grey-color-lightest; padding: 15px;}` at the beginning to keep the box
  - If you get the error
   ```
   SyntaxError: /Users/taylor/Projects/personal_website/_plugins/generate_categories.rb:50: else without rescue is useless ...L = ”” if (BASEURL == nil) else BASEURL end ... ^~
   ```
      Go to `_plugins/generate_categories.rb` and change the line
  ```
BASEURL = "" if (BASEURL == nil) else BASEURL end
  ```
  to
  ```
	if (BASEURL == nil)
	  BASEURL = ""
	else
	  BASEURL = BASEURL
	end
  ```

## Additional resources
- [Working with Github Pages](https://help.github.com/en/github/working-with-github-pages)
- [How do I order pages in the side bar?](https://stackoverflow.com/a/33983971/948768)
- [How can I add Jekyll Tags using Github Pages?](https://longqian.me/2017/02/09/github-jekyll-tag/)
- [How can I add Jekyll Tags using Github Pages automatically?](https://arturomoncadatorres.com/automatically-generating-tag-posts-for-github-pages-using-jekyll/)

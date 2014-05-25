## Things to install

### install homebrew
`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`

### install rvm
`\curl -sSL https://get.rvm.io | bash
Downloading https://github.com/wayneeseguin/rvm/archive/master.tar.gz`
For using rvm in current shell: `source /Users/nicoledominguez/.rvm/scripts/rvm`

### add sublime text symlink
`ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" ~/.rvm/bin/subl`

### sublime settings
{
	"font_size": 12.0,
	"ignored_packages":
	[
		"Vintage"
	],
	"save_on_focus_lost": true,
	"theme": "Soda Light.sublime-theme"
}

### sublime packages
* install package manager
* install LESS syntax
* install "Tags"


### add git config
* `git config --global user.name "Nicole Dominguez"`
* `git config --global user.email sodevious.net@gmail.com`


## Documentation & Instructions

### Python

Python demo
  /usr/local/share/python/Extras

Setuptools and Pip have been installed. To update them
  pip install --upgrade setuptools
  pip install --upgrade pip

To symlink "Idle" and the "Python Launcher" to ~/Applications
  `brew linkapps`

You can install Python packages with (the outdated easy_install or)
  `pip install <your_favorite_package>`

They will install into the site-package directory
  /usr/local/lib/python2.7/site-packages

See: https://github.com/Homebrew/homebrew/wiki/Homebrew-and-Python


### muckrack & shorties
`
$ brew install python
$ brew install mysql
$ brew install libjpeg
$ brew install libpng
$ brew install redis
$ brew install rabbitmq 
`

### running servers

`workon muckrack`
`python manage.py runserver`
`python manage.py migrate`

#### muckrack

`workon muckrack`

`python manage.py runserver`

`rabbitmq-server`

`redis-server /usr/local/etc/redis.conf`

`mysql.server start`

#### shorties

`rabbitmq-server`

`mysql.server start`

`/usr/local/opt/memcached/bin/memcached -d`

`workon shortyawards`

`python manage.py runserver`


### virtualenv

`
$ easy_install virtualenv
$ easy_install pip
$ pip install virtualenvwrapper
`

### MySql

A "/etc/my.cnf" from another install may interfere with a Homebrew-built
server starting up correctly.

To connect:
    mysql -uroot

To have launchd start mysql at login:
    ln -sfv /usr/local/opt/mysql/*.plist ~/Library/LaunchAgents
    
Then to load mysql now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
    
Or, if you don't want/need launchctl, you can just run:
    `mysql.server start`
    

### memcached

To have launchd start memcached at login:
    ln -sfv /usr/local/opt/memcached/*.plist ~/Library/LaunchAgents
    
Then to load memcached now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.memcached.plist
    
Or, if you don't want/need launchctl, you can just run:
    `/usr/local/opt/memcached/bin/memcached -d`

### rabbitmq

Management Plugin enabled by default at v
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d

To have launchd start rabbitmq at login:
    ln -sfv /usr/local/opt/rabbitmq/*.plist ~/Library/LaunchAgents
    
Then to load rabbitmq now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.rabbitmq.plist
Or, if you don't want/need launchctl, you can just run:
    rabbitmq-server

### redis

To have launchd start redis at login:
    ln -sfv /usr/local/opt/redis/*.plist ~/Library/LaunchAgents
    
Then to load redis now:
    launchctl load ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
    
Or, if you don't want/need launchctl, you can just run:
    redis-server /usr/local/etc/redis.conf 
    
---

# Troubleshooting
ImportError: No module named allauth.socialaccount.providers.facebook : make sure you're on the virtualenv

---

# Voting commands

`python manage.py make_random_link_votes --slug=kickstarter`

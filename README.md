Sublime Text 2 Simple Test
==========================

Overview
--------
  - It save the path of the current file into ~/.last_test
  - It calls a script t to run it

You can customize t as you want.
I suggest:

```shell
#!/bin/bash
# If we have a param then we execute that test and save its path for later
if [ "$#" -gt 0 ]; then
  echo "$@" > ~/.last_test
  echo "Testing on: $@"
  ruby -Itest -Ispec $@

# there is no param, so we read from ~/.last_test
else
  echo "Testing on: $(cat ~/.last_test)"
  ruby -Itest -Ispec $(cat ~/.last_test)
fi

```

Usage
-----

 - Run single test: `Command-Control-t`

Installation
------------

Go to your Sublime Text 2 `Packages` directory

 - OS X: `~/Library/Application\ Support/Sublime\ Text\ 2/Packages`
 - Windows: `%APPDATA%/Sublime Text 2/Packages/`
 - Linux: `~/.config/sublime-text-2/Packages/`

and clone the repository using the command below:

``` shell
git clone https://github.com/libo/sublime-text-simple-test.git SimpleTest
```

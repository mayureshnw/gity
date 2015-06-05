![](http://i.imgur.com/y8g506n.png?1)

# gity

        _ _         
   __ _(_) |_ _   _ 
  / _` | | __| | | |
 | (_| | | |_| |_| |
  \__, |_|\__|\__, |
  |___/       |___/ 


The git magician for python. gity makes using git commands in python, a piece of cake.



## Features

- Written in uncomplicated Python
- Easy to [install](https://github.com/mnw2212/gity#installation)
- Stupidly [easy to use](https://github.com/mnw2212/gity#usage)
- Works on Linux and Mac

## Current Support
- git init
- git clone
- git status
- git add
- git commit
- git push
- git pull
- git checkout


## Installation


### Option 1: [Pip](https://pypi.python.org/pypi/gity)

```bash
$ pip install gity
```

### Option 2: From source

```bash
$ git clone --recursive git@github.com:mnw2212/gity.git
$ cd gity/
$ python setup.py install
```



## Contributing

#### Bug Reports & Feature Requests

Please use the [issue tracker](https://github.com/mnw2212/gity/issues) to report any bugs or file feature requests.

#### Developing

PRs are welcome. To begin developing, follow this:

```bash
# make virtual env
$ git clone --recursive git@github.com:mnw2212/gity.git
$ cd gity/
$ python gity/gity.py
```
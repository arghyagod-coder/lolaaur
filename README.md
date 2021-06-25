# Lola
### `lolaAUR` : A simple CLI package manager for Arch/Arch Based Linux 

[![Downloads](https://static.pepy.tech/personalized-badge/lolaaur?period=total&units=abbreviation&left_color=black&right_color=blue&left_text=Downloads)](https://pepy.tech/project/lolaaur)

**lola is made for linux users who want to download software fast and easy!**

Now many will ask, Why use lola when we have those software managers?

Well, lola is a Command Line Interface and is used inside the terminal. And as we know, terminal downloads are way more faster than the software managers. While many softwares can be downloaded with a single `pacman -S`, most common ones need some more commands.

So `lola` is here to make your life way more easier while installing software! This project targets both advanced and beginner users, because who doesn't like speedy and quicky stuff?

#### Dependencies
+ `click` 

### Built with
+ `Python 3.8.5` 

![python](https://raw.githubusercontent.com/MikeCodesDotNET/ColoredBadges/master/svg/dev/languages/python.svg)


## Installation

#### Method 1 (Recommended):

If you dont have python3 and pip installed on your system, or are not that much of PYTHON CODER, use this method

- Install wget with `sudo pacman -S wget`

- In your terminal-

```bash
cd ~/Downloads;wget https://raw.githubusercontent.com/arghyagod-coder/lolaaur/master/lolaaur/install.sh; sudo bash install.sh
```

- Now `lola` is ready to work!

#### Method 2

If you have python and pip installed in your computer, execute the following

```bash
pip3 install lolaaur
```

But, there are some dependencies that you will need if you go for method 2. They are the following:

- git (`sudo pacman -S git`)
- yay (`sudo pacman -S yay`)

## Supported Platforms:

+ Operating System = Linux64 

![lin](https://raw.githubusercontent.com/MikeCodesDotNET/ColoredBadges/master/svg/dev/tools/bash.svg)
    
  - Arch Linux and Derivatives like Manjaro, Garuda etc

### Guide

- The help command

```bash
>lola --help


  I am Lola! Your assistant who can help you setup your Linux in an easy way!
  You can know more about me in https://github.com/arghyagod-coder/lolaaur.

  I can help you install apps through terminal, and you need to know almost
  nothing about the terminal to do so! Just simple prompts will be enough

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  list        Check the list of supported apps!
  install     Install an app

```

- Check some supported apps of AUR by using the `lola list` command. This list only gives names of a few packages, but every package in AUR repos can be installed via lolaAUR

```bash
> lola list


anaconda ------------- Anaconda- Powerful Tool for DS, DL and ML learners
atom-editor ---------- Atom Code Editor 
audacious ------------ Audacious Music Player
audacity ------------- Professional Audio Edition Software
blender-3.0 -------------- Open Source 3D Creation Suite
brave ---------------- Brave Browser- Fast, Light and Secure
brave-beta ----------- Brave Browser BETA- Regular updates and Bug Fixes
brave-nightly -------- Brave Nightly- Nightly Updates and Bug Fixes
calibre -------------- Free E-Book Suite
cheese --------------- Camera App for Linux
chrome --------------- Google Chrome Browser, the No.1 Browser in market
chromium ------------- Chromium Browser- A Light Browser like Chrome by GOOGLE
clang90 -------------- CLang Compiler for C
codeblocks-svn ------- Code::Blocks editor- Fast and Powerful
crystal -------------- Crystal language support
desmume -------------- DesMume Emulator for NDS and GB Games
discord -------------- Discord Client in Linux
dosbox -------------- DOS-BOX Emulator
dropbox -------------- Cloud Storage Client
microsoft-edge-dev-bin - MS Edge for Linux- Regular Updates 
emacs ---------------- Featureful Text Editor
...
```

- Install an app through lola with the `lola install <appname>` command

```bash
> lola install etcher
 
[sudo] password for user: 
resolving dependencies...
looking for conflicting packages...

Packages (1) etcher-1.5.120-1

Total Installed Size:  36.26 MiB

:: Proceed with installation? [Y/n] y
(1/1) checking keys in keyring                                                    [##############################################] 100%
(1/1) checking package integrity                                                  [##############################################] 100%
(1/1) loading package files                                                       [##############################################] 100%
(1/1) checking for file conflicts                                                 [##############################################] 100%
(1/1) checking available disk space                                               [##############################################] 100%
:: Processing package changes...
(1/1) installing etcher                                                           [##############################################] 100%
Optional dependencies for etcher
    libnotify: for notifications [installed]
:: Running post-transaction hooks...
(1/3) Arming ConditionNeedsUpdate...
(2/3) Updating icon theme caches...
(3/3) Updating the desktop file MIME type cache...
```

- Search Option
  - `lola search <appname>` checks the availability of an app in lola.
  
```bash
> lola search vlc

vlc available!
```

- `lola update` updates lola to the latest version
  
- **Fun Feature-** Use `lola hack <computer_name>` to perform a fake hack on any target pc >_<

- `lola info` gives you a brief description of Lola

## Developer Tools

- [Python 3.8.5](https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz) 

![python](https://raw.githubusercontent.com/MikeCodesDotNET/ColoredBadges/master/svg/dev/languages/python.svg)

- [Sublime Text 3](https://www.sublimetext.com/3)

- [Visual Studio Code](https://code.visualstudio.com) 

![vscode](https://raw.githubusercontent.com/MikeCodesDotNET/ColoredBadges/master/svg/dev/tools/visualstudio_code.svg)

- [Git](https://git-scm.com/) 

![git](https://raw.githubusercontent.com/klaasnicolaas/ColoredBadges/new-badges/svg/dev/tools/git.svg)

- [Python Poetry](https://python-poetry.org/) for package management and publishing

## Release Notes

- **Current Release- 0.1.4**

### What's new?

- Connections to AUR repository make lola very powerful
- By chance, if there's no such repository in AUR, lola attempts to resolve the packages with other managers
- Better Exception Handling
- Added few fun features to enhance user experience
- Updated README

#### Developers
- [Arghya Sarkar](https://github.com/arghyagod-coder)

## License

License © 2021-Present Arghya Sarkar

This repository is licensed under the MIT license. See [LICENSE](https://github.com/arghyagod-coder/lolaaur/master/LICENSE) for details.

## Special Notes

- Contribution is appreciated! Visit the contribution guide in [Contribution Guide](CONTRIBUTING.md)
- If you don't find an app in the supported app list, file an issue in [the issue page](https://github.com/arghyagod-coder/lolaaur/issues). Issues aren't ignored by the developers
- Thanks for seeing my project!
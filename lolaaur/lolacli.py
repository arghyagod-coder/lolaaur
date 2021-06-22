
import click
import requests
import os
import subprocess as sb
import time


def run(command):
    sb.run(command, shell=True)


apps = '''
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
etcher --------------- Professional ISO Disk Image Writer
evolution ------------ A lightweight yet reliable Mail Client
firefox -------------- Firefox Web Browser- Security at top
fish ----------------- Fish Shell
drive ---------------- Google Drive Client for Linux
google-earth-pro ----- Google Earth Feature for Linux
g++ ------------------ G++ Compiler for C/CPP
gcc ------------------ GCC Compiler for C
geany ---------------- Lightweight Text Editor
gedit ---------------- Casual Text Editor
geogebra-5 ----------- Applications for dealing with mathematical operations and visualizations
gimp ----------------- Professional Photo Edition Software
go ------------------- Go Language for Linux
gparted -------------- Manage your disks and partitions with GParted
htop ----------------- Monitor your resources with htop
intellij-idea-ce ----- IntelliJ IDEA Community Edition
jdk ------------------ JDK 11 for Linux
jedit----------------- Casual Text Editor
kate ----------------- Casual Text Editor
kazam ---------------- Light Screen Recorder for Linux
kdenlive ------------- Casual Video Edition Software
krita ---------------- Bring your artistic skills to life with Krita
lazarus-svn ---------- Pascal IDE 
libreoffice-dev-bin -- Complete Office Suite
lutris --------------- Open Source Gaming Platform for Linux
miniconda3 ----------- Miniconda- Light and Powerful
mypaint -------------- Draw beautiful art with MyPaint
nim ------------------ Nim Language Support
nodejs --------------- NodeJS for Linux
obs-studio ----------- Professional Screen Recorder
pinta ---------------- Draw beautiful images with Pinta
plank ---------------- Plank Dock for Desktop Linux
pycharm-community-edition -- PyCharm Community Edition
r -------------------- R Language for linux
rstudio-desktop ------ Best IDE for R Programming
scribus -------------- Professional DTP Software
shotwell ------------- Shotwell light casual Image Editor
signal-desktop ------- Signal client for Linux
simplescreenrecorder - Professional Screen Recorder
spotify -------------- Spotify Client
spyder --------------- An IDE for Scientists
steam ---------------- Steam Proton Client for Linux
sublime-text-dev ----- Sublime Text- A powerful yet lightweight Editor
telegram-desktop ------------- Telegram Client for Linux
terminator ----------- Terminal Manager Terminator
thonny --------------- Thonny Python Beginner's IDE
thunderbird ---------- Thunderbird Mail Client from Moz://a
vim ------------------ Professional Terminal Text Editor
virtualbox ----------- Make and Manage Virtual Machines with Vbox
vlc ------------------ No. 1 Media Player
visual-studio-code-bin - Visual Studio Code Text Editor
zoom ----------------- Zoom Client for Conferences and Meetings
and many more...
'''


@click.group()
@click.version_option('0.1.3', prog_name='lola')
def main():
    '''I am Lola! Your assistant who can help you setup your Linux in an easy way! You can know more about me in https://github.com/arghyagod-coder/lolaaur.
I can help you install apps through terminal, and you need to know almost nothing about the terminal to do so! Just simple prompts will be enough'''
    pass


@main.command('list', help='Check the list of supported apps!')
def list():
    print(apps)


@main.command('install', help=('Install an app'))
@click.argument('files', nargs=-1)
def install(files):
    for file in files:
    
        os.chdir(os.path.join(os.path.expanduser("~"), "Downloads"))

        pos= {
            f'https://aur.archlinux.org/packages/{file}' : [f'https://aur.archlinux.org/{file}.git', f'{file}'],
            f'https://aur.archlinux.org/packages/{file}-bin' : [f'https://aur.archlinux.org/{file}-bin.git', f'{file}-bin'],
            f'https://aur.archlinux.org/packages/{file}-git' : [f'https://aur.archlinux.org/{file}-git.git', f'{file}-git'] 
        }
        home = (os.path.expanduser('~'))
        i=0
        for key, value in pos.items():
            res = requests.get(key)
            if res.status_code!=404:
                run(f"git clone {value[0]}; cd {home}/Downloads/{value[1]};makepkg -si;cd ..;")
                run(f'rm -rf {home}/Downloads/{file}')
                i+=1
                break

        if i==0:
            try:
                sb.check_output(f'yay -S {file} -y', shell=True)
                run(f'yay -S {file} -y')
            except sb.CalledProcessError:
                click.echo(f"\n\n  -->> {file} was not found.")
        
        
@main.command('info', help='Know lola well!')
def info():
    click.echo("""
db       .d88b.  db       .d8b.  
88      .8P  Y8. 88      d8' `8b 
88      88    88 88      88ooo88 
88      88    88 88      88~~~88 
88booo. `8b  d8' 88booo. 88   88 
Y88888P  `Y88P'  Y88888P YP   YP 
                                 
I am lola! I am here to help you install software in your system fast and easily! 

Why use lola when we have those software managers?

Well, lola is a Command Line Interface and is used inside the terminal. And as we know, terminal downloads are way more faster than the software managers. While many softwares can be downloaded with a single pacman -S, most common ones need some more commands.

So I am here to make your life way more easier while installing software! This project targets both advanced and beginner users, because who doesn't like speedy and quicky stuff?

""")

@main.command('hack', help="A fun option to fake-hack a pc by giving it's username")
@click.argument('pc', nargs=1)
def hack(pc):
    i=0
    with click.progressbar(range(0,50)) as bar:
        for user in bar:
            i+=1
            time.sleep(0.23)
            click.echo(click.style(i, bg='black', fg='green'))
    click.echo(click.style(f'Entering into {pc} system...', bg='black', fg='green'))
    time.sleep(2)
    click.echo(click.style(f'Obtaining IP Address...', bg='black', fg='green'))
    time.sleep(2)
    click.echo(click.style('Obtained Data Successfully! Selling them to dark web!', bg='black', fg='green'))
    time.sleep(4)
    os.system('clear')
    click.echo(click.style('--SOLD DATA--', bg='black', fg='green'))
    click.echo(click.style('PHASE 1 COMPLETED!', bg='black', fg='green'))
    time.sleep(4)
    os.system('clear')
    click.echo(click.style('Now infecting the target with Viruses', bg='black', fg='green'))
    click.echo(click.style('List of Viruses: \n\n memz\nwannacry\nbutterfly-ware\n', bg='black', fg='green'))
    time.sleep(3)
    with click.progressbar(range(0,50)) as bar:
        for user in bar:
            i+=1
            time.sleep(0.10)
            click.echo(click.style('Installing VIRUSES.... \n Running them', bg='black', fg='green'))
            click.echo(click.style(i, bg='black', fg='green'))
    time.sleep(2)
    click.echo(click.style('Computer Infected Successfully!', bg='black', fg='green'))
    time.sleep(2)
    click.echo(click.style('Processing Data', bg='black', fg='green'))
    time.sleep(1)
    run('clear')
    click.echo(click.style(f'{pc} was hacked successfully!', bg='black', fg='green'))

@main.command('update', help='Update lolacli to the latest version')
def update():
    os.system(f'pip3 install lolaaur -U')

@main.command('search', help='Check Availability of an app in lola')
@click.argument('app', nargs=1)
def search(app):
    pos= [
            f'https://aur.archlinux.org/packages/{app}',
            f'https://aur.archlinux.org/packages/{app}-bin',
            f'https://aur.archlinux.org/packages/{app}-git' 
        ]
    i=0
    for key in pos:
        res = requests.get(key)
        if res.status_code!=404:
            i+=1

    if i==0:
        print(f'No package named {app} found')
    else:
        print(f'{app} available')

if __name__ == "__main__":
    main()
    
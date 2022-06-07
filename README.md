Dougie's System Monitoring Tool
---

This is utility I'm writing to be a Swiss Army Knife of my sysadmin monitoring needs.

For now, I just needed a simple memory/CPU usage utility. The problem with `htop` and `ps` is they do not group scripts. So there could be multiple Firefox/Apache/whatever programs running with their separate memory usage. I want to see what memory/CPU usage they are using in TOTAL - in aggregate.

```
Usage: dsmt mem|cpu [MAX_RESULTS]
```

Example uses:

```
# See the highest memory usage programs:
dsmt mem

# See the 10 highest memory usage programs:
dsmt mem 10

# See the highest CPU using programs:
dsmt cpu
```

Example output (`dsmt mem 10`):

```
4264M	/usr/lib/firefox/firefox
394M 	/app/extra/lib/slack/slack
315M 	/usr/bin/gnome-shell
150M 	/usr/bin/python
126M 	/usr/lib/gnome-terminal-server
110M 	emacs
94M  	/usr/bin/nautilus
86M  	/usr/bin/geary
63M  	/usr/bin/syncthing
63M  	/usr/bin/gedit
```

## Recommended Install

I have `$HOME/.local/bin` in my executable `$PATH` variable.

So, the recommended install is:

```
git clone https://github.com/DougBeney/DSMT.git
cd DSMT
chmod +x ./dsmt.py
ln -s $PWD/dsmt.py ~/.local/bin/dsmt
```

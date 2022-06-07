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
966M	/usr/sbin/apache2
243M	/usr/sbin/mysqld
89M 	/lib/systemd/systemd-journald
42M 	/usr/bin/redis-server
24M 	/usr/bin/python3
22M 	/usr/lib/snapd/snapd
16M 	/sbin/multipathd
14M 	sshd:
10M 	/sbin/init
10M 	python3
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

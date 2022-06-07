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
1279M  	/usr/sbin/apache2
243M   	/usr/sbin/mysqld
89M    	/lib/systemd/systemd-journald
24M    	/usr/bin/python3
22M    	/usr/lib/snapd/snapd
16M    	/sbin/multipathd
14M    	sshd:
14M    	/usr/bin/redis-server
10M    	/sbin/init
10M    	python3
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

## TODO

The next step is to add an argument to the command that returns results as JSON.

From there I could create a "log" argument that logs the results to a JSON with a timestamp.

Prototype:

```
dsmt mem 10 --log=~/mem-usage-log.json
```

Output (`~/mem-usage-log.json`):

```json
{
	"2022-06-07T15:15:18-0400": {
		"cmd": "/usr/sbin/apache2"
		"mem": 1000
	}
}
```

*`mem` would be in megabytes*

Maybe add a Flask web server that shows an interactive graph:

```
dsmt log_server ~/mem-usage-log.json
```

The idea of this is you can add the `dsmt mem 10 --log=~/mem-usage-log.json` command to your crontab. You'd have a log of memory usage for later analysis.

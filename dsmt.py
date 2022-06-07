#!/usr/bin/env python3
import sys
import subprocess
import re

DEDITATED_WAM = 0
with open('/proc/meminfo') as f:
	meminfo = f.read()
matched = re.search(r'^MemTotal:\s+(\d+)', meminfo)
if matched:
	# deditated wam in megabytes
	DEDITATED_WAM = int(matched.groups()[0]) / 1000


processes = subprocess.run(
	['ps', 'ax', '-o', 'command:100,%mem:5,%cpu:5'], capture_output=True)

lines = processes.stdout.decode('utf-8').split('\n')

process_obj = {}

for line in lines[1:]:
	if len(line) == 0:
		continue

	cmd = line[0:100].strip()
	cmd_split = cmd.split(' ', 1)
	cmd_name = cmd_split[0]
	cmd_args = '[no args]'

	if len(cmd_split) > 1:
		cmd_args = cmd_split[1]

	mem = float(line[101:106].strip())
	cpu = float(line[106:112].strip())

	pobj = process_obj[cmd_name] = process_obj.get(cmd_name, {})
	pobj['mem'] = pobj.get('mem', 0.0)
	pobj['cpu'] = pobj.get('cpu', 0.0)

	pobj['args'] = pobj.get('args', {})
	the_args = pobj['args'].get(cmd_args, {})
	the_args['mem'] = the_args.get('mem', 0.0)
	the_args['cpu'] = the_args.get('cpu', 0.0)

	pobj['mem'] += mem
	pobj['cpu'] += cpu
	the_args['mem'] += mem
	the_args['cpu'] += cpu

	pobj['args'][cmd_args] = the_args
	process_obj[cmd_name] = pobj

sysargs = sys.argv
sortmethod = ''
max_results = -1


def printhelp():
	print('Usage: dsmt mem|cpu [MAX_RESULTS]')
	sys.exit(0)


if len(sysargs) <= 1:
	printhelp()
elif len(sysargs) > 2:
	max_results = sys.argv[2]
	if not max_results.isnumeric():
		print('Error: MAX_RESULTS must be an integer.')
		sys.exit(1)
	max_results = int(max_results)

requested_sort_method = sys.argv[1]

if requested_sort_method.lower() == 'mem':
	sortmethod = 'mem'
elif requested_sort_method.lower() == 'cpu':
	sortmethod = 'cpu'

if sortmethod == '':
	printhelp()

sorted_processes = sorted(process_obj, key=lambda p:process_obj[p][sortmethod], reverse=True)

if max_results != -1:
	sorted_processes = sorted_processes[0:max_results]

for p in sorted_processes:
	o = process_obj[p]
	mem_or_cpu = o[sortmethod]

	if mem_or_cpu == 0:
		continue

	if sortmethod == 'mem':
		mem_or_cpu = str(int(DEDITATED_WAM * (mem_or_cpu / 100))) + 'M'
	else:
		mem_or_cpu = str(mem_or_cpu)[0:5]

	print(mem_or_cpu + '\t' + p)

# with open('/home/doug/Downloads/json_data.json', 'w') as outfile:
#     outfile.write(json.dumps(process_obj, indent=2))

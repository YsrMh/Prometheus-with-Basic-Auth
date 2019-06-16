#!/usr/bin/env python3

from pexpect import spawn
from subprocess import call
import logging

def start_prometheus_with_authentication():
	prom_shell = spawn('bash', timeout=None)
	lg = logging.getLogger('prometheus_wrapper_logger')
	lg.setLevel(logging.DEBUG)
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch = logging.StreamHandler()
	ch.setFormatter(formatter)
	ch.setLevel(logging.INFO)
	lg.addHandler(ch)
	try:
		prom_shell.sendline('./prometheus -web.listen-address ":9090" -config.file "./prometheus.yml" -storage.local.retention=744h & mitmdump -R http://0.0.0.0:9090 -p 8080 --htpasswd ./.htpasswd &')
		prom_shell.sendline('echo $! > .pid')
		for line in prom_shell: lg.info(line.decode('utf-8')[:-1])
	except KeyboardInterrupt:
		lg.info('Stopping prometheus and mitmproxy.')
		with open('.pid', 'r') as f: apid = int(f.read())
		kill_list = [str(apid), str(apid-1)]
		lg.info('killing pids %r' %(kill_list))
		for pid in kill_list: call(['kill', pid])


if __name__=='__main__':
	start_prometheus_with_authentication()

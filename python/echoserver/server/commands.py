import json
import os
import platform

class Commands:

	def list_devices(self):
		devices = {}
		devices['drive1'] = "C"
		devices['drive2'] = "D"
		return json.dumps(devices)

	def get_environment(self):
		environment = {}
		environment['sysinfo'] = {}
		environment['sysinfo']['platform'] = platform.platform()
		environment['sysinfo']['node'] = platform.node()
		environment['sysinfo']['processor'] = platform.processor()
		environment['sysinfo']['python_compiler'] = platform.python_compiler()
		return json.dumps(environment)

	def scan_dir(self, dir):
		listing = {}
		listing['files'] = {}
		for direntry in os.scandir(path=dir):
			listing['files'][direntry.name] = {}
			listing['files'][direntry.name]['name'] = direntry.name
			listing['files'][direntry.name]['path'] = direntry.path
			listing['files'][direntry.name]['is_dir'] = direntry.is_dir()

		return json.dumps(listing)
		



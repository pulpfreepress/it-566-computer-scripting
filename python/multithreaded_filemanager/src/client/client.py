import socket
import json


class Client:

	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self._connect()

	def _connect(self):
		print("Connecting to %s:%d" % (self.ip,self.port))
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((self.ip, self.port))
		print("Connected to %s:%d" % (self.ip,self.port))

	def _process_server_response(self):
		response = self.client.recv(4096)
		json_string = response.decode('utf-8')
		parsed = json.loads(json_string)
		print(json.dumps(parsed, indent=4, sort_keys=True))


	def send(self, message_string):
		self.client.send(bytearray(message_string, 'utf-8'))
		#self._process_server_response()

	def close(self):
		self.client.close()
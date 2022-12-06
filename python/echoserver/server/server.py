"""This is the server."""
import socket
import threading
import json
import os
from commands import Commands

class Server:

	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.commands = Commands()
		self._listen(self.ip, self.port)
		self._accept_connections()


	def _listen(self, ip, port):
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind((ip, port))
			self.server.listen(5)
			print("Listening on %s:%d" % (ip,port))
		except Exception as e:
			print(e)

	def _process_client_requests(self, client):
		try:
			with client:
				while True:
					order = client.recv(1024)
					if not order: break
					command = (order.decode("utf-8")).split(':')
					print("Received: %s" % command)

					'''Command Processing Section '''
					response = ""

					if(command[0] == "LIST_DEVICES"):
						response = self.commands.list_devices()
					elif(command[0] == "GET_ENVIRONMENT"):
						response = self.commands.get_environment()
					elif(command[0] == "SCAN_DIR"):
						response = self.commands.scan_dir(command[1])
					


					client.send(bytearray(response, "utf-8"))
		
		except Exception as e:
			print(e)
		


	def _accept_connections(self):
		try:
			with self.server:
				while True:
					print("Waiting for incomming client connection...")
					client,address = self.server.accept()
					print("Accepted connection from %s:%d" % (address[0],address[1]))
					client_handler = threading.Thread(target=self._process_client_requests,args=(client,))
					client_handler.start()
		except Exception as e:
			print(e)
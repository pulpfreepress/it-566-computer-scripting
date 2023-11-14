"""This is the server."""
import socket
import threading
import json
import os
from app import App


class Server:
	def __init__(self, ip, port):
		self.port = port
		self.ip = ip
		self.app = App()
		self._listen(ip, port)
		self._accept_connections()


	def _listen(self, ip, port):
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			if os.name == 'nt':
				self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			else:
				self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
			self.server.bind((ip, port))
			self.server.listen(5)
			print("Listening on %s:%d" % (ip,port))
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

					if(command[0] == "ADD_PERSON"):
						response = self.add_person(command[1])
					elif(command[0] == "LIST_PEOPLE"):
						response = self.list_people()
					elif(command[0] == "DELETE_PERSON"):
						response = self.delete_person()
					

					#client.send(bytearray(response, "utf-8"))
		
		except Exception as e:
			print(e)

	def add_person(self, data):
		print(f"add_person() method called with person data: {data}")
		person_list = data.split(',')
		self.app.add_person(person_list[0], person_list[1], person_list[2])

	def list_people(self):
		print("list_people() method called")

	def delete_person(self):
		print("delete_person() method called")
		
	
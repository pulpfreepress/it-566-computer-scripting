from client import Client 
import time

def main():
	c1 = Client("127.0.0.1", 5000)
	c1.send("LIST_DEVICES")
	c1.send("GET_ENVIRONMENT")
	c1.send("SCAN_DIR:../../..")
	
	c1.close()



if __name__ == "__main__":
	main()
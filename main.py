import hashlib
import datetime

class Block:
	def __init__(self, index, timestamp, data, previous_hash):
		self.index = index
		self.timestamp = timestamp
		self.data = data
		self.previous_hash = previous_hash
		self.hash = self.calculate_hash()

	def calculate_hash(self):
		sha = hashlib.sha256()
		sha.update(str(self.index).encode('utf-8')+
			str(self.timestamp).encode('utf-8')+
			str(self.data).encode('utf-8')+
			str(self.previous_hash).encode('utf-8'))

		return sha.hexdigest()

class Blockchain:
	def  __init__(self):
		self.chain = [self.create_genesis_block()]

	def create_genesis_block(self):
		return Block(0, datetime.datetime.now(), 'Genesis Block', '0')

	def add_block(self, new_block):
		new_block.previous_hash = self.chain[-1].hash
		new_block.hash = new_block.calculate_hash()
		self.chain.append(new_block)

	def is_valid(self):
		for i in range(1, len(self.chain)):
			current_block = self.chain[i]
			previous_block = self.chain[i - 1]

			if current_block.hash != current_block.calculate_hash():
				return False
			if current_block.previous_hash != previous_block.hash:
				return False

		return True
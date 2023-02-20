# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class ChainingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key = key
			self.value = value

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):
		self.the_table = [[] for i in range(cap)]
		self.cap = cap
		self.counter = 0

	def get_hashvalue(self,key):
		h = 0
		for c in key:
			h += ord(c)
		return h % self.cap

	def insert(self,key, value):
		h = self.get_hashvalue(key)
		Isfound = False
		for kd in self.the_table[h]:
			if kd[0] == key:
				Isfound = True
				return False

		if not Isfound:
			self.the_table[h].append((key,value))
			self.counter += 1
    	
		load = self.counter/self.cap
		if load > 1.0 :
			new_table = [[] for i in range(self.cap*2)]
			self.cap *= 2
			for i in range(len(self.the_table)):
				if len(self.the_table[i]) != 0:
					for kd in self.the_table[i]:
						h = self.get_hashvalue(kd[0])
						new_table[h].append((kd[0],kd[1]))
			self.the_table = new_table
		return True
	
	def modify(self, key, value):
		h = self.get_hashvalue(key)

		for index,ele in enumerate(self.the_table[h]):
			if len(ele) == 2 and ele[0] == key:
				self.the_table[h][index] = (key,value)
				return True
		return False

	def remove(self, key):
		h = self.get_hashvalue(key)
		for i,el in enumerate(self.the_table[h]):
			if len(el) == 2 and el[0] == key:
				del self.the_table[h][i]
				self.counter -= 1
				return True
		return False
	
	def search(self, key):
		h = self.get_hashvalue(key)
		for i in self.the_table[h]:
			if i[0] == key:
				return i[1]
		return None
				
	def capacity(self):
		return self.cap

	def __len__(self):
		return self.counter


class LinearProbingHash:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key = None, value=None):
			self.key = key
			self.value = value

	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use linear probing for collision resolution)
	
	def __init__(self, cap=32):
		self.the_table = [None for i in range(cap)]
		self.cap = cap
		self.counter = 0

	# insert method
	def insert(self,key, value):
		hash_idx = self.get_hashvalue(key)
		self.counter += 1

		if self.the_table[hash_idx] == None:
			self.the_table[hash_idx] = (key,value)

		elif self.the_table[hash_idx][0] == key:
			self.counter -= 1
			return False
		 
		else:
			i = 1
			Isfound = False
			while Isfound != True:
				new = (hash_idx + i)
				if new == self.cap:
					new = hash_idx = 0

				if self.the_table[new] == None:
					Isfound = True
					self.the_table[new] = (key,value)

				elif self.the_table[new][0] == key:
					self.counter -= 1
					return False
				i += 1

		load = self.counter/self.cap
		if load > 0.7 :
			new_table = self.the_table
			old = self.cap
			self.the_table = [None for i in range(self.cap*2)]
			self.cap *= 2
			self.counter = 0

			for i in range(old):
				if new_table[i] != None:
					self.insert(new_table[i][0],new_table[i][1])
	
		return True

	def modify(self, key, value):
		return_index = self.key_finder(key)

		if return_index == None:
			return False
		
		self.the_table[return_index] = (key,value)
		return True
			
	def remove(self, key):
		return_index = self.key_finder(key)

		if return_index == None:
			return False
		
		self.the_table[return_index] = key
		self.counter -= 1
		return True 
		
	def search(self, key):
		return_index = self.key_finder(key)

		if return_index == None:
			return None
		return self.the_table[return_index][1]

	def capacity(self):
		return self.cap

	def __len__(self):
		return self.counter

	def get_hashvalue(self,key):
		hash = 0
		for char in key:
			hash += ord(char)
		return hash % self.cap

	def key_finder(self,key):
		return_index = self.get_hashvalue(key)

# this means that there is no key-value pair on the first
# hash value provided
		if self.the_table[return_index] == None:
			return None
		
		if self.the_table[return_index][0] != key:
			original = return_index
			step_up = 1
			while self.the_table[return_index][0] != key:
				return_index = (return_index + step_up)%self.cap
				if self.the_table[return_index] == None:
					return None
				if original == return_index:
					return None

		return return_index
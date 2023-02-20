class SortedTable:

	# packaging the key-value pair into one object
	class Record:
		def __init__(self, key, value):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		# this initializes a list of of capacity length with None
		self.the_table = [None for i in range(cap)]
		self.cap = cap


	def insert(self, key, value):        
		if (self.search(key)!=None):                            # 1
			return False                                        # 0

		if(len(self) == self.cap):                             #  1
			# increase the capacity if list is full
			new_table = [None for i in range(self.cap*2)]       # 2n + 1
			for i in range(self.cap):                          # n
				new_table[i]=self.the_table[i] 					# n(1)
			self.the_table = new_table                         # 1
			self.cap *= 2                                     # 2


		self.the_table[len(self)]=self.Record(key,value)         # 1
		size = len(self)                                        # 1
		for i in range (0,size-1):                               # (n - 1 ) + 2      
			for j in range(0,size-1-i):							# (n - 1)(n - 1 + 2)
				if(self.the_table[j].key>self.the_table[j+1].key): # 2
					tmp=self.the_table[j]                          # 1
					self.the_table[j]=self.the_table[j+1]          # 1
					self.the_table[j+1]=tmp                       # 1
		return True 												# 1
# T(n) = 1 + 1 + 2n + 1 + n + n + 1 + 2 + 1 + 1 + n + 1 + n^2 - 1 + 2 + 1 + 1 + 1 + 1 + 1
# T(n) = n^2 + 5n + 15
# T(n) = O(n^2)

# O(n) is asymptotically faster than O(n^2).

	def modify(self, key, value):
		i = 0          # 1
		while (i < len(self) and self.the_table[i].key != key): # (1 + logn) * 2
			i+=1												# (1 + logn) * 4
		if(i==len(self)):                                       # 1
			return False                                        # 1
		else:
			self.the_table[i].value = value                     # 1
			return True        								    # 1
# T(n) = 1 + (1 + logn) * 2 + (1 + logn) * 4 + 1 + 1 + 1 + 1
# T(n) = 11 + 6logn
# T(n) = O(log n)


	def remove(self, key):
		i = 0                              # 1
		size = len(self)                   # 2
		while (i < size and self.the_table[i].key != key):      # (1 + logn) * 2
			i+=1                                                # ((1 + logn) * 2)(2) = (1 + logn) * 4
		if(i==size):                                            # 1
			return False                                        # 1
		while(i+1 < size):                                      # n - 1
			self.the_table[i]=self.the_table[i+1]               # (n - 1)(2) = 2n - 2
			i+=1												# (n - 1)(2) = 2n - 2
		self.the_table[i] = None                                # 1
		return True                                             # 1
# T(n) = 1 + 2 + (1 + logn)*2 + (1 + logn)*4 + 1 + 1 + n - 1 + 2n - 2 + 2n - 2 + 1 + 1
# T(n) = 6logn + 3n + 8
# n >>>>> logn
# T(n) = O(n)


	def search(self, key):
		i = 0       # 1
		size = len(self)        # 2
		while  i < size and self.the_table[i].key != key :  # n + 1
			i+=1                   # (n + 1)(2)
		if i==size:                # 1
			return None            # 0 
		else:
			return self.the_table[i].value    # 1
# T(n) = 1 + 2 + (n + 1) + (n + 1)(2) +  1 + 1 
# T(n) = 3n + 8
# T(n) = O(n)

# Searching should be done using binary search
# becuase all the data is sorted and this will give us
# O(log n) which is better O(n)


	def capacity(self):
		return self.cap              # 1
# T(n) = Constant
# T(n) = O(1)


	def __len__(self):
		i =0                       # 1
		count = 0                  # 1
		while(i < len(self.the_table)):       # n
			if(self.the_table[i]!=None):      # n(2)
				count+=1					  # n(2)
			i+=1                              # n(2)
		return count                          # 1
# T(n) = n + 2n + 2n + 2n + 1 = 7n + 1
# T(n) = O(n)


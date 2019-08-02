import copy

class visiter:
	def __init__(self, l):
		self.l = l
		self.iter = iter(l)
		self.previous = None
		self.end = len(l) - 1
		self.current_index = 0
		self.current = l[self.get_index()]
		self.next = l[self.get_index(increment=1)]

	def __call__(self):
		return self

	def __iter__(self):
		return self

	def __next__(self):
		self.previous = self.l[self.get_index(-1)] if self.current_index > 0 else None
		self.current = next(self.iter)
		self.next = self.get_next() if self.current_index < self.end else None
		self.current_index += 1
		return self

	def get_index(self, increment=0):
		return min(self.current_index + increment, max(self.end, 0))

	def get_next(self):
		return self.l[self.get_index(1)]

g = visiter([1, 2, 3, 4])
for n in g:
	print(f"previous: {g.previous} -- current: {g.current} -- next: {g.next}")

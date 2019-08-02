class visiter:
	def __init__(self, gen_iter):
		self._iter = gen_iter()
		self.previous = None
		self.end = len(self._iter) - 1
		self.current_index = 0
		self.current = list(self._iter)[self.current_index]
		self.next = list(self._iter)[min(self.current_index + 1, self.end)]

	def get_next(self):
		next_index = min(self.current_index + 1, self.end)
		next_value = list(self._iter)[next_index]
		return next_value

	def __next__(self):
		self.previous = self.current
		self.current = next(self._iter)
		self.current_index += 1
		self.next = self.get_next()
		return self

g = visiter([1, 2, 3, 4])
[print(f"previous: {g.previous} -- current: {g.current} -- next: {g.next}") for n in g]

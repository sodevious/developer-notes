prices = []

def compute_total(a):
	prices.append(a)

	return a * 0.10 + a

compute_total([19.95, 3.75, 8.50])

print compute_total




class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
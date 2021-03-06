'''
之前有同学提到说，想知道更多关于Generator的东西。

那么这一期就给大家讲一讲Generator是什么？为什么要使用Generator？
'''

def example1():
	def generator_function():
		yield 1
		yield 2
		return 3
	generatorObject = generator_function()
	print(next(generatorObject))
	print(next(generatorObject))
	try:
		print(next(generatorObject))
	except:
		print('We have reached the end of iteration')

def example2():
	def generator_function(number):
		while number > 0:
			yield number
			number -= 1
	for number in generator_function(10):
		print(number)

def example3():
	def generator_function(number):
		if number > 0:
			yield number
			yield from generator_function(number-1)
	for number in generator_function(10):
		print(number)

example1()
example2()
example3()


# Event Loop
class Event():
	pass


class EventLoop():
	pass


class Future():
	pass



import socket
import time

def get(path):
	s = socket.socket()
	s.connect(('localhost', 3000))

	request = 'GET %s HHTP/1.0\r\n\r\n' % path
	s.send(request.encode())

	chunks = []
	while True:
		chunk = s.recv(1000)
		if chunk:
			chunks.append(chunk)
		else:
			body = (b''.join(chunks)).decode()
			print('--------------------------------------')
			print(body)
			print('--------------------------------------\n\n')
			return

start = time.time()
get('/super-slow')
get('/super-slow')
get('/super-slow')
print('%.1f sec' % (time.time() - start))












#

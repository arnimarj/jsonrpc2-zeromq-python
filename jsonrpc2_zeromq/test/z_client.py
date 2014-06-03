import time
from jsonrpc2_zeromq import RPCClient

c = RPCClient("tcp://127.0.0.1:57570", logger = None)
N = 10000

while True:
	t_0 = time.time()

	for i in xrange(100):
		c.echo("Echo?")
	t_1 = time.time()
	print N / (t_1 - t_0)

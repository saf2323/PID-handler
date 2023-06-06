import os
import signal

inp = int(input('Enter PID:'))
os.kill(inp, signal.SIGILL)
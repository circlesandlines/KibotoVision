import time
import livestreamer

streams = livestreamer.streams('http://www.twitch.tv/nightblue3')

stream = streams["source"]
print stream

fd = stream.open()

while True:
        data = ''
        data = fd.read(300000)

	f = open('stream/stream.bin', 'wb+')
	f.write(data)
	f.close()

	time.sleep(0.01)

fd.close()

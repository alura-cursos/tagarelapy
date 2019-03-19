import ffmpy

class Video:

	def __init__(self, basename, basefolder="../"):
		self.basefolder = basefolder
		self.basename = basename

	def snapshot(self, seconds, nanoseconds = 0):
		timestamp = '{}.{}'.format(seconds, nanoseconds)
		output = '{}data/processed/{}-{}.jpg'.format(self.basefolder, self.basename, timestamp)
		seek = '-ss {}'.format(timestamp)
		ff = ffmpy.FFmpeg(
			inputs={'{}data/raw/{}.mp4'.format(self.basefolder, self.basename): seek},
			outputs={output: '-vframes 1'}
		)
		print(ff.cmd)
		return output

	def to_wav(self):
		output = '{}data/processed/{}.wav'.format(self.basefolder, self.basename)
		if os.path.isfile(output):
			print("Skipping {}".format(output))
			return
		ff = ffmpy.FFmpeg(
			inputs={'{}data/raw/{}.mp4'.format(self.basefolder, self.basename): None},
			outputs={output: '-ar 16000 -ac 1'}
		)
		print(ff.cmd)
		return ff.run()

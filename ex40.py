class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy Birthday to you",
									 "I don't want to get sued",
									 "So I'll stop right there"])
									 
bulls_on_parade = Song(["They rally around the family",
												"With pockets full of shells"])

#mary_had_a_little_lamb = Song(["Mary had a little lamb",
#															 "Its fleece was white as snow"])

var1 = "Mary had a little lamb"

var2 = "Its fleece was white as snow"

item = Song(var1)
item.sing_me_a_song()
								
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

mary_had_a_little_lamb.sing_me_a_song()

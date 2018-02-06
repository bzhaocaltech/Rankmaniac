import random
import string
import sys

for line in sys.stdin.read().splitlines():
	print line

nouns = ["puppy"] * 20 + ["car"]*20 + ["rabbit"]* 20 + ["girl"]* 20 + ["monkey"]* 20 + ["FinalRank"] + ["FinalRankr"]
verbs = ["runs", "hits", "jumps", "drives", "barfs", "FinalRank"]
adv = ["crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", "FinalRank."]
adj = ["adorable", "clueless", "dirty", "odd", "stupid", "FinalRank"]

l = [nouns, verbs, adj, adv]

for i in range(random.randint(1,20)):
	print ' '.join([random.choice(i) for i in l])

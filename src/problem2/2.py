# -*- coding: utf-8 -*-
import codecs
fi = codecs.open("2.in", encoding="utf-8")
fo = codecs.open("2.out", encoding="utf-8", mode="w")

# C = Ch, Tr;
# K = C, Q; 
# D = Đ; 
# G = Gh;
# F = Ph; 
# Q = Ng, Ngh; 
# X = Kh; 
# W = Th; 
# Z = d, r;
# Nh = n';

arr = [
	["nh", "n'"],
	["kh", "x"],
	["th", "w"],
	["ph", "f"],
	["gh", "g"],
	["d", "z"],
	[u"đ", "d"],
	["r", "z"],
	["q", "k"],
	["ngh", "q"],
	["ng", "q"],
	["c", "k"],
	["kh", "c"],
	["tz", "c"],
]
for line in fi:
	for a in arr:
		line = line.replace(a[0], a[1])
	fo.write(line)
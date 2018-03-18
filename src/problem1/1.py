def rmSpace(str):
	while(str.find("  ") != -1):
		str = str.replace("  ", " ");
	str = str.strip()
	return str


fi = open("1.in", "r")
fo = open("1.out", "w")
for line in fi:
   res = rmSpace(line)
   print res
   fo.write(res)
   fo.write("\n")

fi.close()
fo.close()

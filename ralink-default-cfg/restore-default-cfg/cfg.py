#

f = file("cfg-bin", "rb")
r = file("cfg-bin-fixed", "wb")

f.seek(256*1024)
#f.seek(0)
data = f.read(256*1024)
r.write(data)
r.write(data)

f.close()
r.close()

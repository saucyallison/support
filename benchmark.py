import time
import gzip

bench1 = time.time()
destpath = "wires_extracted"
filename = "/Users/allison/Downloads/wires-0.6.2-OSX.gz"
with gzip.open(filename,"rb") as zipfile:
    with open(destpath,"wb") as destfile:
        content = zipfile.read()
        destfile.write(content)
bench2 = time.time()
print "benchmark: %s ms" % ((bench2-bench1)*1000)
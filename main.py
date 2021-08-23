import subprocess

results = subprocess_output (["netsh", "wlan", "show", "network"])
results = results.replace("\r", "")

ls = results.split ("\n")
ls = ls[4:]

ssids = []
x = 0
y = 0

while x < len(ls):
        if x % 5 == 0 :
             ssids.append(ls[x])
        x += 1

while y < len (ssids):
        print ssids[y] 

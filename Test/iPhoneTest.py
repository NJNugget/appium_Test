# -*- coding: UTF-8 -*-

'''
Created on 2015年8月11日

@author: NJNUGGET
'''

import pylab
x = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [4.29, 3.83, 2.28, 1.44, 3.22, 2.30, 4.29, 3.83, 2.28, 1.44, 3.22, 2.30, 4.29, 3.83, 2.28, 1.44, 3.22, 2.30, 4.29, 3.83, 2.28, 1.44, 3.22]
pylab.plot(x, y)
pylab.xlabel('Isoelectric point')
pylab.ylabel('Normalized percent of regions')
pylab.title('Protein charge of amino acid windows')
figure = pylab.savefig("test.png")

import os,sys

html = open('index.html', 'w')
html.write("""
<html>
<head>
  <title>Test</title>
  <style>img{float:left;margin:5px;}</style>
</head>
<body>
""")

files = os.listdir('.')
for f in files:
    if f.lower().endswith('.jpg') or f.lower().endswith('.png'):
        html.write("<img src='%s' />" % f)

html.write('</body></html>')
html.close()

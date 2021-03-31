# Speed tests

import os
import datetime

baselength = 1000000
iterations = 1
benchIterations = iterations
maxSamples = 50
sampleAttenuationRate = 50
sampleAttenuationBase = 50
sampleRate = 0.5

cwd = os.getcwd()
print(cwd)

with open('log-sa-' + str(sampleAttenuationRate) + '-sb-' + str(sampleAttenuationBase) + '-sc-' + str(sampleRate) + '-m-' + str(maxSamples) + '-length-' + str(baselength) + '.txt', 'w') as f:
   f.write('length\tcorrupt\titeration\tseconds\n')
   # run the benchmark
   for j in range(benchIterations):
      print('benchmark XSLT')
      tstart = datetime.datetime.now()
      os.system(r'java -cp "e:\saxon9.9\saxon9he.jar" net.sf.saxon.Transform -s:"..\benchmark-zero.xsl" -xsl:"..\benchmark-zero.xsl" -o:zero.xml')
      tend = datetime.datetime.now()
      tdiff = tend - tstart
      f.write('xslt\t0\t' + str(j) + '\t' + str(tdiff.total_seconds()) + '\n')
      print('Operation time (seconds): ' + str(tdiff.total_seconds()))
	  
   for j in range(benchIterations):
      print('benchmark TAN diff')
      tstart = datetime.datetime.now()
      os.system(r'java -cp "e:\saxon9.9\saxon9he.jar" net.sf.saxon.Transform -s:"..\benchmark-zero-tan.xsl" -xsl:"..\benchmark-zero-tan.xsl" -o:zero-tan.xml')
      tend = datetime.datetime.now()
      tdiff = tend - tstart
      f.write('tan\t0\t' + str(j) + '\t' + str(tdiff.total_seconds()) + '\n')
      print('Operation time (seconds): ' + str(tdiff.total_seconds()))
	  
   for i in range(101):
      print(str(i))
      for j in range(iterations):
         tstart = datetime.datetime.now()

         os.system(r'java -cp "e:\saxon9.9\saxon9he.jar" net.sf.saxon.Transform -s:"..\benchmark.xsl" -xsl:"..\benchmark.xsl" -o:diff-length-' + str(baselength) + '-corrupt-' + str(i) + r'.xml -xmlversion:1.1 corrupt-n=' + str(i) + ' controlled-length=' + str(baselength) + r' {tag:textalign.net,2015:ns}diff-sample-size-attenuation-rate=0.' + str(sampleAttenuationRate) + r' {tag:textalign.net,2015:ns}diff-sample-size-attenuation-base=0.' + str(sampleAttenuationBase) + r' {tag:textalign.net,2015:ns}diff-horizontal-pass-frequency-rate=' + str(sampleRate) + r' {tag:textalign.net,2015:ns}diff-maximum-number-of-horizontal-passes=' + str(maxSamples))

         tend = datetime.datetime.now()
         tdiff = tend - tstart
         f.write(str(baselength) + '\t' + str(i) + '\t' + str(j) + '\t' + str(tdiff.total_seconds()) + '\n')
         print('Operation time (seconds): ' + str(tdiff.total_seconds()))

"Ben Identifier"

This is a low level, extremely fast, neural network implementation of an object detector.
It is currently trained to identify if 'Ben' our mascot is in a live image feed, outputting 'ben' or 'notben'
This program does not run of popular backends like tensflow or pytorch and has all backend maths in the helper.py file.
With only 80 focus (ben) and 20 empty (notben) images, this network achieves > 90% accuracy on detecting ben.

The network can easily be trained to detect other images, included scripts for formatting data are included in the repo.

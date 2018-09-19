## **"Ben Identifier"**

This is a low level, extremely fast, neural network implementation of an object detector.
It is currently trained to identify if 'Ben' our mascot is in a live image feed, outputting 'ben' or 'notben'
This program does not run of popular backends like tensflow or pytorch and has all backend maths in the helper.py file.
With only 80 focus (ben) and 20 empty (notben) images, this network achieves > 90% accuracy on detecting ben.
(Network will almost never predict an image to contain ben if he is not present but will sometimes predict not ben when he is present)

The network can easily be trained to detect other images, included scripts for formatting data are included in the repo.

~~

The network takes 64x64 rgb images
All processing is done on a CPU, most systems can run this network at > 30 fps, most bottlenecking would occur withing open cv mothods.

Ben image example:

![Alt text](dataBen/TestImageRes/00.png?raw=true "Ben")

NotBen image example:

![Alt text](dataBen/TestImageRes/10.png?raw=true "NotBen")

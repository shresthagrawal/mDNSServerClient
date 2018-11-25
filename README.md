In this project I have tried to demonstrate the mDNS/DNS-SD using python zeroconf library and avahi server. For this demonstration the server currently generates random number once the upperbound is sent through client. The client is capable of handling multiple services/servers and the server is multi threaded. 

Project Repo: https://github.com/shresthagrawal/mDNSServerClient.git

After reading about the concept of multicast DNS system, I was really fascinated about the ways it could be implemented on several devices. Hence I wasn't able to stop myselves in implementing it in one of my GCI tasks (Database and Motion) where I used the concept of zeroconf for an IOT device which stores timeStamp once the motion is detected. This device uses mDNS and Lifi technology to configure everything- zero configuration.

I would really be thankfull if you could once also see that project to:
https://github.com/shresthagrawal/Working-with-DATABASE-and-MOTION
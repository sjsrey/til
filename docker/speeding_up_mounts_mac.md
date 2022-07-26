# Speeding up Docker on Mac M1 When using mounts

Running docker on the m1 is definitely not the same as running docker on a linux host.

One of the pain points involves running containers with mounts to the host on an M1. 
The pain comes in the form of slowness.

One way to reduce this pain is to toggle on the experimental feature `VirtioFS` which is under the docker preferences:


![Screen Shot 2022-07-26 at 10 48 44 AM](https://user-images.githubusercontent.com/118042/181076145-4995f295-b8bc-4fcf-860a-be11d9b0b622.png)

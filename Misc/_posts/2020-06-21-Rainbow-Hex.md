---
layout: post
title: "Rainbow Hex"
author: "vishalananth"
---

## Question

Have you ever seen this sort of stuff? I haven't seen it in my life. Maybe it's a Rainbow? or a Unicorn's Tail? or a lot of colorful Bees? or a lot of colorful Hues?

## Solution

Opening the zip will give us a video file, which conatins the washing hands video and a file with flashy colors. I saw a few writeups online to learn to solve video forensics and learnt that splitting the video into frames might give us the flag. I used ffmpeg to split the video into frames.

```
ffmpeg -i washing_hands.mp4 image-%07d.png
```
An example frame:
</br></br>![alt text](images/frame001.png)</br></br>

The video is split into nearly 600 frames but unfortunately none of the frames contained the flag or anything related. So it was time to find some other way. 
<br><br>
On reading the question again, I noticed that the word hues was a bit suspicious. Googling more would give us HexaHues, a color based encryption scheme.
<br><br>
I tried to write a script to read all the image files and give me the flag, but since most image files were unclear, it did'nt work. So I manually searced the images to fid the image which corresponded to 'z' and decrypted from that point using https://www.boxentriq.com/code-breaking/hexahue to get the flag.
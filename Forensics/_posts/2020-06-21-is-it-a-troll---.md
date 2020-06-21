---
layout: post
title: "is it a troll???"
author: "vishalananth"
---

## Question

there is baby key and baby hide the key somewhere. Can you help his father to find the key??

## Solution

We are given a JPG file:
</br></br>![alt text](images/Trollface.jpeg)</br></br>

First, I tried inspecting the file with stegsolve.jar and got nothing useful. Running exiftool:

```
exiftool Trollface.jpeg
```

We observe a suspicious string '**wJNVU1tljMDBTVKm5HekQ8xx**' in the author section. Decoding with base62 we get the password
for the jpeg file as **itrolledyou**. Using Steghide to uncover the hidden data:

```
steghide extract -sf Trollface.jpeg
```

We get a troll.zip, which contains the following image:
</br></br>![alt text](images/troll.png)</br></br>

Running zsteg on the image:

```
steg troll.png
```

We get a suspicious string '**aDutCu4gwUtnqdVuhLUL6jFueSgRFi**' which on decoding with base58 gives us the flag.
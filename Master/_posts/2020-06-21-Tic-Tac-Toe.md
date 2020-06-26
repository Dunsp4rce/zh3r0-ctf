---
layout: post
title: "Tic Tac Toe"
author: "vishalananth"
---

## Question

Can you beat the image?

## Solution

We are given a file named image, without any extension and running the file command on it did not give any information about the file. So I ran
```
xxd image
```
and got the following result:
</br></br>![alt text]({{ site.baseurl }}/images/hex.png)</br></br>

We can see the signature bytes **JFIF** which are the signature bytes of a jpg file. But instead of being the first bytes of the file, it was in the end. So, the given file is a jpg file, but reversed completely.
So I wrote a python script - reversejpg.py to reverse the file byte by byte and constuct the new jpg. After reversing we got the following image:
</br></br>![alt text]({{ site.baseurl }}/images/modified_image.jpg)</br></br>

As we can see here, we got an image with the words **Stego** which clearly indicates something to do with Image Steganography. So I tried opening the tool in stegsolve.jar
to check if there is anything hidden within the image, but nothing useful. Next, I ran exiftool on the image:

```
exiftool modified_image.jpg
```

I got a suspicious encoded text "**aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj01bHNvRkc3bXVQNAo=**" in the comments section. This looked like a base64 encoded string which on decoding gave the 
youtube link https://www.youtube.com/watch?v=5lsoFG7muP4. On opening the link we see the song Kapela - Rock my way, so this was a clue hinting us to bruteforce the image using password file rockyou.txt.
So I ran Stegcracker with rockyou.txt:

```
stegcracker modified_image.jpg rockyou.txt
```

It worked and immediately found the password of the file which was "**spongebob**" and the contents were written to modified_image.jpg.out. It contained the following:

```
In [35]: n,e,ct,p+q
Out[35]: 
(156935655500198733255923805969370297538115753312746380213875723177744608509780722798549730106834861986575848272630355804840179947615966722051370804273521733290376009020885919941338141950993008276537987193794648055241515380150115338397065198086893695560540379329063476893211153270247222670504019722793971516489,
 65537,
102778142076243116117419062640171713879684005471846556860689446479305435562766590357152362175278713093609670819423506015563433111872029023117856369287465874159889936283732420732086482645886112577942492103417960605158427793203017078930148395937563028135853490687072326149444788825363901282252753328289332801180,
25089219254058723086004960979954103479984362695038160907003438818016936688465630366701002710571334149929206994096775851785636272938202242921638312612784566)
```

We can clearly see the parameters were for RSA and the ciphertext(ct) was given to us. So I wrote a script: rsasolve.py to find phi using n and p+q and hence find the private key 'd' to decrypt the ciphertext which gave out the flag.
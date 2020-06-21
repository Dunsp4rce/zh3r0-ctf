---
layout: post
title: "Flag 6: Parallel Ninja"
author: "shreyas-sriram"
---

# Category
Web

# Challenge
## Flag 6 - Parallel Ninja
We are given a URL - ``` hackit.zh3r0.ml ```
Hint : Something to do with a secure website and Greek demi-gods

# Solution

> Optional: Find IP address of the given domain using **ping**

Since it is a machine, begin with a full port scan

``` nmap -T4 -sC -sV -p- hackit.zh3r0.ml ```

> Note: Not sure if I used the right [options], run ``` nmap --help ``` for better understanding and optimisation

This reveals all the open ports and services running on each port. Also notice that the services running are all mixed up.

```
22/tcp    open     http
25/tcp    filtered smtp
99/tcp    open     ssh
324/tcp   open     ftp
4994/tcp  open     unknown
11211/tcp filtered memcache
```

* Since ``` http ``` is running on port ``` 22 ```, it will be restricted by the browser and we will not be able to access it directly. There are two ways around this problem.
	1. Allow restricted ports in Firefox Browser
		* Go to ``` about:config ``` in Firefox address bar
		* Add the string name and value as ```   (network.security.ports.banned.override, 22) ```
		* Access ``` http://hackit.zh3r0.ml:22/robots.txt ```
	2. Access the webpage through cURL or wget
	``` curl http://hackit.zh3r0.ml:22/robots.txt ```
	``` wget http://hackit.zh3r0.ml:22/robots.txt ```
* There is a clue which has something to do with **ads**. There are two ways to go about this.
	1. Make a guess to visit ``` http://hackit.zh3r0.ml:22/ads.txt ```
		* Obtain a string encoded in ``` Base 62 ``` (Damn, these aren't the bases I am aware of :tired_face:)
		* Use https://gchq.github.io/CyberChef/ to decode and get another webpage ``` /index2.html ```
		* This page contains a login
		* Bypass this login using simple **SQL injection**, any one of the payloads can be used
		``` Payload : ' OR 1=1 OR '```
		``` Payload : 'OR '1'=1 ```
		* After successful login, inspect page to find another encrypted string
		* Getting a hint from the challenge clue (Greek demi-gods), decode the cipher text using **Pollux Cipher**, use https://www.dcode.fr/pollux-cipher
		* Obtain **Flag 6**
		``` Flag 6: zh3r0{wasnt_this_awesomeee} ```
	2. Use directory busting tools on ``` http://hackit.zh3r0.ml:22/ ```
		* ``` gobuster dir -u http://hackit.zh3r0.ml:22/ -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -t 50 -x php,txt,html,htm ```
		* ``` dirbuster ``` - GUI tool
		* This also reveals ``` /index2.html ``` without getting to ``` ads.txt ```
		* Proceed as described above to get **Flag6**
		``` Flag 6: zh3r0{wasnt_this_awesomeee} ```

Title: the blog went down... oh no!
Date: 2025-04-08
Modified: 2025-04-14
Category: sisyphean didactic auto-flagellator
Tags: meta
Slug: the-blog-went-down-oh-no
Author: aadith thiruvallarai

If you're my weekly 1-3 visitors[^weekly users], you may have noticed the website went down… 
It seems that when you host a website using 
***[DDNS](https://en.wikipedia.org/wiki/Dynamic_DNS){:target="_blank"}*** (dynamic ***[DNS](https://en.wikipedia.org/wiki/Domain_Name_System){:target=”_blank”}***) on your home WiFi, your ISP (internet service provider) may not be a huge fan.

> 
Accessing a website is tantamount to accessing files hosted by or on a computer, often called a server, through the Internet.
The way our computer, often called the client, can talk to the server is through the use of an IP (Internet Protocol) address, the Internet version of a mailing address.
It would be a pain if you had to remember the IP address for every website you want to use on a daily basis.
Thankfully, we don’t have to memorize every website’s IP address because of DNS (domain name system).
DNS allows you to use a human-friendly domain name, or URL, instead of the computer's IP address.
Then, DNS servers will help find the IP address related to the website you’re seeking and provide it to your computer.

Previously, when I had my website’s related files on my ***[Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi){:target=”_blank”}***, I used DDNS with the help of a company ***[No-IP](https://en.wikipedia.org/wiki/No-IP){:target=”_blank”}***​​.
No-IP’s DDNS application would run every 5-10 minutes on my Raspberry Pi telling No-IP’s servers if my external IP address had changed.
If it did change, they would make sure to publish new DNS records saying what IP address my website should point towards.

> 
Every computer in a home network talks to the internet using the home router. 
The home router has an external, or public-facing, IP address used to access websites. 
This IP address can be changed by an ISP without warning. 
In order to utilize DNS, it’s important to know what your IP address is at all times and rely on the fact that it will not change over time. 
This is where DDNS comes into play.

I noticed that the WiFi would intermittently go down on a daily basis – of course there couldn’t possibly be a reason for this…

My best conclusion is that my ISP didn't like No-IP’s application having periodic traffic to confirm my home router's external IP address. Otherwise, it could have been a malicious actor or a bot was actually scanning my network/ports, or some other unforeseeable reason.

## choosing the tech stack

> 
A tech stack is a list of all the technology services used to run a single application or website.

What I was using before I had to shutdown the website:

1. “On-premise” hardware: Raspberry Pi
2. Operating System: ***[Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS){:target=”_blank”}***, based off of ***[Debian](https://en.wikipedia.org/wiki/Debian){:target=”_blank”}*** (a ***[Linux](https://en.wikipedia.org/wiki/Linux){:target=”_blank”}*** distribution)
3. Web Server: ***[nginx](https://nginx.org/en/){:target=”_blank”}***
4. Content Type: some good ol’ HTML and CSS[^basic website]

### to ***[cloud](https://en.wikipedia.org/wiki/Cloud_computing){:target=”_blank”}*** or to self-host, that is the question

After much deliberation and moral indignation at the choices that led me here, I unwillingly chose to switch to using the cloud[^cloud meme]. 
Instead of being cool and hosting a website on a goddamn Raspberry Pi, I'm now hosting the website in ***[GCP](https://en.wikipedia.org/wiki/Google_Cloud_Platform){:target=”_blank”}*** (the Google Cloud Platform). 
I was really proud of myself for getting hardware I could touch and feel to host a website readily accessible from the Internet. 
But, in order to mitigate the ISP issues from occurring, I had no choice but to host the website remotely. 
It’s not like I have another network laying around so the next best thing is to use the cloud. 

### the software’s hardware

I left a lot of the hardware set up details out in my previous blog post simply because I felt like it would be a blog post of its own. 
Setting up the Raspberry Pi, to put it succinctly, involved putting some of the hardware together, downloading the appropriate 
***[image](https://en.wikipedia.org/wiki/System_image){:target="_blank"}***, and then 
***[hardening](https://en.wikipedia.org/wiki/Hardening_(computing)){:target=”_blank”}*** the OS, operating system. 
I must admit, creating ***[VMs](https://en.wikipedia.org/wiki/Virtual_machine){:target=”_blank”}***, (virtual machines) in the cloud is much easier.

> 
A VM is a software-defined computer existing only in code. 
Most likely the machine, or computer, that you and I are using everyday is physically, or hardware-, defined.
A VM, much like a hardware-defined machine, has a CPU, RAM, storage, and can even connect to the internet.

In the GCP console, I created a project to hold all of my resources related to running this website, attached a billing account (gave my credit card info yippee), specified my hardware/network requirements for the VM, and then created it with a simple tap of a button. 


> 
The VM, itself, is an "e2 standard" instance which means it uses ***[Intel Core Broadwell processors](https://en.wikipedia.org/wiki/Broadwell_(microarchitecture)){:target=”_blank”}***. 
The VM’s hardware specs include two ***[vCPUs](https://www.techtarget.com/whatis/definition/virtual-CPU-vCPU){:target=”_blank”}*** ( virtual CPUs), 16 GB of RAM, and 128[^storage overkill] GB of storage.

### the OS

The old tech stack used RPO, Raspberry Pi OS. 
RPO, if you couldn’t tell from the name, was made for the Raspberry Pi because it needed something more suitable for a single-board computer. 
Asides from that, I wanted to familiarize myself with a Linux flavor I hadn’t used before.

On the flip side, working in the cloud gives me flexibility on what OS I can choose to use. 
I’m pretty familiar with using ***[Ubuntu](https://en.wikipedia.org/wiki/Ubuntu){:target=”_blank”}***, a Linux distribution, from messing around with VMs on my personal machine and class assignments.
I wanted to quickly get the website back and running, so I just went with what I was most familiar with!

### the web restaurant

I used nginx as an HTTP web server to serve the static content I generated using ***[Pelican](https://getpelican.com/#quickstart){:target=”_blank”}***, a static site generator. 
nginx is an incredibly useful tool that removes the need to create an HTTP web server from scratch[^future project].

### the arcane magic of DNS, or how did i set up my URL

With my new set-up, I didn’t have to worry about DDNS because there was no Internet traffic going through my home router. 
In the GCP console, I configured my external IP address to be static. 
Then, I obtained a lease to the domain `aadith-thiruvallarai.com` from ***[Squarespace](https://www.squarespace.com/){:target=”_blank”}***.

> 
You can’t actually own a URL. 
You can only lease it from companies like GoDaddy and Squarespace.

Then, I created two custom records: an A record with the hostname `@` pointing to my VM’s external IP address and a CNAME record with the hostname `www.aadith-thiruvallarai.com` pointing to `aadith-thiruvallarai.com`

### the final choices

So, here’s the new and improved stack:

1. Cloud Infrastructure: GCP
2. Operating System: Ubuntu
3. Web Server: nginx
4. Content type: some good ol’ HTML/CSS[^basic website]

## updates

### April 14th, 2025

- Accidentally published the blog post early because I wanted to test the DNS settings with a new blog post
- Completed the blog post

[^weekly users]: 
Yeah, I'm proud to admit that I have at least 1 weekly visitor! 
On a more serious note, I didn't figure out how to track how many people were visiting the site. My numbers are solely based on the friends I shared the website with... yeah that's right I have 1-3 friends, at least!

[^basic website]: 
I’m sorry for not using the new React framework of the day :( … 
I’m not actually sorry :p. 
I just wanted to keep it simple, stupid, and short!
If you’re reading this a second time… I still stand by what I said :p!

[^cloud meme]: 
I’m envisioning the ***[“Old Man Yells at Cloud”](https://knowyourmeme.com/memes/old-man-yells-at-cloud){target=”_blank”}*** meme.

[^storage overkill]: 
For what I need this VM to do, this amount of storage is definitely overkill.

[^future project]: 
Maybe I should make an HTTP web server in C, C++, or Rust? 
I don’t know, shoot me an email if you’d like to see me do this and blog about it!

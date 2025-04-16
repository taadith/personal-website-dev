Title: the blog went down... oh no!
Date: 2025-04-08
Modified: 2025-04-16
Category: sisyphean didactic auto-flagellator
Tags: meta
Slug: the-blog-went-down-oh-no
Author: aadith thiruvallarai

If you're my weekly visitor[^weekly users], you may have noticed the website went down for a few weeks… 
When hosting a website using 
***[DDNS](https://en.wikipedia.org/wiki/Dynamic_DNS){:target="_blank"}*** (dynamic ***[DNS](https://en.wikipedia.org/wiki/Domain_Name_System){:target=”_blank”}***) on your home WiFi, your ISP (internet service provider) may not be a huge fan.

<hr style = “height:100px;color:cornflowerblue;”>
<hr style = “height:100px;color:cornflowerblue;”>

### an aside on DNS[^big block quotes]: 
Accessing a website is tantamount to accessing files hosted by or on a computer, often called a server, through the Internet.
The way our computer, often called the client, can talk to the server is through the use of an IP (Internet Protocol) address, the Internet version of a mailing address.
However, it would be a pain if you had to remember every website’s IP address you want to use on a daily basis. 

The solution comes in the form of ***[DNS (Domain Name System)](https://en.wikipedia.org/wiki/Domain_Name_System){:target=”_blank”}***.
DNS allows you to use a human-friendly domain name, or URL, instead of the computer's IP address.
DNS servers store DNS records which include the associated IP addresses for domains.

> 
“DNS records are sets of instructions that live on DNS servers. 
These instructions are vital to the success of a DNS lookup.” 
- Cloudflare

Web browsers communicate with DNS servers, through what is called a DNS lookup, whenever you look up a URL to find the website’s associated IP address.

<hr style = “height:100px;color:cornflowerblue;”>
<hr style = “height:100px;color:cornflowerblue;”>

Previously, when I had my website’s related files on my ***[Raspberry Pi](https://en.wikipedia.org/wiki/Raspberry_Pi){:target=”_blank”}***, I used DDNS through the company ***[No-IP](https://en.wikipedia.org/wiki/No-IP){:target=”_blank”}***​​. 
No-IP provides domains, free of charge, and a DDNS application for the machine hosting the website’s server.
I configured No-IP’s DDNS application to run every five to ten minutes on the Raspberry Pi  to communicate changes in my public IP address to No-IP’s DNS servers.
If it did change, they would make sure to publish new DNS records saying what IP address my website should point towards.

<hr style = “height:100px;color:cornflowerblue;”>
<hr style = “height:100px;color:cornflowerblue;”>

### an aside on DDNS:
Every computer in a home network talks to the internet using the home router. 
The home router has an external, or public-facing, IP address used to access the Internet. 
This IP address can be changed by an ISP without warning. 
In order to utilize DNS, it’s important to know what your IP address is at all times and rely on the fact that it will not change over time. 
This is where DDNS comes into play.
DDNS allows for a changing public IP address (that’s why it’s called dynamic DNS).

<hr style = “height:100px;color:cornflowerblue;”>
<hr style = “height:100px;color:cornflowerblue;”>

I noticed that the WiFi would intermittently go down on a daily basis – of course there couldn’t possibly be a reason for this…

My best conclusion is that my ISP didn't like the fact that I was hosting a website on the network with many visitors (at least one a week). 
Alternatively, the issue could be with No-IP’s application having periodic traffic to confirm my home router's external IP address. 
Otherwise, it could have been a malicious actor or a bot was actually scanning my network/ports.

## choosing the right tech stack

> 
A tech stack is a list of all the technology services used to run a single application or website.

What I was using before I had to shutdown the website:

1. “On-premise” hardware: Raspberry Pi
2. Operating System: ***[Raspberry Pi OS](https://en.wikipedia.org/wiki/Raspberry_Pi_OS){:target=”_blank”}***, based on ***[Debian](https://en.wikipedia.org/wiki/Debian){:target=”_blank”}*** (a ***[Linux](https://en.wikipedia.org/wiki/Linux){:target=”_blank”}*** distribution)
3. [Web Server](https://en.wikipedia.org/wiki/Web_server){:target=”_blank”}: ***[nginx](https://nginx.org/en/){:target=”_blank”}***
4. Content Type: some good ol’ HTML and CSS[^basic website]

> 
A web server distributes web content that has been requested.

### to ***[cloud](https://en.wikipedia.org/wiki/Cloud_computing){:target=”_blank”}*** or to self-host, that is the question

After much deliberation and moral indignation at the choices that led me here, I unwillingly chose to switch to using the cloud[^cloud meme]. 
Instead of being cool and hosting a website on a Raspberry Pi – really cool to me if you were asking – I'm now hosting the website on ***[GCP](https://en.wikipedia.org/wiki/Google_Cloud_Platform){:target=”_blank”}*** (the Google Cloud Platform). 
I was really proud of myself for getting hardware I could touch and feel to host a website readily accessible from the Internet. 
But, in order to prevent the ISP attack messages and WiFi issues, I had no choice but to host the website remotely. 
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
Besides that, I wanted to familiarize myself with a Linux flavor I hadn’t used before.

On the flip side, working in the cloud gives me flexibility on what OS I can choose to use. 
I’m pretty familiar with using ***[Ubuntu](https://en.wikipedia.org/wiki/Ubuntu){:target=”_blank”}***, a Linux distribution, from messing around with VMs on my personal machine and class assignments during my undergrad.
I wanted to get the website up and running again, so I just went with what I was most familiar with!

### the web restaurant

I chose nginx as my web server because it is known to outperform other popular web server implementations in benchmark tests, especially when it comes to serving static content.

> 
Static content (or web pages) is delivered to a web browser exactly as stored. 
The web browser then converts the content to the web page for you to view. 
In contrast, dynamic content is generated by a web application which is then processed by the web browser.

nginx is an incredibly useful tool that removes the need to create an [HTTP (Hypertext Transfer Protocol)](https://en.wikipedia.org/wiki/HTTP){:target=”_blank”} web server from scratch[^future project]. 

> 
HTTP is the protocol, specification/method, by which information is communicated over the World Wide Web.

Thankfully, there was no need to make [HTML (Hypertext Markup Language)](https://en.wikipedia.org/wiki/HTML){:target=”_blank”} and [CSS (Cascading Style Sheets)](https://en.wikipedia.org/wiki/CSS){:target=”_blank”} files from scratch.

> 
HTML is a markup language used to create the basic structure and text for each web page in a website. 
CSS is a style sheet language used for the styling and making the webpage/website visually appealing. 
[JavaScript](https://en.wikipedia.org/wiki/JavaScript){:target=”_blank”} is a programming language used for any logic that needs to be handled.

I used ***[Pelican](https://getpelican.com/#quickstart){:target=”_blank”}***, a static site generator, to convert [Markdown](https://en.wikipedia.org/wiki/Markdown){:target=”_blank”}, essentially plaintext, files to HTML and CSS files.

### the arcane magic of DNS, or how did i set up my URL

With my new set-up, I didn’t have to worry about DDNS because there was no Internet traffic going through my home router. 
In the GCP console, I configured my external IP address to be static. 
Then, I obtained a lease to the domain `aadith-thiruvallarai.com` from ***[Squarespace](https://www.squarespace.com/){:target=”_blank”}***.

> 
You can’t actually own a URL. 
You can only lease it from companies like GoDaddy and Squarespace.

Configuring DNS involves creating and publishing what is known as DNS records.

DNS records come in many flavors but the only one I had to be concerned with was an A record.
An A record points the URL to the website’s server’s IP address.

<figure>
  <img src="/images/blog/2025/april/the-blog-went-down-oh-no/custom-records.png" alt="Squarespace Custom Records" width="600">
  <figcaption style="text-align:center;">Squarespace Custom Records</figcaption>
</figure>

In Squarespace, I created an A record with the hostname (data field) set as `@`, shorthand for the domain `aadith-thiruvallarai.com`, pointing to my VM’s public IP address.

### the final choices

So, here’s the new and improved stack:

1. Cloud Infrastructure: GCP
2. Operating System: Ubuntu
3. Web Server: nginx
4. Content type: some good ol’ HTML/CSS[^basic website]

## updates

### April 16th, 2025
- Changed some verbiage for clarity
- Made long block quotes into “asides”

### April 15th, 2025

- Accidentally published the blog post early because I wanted to test the DNS settings with a new blog post
- Completed the blog post

[^weekly users]: 
Yeah, I'm proud to admit that I have at least one weekly visitor! 
On a more serious note, I didn't figure out how to track how many people were visiting the site. My numbers are solely based on the friends I shared the website with... yeah that's right I have one friend, at least!

[^big block quotes]: 
I felt like some of my block quotes were getting too big. I hope you like this style of inserting “asides” when some critical, yet verbose, information needs to be communicated.

[^basic website]: 
I’m sorry for not using the new React framework of the day `:(` … 
I’m not actually sorry `:p`. 
I just wanted to keep it simple, stupid, and short!
If you’re reading this a second time… I still stand by what I said `:p`

[^cloud meme]: 
I’m envisioning the ***[“Old Man Yells at Cloud”](https://knowyourmeme.com/memes/old-man-yells-at-cloud){:target=”_blank”}*** meme.

[^storage overkill]: 
For what I need this VM to do, this amount of storage is definitely overkill.

[^future project]: 
Maybe I should make an HTTP web server in C, C++, or Rust? 
I don’t know, shoot me an email if you’d like to see me do this and blog about it!

---
title: 'Fixing Unstable WiFi Connection in Windows 8'
date: 2014-04-22T02:02:06+01:00
author: Arturo
layout: post
permalink: /fixing-unstable-wifi-connection-in-windows-8/
categories:
  - Windows 8
  - Troubleshooting
tags:
  - internet
  - internet connection
  - wifi
  - windows
---
<figure class="alignleft">
	<img width="32" src="../multimedia/icons/windows8.png"/>
</figure>

I just upgraded my old laptop to a new one with Windows 8.1 installed. Putting aside the small details of getting used to a new operating system (OS), I found something that was terribly annoying

<!--more-->

Apparently, there is an awful issue with Windows 8.1 management of the wireless adapter. This translates into an unstable, limited WiFi connection. I immediately jumped into the internet, trying to find a solution. Surprisingly, this was a very common issue. Nevertheless, it took me quite a few tries to finally fix it. If you find yourself in the same situation, I recommend you to try the following options (in this order):

## 1. Update Windows 8.1.

When you get a computer brand new, it comes with the factory version of your OS. From the moment your computer left the factory until you turned it on, the manufacturer probably released a few important updates for it. The OS might try to download them eventually, but you might need them now, like in this case. To do so:

  1. Go to **Control Panel (select &#8220;View by large/small icons) &#8220;→ Windows Update**
  2. Select **Check for updates**. Then download and install all the updates found. This might be tricky, since the internet connection is unstable you will probably have to manually try to download the updates a couple of times. You could also try to connect to the internet meanwhile using a wired connection.
  3. Anyway, you will need to restart your system after this.


## 2.1 Change your WiFi adapter power settings.

Apparently, people thought it would be a good idea to turn off your WiFi adapter to save power&#8230; We want internet all the time. To change this:

  1. Go to **Control Panel (select &#8220;View by large/small icons) &#8220;→ Network and Sharing Center → Change adapter settings**
  2. There, right-click your WiFi connection and go to **Properties**.
  3. Go to the **Networking** tab. There, go to **Configure**.
  4. Go to the **Power Management** tab and be sure that the **Allow the computer to turn of this device to save power** option is unchecked.
  5. Click **OK** to save the changes.

## 2.2 Change your Power Plan settings.

This goes hand by hand with the last one.

  1. Go to **Control Panel (select &#8220;View by large/small icons) &#8220;→ Power Options**
  2. Choose your selected power plan (usually Balanced) and click on **Change plan settings**.
  3. Go to **Change advanced power settings**.
  4. There, go to **Wireless Adapter Settings** and then to **Power Saving Mode**. Make sure that in both cases, **On battery** and **Plugged in** are defined as **Maximum Performance**.
  5. Click **OK** to save the changes.

## 3. Reset your Winsock entries & TCP/IP stack.

<p style="color: #2a2a2a;">
  <span style="font-weight: inherit; font-style: inherit;">Winsock entries tells your OS how to access your network (i.e. internet) services. Additionally, your TCP/IP stacks can get corrupted. In order to reset both:</span>
</p>

  1. Open a **Command Prompt** with admin rights.
  2. Type the following commands to reset your Winsock catalog and your TCP/IP stacks, respectively:  
    `netsh winsock reset catalog`  
    `netsh int ip reset reset.log hit`
  3. Restart your system.

## 4. Update (change) your WiFi driver.

Sometimes you need to update (change) your WiFi driver. To do so:

  1. Go to **Control Panel (select "View by large/small icons)" → Device Manager**
  2. There, go to **Network Adapters** and double click your WiFi adapter.
  3. Go to the **Driver** tab and select **Update driver**.
  4. Select **Browse my computer for driver software**.
  5. Select **Let me pick from a list of device drivers on my computer**.
  6. Make sure the **Show compatible hardware** option is checked. You will see a list of different drivers you can update (change to). Select one, click **Next** and finish the process. You might want to try with all the different options until you find one that works.

## 5. Change your DNS settings.

If none of the previous options worked for you, this is your Hail Mary (at least it was for me). Again, I am no internet expert and have no experience with DNS or similar. Therefore, I don&#8217;t know what other consequences could changing this setting do (if you do, please share it in the comments). However, it allowed me to finally have stable WiFi on my laptop, which is good enough for me.

You will be changing your DNS to Google Public DNS. To do so:

  1. Go to **Control Panel (select "View by large/small icons)" → Network and Sharing Center → Change adapter settings**
  2. There, right-click your WiFi connection and go to **Properties**.
  3. Go to the **Networking** tab. There, scroll down, select **Internet Protocol Version 4 (TCP/IPv4)** and click on **Properties**.
  4. Click on **Advanced** and go to the tab **DNS**. If there is an existing IP address listed, write it down for future reference (you never know) and remove it. Then, add the following:  
    `8.8.8.8`  
    `8.8.4.4`  
    Be sure that they are shown in that order (first `8.8.8.8`, then `8.8.4.4`). You can do that using the arrows at the right.
  5. Click **OK**. On the open window, you should see the option **Use the following DNS server addresses** checked. You should also see **Preferred DNS server** with `8.8.8.8` and **Alternate DNS server** with `8.8.4.4`. Click **OK** again to save the changes.
  6. Restart your system.


I hope at least one of these works for you. Do you have any other solution you might want to share? Drop it in the comments below.

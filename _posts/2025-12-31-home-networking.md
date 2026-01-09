---
layout: post
title:  "Fun with home networking"
date:   2025-12-31 00:00:00 +0000
tags: []
---

Two short months after moving into my new (old) house, I now have a basic home networking & smart home setup in place.

This post documents my current setup, with some thoughts on how the process has gone and plans for the future.

My networking skills are firmly "DIY" - that is, I know much more than most people, and much less than any networking professional. My experience mostly comes from server & devops admin work now long in the past, plus scraps of knowledge remembered from school.

My goals, roughly prioritised:

- "Seamless" high-speed internet across the house (ca. 200 square meters, with plenty of brick & concrete separating floors & sections).
- Climate sensors in every room, with live status as a top priority and data gathering & potential for analysis as a close second.
- Ability to segregate 'smart' devices away from the main networ, like the TV, washer, dryer, etc.
- Additional sensors like doors & windows and leak detectors, mostly to supplement the data from the climate sensors.
- Ability to check the status of my sensors when away from home.
- Get to a technical baseline that is maintainable and extensible enough to serve us for years to come.

I spent about two weeks getting this initial baseline in place, mostly in the small pockets of time one has as a quick initial baseline, as I had a couple waves of family visiting, followed by a long holiday travel period where I wanted the ability to monitor the state of the house from afar.

## Smart devices

The first step I took was to go out and buy *all the sensors*, filling up a shopping cart in Ikea with 65 different sensors from their new Matter-

## Network devices

### Router

Unifi Dream Router 7

The most impactful change I made was to replace my 'old' [Asus Router](https://www.asus.com/dk/networking-iot-servers/wifi-routers/asus-wifi-routers/rt-ax59u/) with my first piece of Unifi equipment - a Dream Router 7.

 the example topography matched exactly with what I envisioned for my network (sans Home Assistant and the mesh under it):
![Network topography example for a router](/static/img/posts/unifi-page-topography.png)

The first 

### Access Point

The router sits in a central position in the basement in the corner of the laundry room, where the electrical panel and ISP box are located. Upstairs, at either end of the house, the Wifi signal from the router is weak enough to be considered a dead zone. The Dream Router 7 isn't pitched as a beefy transmitter, and it isn't! 

## Topography

## Smart devices

## Home Assistant

The easiest part of the entire solution was getting Home Assistant up on my Raspberry Pi 5.

I purchased a decent SD card, flashed it with the Home Assistant OS, hooked it up to my router via an ethernet cable, and it all worked immediately.

Setup was also a breeze. After a few weeks of intense use, I can see some of the cracks in the UI/UX, but anything I don't have in place is mostly a function of lack of time, and not lack of ability or power in the platform itself.

## Protections

## VPN

## Next steps

### Security & segregated network

I want to to a security review of my network as currently configured. I'm not sure exactly how to proceed with this, besides reading articles and watching videos, and going over things like the firewall rules. Unifi has made this so easy, that I feel like something *must* be missing!

Once I'm comfortable with my network configuration, I want to add my cloud-connecting 'smart' devices to the segregated zone of the network. My washer, dryer, television, wireless speaker, and in-floor heating control panel are all waiting (some rather impatiently) to be added to the network.

### Outdoor networking & PoE

The network functions 

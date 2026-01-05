---
layout: post
title:  "Fun with home networking"
date:   2025-12-31 00:00:00 +0000
tags: []
---

Two short months after moving into a new (old) house, I finally managed to find the time to put together a useful home networking & smart home solution.

Before I could start shelling out for new equipment, I had time to think up the following goals, roughly in order:

- Reliable, high-speed internet across the house (ca. 200 square meters, with plenty of brick & concrete separating floors & sections).
- Temperature & humidity sensors in every room, so I can see the immediate status but also to gather & analyse data.
- Ability to segregate 'smart' internet-reliant devices on a secured VLAN, like the TV, washer, dryer, etc.
- Additional sensors like doors & windows and leak detectors, so I can have a (thin) layer of security
- Ability to check the status of my sensors when away from home
- Have fun & learn while building a maintainable, extensible platform that can serve us for years to come.

## Network devices

### Router

Unifi Dream Router 7

My first step was to replace my 'old' [Asus Router](https://www.asus.com/dk/networking-iot-servers/wifi-routers/asus-wifi-routers/rt-ax59u/) with my first piece of Unifi equipment - a Dream Router 7.

I went with the DR7 because it 
Also, on the product page, the example topography matched exactly with what I envisioned for my network (sans Home Assistant and the mesh under it):
![Network topography example for a router](/static/img/posts/unifi-page-topography.png)

The first 

### Access Point

The router sits in a central position in the basement in the corner of the laundry room, where the electrical panel and ISP box are located. Upstairs, at either end of the house, the Wifi signal from the router is weak enough to be considered a dead zone. The Dream Router 7 isn't pitched as a beefy transmitter, and it isn't! 

## Topography

## Smart devices

## Home Assistant

I took my Raspberry Pi 5, 

## Protections

## VPN

## Next steps

### Security & segregated network

I want to to a security review of my network as currently configured. I'm not sure exactly how to proceed with this, besides reading articles and watching videos, and going over things like the firewall rules. Unifi has made this so easy, that I feel like something *must* be missing!

Once I'm comfortable with my network configuration, I want to add my cloud-connecting 'smart' devices to the segregated zone of the network. My washer, dryer, television, wireless speaker, and in-floor heating control panel are all waiting (some rather impatiently) to be added to the network.

### Outdoor networking & PoE

The network functions 

---
title: "Nyanpad"
github: "https://github.com/SwiftDust/nyanpad"
description: "A Nyan Cat-shaped macropad"
created_at: "2026-08-25"
total_time: "10h 54m"
---

# August 25, 2026
<!-- fabricate:entry 3054 -->

I wanted to get into hardware again, so decided to build a macropad. I have made some very simple PCBs before, but none used a microcontroller yet. So that's what I'm aiming to learn in this project.

If it's possible, my macropad will use translucent keys with a LCD screen below it. There, you will find app icons that you can change using firmware. It will possibly have a rotary encoder.

Today, I followed the tutorial and set up the basic project structure and built a simple PCB. Tomorrow I will brainstorm my project further and get started on the case.

![](https://fabricate.hackclub-assets.com/4aa131b56c786acb478593be953216ee5b658bedd0969d6e13ec96f201e00b4f/image-png/Schermafdruk_20260825_225248.png)

**Total time spent: 43m**

# August 26, 2026
<!-- fabricate:entry 3053 -->

It was time to do some planning. I read the Hackpad website to find out what possibilities there are, then started designing. The end result was quite nice. Now I'll be designing the PCB and schematic to look like this.

![](https://fabricate.hackclub-assets.com/3c7cae19dbe081c193dad8f55e966e32ea6723775524ef88fc223d030bf07cc3/image-jpeg/PXL_20260826_123357969.jpg)

**Total time spent: 17m**

# August 26, 2026 (entry 2)
<!-- fabricate:entry 3052 -->

Now that the design is ready, I worked on making the *actual* schematic. Even though I followed the tutorial earlier, it was far from complete. I even ended up just deleting everything because it was easier.

For the schematic, I mostly stole [this schematic](https://github.com/hackclub/hackpad/tree/clean/extras/orpheuspad) - slightly embarrassed, but y'know - better steal something that works, than design something that doesn't. I obviously added my own changes into it, like a 6-key matrix and two rotary encoders, to stay in the Nyan Cat theme. Also, I needed to research how to wire two rotary encoders because there weren't enough pins to wire them normally. There was a really friendly guy in the Keyboard Atelier Discord server that helped me out. This is one thing I've really come to love about hardware: you don't just ask AI because that doesn't work well. You'll actually have to go out and understand what's happening.

Tomorrow I'll be designing my PCB plus decorating it. Because what's a good PCB without some decoration? ;)

![](https://fabricate.hackclub-assets.com/45c1517dcb1ba14f3c6edd6db7991b9c9bc94d3c1ccf1d49c7a9942458b040a5/image-png/Schermafdruk_20260826_231715.png)

**Total time spent: 1h 27m**

# August 28, 2026
<!-- fabricate:entry 3051 -->

Today I drew the outline of the board. I had to reduce scope a bit, because the maximum board size was 100x100mm. That was *slightly* annoying, but I guess it's fine... I also added all the components

## The changes
I removed the rotary encoders and added four buttons instead of six. I also added some more LEDs, since there was space for them :)

Now onto the routing!

![](https://fabricate.hackclub-assets.com/e3a4d063098f8a8d07c96140e0311069e2266df4d30398c3edf56cd12473f6f2/image-png/image.png)

**Total time spent: 1h 15m**

# August 28, 2026 (entry 2)
<!-- fabricate:entry 3050 -->

It was time for the routing. I first tried an approach where the B.Cu layer was the ground pour. Afterwards while running the DRC, I found out actually the GND and VCC traces should be routed through the front layer for some reason. So what I did was flipping all the traces to the opposite layer of what they were, and put a copper island on F.Cu. But then I had the problem that VCC was blocking from making a proper ground pour... So I needed to remove a bunch of wires and wire everything the normal way.

In the end I added some decoration and.... The PCB is finished! :yay:

![](https://fabricate.hackclub-assets.com/2b1d86f52599ba49654fcc5310ec2d131d5b97c9215ec67e4fcd975bb444aa6a/image-png/Schermafdruk_20260828_154252.png)

**Total time spent: 1h 15m**

# October 26, 2026
<!-- fabricate:entry 3049 -->

Finally I finished the case. It took a lot of time to figure out what was the best way to make the outline, because it was almost impossible to outline correctly. I tried a lot of different methods and now finally got it right. The feeling was really great after quite a lot of incorrect attempts ;)

![](https://fabricate.hackclub-assets.com/03843eef945013932e1b2060058bee302c03a9b87e52f48561550ceafc080d5a/image-png/Schermafdruk_20261026_173623.png)

**Total time spent: 4h 19m**

# October 31, 2026
<!-- fabricate:entry 3048 -->

After consulting with a friend I figured out that I'd been doing it all wrong and needed to export a step file from kicad... anyways, having done that I finally finalised the case. Heck yeah.

![](https://fabricate.hackclub-assets.com/27d18d988c2896e665701e3050f31574aa7237d077f415aabed96c057820e129/image-png/Schermafdruk_20261108_210945.png)

**Total time spent: 1h 38m**

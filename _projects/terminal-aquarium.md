---
layout: project
title: "Terminal Aquarium"
tag: fun
color: cyan
github: https://github.com/kinifi/terminal-aquarium
order: 14
---
A little ASCII fish tank that lives in your terminal. Fish swim back and forth, bubbles rise, and every so often a kraken shows up and ruins everyone's day.

* * *

### Why

I wanted something dumb to stare at while builds were running. `cmatrix` was too serious. This is not serious.

* * *

### How it works

Just a curses loop redrawing a grid of characters every 100ms. Fish are a handful of frames of ascii art flipped depending on direction. Nothing fancy, which is sort of the point.

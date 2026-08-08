---
layout: project
title: "Nerdery People Archive"
tag: web_archiving
color: cyan
---

## Achiving The Nerdery Employee Wall

[View the archived employee wall](/assets/archives/nerdery-people/index.html)

### Why

I found a 2016 snapshot of The Nerdery's "Meet the Nerds" page on the Wayback Machine and wanted a permanent, offline-viewable copy — no dependency on archive.org staying up or the snapshot staying indexed.

### How

I pulled down the page HTML along with its stylesheets, scripts, fonts, and every background image referenced by the site's CSS, then rewrote all the asset paths to point at local copies instead of `web.archive.org`. The result is a fully self-contained static copy: open `index.html` and it renders identically, offline, with no archive.org toolbar or rewrite scripts in the way.

### Employees Missing

Some may notice that their picture is not included. Thats because the Nerdery would remove your photo from the wall if you left the company. The archive I found and put together was the latest archive that I could find from 2016. In the future I'll try to make a more definite timeline of the wall.

### Important Note

One thing that didn't survive: clicking a person in the photo grid. That feature calls a JSON API endpoint per-person, and archive.org's crawler only ever captured those URLs as redirects, not the actual JSON responses — so the interactive detail view was already broken in the original snapshot, not something lost in this process.

### Special Thanks

Archive.org is an amazing service that saved lots of nerdery-people webpages. This would not exist if it wasn't for the great people working there and crawling the internet at this time. 



[View the archived employee wall](/assets/archives/nerdery-people/index.html)

"""Fail if a build would make feed readers re-show old posts.

Compares each built feed against the live one. Readers key items on <guid>, so:
- a live item that should still be in the feed window must keep its guid,
- an item in both feeds must keep its link and pubDate.
New posts and old ones dropping off the end are fine.

Usage: check-feeds.py <site_dir> [base_url]
"""
import email.utils, pathlib, sys, urllib.request, xml.etree.ElementTree as ET

FEEDS = ["feed.xml", "feed-emacs.xml"]
site = pathlib.Path(sys.argv[1])
base = sys.argv[2] if len(sys.argv) > 2 else "https://www.kriscarta.com"


def items(xml):
    return {
        it.findtext("guid"): (
            email.utils.parsedate_to_datetime(it.findtext("pubDate")),
            it.findtext("link"),
            it.findtext("title"),
        )
        for it in ET.fromstring(xml).iter("item")
    }


failed = False
for feed in FEEDS:
    try:
        with urllib.request.urlopen(f"{base}/{feed}", timeout=20) as r:
            live = items(r.read())
    except Exception as e:
        print(f"WARN {feed}: could not fetch live feed ({e}); skipping")
        continue
    built = items((site / feed).read_bytes())
    cutoff = min(d for d, _, _ in built.values())
    print(f"{feed}: live {len(live)} items, built {len(built)} items")
    for guid, (date, link, title) in live.items():
        if guid not in built:
            if date >= cutoff:
                print(f"  FAIL guid gone but still in window: {guid} ({title})")
                failed = True
            continue
        if built[guid][0] != date or built[guid][1] != link:
            print(f"  FAIL changed: {guid}\n    {date} {link}\n -> {built[guid][0]} {built[guid][1]}")
            failed = True
    for guid, (date, _, title) in built.items():
        if guid not in live:
            print(f"  new: {guid} ({title}, {date:%Y-%m-%d})")

sys.exit(1 if failed else 0)

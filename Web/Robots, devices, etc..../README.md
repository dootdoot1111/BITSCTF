# Robots, devices, etc....

This challenge introduce us to the concept of robots.txt. robots.txt are text files often present on servers to help crawlers, crawl their site. They decide what pages should be allowed to the crawler for indexing.

Head over to the challenge site. Left click and choose 'Inspect element' to view the source html. Notice the comment:

![comment](https://i.ibb.co/9TJBWHj/comment.png)

Head over to robots.txt, we see :

![robots](https://i.ibb.co/0fTS9XD/Screenshot-2021-01-12-at-2-16-58-PM.png)

We change our user-agent string to "something". This can be done easily by using [add-ons](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) for your browser.

Head over to /flag, with your user-agent switched to get the flag!

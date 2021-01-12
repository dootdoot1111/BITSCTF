# biscuits

Challenge Link : [biscuits](https://ctf.bitskrieg.org/web_chall1)

From the challenge name it should be apparent that this refers to cookies. Yeah the same stuff suspicious sites offer you when you visit them. Cookies are data stored by a website in your browser used to identify you when you visit the server again. It is often (ab)used by sites to collect data, and create a digital fingerprint.
Scary stuff.

Head over to the challenge site. It asks for us to give cookies for user. We can do this by making a cookie named "user" and adding any value to it. This can be done again by using [add-ons](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/?utm_source=addons.mozilla.org&utm_medium=referral&utm_content=search) in your browser.

However this is not the last step since the site asks us for having admin info as well. We can do that by simply changing the value in the user cookie to "admin" !

Change the user cookie value to get the flag!

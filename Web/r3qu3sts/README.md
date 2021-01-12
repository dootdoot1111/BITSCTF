# r3qu3sts

Challenge link : [r3qu3sts](https://ctf.bitskrieg.org/web_chall2)

This challenges introduces us to concept of POST. POST is a method of sending data to a server. It is the most commonly used method for sending username and password for authentication.
POST requests are usually sent over a http-post-form, but since we dont see anything in our challenge link, we'll be using the CLI command curl for it. 

Curl is a very important tool for sending and receiving requests from a terminal. You can learn more about curl over [here](https://linuxhandbook.com/curl-command-examples/).

Run the following in your terminal :

```
curl -X POST https://ctf.bitskrieg.org/web_chall2/flag

```

You'll get the flag as a response in your teminal!

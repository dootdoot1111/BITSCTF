# Bases

Bases (note the plural) introduces us to the most important text encoding scheme, base64. It is most commonly asked in CTF's and is very useful.

The challenge provides us with :

```
Vm0xNFlXRXdNVWhVV0doWVlrZFNXRll3WkZOV2JHeHlWMjFHVjFKdGVEQlViRnBQVlRGS2MxTnViRmROYmsxNFdXdGtTMU5HY0RaVGJHUk9WbXR3UlZkWGVHRldNVnBXVFZWV2FHVnFRVGs9
```

We base64 [decode](https://www.base64decode.org/) the above text, and notice we get similar text again. 

Base64 decode again and again (7 times) to get the flag!

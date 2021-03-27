"""
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as 
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as 
http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. 
There is no restriction on how your encode/decode algorithm should work. 
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.


Reference 
    - https://leetcode.com/problems/encode-and-decode-tinyurl/
"""
import string
import random 
import math


full_tiny, tiny_full = {}, {}
letters = string.ascii_letters + string.digits


class Codec:

    # Runtime: 36 ms, faster than 43.51%, Memory Usage: 14.4 MB, less than 30.45%
    """ 較佳做法 """    
    def encode(self, longUrl: str):
        # encodes a URL to shortened URL.

        def short_add():
            ans = ''
            tmp = ''
            for i in range(6):
                tmp = letters[random.randint(0, 10000) % 62]
                ans += tmp
            return ans

        if longUrl in full_tiny:
            return 'http://tinyurl.com/' + full_tiny[longUrl]
        else:
            suffix = short_add()
            full_tiny[longUrl] = suffix
            tiny_full[suffix] = longUrl
            return 'http://tinyurl.com/' + suffix


    def decode(self, shortUrl: str):
        # decodes a shortened URL to its original URL.
        shortUrl = shortUrl.split('/')[-1]
        if shortUrl in tiny_full:
            return tiny_full[shortUrl]
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))


if __name__ == '__main__':
    url = 'http://www.google.com/ssssdawf'
    codec = Codec()

    shortUrl = codec.encode(url)
    print('shortUrl: ', shortUrl)

    orignUrl = codec.decode(shortUrl)
    print('orignUrl', orignUrl)


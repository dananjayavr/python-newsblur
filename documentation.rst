Login:

  ``import newsblur``

  ``newsblur.login('samuelclay','new$blur')``

Output:

  ``{"code": 1, "result": "ok"}``



Logout:

  ``newsblur.logout()``

Output:

  ``{"code": 1, "result": "ok"}``



Signup:
  
  ``newsblur.signup('samuelclay','new$blur','samuel@ofbrooklyn.com')``

Output (Successful):

  ``{"code": -1, "result": "ok"}``

Output (Unsuccessful):

  ``{"code": -1, "result": "ok"}``



Search Feed:

  ``newsblur.search_feed('techcrunch.com')``

Output:

  ``{"feed_address": "http://www.techcrunch.com/author/mg/", "updated": "5077 hours", "subs": 1, "feed_link": "[]", "favicon_fetching": true, "feed_title": "TechCrunch \xc2\xbb MG Siegler", "exception_type": "feed", "exception_code": 404, "result": "ok", "has_exception": true, "id": 237525, "favicon_color": null}``



Feeds:

  ``newsblur.feeds()``

Output:

  ``{"flat_folders": {"Blogs": [{"ps": 0, "feed_link": "http://kottke.org/", "feed_title": "kottke.org", "ng": 0, "nt": 0, "id": 39}, {"ps": 0, "feed_link": "http://blog.newsblur.com/", "feed_title": "The NewsBlur Blog", "ng": 0, "nt": 0, "id": 558041}, {"ps": 0, "feed_link": "http://www.waxy.org/links/", "feed_title": "Waxy.org Links", "ng": 0, "nt": 0, "id": 3581}, {"ps": 0, "feed_link": "http://xkcd.com/", "feed_title": "xkcd.com", "ng": 0, "nt": 1, "id": 169}], "Cooking": [{"ps": 0, "feed_link": "http://americandrink.net/", "feed_title": "American Drink", "ng": 0, "nt": 0, "id": 64313}, {"ps": 0, "feed_link": "http://saltandfat.com/", "feed_title": "Salt & Fat", "ng": 0, "nt": 0, "id": 48}, {"ps": 1, "feed_link": "http://savorysweetlife.com", "feed_title": "Savory Sweet Life", "ng": 0, "nt": 0, "id": 45}, {"ps": 0, "feed_link": "http://smittenkitchen.com", "feed_title": "smitten kitchen", "ng": 0, "nt": 0, "id": 47}], "Blogs - Photoblogs": [{"ps": 0, "feed_link": "http://iconicphotos.wordpress.com", "feed_title": "Iconic Photos", "ng": 0, "nt": 0, "id": 50}, {"ps": 0, "feed_link": "http://blog.pictorymag.com/", "feed_title": "Pictory Blog", "ng": 0, "nt": 0, "id": 551953}, {"ps": 0, "feed_link": "http://theimpossiblecool.tumblr.com/", "feed_title": "the impossible cool.", "ng": 0, "nt": 1, "id": 34}], "New York": [{"ps": 2, "feed_link": "http://gothamist.com/", "feed_title": "Gothamist", "ng": 4, "nt": 17, "id": 23}, {"ps": 0, "feed_link": "http://www.scoutingny.com", "feed_title": "Scouting NY", "ng": 0, "nt": 0, "id": 27}], "Tech": [{"ps": 0, "feed_link": "http://www.codinghorror.com/blog/", "feed_title": "Coding Horror", "ng": 0, "nt": 0, "id": 2}, {"ps": 2, "feed_link": "http://news.ycombinator.com/", "feed_title": "Hacker News", "ng": 0, "nt": 133, "id": 6}, {"ps": 0, "feed_link": "http://www.macrumors.com", "feed_title": "MacRumors: Mac News and Rumors - Front Page", "ng": 0, "nt": 1, "id": 11}, {"ps": 2, "feed_link": "http://techcrunch.com", "feed_title": "TechCrunch", "ng": 0, "nt": 7, "id": 12}], "Absolute Reads": [{"ps": 0, "feed_link": "http://daringfireball.net/", "feed_title": "Daring Fireball", "ng": 0, "nt": 0, "id": 3}, {"ps": 1, "feed_link": "http://www.avc.com/a_vc/", "feed_title": "Fred Wilson: A VC", "ng": 0, "nt": 0, "id": 159}, {"ps": 0, "feed_link": "http://blog.louisgray.com/", "feed_title": "louisgray.com", "ng": 0, "nt": 0, "id": 172}, {"ps": 0, "feed_link": "http://www.marco.org/", "feed_title": "Marco.org", "ng": 0, "nt": 0, "id": 76}, {"ps": 0, "feed_link": "http://www.randsinrepose.com/", "feed_title": "Rands In Repose", "ng": 0, "nt": 0, "id": 38}]}, "user": "conesus", "result": "ok"}``



Favicons:

  ``newsblur.favicons()``
  
Output:

  Will return a list of favicons



Retrieve a Page from the Feed:

  ``newsblur.id(32)``
  
Output:
 
  Will return the HTML data of the story.



  


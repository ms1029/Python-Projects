### Web Scraping using Python from SCRATH

Web scraping is hot topic and one of the favourites for many, its nothing but
downloading data from a Website. We will be using Python as it is Powerful and
really fast. While scraping any data, first analyze the website from which you
are scraping.

So if we see our webpage, there will be many titles, just go for any one and
right click and inspect. We shall use python script, use request and send a
webpage request and store as a request object and convert it to BeautifulSoup.

Before you start with, you will need to have few installed, so use terminal to
install.

1.  [Python3](https://docs.python-guide.org/starting/install3/linux/)
1.  PIP
1.  Requests
1.  bs4([BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/))
1.  lxml

    $ python3 --version
    It checks, if you dont have then install

    $ sudo apt-get update
    make sure that all your system packages are up-to-date

    $ sudo apt-get install python3.6

    $ sudo apt 
     python3-

    $ pip3 install requests

    $ pip install BeautifulSoup

    $ pip3 install lxml

We can’t depend totally on BeautifulSoup it doesn’t make request to website, so
we are using request. Open the python shell in terminal.

All set, now go to python3(by typing python3 in terminal) and import requests,
bs4(BeautifulSoup) and making a requests in a website(here in this case we have
used a wikipedia — Deep Learning) using request.get() and equate it to resq. The
resq holds the request that we made where its nothing but a object of request
which stores entire webpage. Yes you heard it right the entire webpage which can
be viewed by typing res.text. Resq saves the source code of a webpage.

![](https://cdn-images-1.medium.com/max/1000/1*A0c4gEfu2Cn7WPJyI7DQCA.png)
<span class="figcaption_hack">Initialisation with Python</span>

Lets use another object soup of BeautifulSoup(it supports many structures like
html.parse, ale-xml.txt, lxml, etc.), but we will be using lxml and it will be
passed as parameter along with tree structure in this case res.text. While
checked the type(soup), now soup is a object of class of BeautifulSoup. Once
after this step, we can try out things mentioned in the documentation of
BeautifulSoup. 

h_1 gives the titles in the website, whereas h_1[0].get, we will accessing the
array and requesting for the first title from the website. If we want the text
of it h_1[0].getText().

![](https://cdn-images-1.medium.com/max/800/1*fNwP66EPayxbjL8np3ry7g.png)
<span class="figcaption_hack">BeautifulSoup</span>

Here I concentrated on title, now lets check for headlines, if we inspect we
have the class, but to know class and id you should go to headline and inspect,
if all the headlines are of the class or id, you can do a better job. 

![](https://cdn-images-1.medium.com/max/1000/1*LH0ZOCkpNyVToTGvr2qQWA.png)

![](https://cdn-images-1.medium.com/max/1000/1*nGyuBzldVSX7LOtVRYvVig.png)

    soup.select('.class') 
    for class

       or

    soup.select('#id')
    for id

![](https://cdn-images-1.medium.com/max/600/1*RFqwgoOKbuzXniCn63tFgw.png)
<span class="figcaption_hack">headlines scrape in a website</span>

I will be using class soup.select(‘.mw-headline’). But since this is Wikipedia,
we will get lost of data. So to get precise, we can loop through it. But while
printing im requesting for text, remember we were initially requested Wikipedia
only for headline, so text of headlines are here for you. <br> So now lets
concentrate on find_all() of BeautifulSoup, so it will be looping, I here
looking out for links in the webpage, and the things that we need to find in
parenthesis. So first one is a tag, I will be looking out for ‘a’ tag. Then
string value(true or false), let me say True, and print it(link having href
values).

![](https://cdn-images-1.medium.com/max/1000/1*wUNezGSQ-2_CtpZIJ5dV8A.png)
<span class="figcaption_hack">link scrape in a website</span>

### Conclusion

Scraping can be said as gathering of data for further analysis, we copy them to
csv or html or text or any other form we require in the local database. We can
reduce the content from enormous to content we want. There are legal problems
surrounding it, so before scraping any website have knowledge about the legal
problems in order to be in a safer side.


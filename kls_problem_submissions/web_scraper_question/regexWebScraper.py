import urllib2
import re

from BeautifulSoup import BeautifulSoup

def searchForRegExpInLinksBFS(baseUrl, regExp):
    """
    Does a breadth first search from a baseUrl to find any matches in the HTML content
    for the regular expression provided. All connecting links will be visited.
    
    :param baseUrl: the base URL to start searching from    
    :type baseUrl: str
    :param regExp: the regular expression to try to match from the content
    :type regExp: str
    
    :rtype: set
    """
    if not baseUrl or not regExp:
        return []
        
    queue = [baseUrl]
    visitedUrls = set() # avoid visiting the same URL twice (to avoid infinite loops)
    visitedSuffixes = set() # avoid visited chained links (/index.py/index.py/...)
    allMatches = set() # get only unique regex matches
    while len(queue) > 0:
        currentUrl = queue.pop(0)
        if currentUrl not in visitedUrls:
            
            # Try to open and read the content of the current URL
            # If it fails move on to the next
            try:
                url = urllib2.urlopen(currentUrl)
                content = url.read()
            except urllib2.HTTPError:
                continue
            finally:
                visitedUrls.add(currentUrl)
            
            print "Visiting %s" % currentUrl
            
            # Get all regex matches on the current page 
            # and include this in the set of matches
            matches = set(re.findall(regExp, content))
            allMatches = allMatches.union(matches)
            
            # Use BeautifulSoup to create a parser for 
            # the content on the page in order to find links
            soup = BeautifulSoup(content)
            for a in soup.findAll('a',href=True):
                suffixLink = a['href'][1:] # ignore the starting slash
                if suffixLink and suffixLink not in visitedSuffixes:
                    fullLink = currentUrl + '/' + suffixLink
                    queue.append(fullLink)
                    visitedSuffixes.add(suffixLink)
            
    return allMatches
    
def main():
    urlString = 'https://www.klsdiversified.com'
    phoneNumberRegExp = '\(?[0-9]{3}[\)\. -][0-9]{3}[\. -][0-9]{4}'
    allPhoneNumbers = searchForRegExpInLinksBFS(urlString, phoneNumberRegExp)
    print "\nThe following phone numbers were found under website %s:" % urlString
    for phoneNumber in allPhoneNumbers:
        print phoneNumber
    
main()

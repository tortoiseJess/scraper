import urllib2
from bs4 import BeautifulSoup, SoupStrainer

###############################################################################################################################
    '''
    module to downloading partial soup of webpage
    partial soup was to decrease memory usage
    the different functions was for parsing different pages 

    '''
###############################################################################################################################

    #parses the item detail page
def CreateItemUrlPageSoup(subCateTuple, depth_para):
    url = subCateTuple[1]
    baseCategory = subCateTuple[0]    
    try:
        subCatePage =  urllib2.urlopen(url)
        soup = BeautifulSoup( subCatePage.read())
    except urllib2.URLError,err:
        print 'non successful download: '+err.reason
    finally:
        try:
            subCatePage.close()
        except NameError, e:
            print ' page cannot be closed ' , e
    return soup

    #parses the page containing the item url
def CreateItemSoup(itemUrl,listTags):
    try:
        itemPage =  urllib2.urlopen(itemUrl)
        only_tags = SoupStrainer(listTags)
        soup = BeautifulSoup(itemPage.read(), "html.parser", parse_only=only_tags)
    except urllib2.URLError,err:
        print err.reason
    finally:
        try:
            itemPage.close()
        except NameError:
            pass
    return soup

    #parses the page for subcategory of the supercategory
def CreateSubCateSoup(subCateTuple, strainerDict):
# eg strainerDict = {id: ID_SUBMENU})
    assert(len(strainerDict)==1), "too many strainers"
    url = subCateTuple[1]
    try:
        itemPage =  urllib2.urlopen(url)
        only_tags = SoupStrainer(**strainerDict)   # <---------------------------------only thing different CreateItemSoup
        soup = BeautifulSoup(itemPage.read(), "html.parser", parse_only=only_tags)
    except urllib2.URLError,err:
        print err.reason
    finally:
        try:
            itemPage.close()
        except NameError:
            pass
    return soup

    #gets the header of the page
def GetHeaderString(url):
    return CreateItemSoup(url,'h1').string
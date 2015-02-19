

from parsers import *
from downloader import *
from writer import *
from constants import *

#==================================================================================================================================
'''
This module sreamlines the parsed list/url to parsing for item detials

'''
#===================================================================================================================================



def ParseProtocolDetailsGen(subCateSoup):
    #generates item details from generic item categories
    itemUrl=parseItemUrl(subCateSoup,PDTBASEURL)
    subCateSoup.decompose()
    if itemUrl is not None:
        listTags = listTagsPdts
        soup = CreateItemSoup(itemUrl,listTags)
        idBase= ITEM_BASE_ID
        ids = IDS_ITEM   
        itemDetails= ParseItemPageBasic(soup, idBase, **ids) 
        soup.decompose()
    else:
        itemDetails = ['no items in this category ']
        
    return itemDetails

      
def ParseProtocolDetailsGiftCard(soup,idNameGiftCards):    
    # parses for the details from gift cards category
    itemUrl = parseItemUrl(soup,PDTBASEURL,idName=idNameGiftCards)
    soup.decompose()
    if itemUrl is not None:
        listTags = listTagsPdts
        soup = CreateItemSoup(itemUrl,listTags)
        idBase= ITEM_BASE_ID
        ids = IDS_ITEM   
        itemDetails= ParseItemPageBasic(soup, idBase, **ids) #proceed to parse item 
        soup.decompose()
    else:
        itemDetails = ['no items in this category ']
    return itemDetails

def ParseProtocolDetailsBundles(subCateSoup,idNameBundles ):
    # parses for the details from the bundles category
    itemUrl = parseItemUrl(subCateSoup,BUNDLESURL,idName=idNameBundles)  
    subCateSoup.decompose()
          
    if itemUrl is not None:
        listTags = listTagsPdts
        soup = CreateItemSoup(itemUrl,listTags)
        idBase= ITEM_BUNDLES
        ids = IDS_BUNDLES
        itemDetails= ParseItemPageBasic(soup, idBase, **ids) #proceed to parse item
        soup.decompose()
    else:
        itemDetails = ['no items in this category ']
    return itemDetails

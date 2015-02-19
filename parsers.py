
#========================================
from downloader import *
import re 
from writer import *
from constants import *
#===================================================================================================================================
'''
purpose of this module is to parse for the right subcategories' list i the left menu
the different functions are customized for different pages 
since the layout and left menu containing the list is different

'''
#========================================== global variables for this module ======================================================
PDTBASEURL = "http://www.visions.ca/Catalogue/Category/"
depth_para =0
#===================================================================================================================================
def ParserSubCateList(subCateSoup,depth_para):
    # generic page to parse for the url
    #IF NO SUBCATELIST IS ON WEBPAGE, PASSES A NONETYPE VALLUE, INDICATING POTENTIAL PAGE CONTAINING ITEM URL/ NO CATEGORIES
    try:
        subCateList=subCateSoup.find_all('li')
        subCateNameList = [x.a.string for x in subCateList]
        subCateUrlList = [PDTBASEURL+x.a['href'] for x in subCateList]
        subCategoriesList= zip(subCateNameList,subCateUrlList) 
        depth_para +=1
        return subCategoriesList
    except (TypeError, IndexError) as e:
        print 'error!!!'
        print e
        return None

def ParserSubCateListRoot(subCateSoup,depth_para,ROOT_URL, tag, CSSAttr):
    #subCateSoup contains the right <ul>
    #parses from the master menu
    #IF NO SUBCATEGORY LIST IS ON WEBPAGE, PASSES A NONETYPE VALLUE, INDICATING POTENTIAL PAGE CONTAINING ITEM URL
    print 'ParserSubCateListRoot generating......................'
    try:
        subCateList=subCateSoup.find_all(tag, class_=CSSAttr)
        subCateNameList = [x.a.string for x in subCateList]
        subCateUrlList = [ROOT_URL+x.a['href'] for x in subCateList]
        subCategoriesList= zip(subCateNameList[:-1:],subCateUrlList[:-1:]) 
        depth_para +=1
        return subCategoriesList
    except (TypeError, IndexError) as e:
        print 'error!!!'
        print e
        print "website does not have any products!"
        return None

def ParseSubCateListFromMenu(subCateSoup,depth_para):
    # parses for the subcategories list from the second page
    subCateList = subCateSoup.find_all('ul',id=False, style=False)
    subCategoriesList=[]
    count =0
    for tag in subCateList:
        if tag.attrs =={} and tag.find_previous('h2').string == H2_SUBCATE:
            tagList = tag.find_all('li')
            subCateNameList = [x.a.string for x in tagList]
            subCateUrlList = [PDTBASEURL+x.a['href'] for x in tagList]
            subCategoriesList= zip(subCateNameList,subCateUrlList) # returns list of tuples of 0 = mother pdt, 1 = her url
            count +=1
            break
        else:
            subCategoriesList= None
    depth_para +=1
    return subCategoriesList


def parseItemUrl(soup,
                 urlBases,
                 tag='a',
                 idName='_ContentPlaceHolder1_ProductItemListUC1_ctrlProducts_ct'): #find url = find href attribute = find a anchor in tag
    try:
        itemUrl = soup.body.find(tag, id=re.compile(idName) )
        itemUrl=itemUrl['href']
        itemUrl = urlBases+itemUrl
    except (AttributeError,TypeError) as e:
        print '{}, so no item in this category'.format(e)
        itemUrl = None
    return itemUrl

def ParseItemPageBasic(soup, idBase, ITEM_NAME,ITEM_PRICE, 
    ITEM_ID='',
    FREE_SHIP='',
    WEB_ONLY = '',
    SALES_END ='',
    STORE_ONLY = '',
    LIMITED = ''
):
    #parses for the specific item details for main output 
    print 'ParseItemPageBasic.........'
    itemName = ''
    itemPrice = ''
    itemAvai = ['in stock']
    itemID =''

    try:
        tags = soup.find_all(id = re.compile('^'+idBase))
        for tag in tags:
            if tag['id'] == idBase + ITEM_NAME:
                try:
                    itemName=tag.h3.string
                except AttributeError: 
                    itemName=tag.string
            elif tag['id']== idBase + ITEM_PRICE:
                itemPrice = tag.string
                print itemPrice
            elif tag['id'] == idBase + ITEM_ID:
                itemID = tag.string
            elif tag['id'] == idBase + FREE_SHIP:
                itemAvai.append('free shipping')
            elif  tag['id'] ==idBase+WEB_ONLY:
                itemAvai.append('web available only')
            elif  tag['id'] ==idBase+SALES_END:
                itemAvai.append(tag.string)
            elif tag['id'] ==idBase+STORE_ONLY:
                itemAvai.append('In store only')
            elif tag['id'] ==idBase+LIMITED:
                itemAvai.append('limited quantities')
            
            
        itemDetails= [itemName+' ('+itemID+')', itemID, itemPrice]+ itemAvai
        return itemDetails
    except TypeError ,err:
        print err



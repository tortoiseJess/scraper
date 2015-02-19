'''
Created on Jan 28, 2015

@author: jessey
'''


from parsers import *
from downloader import *
from writer import *
from constants import *
from procedure import *
import sys

#===================================================================================================================================
'''
main contains the recursion process 
determines when to go deeper one level and when to stop and parse for the item details

'''
#===================================================================================================================================



def CrawlTillPdt(subCateTuple, superCateName): 

    CsvWriterRel(pathRel, superCateName,subCateTuple[0])
    strainerDict = {'class_':SUBMENU_CLASS} 
    subCateSoup =  CreateSubCateSoup(subCateTuple, strainerDict)

    header=GetHeaderString(subCateTuple[1])
    
    #CASE 1: need to continue with recursion 
    #CASE 2: an item page to be parsed is found
    if header is None:
        strainerDict = {'id':'subcatemenu-container'} 
        subCateSoup =  CreateSubCateSoup(subCateTuple, strainerDict)
        subCategoriesList = ParseSubCateListFromMenu(subCateSoup,depth_para)
        subCateSoup.decompose()
        if subCategoriesList is not None:
            for subCateTupleNew in subCategoriesList:
                CrawlTillPdt(subCateTupleNew,superCateNameNew)        
        else:
            subCateSoup =  CreateItemUrlPageSoup(subCateTuple, depth_para)  
            itemDetails=ParseProtocolDetailsGiftCard(subCateSoup,idNameGiftCards)
            nodeCateName = subCateTuple[0]
            CsvWriterItems(pathItems,nodeCateName, itemDetails)
            subCateSoup.decompose() 
    else:
        subCategoriesList=ParserSubCateList(subCateSoup,depth_para)
        if subCategoriesList is None:
            subCateSoup =  CreateItemUrlPageSoup(subCateTuple, depth_para)
            itemDetails=ParseProtocolDetailsGen(subCateSoup)
            nodeCateName = subCateTuple[0]
            CsvWriterItems(pathItems,nodeCateName, itemDetails)
            subCateSoup.decompose() 

            
        else:
            if superCateName in [x[0] for x in subCategoriesList]:
                print 'CrawlTillPdt is going to parse the page '
                subCateSoup =  CreateItemUrlPageSoup(subCateTuple, depth_para)
                itemDetails=ParseProtocolDetailsGen(subCateSoup)
                nodeCateName = subCateTuple[0]
                CsvWriterItems(pathItems,nodeCateName, itemDetails)
                subCateSoup.decompose() 
            else: 
                print "CrawlTillPdt has to continue crawling "
                superCateNameNew = subCateTuple[0]
                for subCateTupleNew in subCategoriesList:
                    CrawlTillPdt(subCateTupleNew,superCateNameNew)


    print "great! CrawlTillPdt exiting from {}....".format(superCateName)
     



#======================================================================================================
def main():
    
    #============================now at root page ==========================================================
    #CREATE SOUP GIVEN URL --DOWNLOADER
    print('mining data layer ONE: ' + PDTBASEURL)
    superCateName = 'NONE. AM ROOT'
    rootUrlTuple = (superCateName, PDTBASEURL)
    strainerDict = {'id': 'mastermenu-startbtn' }
    mainSoup=CreateSubCateSoup(rootUrlTuple, strainerDict)
    tag = 'li'
    CSSAttr = 'menulevel-0'
    ROOT_URL = BASEURL
    rootSubCategoriesList = ParserSubCateListRoot(mainSoup,depth_para,ROOT_URL,tag, CSSAttr)
    mainSoup.decompose() 
    # ONLYSOME = rootSubCategoriesList[-5:]
    #====================================now at Other pages that follow===========================================================
    
    SPECIAL_PAGE =  [ 'BUNDLES']
    superCateName = 'NONE. AM ROOT'
    for cateTuple in rootSubCategoriesList: 
        if cateTuple[0] not in SPECIAL_PAGE:
            CrawlTillPdt(cateTuple,superCateName)
        elif cateTuple[0] =='BUNDLES':
            CsvWriterRel(pathRel, superCateName,cateTuple[0])
            nodeCateName = 'Bundles'
            urlTuple = (nodeCateName , BUNDLESURL)
            subCateSoup = CreateItemUrlPageSoup(urlTuple,depth_para)   
            itemDetails=ParseProtocolDetailsBundles(subCateSoup,idNameBundles)
            CsvWriterItems( pathItems, nodeCateName, itemDetails)    
              

            
 #=============================================================================

if __name__ == "__main__":
    pathItems = 'items.csv'
    pathRel = 'rel.csv'
    fieldNames= ['superCate', 'ItemName',"itemID",'itemNowPrice','itemAvailability']
    relFieldNames = ['SuperCategoryName', 'SubCategoryName']
    CsvWriteHeader(pathItems,fieldNames)
    CsvWriteHeader(pathRel , relFieldNames)
#     sys.stdout = open('consoleOutput.txt', 'w')
    main()
    
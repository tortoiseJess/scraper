# The purpose of this module is to store all the tags to identify the right elements from the html page

#SPECIFIC TO SESSION=======================================================================================

#SPECIFIC TO WEBSITE======================================================================================
BASEURL = "http://www.visions.ca/"
PDTBASEURL = "http://www.visions.ca/Catalogue/Category/"
SUBMENU_CLASS = 'subcatemenu-items'
H2_SUBCATE = 'Browse By Category'
#========================================================================================================
#SPECIFIC TO GENERAL CATEGORY ITEMdETAILS:===============================================================
ITEM_BASE_ID='ctl00_ContentPlaceHolder1_ctrlProdDetailUC_'
listTagsPdts = ['span','img','div']
TEXTS='lbl'
NAME_ID = 'ProdTitle'
ITEM_ID = 'SKU'
PRICE_ID = 'Saleprice'
WEB_ONLY_ID='Webonly'
SALES_END_ID='SaleEnds'
STORE_ONLY_ID = "imgInstoreonly" 
LIMITED_ID ='pnlFinalClearance'
IDS_ITEM= {  'ITEM_NAME': TEXTS+NAME_ID, 
              'ITEM_ID': TEXTS+ITEM_ID, 
              'ITEM_PRICE':TEXTS+PRICE_ID, 
              'FREE_SHIP' :'lblFreeShipping', 
              'WEB_ONLY': TEXTS+WEB_ONLY_ID,
              'SALES_END': TEXTS+SALES_END_ID,
               'STORE_ONLY': STORE_ONLY_ID, 
               'LIMITED': LIMITED_ID 
}
#=============================================================================================================
#SPECIFIC TO ROOT -->SDARY MENU, eg GIFT CARDS
#=============================================================================================================
idNameGiftCards = '_ContentPlaceHolder1_ProductMainListUC1_dlProducts_ct'
idNameBundles = '_ContentPlaceHolder1_rptItems_ctl'
#=============================================================================================================
# SPECIFIC TO BUNDLES
#=============================================================================================================
BUNDLESURL= "http://www.visions.ca/Catalogue/Bundles/"
ITEM_BUNDLES='ctl00_ContentPlaceHolder1_'
listTagsBundles =['span','div','img']
IDS_BUNDLES= {'ITEM_NAME': 'pnlTitle', 'ITEM_PRICE':'lblSalePrice', 'FREE_SHIP' :'lblFreeShipping'}
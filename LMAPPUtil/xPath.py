# -*- coding: UTF-8 -*-

'''
Created on 2015年9月25日

@author: NJNUGGET
'''
# ===================================
# ANDROID控件xPath地址
# ===================================
EIDTTEXT_ANDROID = "//android.widget.EditText"
NOTICE_IMAGE_ANDROID = "//android.widget.ImageView"
REPLY_BUTTON_ANDROID = "//android.widget.LinearLayout[3]/android.widget.ImageView[1]"
SALE_PRODUCT_ANDROID_1 = "//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]"
SALE_PRODUCT_ANDROID_2 = "//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]"
SALE_PRODUCT_ANDROID_3 = "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]"
SALE_PRODUCT_ANDROID_4 = "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]"
SALE_PRODUCT_ANDROID_5 = "//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.FrameLayout[1]"
SALE_PRODUCT_ANDROID_6 = "//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.FrameLayout[2]"
SELECTED_PRODUCT_ANDROID = "//android.widget.ListView[1]/android.widget.FrameLayout[1]"
OPREATION_IMAGE_ADNROID = "//android.support.v4.view.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]"
SHARE_TOPIC_BUTTON_ANDROID = "//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.ImageView[1]"
ADD_PASSANGER_SUCCESS_ANDROID = " //android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]"
PRODUCT_TYPE_ANDROID_1 = "//android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
PRODUCT_TYPE_ANDROID_2 = "//android.widget.RelativeLayout[2]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
PRODUCT_TYPE_ANDROID_3 = "//android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
PRODUCT_TYPE_ANDROID_4 = "//android.widget.RelativeLayout[4]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
PRODUCT_TYPE_ANDROID_5 = "//android.widget.RelativeLayout[5]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
PRODUCT_TYPE_ANDROID_6 = "//android.widget.RelativeLayout[6]/android.widget.RelativeLayout[1]/android.widget.TextView[1]"
DATE_PICKER_ANDROID_YER_BEFORE = "//android.widget.NumberPicker[1]/android.widget.Button[1]"
DATE_PICKER_ANDROID_YER_AFTER = "//android.widget.NumberPicker[1]/android.widget.Button[2]"
DATE_PICKER_ANDROID_MON_BEFORE = "//android.widget.NumberPicker[2]/android.widget.Button[1]"
DATE_PICKER_ANDROID_MON_AFTER = "//android.widget.NumberPicker[2]/android.widget.Button[2]"
DATE_PICKER_ANDROID_DAY_BEFORE = "//android.widget.NumberPicker[3]/android.widget.Button[1]"
DATE_PICKER_ANDROID_DAY_AFTER = "//android.widget.NumberPicker[3]/android.widget.Button[2]"
DATE_PICKER_ANDROID_DAY_EDIT = "//android.widget.NumberPicker[3]/android.widget.EditText"
WIFI_GET_TIME_ANDROID = "//android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[2]/android.widget.TextView[2]"
WIFI_RETURN_TIME_ANDROID = "//android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[3]/android.widget.TextView[2]"
WIFI_GET_PLACE_ANDROID = "//android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]"
WIFI_RETURN_PLACE_ANDROID = "//android.widget.RelativeLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]"
TIME_LIST_ANDROID_1 = "//android.widget.ListView[1]/android.widget.RelativeLayout[1]"
TIME_LIST_ANDROID_2 = "//android.widget.ListView[1]/android.widget.RelativeLayout[2]"
TIME_LIST_ANDROID_3 = "//android.widget.ListView[1]/android.widget.RelativeLayout[3]"
APPLICANT_PEOPLE_ANDROID = "//android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]"
# ===================================
# ANDROID控件ID
# ===================================
COLLECT_PRODUCT_ID_ANDROID = "com.qyer.android.lastminute:id/deal_layout"
IRREGULAR_IMAGE_ID_ANDROID_1 = "com.qyer.android.lastminute:id/ivSale1"
NOTICE_DELETE_ID_ANDROID = "com.qyer.android.lastminute:id/iv_notifi_delete"
SEARCH_IMAGE_ID_ANDROID = "com.qyer.android.lastminute:id/ic_left_image"
SELECTED_PRODUCT_LEFT_ID_ANDROID = "com.qyer.android.lastminute:id/llLeftPanle"
SORT_BUTTON_ID_ANDROID = "com.qyer.android.lastminute:id/ivOrderType"
CHOOSE_PASSANGER_ANDROID = "com.qyer.android.lastminute:id/rlRightContent"
ORDER_SUBMIT_ANDROID_1 = "com.qyer.android.lastminute:id/bt_order_submit"
ORDER_SUBMIT_ANDROID_2 = "com.qyer.android.lastminute:id/tvSubmitOrder"

# ===================================
# IOS控件xPath地址
# ===================================
MAIN_CATEGORY_IOS_FREETOUR = "//UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[1]"
MAIN_CATEGORY_IOS_FLIGHT = "//UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[2]"
MAIN_CATEGORY_IOS_CITYFUN = "//UIACollectionView[1]/UIACollectionCell[1]/UIAStaticText[3]"

MINE_BUTTON_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAButton[4]"
MINE_USERNAME_IOS = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAStaticText[1]"
MINE_QYLOGIN_BUTTON_IOS = "//*[@label='QYLoginButton']"
MINE_YHP_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAButton[4]"
CATEGORY_BUTTON_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAButton[2]"
CATEGORY_FLIGHT_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAStaticText[1]"
SALE_PRODUCT_IOS_1 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[1]/UIAButton[1]"
SALE_PRODUCT_IOS_2 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[2]/UIAButton[1]"
SALE_PRODUCT_IOS_3 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[3]/UIAButton[1]"
SALE_PRODUCT_IOS_4 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[4]/UIAButton[1]"
SALE_PRODUCT_IOS_5 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[5]/UIAButton[1]"
SALE_PRODUCT_IOS_6 = "//UIAApplication[1]/UIAWindow[1]/UIAScrollView[2]/UIAImage[6]/UIAButton[1]"
PRODUCT_TYPE_IOS_1 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[2]/UIAButton[1]"
PRODUCT_TYPE_IOS_2 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAButton[1]"
PRODUCT_TYPE_IOS_3 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[4]/UIAButton[1]"
PRODUCT_TYPE_IOS_4 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[5]/UIAButton[1]"
PRODUCT_TYPE_IOS_5 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[6]/UIAButton[1]"
PRODUCT_TYPE_IOS_6 = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[7]/UIAButton[1]"
CALENDAR_BUTTON_FREETOUR_IOS = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[9]/UIAButton"
CALENDAR_BUTTON_DAYTRIP_IOS = " //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[8]/UIAButton"
CALENDAR_BUTTON_PICKUP_IOS = " //UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[7]/UIAButton"
DATE_PICKER_IOS_YER = "//UIAPicker[1]/UIAPickerWheel[1]"
DATE_PICKER_IOS_MON = "//UIAPicker[1]/UIAPickerWheel[2]"
DATE_PICKER_IOS_DAY = "//UIAPicker[1]/UIAPickerWheel[3]"
SUBMIT_DATE_IOS = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[3]/UIAStaticText[2]"
PASSANGER_CHECKBOX_IOS = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[1]"
NOTICE_TRAVELTIME_IOS = "//UIAScrollView[1]/UIAImage[3]"
NOTICE_DELETE_IOS = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]/UIAButton[2]"
SELECTED_BUTTON_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAButton[3]"
SELECTED_PRODUCT_IOS = "//UIAApplication[1]/UIAWindow[1]/UIATableView[1]/UIATableCell[1]"
SEARCH_BUTTON_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAImage[1]/UIAButton[2]"
ORDER_DELETE_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]"
REPLY_BUTTON_IOS = "//UIAApplication[1]/UIAWindow[1]/UIAImage[3]/UIAButton[1]"
REPLY_TEXTFIELD_IOS = "//UIAScrollView[1]/UIATextView[1]"
# ===================================
# IOS精确点击脚本
# ===================================
SUBMIT_DATE_WIFI_script_IOS = (348,468)
SUBMIT_PLACE_script_IOS = (352,507)
SUBMIT_DATE_TICKET_script_IOS = (352,440)
SUBMIT_ORDER_script_IOS = (311,639)
#SUBMIT_PICKER_IOS = execute_script("mobile: tap", {"tapCount": 1, "touchCount": 1, "duration": 0.5, "x": 348, "y": 468 })

from selenium.webdriver.common.by import By

url = "https://www.taobao.com/"

login_link = By.PARTIAL_LINK_TEXT, "亲，请登录"

login_username = By.CSS_SELECTOR, "#fm-login-id"

login_password = By.CSS_SELECTOR, "#fm-login-password"

login_sliding = By.CSS_SELECTOR, '#nc_1_n1z'

login_bnt = By.CSS_SELECTOR, "#login-form > div.fm-btn > button"

shopping_search_box = By.CSS_SELECTOR, "#q"

shopping_search_btn = By.CSS_SELECTOR, "#J_TSearchForm > div.search-button > button"

shopping_commodity_page = By.CSS_SELECTOR, ("#pageContent > div.LeftLay--leftWrap--xBQipVc.search-content-leftWrap > "
                                            "div.LeftLay--leftContent--AMmPNfB > div.Content--content--sgSCZ12 > div >"
                                            " a:nth-child(1) > div > div.Card--mainPicAndDesc--wvcDXaK > div.MainPic--"
                                            "mainPicWrapper--iv9Yv90 > img.MainPic--mainPic--rcLNaCv")

shopping_add_shopping_cart = By.CSS_SELECTOR, "#purchasePanel > div.PurchasePanel--footWrap--3w0gUyF.PurchasePanel-" \
                                              "-floatShow--1p-8tE4 > div > div.Actions--leftButtons--2fasaTH > butt" \
                                              "on.Actions--btn--1S_ka08.Actions--rightBtn--31O_Xka.Actions--prima" \
                                              "ryBtn--1eLlUkI > span"

shopping_bnt_my_cart = By.CSS_SELECTOR, "#sn-bd > div > ul > li.sn-cart > a"

order_bnt_all_choose = By.CSS_SELECTOR, "#mainHeaderContainer_1 > div.cartOperation--JUDK2BYF > label > span:nth-" \
                                        "child(2)"

order_bnt_settle = By.CSS_SELECTOR, "#settlementContainer_1 > div:nth-child(4) > div > div.btn--QDjHtErD"

order_bnt_submit = By.CSS_SELECTOR, "#submitOrder > div > div.btnBox--p9CumEtE > div"

order_purchase_password = By.CSS_SELECTOR, "#payPassword_rsainput"

order_bnt_sure = By.CSS_SELECTOR, "#validateButton"



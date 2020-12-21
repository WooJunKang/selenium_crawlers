{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "# from selenium.webdriver.common.keys import Keys\n",
    "# from selenium.webdriver.support.ui import Select\n",
    "import time\n",
    "import pandas as pd\n",
    "import datetime as dt # 4 convert string to datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "SessionNotCreatedException",
     "evalue": "Message: session not created: This version of ChromeDriver only supports Chrome version 79\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mSessionNotCreatedException\u001b[0m                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-9a5ba6e4f952>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# 크롬 드라이브 실행\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mchrome\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'../chromedriver'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mchrome\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'https://play.google.com/store/apps'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# 검색 input box에 검색어 입력 후 검색 실행\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, executable_path, port, options, service_args, desired_capabilities, service_log_path, chrome_options, keep_alive)\u001b[0m\n\u001b[1;32m     79\u001b[0m                     \u001b[0mremote_server_addr\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice_url\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     80\u001b[0m                     keep_alive=keep_alive),\n\u001b[0;32m---> 81\u001b[0;31m                 desired_capabilities=desired_capabilities)\n\u001b[0m\u001b[1;32m     82\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     83\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mquit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, command_executor, desired_capabilities, browser_profile, proxy, keep_alive, file_detector, options)\u001b[0m\n\u001b[1;32m    155\u001b[0m             warnings.warn(\"Please use FirefoxOptions to set browser profile\",\n\u001b[1;32m    156\u001b[0m                           DeprecationWarning, stacklevel=2)\n\u001b[0;32m--> 157\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart_session\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcapabilities\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbrowser_profile\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    158\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_switch_to\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mSwitchTo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    159\u001b[0m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_mobile\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mMobile\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mstart_session\u001b[0;34m(self, capabilities, browser_profile)\u001b[0m\n\u001b[1;32m    250\u001b[0m         parameters = {\"capabilities\": w3c_caps,\n\u001b[1;32m    251\u001b[0m                       \"desiredCapabilities\": capabilities}\n\u001b[0;32m--> 252\u001b[0;31m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mCommand\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mNEW_SESSION\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparameters\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    253\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;34m'sessionId'\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    254\u001b[0m             \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'value'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self, driver_command, params)\u001b[0m\n\u001b[1;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    320\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 321\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[1;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/remote/errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[0;34m(self, response)\u001b[0m\n\u001b[1;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'alert'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'text'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    241\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 242\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    243\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    244\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mSessionNotCreatedException\u001b[0m: Message: session not created: This version of ChromeDriver only supports Chrome version 79\n"
     ]
    }
   ],
   "source": [
    "# 크롬 드라이브 실행\n",
    "chrome = webdriver.Chrome('../chromedriver')\n",
    "chrome.get('https://play.google.com/store/apps')\n",
    "\n",
    "# 검색 input box에 검색어 입력 후 검색 실행\n",
    "input_box = chrome.find_element_by_css_selector('#gbqfq')\n",
    "input_box.send_keys('요기요')\n",
    "input_box.submit() \n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 검색 결과 중 첫 번째 앱 클릭 \n",
    "link = chrome.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz:nth-child(4) > div > div.N4FjMb > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(1) > c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a')\n",
    "link.click()\n",
    "time.sleep(3)\n",
    "\n",
    "# 리뷰 하단의 '리뷰 모두 보기' 버튼 클릭\n",
    "review_show_all = chrome.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz.zQTmif.SSPGKf.I3xX3c.drrice > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div.XnFhVd > div')\n",
    "review_show_all.click()\n",
    "time.sleep(1)\n",
    "\n",
    "# 리뷰 정렬 변경을 위해 드롭박스 클릭\n",
    "drop_arrow = chrome.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div:nth-child(1) > div.CeEBt.Ce1Y1c.eU809d > span')\n",
    "drop_arrow.click()\n",
    "time.sleep(2)\n",
    "\n",
    "# 리뷰 정렬을 '최신순'으로 변경\n",
    "order_by_date = chrome.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > c-wiz > div:nth-child(1) > div > div.OA0qNb.ncFHed > div:nth-child(1)')\n",
    "order_by_date.click()\n",
    "time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 마우스 커서 페이지 가장 하단으로 이동 -> 리뷰 더 로드하기 위함\n",
    "# 4번 이동 후 '더보기' 버튼 클릭 -> 이 과정 반복\n",
    "# 이동 위치는 페이지 하단의 정보 div 태그\n",
    "move_cursor = chrome.find_element_by_css_selector('#ZCHFDb > c-wiz > div > div.sIIDsc.IQ1z0d > div:nth-child(3)')\n",
    "move_cursor.click()\n",
    "time.sleep(2)\n",
    "move_cursor.click()\n",
    "time.sleep(2)\n",
    "move_cursor.click()\n",
    "time.sleep(2)\n",
    "move_cursor.click()\n",
    "time.sleep(4)\n",
    "\n",
    "review_more = chrome.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > div.PFAhAf > div > span')\n",
    "review_more.click()\n",
    "\n",
    "review_all = chrome.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div > div > div > div > div.d15Mdf.bAhLNe')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 마우스 커서 페이지 가장 하단으로 이동 -> 리뷰 더 로드하기 위함\n",
    "# 4번 이동 후 '더보기' 버튼 클릭 -> 이 과정 반복\n",
    "# 이동 위치는 페이지 하단의 정보 div 태그\n",
    "\n",
    "# 앱 리뷰의 작성 일이 2019년 이후인 것만 수집\n",
    "while dt.datetime.strptime(review_all[len(review_all)-1].find_element_by_class_name('p2TkOb').text, '%Y년 %m월 %d일') >= dt.datetime.strptime('2019-01-01', '%Y-%m-%d'):\n",
    "    \n",
    "    # 마우스 커서 4번 이동\n",
    "    move_cursor = chrome.find_element_by_css_selector('#ZCHFDb > c-wiz > div > div.sIIDsc.IQ1z0d > div:nth-child(3)')\n",
    "    move_cursor.click()\n",
    "    time.sleep(2)\n",
    "    move_cursor.click()\n",
    "    time.sleep(2)\n",
    "    move_cursor.click()\n",
    "    time.sleep(2)\n",
    "    move_cursor.click()\n",
    "    time.sleep(2)\n",
    "    \n",
    "    # '더보기' 버튼 element 못 찾으면 수집 종료\n",
    "    try:\n",
    "        review_more = chrome.find_element_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div:nth-child(2) > div.PFAhAf > div > span')\n",
    "        review_more.click()\n",
    "        review_all = chrome.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div > div > div > div > div.d15Mdf.bAhLNe')\n",
    "        \n",
    "    except:\n",
    "        review_all = chrome.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.ZfcPIb > div > div.JNury.Ekdcne > div > div > div.W4P4ne > div > div > div > div > div.d15Mdf.bAhLNe')\n",
    "        print('수집완료')\n",
    "        break\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_review = pd.DataFrame()\n",
    "\n",
    "for i in range(len(review_all)-1):\n",
    "    \n",
    "    print(str(i+1) + ' / ' + str(len(review_all)-1) + '번째 진행중...')\n",
    "\n",
    "    date = review_all[i].find_element_by_class_name('p2TkOb').text\n",
    "    writer = review_all[i].find_element_by_class_name('X43Kjb').text\n",
    "    rating = review_all[i].find_element_by_css_selector('div.xKpxId.zc7KVe > div.bAhLNe.kx8XBd > div > span.nt2C1d > div > div').get_attribute('aria-label').split('만점에 ')[1].split('개')[0]\n",
    "    review = review_all[i].find_element_by_class_name('UD7Dzf').text\n",
    "    \n",
    "    tmp = pd.DataFrame({'date': date, 'writer': writer, 'rating': rating, 'review_content': review}, index = [0])\n",
    "    df_review = df_review.append(tmp)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

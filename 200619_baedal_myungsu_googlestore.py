{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
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
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "WebDriverException",
     "evalue": "Message: 'chromedriver`' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home\n",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     75\u001b[0m                                             \u001b[0mstderr\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog_file\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 76\u001b[0;31m                                             stdin=PIPE)\n\u001b[0m\u001b[1;32m     77\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/subprocess.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, args, bufsize, executable, stdin, stdout, stderr, preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags, restore_signals, start_new_session, pass_fds, encoding, errors, text)\u001b[0m\n\u001b[1;32m    774\u001b[0m                                 \u001b[0merrread\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merrwrite\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 775\u001b[0;31m                                 restore_signals, start_new_session)\n\u001b[0m\u001b[1;32m    776\u001b[0m         \u001b[0;32mexcept\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/subprocess.py\u001b[0m in \u001b[0;36m_execute_child\u001b[0;34m(self, args, executable, preexec_fn, close_fds, pass_fds, cwd, env, startupinfo, creationflags, shell, p2cread, p2cwrite, c2pread, c2pwrite, errread, errwrite, restore_signals, start_new_session)\u001b[0m\n\u001b[1;32m   1521\u001b[0m                             \u001b[0merr_msg\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;34m': '\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mrepr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merr_filename\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1522\u001b[0;31m                     \u001b[0;32mraise\u001b[0m \u001b[0mchild_exception_type\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merrno_num\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr_msg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0merr_filename\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1523\u001b[0m                 \u001b[0;32mraise\u001b[0m \u001b[0mchild_exception_type\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merr_msg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '../chromedriver`': '../chromedriver`'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mWebDriverException\u001b[0m                        Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-10-deb689c90fba>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# 크롬 드라이브 실행\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mchrome\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'../chromedriver`'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mchrome\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'https://play.google.com/store/apps'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;31m# 검색 input box에 검색어 입력 후 검색 실행\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/webdriver.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, executable_path, port, options, service_args, desired_capabilities, service_log_path, chrome_options, keep_alive)\u001b[0m\n\u001b[1;32m     71\u001b[0m             \u001b[0mservice_args\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mservice_args\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     72\u001b[0m             log_path=service_log_path)\n\u001b[0;32m---> 73\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mservice\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     74\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     75\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.7/site-packages/selenium/webdriver/common/service.py\u001b[0m in \u001b[0;36mstart\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     81\u001b[0m                 raise WebDriverException(\n\u001b[1;32m     82\u001b[0m                     \"'%s' executable needs to be in PATH. %s\" % (\n\u001b[0;32m---> 83\u001b[0;31m                         os.path.basename(self.path), self.start_error_message)\n\u001b[0m\u001b[1;32m     84\u001b[0m                 )\n\u001b[1;32m     85\u001b[0m             \u001b[0;32melif\u001b[0m \u001b[0merr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0merrno\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0merrno\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mEACCES\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mWebDriverException\u001b[0m: Message: 'chromedriver`' executable needs to be in PATH. Please see https://sites.google.com/a/chromium.org/chromedriver/home\n"
     ]
    }
   ],
   "source": [
    "# 크롬 드라이브 실행\n",
    "chrome = webdriver.Chrome('../chromedriver`')\n",
    "chrome.get('https://play.google.com/store/apps')\n",
    "\n",
    "# 검색 input box에 검색어 입력 후 검색 실행\n",
    "#input_box = chrome.find_element_by_css_selector('#gbqfq')\n",
    "#input_box.send_keys('배달의명수')\n",
    "#input_box.submit() \n",
    "#time.sleep(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'chrome' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-9-f4951478a613>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# 검색 결과 중 첫 번째 앱 클릭\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mlink\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mchrome\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfind_element_by_css_selector\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'#fcxH9b > div.WpDbMd > c-wiz:nth-child(4) > div > div.N4FjMb > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div:nth-child(1) > c-wiz > div > div > div.RZEgze > div > div > div.bQVA0c > div > div > div.b8cIId.ReQCgd.Q9MA7b > a'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mlink\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclick\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m3\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'chrome' is not defined"
     ]
    }
   ],
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

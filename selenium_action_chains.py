{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.common.action_chains import ActionChains\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome('../chromedriver')\n",
    "url = 'https://google.com'\n",
    "driver.get(url)\n",
    "# driver.maximize_window() -> 크롬 창 가장 크게 만들어라"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "action = ActionChains(driver)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 로그인 창 id: gb_70\n",
    "driver.find_element_by_css_selector('#gb_70').click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# action chains를 활용하여 로그인하기\n",
    "# 아이디 입력 후 다음 버튼 클릭\n",
    "action.send_keys('woojiworld').perform()\n",
    "driver.find_element_by_css_selector('#identifierNext').click()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 비밀번호 입력 후 다음 버튼 클릭\n",
    "driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys('goodkris')\n",
    "driver.find_element_by_css_selector('#passwordNext').click()"
   ]
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

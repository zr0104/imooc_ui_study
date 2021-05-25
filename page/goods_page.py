# coding=utf-8
from base.find_element import FindElement
class GoodsPage(object):
    def __init__(self,driver):
        self.gp = FindElement()

    def get_goods_list(self):
        return self.gp.get_element("goods_list")

    def get_goods_search_input(self):
        return self.gp.get_element("goods_search_input")

    def get_goods_search_button(self):
        return self.gp.get_element("goods_search_button")

    def get_goods_search_laws(self):
        return self.gp.get_element("goods_search_laws")

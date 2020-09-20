from myBisect import bisect


class SortedListNoDubl:

    def __init__(self, init_list=None, ascending_order=True):
        self.__array = []
        self.__ascending_order = ascending_order

        if init_list is not None:
            self.add_unsorted_list(init_list)

    def add(self, ad_item, ignore_flag=False, low=0, high=None):
        if ad_item in self.__array:
            assert not ignore_flag, "item already in list"
            return

        ind = bisect(self.__array, ad_item, self.__ascending_order, low, high)
        self.__array.insert(ind, ad_item)

    def add_unsorted_list(self, ad_list, ignore_flag=False):
        for i in ad_list:
            self.add(i, ignore_flag)

    def merge_with_sorted_list(self, ad_list, ignore_flag=True):
        low = 0
        for ad_item in ad_list:
            ind = bisect(self.__array, ad_item, self.__ascending_order, low)
            low = ind
            if self.__array[ind] == ad_item:
                assert not ignore_flag, "item already in list"
            else:
                self.__array.insert(ind, ad_item)

    def remove(self, index):
        del self.__array[index]

    def clear(self):
        self.__array = []

    def __repr__(self):
        return str(self.__array)

    def __getitem__(self, key):
        return self.__array[key]

#就尼玛离谱，超时怎么都过不了  9 / 18 个通过测试用例   11 / 18 个通过测试用例
class StockPrice:
    #一支股票价格的数据流
    def __init__(self):
        self.price_info=dict()
        self.newtimestamp=[]
        self.maxprice=[]
        self.minprice=[]


    #超时，考虑
    def update(self, timestamp: int, price: int) -> None:
        self.price_info[timestamp]=price
        #不管有无，都直接赋值即可
        #update时就存储好最大值及最小值还有最新的值
        if not self.maxprice:
            self.maxprice=[timestamp,price]
        elif price>=self.maxprice[-1]:
            self.maxprice=[timestamp,price]
        elif timestamp==self.maxprice[0]:
            self.maxprice=[timestamp,price]
            for key,value in self.price_info.items():
                if value>self.maxprice[-1]:
                    self.maxprice=[key,value]
        #update时就存储好最大值及最小值
        if not self.minprice:
            self.minprice=[timestamp,price]
        elif price<=self.minprice[-1]:
            self.minprice=[timestamp,price]
        elif timestamp==self.minprice[0]:
            self.minprice=[timestamp,price]
            for key,value in self.price_info.items():
                if value<self.minprice[-1]:
                    self.minprice=[key,value]
        if not self.newtimestamp:
            self.newtimestamp=[timestamp,price]
        elif timestamp>self.newtimestamp[0]:
            self.newtimestamp=[timestamp,price]

    def current(self) -> int:
        return self.newtimestamp[-1]

    def maximum(self) -> int:
        return self.maxprice[-1]


    def minimum(self) -> int:
        return self.minprice[-1]



   
# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


#以下为别人的答案
# 方法一：哈希表 + 有序集合
# 时间复杂度：
# upgrade(): O(nlogn)
# current(): O(1)
# maximum(): O(1)
# minimum(): O(1)
# 空间复杂度：O(n)
"""from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.timePrice = defaultdict(int)  # 时间价格对应表
        self.price = SortedList()          # 价格表
        self.lastPrice = [-1, -1]          # 最新价格

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.timePrice:
            self.price.discard(self.timePrice[timestamp])
        self.price.add(price)
        self.timePrice[timestamp] = price
        if timestamp >= self.lastPrice[0]:
            self.lastPrice = [timestamp, price]       

    def current(self) -> int:
        return self.lastPrice[1]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]"""


# 方法二：哈希表 + 2个优先队列
# 时间复杂度：
# upgrade(): O()
# current(): O()
# maximum(): O()
# minimum(): O()
# 空间复杂度：O(n)
import heapq
class StockPrice:
  
    def __init__(self):
        self.timePrice = defaultdict(int)
        self.maxPrice = []
        self.minPrice = []
        self.lastPrice = [-1, -1]

    def update(self, timestamp: int, price: int) -> None:
        heapq.heappush(self.minPrice, (price, timestamp))
        heapq.heappush(self.maxPrice, (-price, timestamp))
        self.timePrice[timestamp] = price
        if timestamp >= self.lastPrice[0]:
            self.lastPrice = [timestamp, price]      

    def current(self) -> int:
        return self.lastPrice[1]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxPrice[0]
            if -price == self.timePrice[timestamp]:
                return -price
            heappop(self.maxPrice)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minPrice[0]
            if price == self.timePrice[timestamp]:
                return price
            heappop(self.minPrice)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
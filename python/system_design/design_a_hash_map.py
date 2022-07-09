'''
Design a hash map

(Key, 欲找尋的資料) -> hash function -> (Value, 對應的伺服器或資料所在地)

Hashing: 實現資料與服務節點的映射關係
    - 在分散式系統中，我們可以將待處理的資料當作 Key，最後找到的 Value 就是資料將要被分送到的服務節點。
    - 同樣地，Open-Falcon 監控系統當中，我們也可以把一台機器上的一個被監控項目的資料當作一個 Key，最後找到的 Value 就是此被監控項目的資料所要分送到的服務節點。

Consistent Hashing 演算法:
    - 當服務節點增加或減少的時候，Key 與 Value 的映射關係變動較小。
    - 如果因為服務節點的增減，導致系統將大部份被監控項目的資料送往和原本不同的服務節點，那麼便會在增加或減少服務節點的當下產生問題：對於同一個被監控項目，增加或減少服務節點之前與之後的資料，並不是給同一個服務節點處理。
    - 而 Consistent Hashing 的優點就是它能盡量保持大部份的資料都能送往和原本相同的服務節點。我們以數字來舉例說明 Consistent Hashing 的運作方式比其他的方式還要適合的原因。

Reference:
    - https://github.com/donnemartin/system-design-primer#how-to-approach-a-system-design-interview-question
    - https://medium.com/@chyeh/consistent-hashing-algorithm-%E6%87%89%E7%94%A8%E6%83%85%E5%A2%83-%E5%8E%9F%E7%90%86%E8%88%87%E5%AF%A6%E4%BD%9C%E7%AF%84%E4%BE%8B-41fd16ad334a
    - https://zhuanlan.zhihu.com/p/135827801
'''

class Item(object):    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def get_key(self):
        return self.key


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def _hash_function(self, key):
        return key % self.size
    
    def set(self, key, value):
        hash_index = self._hash_function(key)
        
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))
    
    def get(self, key):
        pass
    
    def remove(self, key):
        pass
        
        

if __name__ == '__main__':
    
    h1 = HashTable(3)
    h1.set(1, 19)
    h1.set(2, 150)
    h1.set(2, 183)
    print(h1.size)
    print(f'size: {h1.table[0]}')
    print(f'table: {h1.table[1][0].get_key()}')
    print(type(h1.table[1][0].get_key()))
    print(h1.table[2])
    
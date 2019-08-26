class Stock(object):
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        self.min_peak_index = []
        self.profit = 0
        self.max_ps = []

    def find_peak_min(self):
        for i in range(len(self.arr)):
            if i == 0 and self.arr[1] > self.arr[0]:
                self.min_peak_index.append(0)

            elif i == len(self.arr) - 1 and self.arr[len(self.arr)-1] < self.arr[len(self.arr)-2]:
                self.min_peak_index.append(len(self.arr) - 1)
            
            else:
                if self.arr[i] < self.arr[i-1] and self.arr[i] < self.arr[i+1]:
                    self.min_peak_index.append(i)

    def find_max_profit(self, arr):
        for i in range(len(self.min_peak_index)):
            
            max_ps.append(max(self.arr[self.min_peak_index[i]:self.min_peak_index[i+1]]) - self.min_peak_index[i])
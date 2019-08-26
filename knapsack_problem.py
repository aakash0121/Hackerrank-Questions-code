class Knapsack(object):
    def __init__(self, val, wt, w):
        self.value = val
        self.wt = wt
        self.w = w
        self.n = len(val)
    
    def find_max_val(self):
        k = [[0 for x in range(self.w+1)] for y in range(self.n+1)]

        for i in range(self.n+1):
            for w in range(self.w+1):
                if i == 0 or w == 0:
                    k[i][w] = 0
                
                elif self.wt[i-1] <= w:
                    k[i][w] =  max(self.value[i-1]+k[i-1][w-self.wt[i-1]], k[i-1][w])
                else:
                    k[i][w] = k[i-1][w]
        
        return k[self.n][self.w]

if __name__ == "__main__":
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    k = Knapsack(val, wt, W)
    print(k.find_max_val())
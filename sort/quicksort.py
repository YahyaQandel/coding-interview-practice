class QuickSort():
    def sort(self,arr):
        if len(arr) > 1:
            pvt = arr[0]
            left = []
            right = []
            for i in range(1,len(arr)):
                if arr[i] > pvt:
                    right.append(arr[i])
                else:
                    left.append(arr[i])
            return self.sort(left) + [pvt] + self.sort(right)
        return arr
    
    def sort_less_storage(self,arr):
        if len(arr) > 1:
            pvt = arr[0]
            i = 1
            j = len(arr) - 1
            while i <= j:
                if arr[i] > pvt and arr[j] < pvt:
                    arr[i],arr[j] = arr[j],arr[i]
                    i+=1
                    j-=1
                    continue
                if arr[i] <= pvt:
                    i+=1
                if arr[j] >= pvt:
                    j-=1
            arr[j],arr[0] = arr[0],arr[j]
            return self.sort_less_storage(arr[:j]) + [pvt] + self.sort_less_storage(arr[j+1:])
        return arr
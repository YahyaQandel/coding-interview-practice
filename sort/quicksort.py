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
class Sorting:
    def mergesort(self, arr, l, h):
        if l >= h:
            return
        mid = l + (h - l) // 2
        self.mergesort(arr, l, mid)
        self.mergesort(arr, mid + 1, h)
        self.merge(arr, l, mid, h)

    def merge(self, arr, l, mid, h):
        temp = []
        i = l
        j = mid + 1
        while i <= mid and j <= h:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= h:
            temp.append(arr[j])
            j += 1
        k = 0
        while k < len(temp):
            arr[l + k] = temp[k]
            k += 1

    def sort(self, nums):
        arr = list(nums)
        if len(arr) > 0:
            self.mergesort(arr, 0, len(arr) - 1)
        return arr


class Comparison:
    def compare(self, nums):
        if len(nums) == 0:
            return None
        max_val = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] > max_val:
                max_val = nums[i]
            i += 1
        return max_val


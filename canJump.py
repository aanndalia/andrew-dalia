    def canJumpRecurse(self, nums, idx=0):
        if idx < 0 or idx >= len(nums):
            return False
        
        if idx == len(nums) - 1:
            return True
        
        maxJump=nums[idx]
        if maxJump <= 0:
            return False
        
        anySuccess = False
        for i in range(1, nums[idx]+1):
            anySuccess = anySuccess or self.canJumpRecurse(nums, idx + i)
            
        return anySuccess
    
    def canJumpRecurseDP(self, nums, idx=0, cache = {}):
        if idx < 0 or idx >= len(nums):
            return False
        
        if idx == len(nums) - 1:
            return True
        
        maxJump=nums[idx]
        if maxJump <= 0:
            return False
        
        if idx in cache:
            return cache[idx]
        
        anySuccess = False
        for i in range(1, nums[idx]+1):
            anySuccess = anySuccess or self.canJumpRecurseDP(nums, idx + i, cache)
        
        cache[idx] = anySuccess
        print cache
        return anySuccess
            
        
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == None or len(nums) == 0:
            return False
        
        return self.canJumpRecurseDP(nums)

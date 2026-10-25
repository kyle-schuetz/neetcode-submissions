class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions = {}

        for i in range(len(nums)):
            if nums[i] in positions:
                positions[nums[i]].append(i)
            else:
                positions[nums[i]] = [i]

        for i in range(len(nums)):
            # addende two is the target minus current number
            add_two = target - nums[i]

            # check to see if this value is the current value and see if we have seen this value more than once
            if add_two == nums[i] and len(positions[add_two]) > 1:
                return positions[add_two][0:2]

            if add_two != nums[i] and add_two in positions:
                pos = positions[add_two][0]

                if pos > i:
                    return [i, pos]
                else:
                    return [pos, i]
    
            
            
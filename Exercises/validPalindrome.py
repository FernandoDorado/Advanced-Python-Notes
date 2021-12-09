# Return true given a string s if the s can be palindromic after removing at most one character from the string.

class Solution:
    def validPalindrome(self, s: str) -> bool:
    
    
        idx_left = 0
        idx_right = len(s) - 1

        if s == s[::-1]: return True 
        
        if len(s) == 3:
            idx = 1 
            s_2 = s[0:idx:] + s[idx+1::]
            s_2_inv = s_2[::-1]

            if s_2 == s_2_inv: return True

        while idx_left < idx_right:

            if s[idx_left] != s[idx_right]: # In case of first character same as the last one
                
                # Then, we need to remove the first item of the substring 
                s_new_init = s[idx_left+1:idx_right+1]
                # Or the last chracter
                s_new_final = s[idx_left:idx_right] 

                if s_new_init == s_new_init[::-1] or s_new_final == s_new_final[::-1]:
                    return True
                else: 
                    return False
            
            # Update idx
            idx_left = idx_left + 1
            idx_right = idx_right - 1 

Sol = Solution()
print(Sol.validPalindrome("bddb"))
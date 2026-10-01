class Solution:
    def isPalindrome(self, s: str) -> bool:
        al=''.join(ch for ch in s if ch.isalnum())
        al=al.lower()
      
        return al==al[::-1]

        
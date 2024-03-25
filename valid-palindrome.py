class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''.join(letter for letter in s if letter.isalnum())
        if st.lower() == st.lower()[::-1]:
            return True
        else:
            return False
        
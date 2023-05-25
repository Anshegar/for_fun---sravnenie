class Solution():

    def __init__(self, magazine: str = None, ransomNote: str = None ):
        self.ransomNote = ransomNote
        self.magazine = magazine

    def canConstruct(self):

        char_count = {}
        magazine = self.magazine.lower()
        ransomNote = self.ransomNote.lower()
        
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Проверяем, можно ли составить строку ransomNote из символов строки magazine
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True




magazine = 'a'
ransomNote = 'b'


solution = Solution(magazine,ransomNote)
print(solution.canConstruct())
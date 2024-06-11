class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        t = set()
        
        for word in words:
            tr = ''
            for char in word:
                tr += morse_code[ord(char) - ord('a')]
            t.add(tr)
        
        return len(t)
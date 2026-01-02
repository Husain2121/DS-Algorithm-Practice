    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
       A,B = len(word1), len(word2)
       a,b = 0,0
       word = word1
       s=[]
       while a<A and b<B:
          if word == word1:
            s += word1[a]
            a +=1
            word = word2
          if word == word2:
            s += word2[b]
            b += 1
            word = word1
       while a <A:
            s += word1[a]
            a +=1
       while b <B:
            s += word2[b]
            b +=1
        

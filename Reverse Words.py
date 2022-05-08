from cgitb import reset


class Solution:
    def solve(self, sentence):
        m = []
        start = 0
        end = 0
        sentence = sentence + " "
        for letter in sentence:
            if(letter == " "):
                m.append(sentence[start:end+1])
                start = end + 1
                end = end
            end = end + 1
        m.append(sentence[start:])
        reversedList = list(reversed(m))
        print("".join(reversedList))

        return "".join(reversedList)

                
                

solution = Solution()
solution.solve("hello there my friend")
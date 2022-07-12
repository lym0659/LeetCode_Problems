class Solution:
    def isValid(self, s: str) -> bool:
        checklist = []
        bracket = list(s)
        
        while bracket:
            if len(checklist) == 0:
                top = 0
            else:
                top = checklist[-1]
            
            checklist.append(bracket.pop())
            
            if top == ")" and checklist[-1] == "(":
                checklist.pop()
                checklist.pop()
            elif top == "]" and checklist[-1] == "[" :
                checklist.pop()
                checklist.pop()
            elif top == "}" and checklist[-1] == "{" :
                checklist.pop()
                checklist.pop()
                
        if len(checklist) == 0:
            
            return True
        else: return False
            
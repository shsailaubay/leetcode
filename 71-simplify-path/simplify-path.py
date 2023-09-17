class Solution:
    def simplifyPath(self, path: str) -> str:
        pull = []
        for d in path.split('/'):
            if d == '' or d == '.':
                continue
            elif d == '..':
                if len(pull) > 0:
                    pull.pop()
                continue
            pull.append(d)
        
        return '/' + ('/').join(pull)
        
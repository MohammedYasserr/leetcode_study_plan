from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
        
        # Handling this Edge case where we have not input
        if not strs : return ""

        prefix = strs[0] 
        # print(prefix)
        for s in strs[1:]: 
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                print(prefix)
                # In case there is no common prefix return empty strings...
                if not prefix:
                    return ""

        return prefix

longestCommonPrefix(["flowers" , "flights", "fly"])
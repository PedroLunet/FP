def isomorphic(astring1, astring2):
    if len(astring1) != len(astring2):
        return f"'{astring1}' and '{astring2}' are not isomorphic"
    
    def map_chars(s1, s2):
        char_map = {}
        for i in range(len(s1)):
            if s1[i] not in char_map:
                char_map[s1[i]] = s2[i]
            elif char_map[s1[i]] != s2[i]:
                return None
        return char_map
    
    map1 = map_chars(astring1, astring2)
    map2 = map_chars(astring2, astring1)
    
    if map1 is None or map2 is None:
        return f"'{astring1}' and '{astring2}' are not isomorphic"
    else:
        return f"'{astring1}' and '{astring2}' are isomorphic"


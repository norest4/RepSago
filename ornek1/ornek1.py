def countMatches(self, items, ruleKey, ruleValue):
    """
    :type items: List[List[str]]
    :type ruleKey: str
    :type ruleValue: str
    :rtype: int
    """

items1 = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color", ruleValue = "silver"
# expected output 1


items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
# ruleKey = "type", ruleValue = "phone"
# expected output 2
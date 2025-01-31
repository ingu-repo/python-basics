# 集合演算
def group_operator():

    # group variable NOT list/tuple/map
    nums1 = {1, 2, 3, 4}
    nums2 = {3, 4, 5, 6}
    print ("nums1:", nums1)
    print ("nums2:", nums2)

    # 和集合: "|" : take w/o duplicated
    print (nums1 | nums2)
    # 積集合: "&" : take only duplicated ones
    print (nums1 & nums2)
    # 差集合: "-" : delete duplication from left
    print (nums1 - nums2)
    # 対称差集合: "^" : remove duplicated ones
    print (nums1 ^ nums2)


group_operator()


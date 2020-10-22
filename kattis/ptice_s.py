adrian = 'ABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABCABC'
bruno = 'BABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABCBABC' 
goran = 'CCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABBCCAABB'
no_q = int(input())
if no_q <= 100:
  inp = input()
  if len(inp) == no_q:
    ad = 0
    bru = 0
    gor = 0
    dict_set = {}
    for i in range(len(inp)):
      if inp[i] == adrian [i]:
        # print('adrian',i)
        ad += 1
      if inp[i] == bruno [i]:
        # print('bruno',i)
        bru += 1
      if inp[i] == goran [i]:
        # print('gordan',i)
        gor += 1
    dict_set ['Adrian'] = ad
    dict_set ['Bruno'] = bru
    dict_set ['Goran'] = gor
    max_match = max(ad,max(bru,gor))
    print(max_match)
    # print(dict_set)
    for name,mark in dict_set.items():
      if max_match == mark:
        print(name)


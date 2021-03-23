'''
From Leetcode Daily Challenge
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/

Question in summary:
Given a wordlist and a query, see if the words exists in wordlist.
Considerations: Case sensitive, vowel masking, position determining.

Lessons learned:
- Iterate too many times so that runtime error.
- Generate list again and again for comparison, when dictionary could have come in handy.
- Optimization point: 
    - use of dictionary
    - masking vowels
    - generating list with ('consonants', positions of vowels) instead of generating two lists.

'''



#wordlist = ["v","t","k","g","n","k","u","h","m","p"]
#queries = ["n","g","k","q","m","h","x","t","p","p"]

#wordlist = ["KiTe","kite","hare","Hare"]
#queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

#wordlist = ["wg","uo","as","kv","ra","mw","gi","we","og","zu"]
#queries = ["AS","in","yc","kv","mw","ov","lc","os","wm","Mw"]

vowels = ["a","e","i","o","u"]
qvwl_lst = []
qcst_lst = []
wrdvwl_lst = []
wrdcst_lst = []
final_lst = []

for q in queries:
    print ("------------------")
    print ("q is ", q)
    if q in wordlist:
        final_lst.append(q)
        #print ("Exact match")
    elif q.lower() in wordlist:
        for wrd in wordlist:
            if q.lower() == wrd.lower() and q != wrd:
                final_lst.append(wrd)
                #print ("word match")
                break
    
    else:
        for cnt0, i in enumerate(q):
            #print (i)
            if i.lower() in vowels:
                qvwl_lst.append(cnt0)
                qcst_lst.append("")
            else:
                qcst_lst.append(i.lower())
        for cnt, wrdd in enumerate(wordlist):
            #print (cnt, len(wordlist), "query = ", q, ", wordlist = ", wrdd)
            for cnt2, j in enumerate(wrdd):
                if j.lower() in vowels:
                    wrdvwl_lst.append(cnt2)
                    wrdcst_lst.append("")
                else:
                    wrdcst_lst.append(j.lower())
            print ("Queries vowel and const list:", qvwl_lst, qcst_lst)
            print ("Wordlist vowel and const list:", wrdvwl_lst, wrdcst_lst)
            if qvwl_lst == wrdvwl_lst and wrdvwl_lst != [] and qcst_lst == wrdcst_lst:
                final_lst.append(wrdd)
                print ("vowel list matched")
                break
            elif cnt+1 ==len(wordlist):
                final_lst.append("")
                print ("no match")
            wrdvwl_lst = []
            wrdcst_lst = []
        qvwl_lst = []
        qcst_lst = []
     
print (final_lst)

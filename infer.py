#test_point = "i have been there and got nothing same as my life.i have a gun.im not on a ledge or something but i have a gun on my lap."
test_point = '''

I have no willpower. I am eating like a pig and I hate it. I am ruining my health. Everybody takes advantage of me because I'm weak.
'''  

from PKiL import ProKnow

pk1 = ProKnow()
pk1.process_knowledge('cssrs.txt','cssrs_annotate.txt')

#test_point = input("Enter test point: ")

label = pk1.evaluate_pk(test_point,explanation=True)

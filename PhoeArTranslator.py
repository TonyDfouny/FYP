from ar_corrector.corrector import Corrector

corr = Corrector()

##########CORRECTORR##############


#####CORRECT WORD SPELLING######
corr.spell_correct('بختب') # return 5 corrections with top frequencies
# [('بكتب', 61), ('برتب', 22), ('بختم', 21), ('بختي', 9), ('بخت', 7)]

corr.spell_correct('بختب', 2) # return 2 corrections with top frequencies
# [('بكتب', 61), ('برتب', 22),]

corr.spell_correct('بختب', 1) # return 1 correction with top frequency
# [('بكتب', 61)]

corr.spell_correct('لتمشتلميتلكب', 4) # return the same word
# لتمشتلميتلكب

corr.spell_correct('من') # return true
# True


#####CONTEXT CORRECTION#####
sent = 'أكدت قواءص التمذد في تشاد أنها تواضضل طريقها للعاحمة'
print(corr.contextual_correct(sent))
#أكدت قوات التمرد في تشاد أنها تواصل طريقها للعاصمة

sent = 'اتتنتهى حدث آبل المنتظو بالإعلاخ عن مموعة من المنتجات'
print(corr.contextual_correct(sent))
#انتهى حدث آبل المنتظر الإعلان عن مجموعة من المنتجات
from Parser import Parser
from ar_corrector.corrector import Corrector
corr = Corrector()


parser = Parser(model_path=r"C:\Users\tony_\Downloads\stanford-corenlp-4.2.0-models-arabic\edu\stanford\nlp\models\lexparser\arabicFactored.ser.gz",
                path_to_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser.jar",
                path_to_models_jar=r"C:\Users\tony_\Downloads\stanford-parser-4.2.0\stanford-parser-full-2020-11-17\stanford-parser-4.2.0-models.jar")

result=parser.parse_sentence(u'أكلت أسد')

print(result)
#parser.tree_print()
#parser.tree_draw()

# result=parser.parse_sentence(u'أنا أقوم ببناء منزل')
# print(result)
# parser.tree_print()
# parser.tree_draw()

###########CORRECTORR##############


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
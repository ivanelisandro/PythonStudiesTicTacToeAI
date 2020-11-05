dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

sentence = input()
words = sentence.split(" ")
incorrect = [word for word in words if not dictionary.__contains__(word)]

if len(incorrect) > 0:
    print("\n".join(incorrect))
else:
    print("OK")

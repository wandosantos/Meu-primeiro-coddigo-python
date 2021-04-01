print("="*40)


trabalhoDeLabototrio = int(input('Digite a nota do trabalho laboratorio ='))
avaliacaoSemestral = int(input('Digite a nota da avaliação semestral ='))
exameFinal = int(input('Digite a nota do Exame final ='))
media = (trabalhoDeLabototrio * 2 + avaliacaoSemestral * 3 + exameFinal * 5) / 10

if media >= 8 and media < 10:
    print('Conceito A!',media)
if media >= 7 and media < 8:
    print('Conceito B',media)
if media >= 6 and media < 7:
    print('Conceito C',media)
if media >= 5 and media < 6:
    print('Conceito D',media)
if media >= 0.0 and media < 5:
    print('Conceito E',media)
print("="*40)
from pathlib import Path

rasta = Path.cwd()
rasta2 = rasta / Path('spam.txt')

rasta2.write_text('Jaggi is good guy')
# print(rasta2.read_text())

rasta3 = open(rasta2,'w')

rasta3.write('hello bye;')
rasta3.close()
rasta3 = open(rasta2)
print(rasta3.read())

rasta3.close()

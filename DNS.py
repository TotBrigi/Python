hair_color = {'black':'CCAGCAATCGC', 'brown':'GCCAGTGCCG', 'blonde':'TTAGCTATCGC'}
face_shape = {'square':'GCCACGG', 'round':'ACCACAA', 'oval':'AGGCCTCA'}
eye_color = {'blue':'TTGTGGTGGC', 'green':'GGGAGGTGGC', 'brown':'AAGTAGTGAC'}
gender = {'female':'TGAAGGACCTTC', 'male':'TGCAGGAACTTC'}
race = {'white':'AAAACCTCA','black':'CGACTACAG', 'asian':'CGCGGGCCG'}

eva = {'gender':'female', 'race':'white', 'hair_color':'blonde', 'eye_color':'blue', 'face_shape':'oval'}
larisa = {'gender':'female', 'race':'white', 'hair_color':'brown', 'eye_color':'brown', 'face_shape':'oval'}
matej = {'gender':'male', 'race':'white', 'hair_color':'black', 'eye_color':'blue', 'face_shape':'oval'}
miha = {'gender':'male', 'race':'white', 'hair_color':'brown', 'eye_color':'green', 'face_shape':'square'}

while True:
    if eva['gender'] == 'female':
        eva['gender'] = gender['female']
        continue
    elif eva['race'] == 'white':
        eva['race'] = race['white']
        continue
    elif eva['hair_color'] == 'blonde':
        eva['hair_color'] = hair_color['blonde']
        continue
    elif eva['eye_color'] == 'blue':
        eva['eye_color'] = eye_color['blue']
        continue
    elif eva['face_shape'] == 'oval':
        eva['face_shape'] = face_shape['oval']
    else:
        eva = eva.values()
        eva = ''.join(eva)

        print eva
        break

while larisa:
    if larisa['gender'] == 'female':
        larisa['gender'] = gender['female']
        continue
    elif larisa['race'] == 'white':
        larisa['race'] = race['white']
        continue
    elif larisa['hair_color'] == 'brown':
        larisa['hair_color'] = hair_color['brown']
        continue
    elif larisa['eye_color'] == 'brown':
        larisa['eye_color'] = eye_color['brown']
        continue
    elif larisa['face_shape'] == 'oval':
        larisa['face_shape'] = face_shape['oval']
        continue
    else:
        larisa = larisa.values()
        larisa = ''.join(larisa)

        print larisa
        break


while matej:
    if matej['gender'] == 'male':
        matej['gender'] = gender['male']
        continue
    elif matej['race'] == 'white':
        matej['race'] = race['white']
        continue
    elif matej['hair_color'] == 'black':
        matej['hair_color'] = hair_color['black']
        continue
    elif matej['eye_color'] == 'blue':
        matej['eye_color'] = eye_color['blue']
        continue
    elif matej['face_shape'] == 'oval':
        matej['face_shape'] = face_shape['oval']
        continue
    else:
        matej = matej.values()

        matej = ''.join(matej)

        print matej
        break

while miha:
    if miha['gender'] == 'male':
        miha['gender'] = gender['male']
        continue
    elif miha['race'] == 'white':
        miha['race'] = race['white']
        continue
    elif miha['hair_color'] == 'brown':
        miha['hair_color'] = hair_color['brown']
        continue
    elif miha['eye_color'] == 'green':
        miha['eye_color'] = eye_color['green']
        continue
    elif miha['face_shape'] == 'square':
        miha['face_shape'] = face_shape['square']
        continue
    else:
        miha = miha.values()

        miha = ''.join(miha)

        print miha
        break


fo=open('dna.txt', 'r')
dna=fo.readline()
print dna
print eva.count(dna)
print larisa.count(dna)
print matej.count(dna)
print miha.count(dna)
fo.close()



#blocos de codigos
#if / elif / else

#para 3 ou mais possibilidades para condições, usar o elif no meio

entrada = input('Do you want to start? Type yes or no:  ')

if entrada == 'yes':
    print('welcome to the system!!')

elif entrada == 'no':
    print('You quit the system!!')

else:
    print('Error... restart the programa!')
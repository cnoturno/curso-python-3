lockdown = True
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(f'O status é: {status}')

esta_chovendo = True

print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[esta_chovendo])
print('Hoje estou com as roupas ' + ('molhadas.' if esta_chovendo else 'secas.'))
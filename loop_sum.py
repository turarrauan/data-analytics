twitter = [
    87.3,
    150,
    0.0,
    2270.0,
    264.0,
    565.0,
    834.0,
    432.0,
    0.0,
    478.0,
    198.0,
    654.0,
    98.7,
    445.0,
    1080.0,
    697.0,
    227.0,
    0.0,
    150.0,
    932.0,
]
twitter_total = 24500

selected_total = 0
# < напишите код здесь >
for element in twitter:
    selected_total += element

selected_part = selected_total / twitter_total
print('Доля выбранных эмодзи в Твиттере: {:.1%}'.format(selected_part))

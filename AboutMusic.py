import matplotlib.pyplot as plt

services = ['Яндекс.Музыка', 'Музыка ВКонтакте', 'YouTube Music', 'Музыка в Одноклассниках', 'МТС Музыка', 'SoundCloud']

market_shares = [73, 67, 37, 29, 11, 6]

plt.figure(figsize=(12, 8))
bars = plt.bar(services, market_shares, color=plt.cm.Pastel1(range(len(services))))

plt.xticks(rotation=45, ha='right', fontsize=10)

plt.title('Доля стриминговых сервисов в России во втором квартале 2022 года')
plt.xlabel('Сервис')
plt.ylabel('Доля рынка (%)')

plt.tight_layout()
plt.show()

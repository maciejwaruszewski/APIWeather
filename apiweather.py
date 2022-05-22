from requests import get
from json import loads

miasta = ['Białystok', 'Bielsko Biała', 'Chojnice', 'Częstochowa', 'Elbląg', 'Gdańsk', 'Gorzów', 'Hel', 'Jelenia Góra',
        'Kalisz', 'Kasprowy Wierch', 'Katowice', 'Kętrzyn', 'Kielce', 'Kłodzko', 'Koło', 'Kołobrzeg', 'Koszalin',
        'Kozienice', 'Kraków', 'Krosno', 'Legnica', 'Lesko', 'Leszno', 'Lębork', 'Lublin', 'Łeba', 'Łódź',
        'Mikołajki', 'Mława', 'Nowy Sącz', 'Olsztyn', 'Opole', 'Ostrołęka', 'Piła', 'Platforma', 'Płock', 'Poznań',
        'Przemyśl', 'Racibórz', 'Resko', 'Rzeszów', 'Sandomierz', 'Siedlce', 'Słubice', 'Sulejów', 'Suwałki',
        'Szczecin', 'Szczecinek', 'Śnieżka', 'Świnoujście', 'Tarnów', 'Terespol', 'Toruń', 'Ustka', 'Warszawa',
        'Wieluń', 'Włodawa', 'Wrocław', 'Zakopane', 'Zamość', 'Zielona Góra']

miasto = input('Wprowadź miasto:')

if miasto in miasta:
    print(f'Pogoda dla miasta Twojego miasta poniżej:')
else:
    miasto = input('Nie ma takiego miasta w bazie danych, spróbuj ponownie:')


def main():
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Prędkość wiatru', 'Suma opadów', 'Ciśnienie']]

    for row in loads(response.text):
        if row['stacja'] in miasto:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['predkosc_wiatru'],
                row['suma_opadu'],
                row['cisnienie']
            ])

    for i in range(1, len(rows)):
        print('\n'.join(rows[i]))

if __name__ == '__main__':
    main()

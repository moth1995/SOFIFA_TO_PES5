from bs4 import BeautifulSoup

def conseguir_jugadores(equipo,session):
    web_opt='?hl=en-US&attr=classic&layout=new&units=mks'
    page = session.get('https://sofifa.com'+equipo+web_opt,headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    #print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    nombre_equipo=soup.find('h1',attrs={'class':'ellipsis'}).text
    jugadores_table = soup.find_all('table',attrs={'class':'table table-hover persist-area'})[0].find('tbody').find_all('tr')
    #para debuguear
    #print(jugadores_table[0].find_all('td',attrs={'class':'col-name'})[0].find('a').get('href'))
    links=[jugadores_table[x].find_all('td',attrs={'class':'col-name'})[0].find('a').get('href') for x in range(len(jugadores_table))]
    return links,nombre_equipo
#equipo = 'https://sofifa.com/team/241/fc-barcelona/'
#print(conseguir_jugadores(equipo))

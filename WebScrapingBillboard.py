import requests
from bs4 import BeautifulSoup
import sqlite3
import argparse

def database(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("CREATE TABLE Billboard200 (ThisWeekRank TEXT , Name TEXT, Artist TEXT,LastWeekRank TEXT, PeakRank TEXT, Duration TEXT )" )
    conn.close()

def upload(info,dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("INSERT INTO Billboard200 VALUES(?,?,?,?,?,?)",info)
    conn.commit()
    conn.close()
    
dbname = 'BillboardAlbum200.db'

database(dbname)

billboard200_url = "https://www.billboard.com/charts/billboard-200"


url = requests.get (billboard200_url)
soup = BeautifulSoup (url.content,'html.parser')  
albums200 = soup.find_all ("button", {"class": "chart-element__wrapper"})
for album in albums200 :
    albums = {}
    albums ["ThisWeekRank"] = album.find ("span", {"class" : "chart-element__rank__number"}).text
    albums ["Name"] = album.find ("span", {"class" : "chart-element__information__song"}).text
    albums ["Artist"] = album.find ("span", {"class" : "chart-element__information__artist"}).text
    albums ["LastWeekRank"] = album.find ("div", {"class" : "chart-element__meta text--last"})
    if albums ["LastWeekRank"] != None:
        albums ["LastWeekRank"]=albums ["LastWeekRank"].text
    else:
        albums ["LastWeekRank"] = None
    albums ["PeakRank"] = album.find ("div", {"class" : "chart-element__meta text--peek"})
    if albums ["PeakRank"] != None:
        albums ["PeakRank"]=albums ["PeakRank"].text
    else:
        albums ["PeakRank"] = None
    albums ["Duration"] = album.find ("div", {"class" : "chart-element__meta text--week"})
    if albums ["Duration"] != None:
        albums ["Duration"]=albums ["Duration"].text
    else:
        albums ["Duration"] = None

    
    information = tuple(albums.values())
    upload (information,dbname)


import sqlite3
conn  = sqlite3.connect ('Billboard.db')
cur = conn.cursor ()
x = cur.execute ("SELECT * FROM Billboard200")

for i in x :
    print (i)
    
conn.commit ()
conn.close ()


"""

OUTPUT :

('1', 'My Turn', 'Lil Baby', None, None, None)
('2', 'Chromatica', 'Lady Gaga', None, None, None)
('3', 'BLAME IT ON BABY', 'DaBaby', None, None, None)
('4', "Hollywood's Bleeding", 'Post Malone', None, None, None)
('5', 'Dark Lane Demo Tapes', 'Drake', None, None, None)
('6', 'High Off Life', 'Future', None, None, None)
('7', 'Wunna', 'Gunna', None, None, None)
('8', 'Eternal Atake', 'Lil Uzi Vert', None, None, None)
('9', 'The GOAT', 'Polo G', None, None, None)
('10', 'After Hours', 'The Weeknd', None, None, None)
('11', 'Fine Line', 'Harry Styles', None, None, None)
('12', 'YHLQMDLG', 'Bad Bunny', None, None, None)
('13', 'Please Excuse Me For Being Antisocial', 'Roddy Ricch', None, None, None)
('14', 'NCT #127: Neo Zone, The 2nd Album', 'NCT 127', None, None, None)
('15', 'What You See Is What You Get', 'Luke Combs', None, None, None)
('16', 'Ungodly Hour', 'Chloe X Halle', None, None, None)
('17', 'When We All Fall Asleep, Where Do We Go?', 'Billie Eilish', None, None, None)
('18', 'Suga', 'Megan Thee Stallion', None, None, None)
('19', "This One's For You", 'Luke Combs', None, None, None)
('20', 'If I Know Me', 'Morgan Wallen', None, None, None)
('21', 'Meet The Woo, V.2', 'Pop Smoke', None, None, None)
('22', 'Goodbye & Good Riddance', 'Juice WRLD', None, None, None)
('23', 'Future Nostalgia', 'Dua Lipa', None, None, None)
('24', 'Greatest Hits', 'Queen', None, None, None)
('25', 'beerbongs & bentleys', 'Post Malone', None, None, None)
('26', 'ASTROWORLD', 'Travis Scott', None, None, None)
('27', 'Divinely Uninspired To A Hellish Extent', 'Lewis Capaldi', None, None, None)
('28', 'Emmanuel', 'Anuel AA', None, None, None)
('29', 'Hot Pink', 'Doja Cat', None, None, None)
('30', 'Pray 4 Love', 'Rod Wave', None, None, None)
('31', 'Chilombo', 'Jhene Aiko', None, None, None)
('32', 'Over It', 'Summer Walker', None, None, None)
('33', 'Changes', 'Justin Bieber', None, None, None)
('34', 'SOUTHSIDE', 'Sam Hunt', None, None, None)
('35', 'Legend: The Best Of...', 'Bob Marley And The Wailers', None, None, None)
('36', 'Time Served', 'Moneybagg Yo', None, None, None)
('37', 'Lover', 'Taylor Swift', None, None, None)
('38', 'Diamonds', 'Elton John', None, None, None)
('39', 'Death Race For Love', 'Juice WRLD', None, None, None)
('40', 'Scorpion', 'Drake', None, None, None)
('41', "Just Cause Y'all Waited 2", 'Lil Durk', None, None, None)
('42', 'Stoney', 'Post Malone', None, None, None)
('43', 'Frozen II', 'Soundtrack', None, None, None)
('44', 'MAP OF THE SOUL : 7', 'BTS', None, None, None)
('45', "I'm Gone", 'iann dior', None, None, None)
('46', 'KIRK', 'DaBaby', None, None, None)
('47', 'Chronicle The 20 Greatest Hits', 'Creedence Clearwater Revival', None, None, None)
('48', "It Was Good Until It Wasn't", 'Kehlani', None, None, None)
('49', 'GIRL', 'Maren Morris', None, None, None)
('50', 'Collection One', 'SAINt JHN', None, None, None)
('51', 'Golden Hour', 'Kygo', None, None, None)
('52', 'JACKBOYS', 'JACKBOYS', None, None, None)
('53', 'Greatest Hits', '2Pac', None, None, None)
('54', 'PTSD', 'G Herbo', None, None, None)
('55', 'Ghetto Gospel', 'Rod Wave', None, None, None)
('56', 'Certified Hitmaker', 'Lil Mosey', None, None, None)
('57', 'Good Intentions', 'NAV', None, None, None)
('58', 'So Much Fun', 'Young Thug', None, None, None)
('59', 'Dont Smile At Me', 'Billie Eilish', None, None, None)
('60', 'Cuz I Love You', 'Lizzo', None, None, None)
('61', '?', 'XXXTENTACION', None, None, None)
('62', "Journey's Greatest Hits", 'Journey', None, None, None)
('63', 'Heaven Or Hell', 'Don Toliver', None, None, None)
('64', 'Manic', 'Halsey', None, None, None)
('65', 'Traveller', 'Chris Stapleton', None, None, None)
('66', 'American Teen', 'Khalid', None, None, None)
('67', 'Free Spirit', 'Khalid', None, None, None)
('68', 'AI YoungBoy 2', 'YoungBoy Never Broke Again', None, None, None)
('69', "Fully Loaded: God's Country", 'Blake Shelton', None, None, None)
('70', 'Rumours', 'Fleetwood Mac', None, None, None)
('71', 'Las Que No Iban A Salir', 'Bad Bunny', None, None, None)
('72', 'Sweet Action', 'Jack Harlow', None, None, None)
('73', '38 Baby 2', 'YoungBoy Never Broke Again', None, None, None)
('74', 'Music To Be Murdered By', 'Eminem', None, None, None)
('75', 'Thank U, Next', 'Ariana Grande', None, None, None)
('76', 'Indigo', 'Chris Brown', None, None, None)
('77', '÷ (Divide)', 'Ed Sheeran', None, None, None)
('78', '1', 'The Beatles', None, None, None)
('79', 'Slime & B', 'Chris Brown & Young Thug', None, None, None)
('80', 'Artist 2.0', 'A Boogie Wit da Hoodie', None, None, None)
('81', 'Greatest Hits', 'Tom Petty And The Heartbreakers', None, None, None)
('82', 'Moana', 'Soundtrack', None, None, None)
('83', 'A Love Letter To You 4', 'Trippie Redd', None, None, None)
('84', 'RTJ4', 'Run The Jewels', None, None, None)
('85', 'Hamilton: An American Musical', 'Original Broadway Cast', None, None, None)
('86', 'Romance', 'Camila Cabello', None, None, None)
('87', 'Pick Me Up Off The Floor', 'Norah Jones', None, None, None)
('88', 'Luv Is Rage 2', 'Lil Uzi Vert', None, None, None)
('89', 'Chapter I: Snake Oil', 'Diplo Presents Thomas Wesley', None, None, None)
('90', 'DAMN.', 'Kendrick Lamar', None, None, None)
('91', 'Lil Boat 3', 'Lil Yachty', None, None, None)
('92', 'Invasion Of Privacy', 'Cardi B', None, None, None)
('93', 'Sounds Of Summer: The Very Best Of The Beach Boys', 'The Beach Boys', None, None, None)
('94', 'good kid, m.A.A.d city', 'Kendrick Lamar', None, None, None)
('95', 'Dreamville & J. Cole: Revenge Of The Dreamers III', 'Various Artists', None, None, None)
('96', 'Abbey Road', 'The Beatles', None, None, None)
('97', '2014 Forest Hills Drive', 'J. Cole', None, None, None)
('98', 'Sleepy Hallow Presents: Sleepy', 'Sleepy Hallow', None, None, None)
('99', 'Take Care', 'Drake', None, None, None)
('100', 'Back In Black', 'AC/DC', None, None, None)
('101', 'Circles', 'Mac Miller', None, None, None)
('102', 'No.6 Collaborations Project', 'Ed Sheeran', None, None, None)
('103', 'Greatest Hits So Far...', 'Zac Brown Band', None, None, None)
('104', 'Where The Light Is', 'Surfaces', None, None, None)
('105', 'The Search', 'NF', None, None, None)
('106', 'Perfect Ten', 'Mustard', None, None, None)
('107', 'Birds In The Trap Sing McKnight', 'Travis Scott', None, None, None)
('108', 'Greatest Hits', 'The Notorious B.I.G.', None, None, None)
('109', 'Appetite For Destruction', "Guns N' Roses", None, None, None)
('110', 'The New Toronto 3', 'Tory Lanez', None, None, None)
('111', 'Views', 'Drake', None, None, None)
('112', 'The Greatest Showman', 'Soundtrack', None, None, None)
('113', 'All Time Greatest Hits', 'Lynyrd Skynyrd', None, None, None)
('114', '7 (EP)', 'Lil Nas X', None, None, None)
('115', 'Hoodie SZN', 'A Boogie Wit da Hoodie', None, None, None)
('116', 'Dan + Shay', 'Dan + Shay', None, None, None)
('117', 'Love Yourself: Answer', 'BTS', None, None, None)
('118', 'Still Flexin, Still Steppin', 'YoungBoy Never Broke Again', None, None, None)
('119', 'Experiment', 'Kane Brown', None, None, None)
('120', 'Beauty Behind The Madness', 'The Weeknd', None, None, None)
('121', 'Shawn Mendes', 'Shawn Mendes', None, None, None)
('122', 'Starboy', 'The Weeknd', None, None, None)
('123', 'Their Greatest Hits 1971-1975', 'Eagles', None, None, None)
('124', '35 Biggest Hits', 'Tim McGraw', None, None, None)
('125', 'Here And Now', 'Kenny Chesney', None, None, None)
('126', '17', 'XXXTENTACION', None, None, None)
('127', 'Graves Into Gardens', 'Elevation Worship', None, None, None)
('128', 'The Essential Michael Jackson', 'Michael Jackson', None, None, None)
('129', 'Wildcard', 'Miranda Lambert', None, None, None)
('130', 'Drip Harder', 'Lil Baby & Gunna', None, None, None)
('131', 'Cry Baby', 'Melanie Martinez', None, None, None)
('132', '1989', 'Taylor Swift', None, None, None)
('133', 'Look Up Child', 'Lauren Daigle', None, None, None)
('134', 'Thriller', 'Michael Jackson', None, None, None)
('135', 'Evolve', 'Imagine Dragons', None, None, None)
('136', 'Ctrl', 'SZA', None, None, None)
('137', 'Poems Of The Past (EP)', 'Powfu', None, None, None)
('138', 'True 2 Myself', 'Lil Tjay', None, None, None)
('139', 'More Life', 'Drake', None, None, None)
('140', 'Center Point Road', 'Thomas Rhett', None, None, None)
('141', 'Die A Legend', 'Polo G', None, None, None)
('142', 'The Eminem Show', 'Eminem', None, None, None)
('143', 'Kane Brown', 'Kane Brown', None, None, None)
('144', 'Baby On Baby', 'DaBaby', None, None, None)
('145', 'Greatest Hits', 'Red Hot Chili Peppers', None, None, None)
('146', 'Man On The Moon: The End Of Day', 'Kid Cudi', None, None, None)
('147', 'Old Dominion', 'Old Dominion', None, None, None)
('148', 'Hot Rocks 1964-1971', 'The Rolling Stones', None, None, None)
('149', 'X 100PRE', 'Bad Bunny', None, None, None)
('150', 'Championships', 'Meek Mill', None, None, None)
('151', 'Victory Lap', 'Nipsey Hussle', None, None, None)
('152', 'The Essential Billy Joel', 'Billy Joel', None, None, None)
('153', 'Doo-Wops & Hooligans', 'Bruno Mars', None, None, None)
('154', 'Funeral', 'Lil Wayne', None, None, None)
('155', 'Baby23', 'JayDaYoungan', None, None, None)
('156', 'Greatest Hits', 'Bob Seger & The Silver Bullet Band', None, None, None)
('157', 'PARTYMOBILE', 'PARTYNEXTDOOR', None, None, None)
('158', 'Quality Control: Control The Streets, Volume 2', 'Various Artists', None, None, None)
('159', 'A Star Is Born (Soundtrack)', 'Lady Gaga & Bradley Cooper', None, None, None)
('160', 'The Kids Are Coming (EP)', 'Tones And I', None, None, None)
('161', 'TROLLS: World Tour', 'Soundtrack', None, None, None)
('162', 'Nevermind', 'Nirvana', None, None, None)
('163', 'Blurryface', 'twenty one pilots', None, None, None)
('164', 'Harder Than Ever', 'Lil Baby', None, None, None)
('165', 'The Essential Elvis Presley', 'Elvis Presley', None, None, None)
('166', 'Blonde', 'Frank Ocean', None, None, None)
('167', 'We Love You Tecca', 'Lil Tecca', None, None, None)
('168', 'ADHD', 'Joyner Lucas', None, None, None)
('169', 'Rage Against The Machine', 'Rage Against The Machine', None, None, None)
('170', '50 Number Ones', 'George Strait', None, None, None)
('171', 'Happiness Begins', 'Jonas Brothers', None, None, None)
('172', 'The Very Best Of Daryl Hall  John Oates', 'Daryl Hall John Oates', None, None, None)
('173', 'Melly vs. Melvin', 'YNW Melly', None, None, None)
('174', 'IGOR', 'Tyler, The Creator', None, None, None)
('175', 'H.E.R.', 'H.E.R.', None, None, None)
('176', 'Frozen', 'Soundtrack', None, None, None)
('177', '9', 'Jason Aldean', None, None, None)
('178', 'Rare', 'Selena Gomez', None, None, None)
('179', 'A Decade Of Destruction', 'Five Finger Death Punch', None, None, None)
('180', 'Greatest Hits: The Ultimate Collection', 'Bon Jovi', None, None, None)
('181', 'The Definitive Collection', 'Stevie Wonder', None, None, None)
('182', 'Reloaded: 20 #1 Hits', 'Blake Shelton', None, None, None)
('183', 'Perception', 'NF', None, None, None)
('184', 'Life On The Flip Side', 'Jimmy Buffett', None, None, None)
('185', 'Metallica', 'Metallica', None, None, None)
('186', '21', 'Adele', None, None, None)
('187', 'Homesick (EP)', 'Trevor Daniel', None, None, None)
('188', 'Sublime', 'Sublime', None, None, None)
('189', 'ANTI', 'Rihanna', None, None, None)
('190', 'Cosmic', 'Bazzi', None, None, None)
('191', 'California Sunrise', 'Jon Pardi', None, None, None)
('192', 'Colores', 'J Balvin', None, None, None)
('193', 'Nothing Was The Same', 'Drake', None, None, None)
('194', 'Ella Mai', 'Ella Mai', None, None, None)
('195', 'SHAKE THE SNOW GLOBE', 'Russ', None, None, None)
('196', 'Swimming', 'Mac Miller', None, None, None)
('197', 'Born To Die', 'Lana Del Rey', None, None, None)
('198', 'Night Visions', 'Imagine Dragons', None, None, None)
('199', 'Purgatory', 'Tyler Childers', None, None, None)
('200', 'The Essential Johnny Cash', 'Johnny Cash', None, None, None)

"""





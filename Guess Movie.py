from time import sleep
import re,math
from os import *
from random import randint


list_movie =['The Shawshank Redemption (1994)', 'The Godfather (1972)', 'The Godfather: Part II (1974)', 'Pulp Fiction (1994)', 'The Good, the Bad and the Ugly (1966)', 'The Dark Knight (2008)', '12 Angry Men (1957)', "Schindler's List (1993)", 'The Lord of the Rings: The Return of the King (2003)', 'Fight Club (1999)', 'Star Wars: Episode V - The Empire Strikes Back (1980)', 'The Lord of the Rings: The Fellowship of the Ring (2001)', "One Flew Over the Cuckoo's Nest (1975)", 'Inception (2010)', 'Goodfellas (1990)', 'Star Wars (1977)', 'Seven Samurai (1954)', 'Forrest Gump (1994)', 'The Matrix (1999)', 'The Lord of the Rings: The Two Towers (2002)', 'City of God (2002)', 'Se7en (1995)', 'The Silence of the Lambs (1991)', 'Once Upon a Time in the West (1968)', 'Casablanca (1942)', 'The Usual Suspects (1995)', 'Raiders of the Lost Ark (1981)', 'Rear Window (1954)', "It's a Wonderful Life (1946)", 'Psycho (1960)', 'L\xe9on: The Professional (1994)', 'Sunset Blvd. (1950)', 'American History X (1998)', 'Apocalypse Now (1979)', 'Terminator 2: Judgment Day (1991)', 'Saving Private Ryan (1998)', 'Memento (2000)', 'City Lights (1931)', 'Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb (1964)', 'Alien (1979)', 'Modern Times (1936)', 'Spirited Away (2001)', 'North by Northwest (1959)', 'Back to the Future (1985)', 'Life Is Beautiful (1997)', 'The Shining (1980)', 'The Pianist (2002)', 'Citizen Kane (1941)', 'The Departed (2006)', 'M (1931)', 'Paths of Glory (1957)', 'Vertigo (1958)', 'Django Unchained (2012)', 'The Dark Knight Rises (2012)', 'Double Indemnity (1944)', 'Aliens (1986)', 'Taxi Driver (1976)', 'American Beauty (1999)', 'The Green Mile (1999)', 'Gladiator (2000)', 'The Intouchables (2011)', 'WALL\x95E (2008)', 'The Lives of Others (2006)', 'Toy Story 3 (2010)', 'The Great Dictator (1940)', 'The Prestige (2006)', 'A Clockwork Orange (1971)', 'Lawrence of Arabia (1962)', 'Am\xe9lie (2001)', 'To Kill a Mockingbird (1962)', 'Reservoir Dogs (1992)', 'Das Boot (1981)', 'The Lion King (1994)', 'Cinema Paradiso (1988)', 'Star Wars: Episode VI - Return of the Jedi (1983)', 'The Third Man (1949)', 'The Treasure of the Sierra Madre (1948)', 'Once Upon a Time in America (1984)', 'Requiem for a Dream (2000)', 'Eternal Sunshine of the Spotless Mind (2004)', 'Full Metal Jacket (1987)', 'Oldboy (2003)', 'Braveheart (1995)', 'L.A. Confidential (1997)', 'Bicycle Thieves (1948)', 'Chinatown (1974)', "Singin' in the Rain (1952)", 'Princess Mononoke (1997)', 'Monty Python and the Holy Grail (1975)', 'Metropolis (1927)', 'Some Like It Hot (1959)', 'Rashomon (1950)', 'Amadeus (1984)', '2001: A Space Odyssey (1968)', 'All About Eve (1950)', 'The Sting (1973)', 'Witness for the Prosecution (1957)', 'Grave of the Fireflies (1988)', 'The Apartment (1960)', 'Indiana Jones and the Last Crusade (1989)', 'Unforgiven (1992)', 'Raging Bull (1980)', 'The Bridge on the River Kwai (1957)', 'Die Hard (1988)', 'Batman Begins (2005)', 'Yojimbo (1961)', 'A Separation (2011)', 'Inglourious Basterds (2009)', 'For a Few Dollars More (1965)', 'Snatch. (2000)', 'Toy Story (1995)', 'The Great Escape (1963)', 'Mr. Smith Goes to Washington (1939)', 'Up (2009)', 'Downfall (2004)', 'On the Waterfront (1954)', "Pan's Labyrinth (2006)", 'The General (1926)', 'The Seventh Seal (1957)', 'Heat (1995)', 'The Elephant Man (1980)', 'The Kid (1921)', 'The Maltese Falcon (1941)', 'Blade Runner (1982)', 'Scarface (1983)', 'Wild Strawberries (1957)', 'Rebecca (1940)', 'Gran Torino (2008)', 'Ikiru (1952)', 'Fargo (1996)', 'Ran (1985)', 'The Big Lebowski (1998)', 'Touch of Evil (1958)', 'The Gold Rush (1925)', 'The Deer Hunter (1978)', 'Cool Hand Luke (1967)', 'Lock, Stock and Two Smoking Barrels (1998)', 'No Country for Old Men (2007)', 'It Happened One Night (1934)', 'Diabolique (1955)', 'Casino (1995)', 'Good Will Hunting (1997)', 'The Sixth Sense (1999)', 'Strangers on a Train (1951)', 'Platoon (1986)', 'The Thing (1982)', 'Jaws (1975)', 'Sin City (2005)', 'Butch Cassidy and the Sundance Kid (1969)', 'Trainspotting (1996)', 'The Wizard of Oz (1939)', 'Kill Bill: Vol. 1 (2003)', 'Warrior (2011)', 'The Grapes of Wrath (1940)', 'The Secret in Their Eyes (2009)', 'Hotel Rwanda (2004)', 'High Noon (1952)', 'Gone with the Wind (1939)', 'Annie Hall (1977)', 'My Neighbor Totoro (1988)', 'V for Vendetta (2005)', 'Finding Nemo (2003)', 'Dial M for Murder (1954)', 'Notorious (1946)', 'The Avengers (2012)', 'How to Train Your Dragon (2010)', 'Into the Wild (2007)', 'The Hunt (2012)', 'Life of Brian (1979)', 'The Night of the Hunter (1955)', 'There Will Be Blood (2007)', 'Network (1976)', 'The Terminator (1984)', 'Ben-Hur (1959)', 'Million Dollar Baby (2004)', 'The Big Sleep (1946)', 'Stand by Me (1986)', "The King's Speech (2010)", 'The Best Years of Our Lives (1946)', 'The 400 Blows (1959)', 'Groundhog Day (1993)', 'Twelve Monkeys (1995)', 'Mary and Max (2009)', 'Dog Day Afternoon (1975)', "Howl's Moving Castle (2004)", 'Donnie Darko (2001)', 'Persona (1966)', 'Amores Perros (2000)', 'The Bourne Ultimatum (2007)', 'Gandhi (1982)', 'The Killing (1956)', 'A Beautiful Mind (2001)', 'The Graduate (1967)', 'Black Swan (2010)', 'The Princess Bride (1987)', "Who's Afraid of Virginia Woolf? (1966)", '8\xbd (1963)', 'The Hustler (1961)', 'La Strada (1954)', 'Rocky (1976)', 'Anatomy of a Murder (1959)', 'The Man Who Shot Liberty Valance (1962)', 'Slumdog Millionaire (2008)', 'Rope (1948)', 'The Exorcist (1973)', 'In the Name of the Father (1993)', 'The Wild Bunch (1969)', 'Barry Lyndon (1975)', 'The Manchurian Candidate (1962)', 'Monsters, Inc. (2001)', 'Stalag 17 (1953)', 'Like Stars on Earth (2007)', 'Infernal Affairs (2002)', '3 Idiots (2009)', 'The Truman Show (1998)', 'Memories of Murder (2003)', 'Pirates of the Caribbean: The Curse of the Black Pearl (2003)', 'Stalker (1979)', 'Roman Holiday (1953)', 'Sleuth (1972)', 'Life of Pi (2012)', 'Fanny and Alexander (1982)', 'Harry Potter and the Deathly Hallows: Part 2 (2011)', 'Jurassic Park (1993)', 'A Fistful of Dollars (1964)', 'Ip Man (2008)', 'Star Trek (2009)', 'Incendies (2010)', 'A Streetcar Named Desire (1951)', 'Shutter Island (2010)', 'The Hobbit: An Unexpected Journey (2012)', 'District 9 (2009)', 'Ratatouille (2007)', 'La Haine (1995)', 'The Diving Bell and the Butterfly (2007)', 'Rain Man (1988)', 'The Artist (2011/I)', 'All Quiet on the Western Front (1930)', 'Nausica\xe4 of the Valley of the Wind (1984)', "Rosemary's Baby (1968)", 'Beauty and the Beast (1991)', 'Papillon (1973)', 'Mystic River (2003)', 'Harvey (1950)', 'Before Sunrise (1995)', 'Spring, Summer, Fall, Winter... and Spring (2003)', 'The Celebration (1998)', "Hachi: A Dog's Tale (2009)", 'Arsenic and Old Lace (1944)', 'The Untouchables (1987)']

print '\n\n\n\t\t\tGuess The Movie!!!\n'

movie_name = (list_movie[randint(0,len(list_movie))])
val = (movie_name[:-7]).lower()
va = '-'*len(val)
sleep(1)

space = []

list_val = list(enumerate(val))

for i,j in list_val:
    if re.match(r'[^a-zA-Z]',val[i]):
        space.append(i)

for i in space:
    va = va[:i]+val[i]+va[i+1:]

print '\t\t\t',va,'\n'

n = int(math.ceil(len(val)/3))
print '\n\t\t\tYou have ',n,'chances'


while(1==1):
    print '\n\t\t\tYour clue is:','\n\t\t\tMovie was from the year ',movie_name[-6:]

    inp = raw_input("\n\t\t\tInput a char:")

    if(inp in val):
        ip = []

        for i,j in list_val:
            if j == inp:
                ip.append(i)

        print ip

        for i in ip:
            va = va[:i]+inp+va[i+1:]

        print va

        system('cls')

        print '\n\n\n\t\t\tYour Movie is :',va,'\n'

        if(va==val):
            system('cls')
            sleep(1)
            print '\n\n\n\n\t\t\tCongrats\n\t\t\tYou Won!!!'
            print '\n \t\t\tYour Movie was :',val
            print '\n\t\t\tWindow closes in:\n'

            for i in range(3,0,-1):
                sleep(1)
                print '\t\t\t',i

            break

    elif n==0:
        system('cls')
        print '\n\n\n\t\t\tGame Over!!!','\n \t\t\tYour Movie was :',val
        print '\n\t\t\tWindow closes in:\n'

        for i in range(3,0,-1):
            sleep(1)
            print '\t\t\t',i

        break
        

    else:
        n = n-1
        system('cls')
        if n == 0:
            print '\n\n\n\n\t\t\tYou have last chance\n\n'
            print '\t\t\tYour word is :',va,'\n'
        else:
            print '\n\n\n\n\t\t\tYou have ',n,' more chance\n\n'
            print '\t\t\tYour word is :',va,'\n'
        
        sleep(2)


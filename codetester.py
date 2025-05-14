import sqlite3

DATABASE = "jazz.db"

def print_song_by_artist():
    '''Print all songs by artists'''
    check = False
    DATABASE = "jazz.db"
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from song INNER JOIN artists on song.artist_id = artist_id INNER JOIN album on song.album_id = album.album_id;"
    cursor.execute(sql)
    results = cursor.fetchall()
    jazzartists = input('Enter you artists name please.\n').upper()
    while True:
        if check:
            break
        elif jazzartists == "Exit":
            break
        else:
            print(f"{'Song':<40}{'Artist':<15}")
            for music in results:
                if jazzartists == music[7].upper():
                    print(f"{music[1]:<40}{music[7]:<15}")
                    print(music[7])
            check = True
            break

while True:
    user_input = input("What would you like to browse \n1. Browse through songs \n2. Browse through albums \n3. Browse through artists \n4. Exit\n")
    if user_input == "1":
        print_song_by_artist()
        print("Goodbye!")
        break
    else:
        print('That was not an option. BITCH ASS NIGGAAAAAAAA')
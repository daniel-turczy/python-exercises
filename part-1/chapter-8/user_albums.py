"""
Start with your program from Exercise 8-7 (write a make_album function that
builds a dictionary describing a music album. It should take an artist name,
album title and optional song count.)
Write a while loop that allows users to input the artist name and album title.
Make sure to include a quit value (to break from the loop).
"""

def make_album(album_title, artist, song_count=None):
    """
    Return a formatted dictionary with an album's title, artist
    and song count (optional).
    """
    album_info = {
        "title": album_title,
        "artist": artist,
    }
    if song_count:
        album_info["song_count"] = song_count
    return album_info


def get_song_count():
    """Prompt the user for a song count (integer, ENTER to skip, or q to quit)."""
    while True:
        song_count = input("Song count (ENTER to skip): ").strip()
        if song_count.lower() == "q":
            return "quit"
        elif song_count == "":
            return None
        elif not song_count.isdigit():
            print("\nPlease enter an integer for the song count, ENTER to skip, or q to quit.")
        else:
            return int(song_count)


def main():
    albums = []
    print("\nPlease enter the details for an album. (enter 'q' to quit at any time)")

    while True:
        print("\n--- NEW ALBUM ---")
        title = input("Title: ")
        if title.lower() == "q": break

        artist = input("Artist: ").strip()
        if artist.lower() == "q": break

        song_count = get_song_count()
        if song_count == "quit":
            break
        elif song_count == None:
            current_album = make_album(title, artist)
        else:
            current_album = make_album(title, artist, song_count)
        
        albums.append(current_album)
    return albums


albums = main()
print("\n--- ALBUMS ---")
for album in albums:
    print(album)
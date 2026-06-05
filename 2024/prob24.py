import os

end = False

while not end:
    genre = input()

    if genre == "END":
        end = True
        continue
    
    library = []
    for filename in os.listdir("student_datasets/files"):
        if filename.endswith(".mp3"):
            continue

        filename = filename.removesuffix(".mp3")

        song, artist, ending = filename.strip().split(" - ")
        song_genres = ending.split(", ")


        matching_genre = False
        for applicable_genre in song_genres:
            if genre.lower() in applicable_genre.lower():
                matching_genre = True
                break

        if not matching_genre:
            continue
        
        printed_genre = genre.replace(" ", "")
        song = song.replace(" ", "")

        library.append(f"{printed_genre.upper()}_{song}_{artist}.mp3")
    
    for song in sorted(library):
        print(song)
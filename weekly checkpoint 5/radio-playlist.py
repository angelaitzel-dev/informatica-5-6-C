import time
def main():
    playlist = ["Boston", "Dracula", "I Knew It, I Knew You", "Hate that i made you love me", "Risk It All"]
    print(playlist)
    playlist.append("Be By You")
    print(playlist)
    playlist.insert(0, "Bohemian Rhapsody")
    print(playlist)
    playlist.pop(4)
    print(playlist)
    print(playlist.index("Risk It All"))
    print("Number of sons in the playlist: ", len(playlist))
    playlist.reverse()
    print(playlist) #Some methods wont work with new methods
    playlist.sort()
    print(playlist)
    repeat = 10
    while repeat > 0:
        print(playlist)
        song_played = playlist[0]
        playlist.pop(0)
        playlist.append(song_played)
        time.sleep(3)
        repeat -= 1

if __name__ == "__main__":
    main()

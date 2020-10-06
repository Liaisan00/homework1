class Track():
    def __init__ (self, name, duration):
        self.name = name
        self.duration = duration
        duration = int()
    def show(self):
        print(f"{self.name_track} - {self.duration}")

    track_list = [{"Just Dance":3, "Teeth":4, "Paparazzi":5}, {"Artpop":4, "Swine":4, "Donatella":7}]


class Album():
    def __init__(self, group, album, track_list):
        self.group = group
        self.album = album
        self.track_list = track_list
        album1 = Album("Lady Gaga", "The Fame Monster", track_list)
        album2 = Album("Lady Gaga", "Artpop", track_list)
        album1.track_list = [{"Just Dance":3, "Teeth":4, "Paparazzi":5}]
        album2.track_list = [{"Artpop":4, "Swine":4, "Donatella":7}]


    def get_tracks(self, track_list):
        for i in track_list:
            for track_name in i.items():
                print(f'{track_name} - {track_duration}')
                return f'{track_name} - {track_duration}'
        new_track = track()
        new_track.show


    def get_add_track(self, track_list):
        new_track = " "
        new_duration = 0
        track_list.append([new_track, new_duration])
        return "New track"

        def get_duration(self, track_list):
            total_duration = 0
            for songs in track_list:
                for track_name, track_duration in songs.items():
                    total_duration += track_duration
                    print(total_duration)






class Movie:
    # create parent class of Movie

    # assign default values for properties
    title = ''
    director = ''
    runtime_mins = 0
    rating = ''

    def __init__(self, title, director, runtime_mins, rating):
        # assign properties 
        self.title = title
        self.director = director
        self.runtime_mins = runtime_mins
        self.rating = rating


class Animation(Movie):
    # create child class Animation, which contains properties of animated movies

    # assign default values for properties
    animation_type = ''
    target_audience = ''

    def __init__(self, animation_type, target_audience):
        # assign properties for animated movies
        self.animation_type = animation_type
        self.target_audience = target_audience


class Musical(Movie):
    # create child class Musical, which contains properties of movies that are musicals

    # assign default values for properties
    music_by = ''
    famous_song = ''

    def __init__(self, music_by, famous_song):
        # assign properties for musicals
        self.music_by = music_by
        self.famous_song = famous_song


if __name__ == '__main__':
    # create instance of Movie class
    titanic_movie = Movie('Titanic' ,'James Cameron', 185, 'PG-13')

    # print properties of Movie instance
    print(titanic_movie.title, ' ', titanic_movie.director)

    # create instance of Animation class
    toy_story_movie = Animation('Computer', 'kids')
    toy_story_movie.title = 'Toy Story'
    toy_story_movie.director = 'John Lassiter'
    toy_story_movie.runtime_mins = 120
    toy_story_movie.rating = 'G'

    # print properties of Animation instance
    print(toy_story_movie.title, ' ' , toy_story_movie.animation_type)


    # create instance of Musical class
    sound_of_music_movie = Musical('Rogers and Hammerstein', 'Do-Re-Mi')
    sound_of_music_movie.title = 'Sound of Music'
    sound_of_music_movie.director = 'I don\'t know'
    sound_of_music_movie.runtime_mins = 135
    sound_of_music_movie.rating = 'G'

    # print properties of Musical instance
    print(sound_of_music_movie.title, ' ' , sound_of_music_movie.famous_song)


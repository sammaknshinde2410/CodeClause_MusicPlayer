# Required libraries Tkinter and pygame

# importing required libraries
from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    ''' creating the class for music player controls'''
    def __init__(self, window):
        window.geometry('320x100');
        window.title('My Music player');
        window.resizable(0,0);
        Load = Button(window, text ='Load', width=10, font=('Times', 10), command=self.load)
        Play = Button(window, text = 'Play', width=10, font=('Times', 10), command=self.play)
        Pause = Button(window, text = 'Pause', width=10, font=('Times', 10), command=self.pause)
        Stop = Button(window, text = 'Stop', width=10, font=('Times', 10), command=self.stop)

        Load.place(x=0, y=20);
        Play.place(x=110, y=20);
        Pause.place(x=220, y=20);
        Stop.place(x=110, y=60);

        self.music_file = False
        self.playing_state = False

    def load(self):
        ''' Adding load method to our music player class'''
        self.music_file = filedialog.askopenfilename()

    def play(self):
        ''' Adding play method to our music player'''
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()

    def pause(self):
        '''Adding pause method to our music player'''
        # this block will pause the playing song
        if not self.playing_state:
            mixer.music.pause();
            self.playing_state = True

        #this block will unpause the paused song
        else:
            mixer.music.unpause()
            self.playing_state = False
            
    def stop(self):
        ''' Adding stop method'''
        mixer.music.stop()

# Creating Tkinter class object
'''tk is the class which we use to create the root(main) window of our application'''
root = Tk()

# Passing Tkinter class object as arguement to MusicPlayer Class
app = MusicPlayer(root)

# Calling a loop to keep app window running
'''a method in the main window which we execute when we want to run our app'''
root.mainloop()

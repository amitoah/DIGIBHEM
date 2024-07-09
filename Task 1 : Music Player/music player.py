import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Initialize pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        
        # Initialize buttons
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.open_button = tk.Button(self.root, text="Open", command=self.open_file)
        
        # Arrange buttons
        self.play_button.pack(pady=10)
        self.pause_button.pack(pady=10)
        self.stop_button.pack(pady=10)
        self.open_button.pack(pady=10)
        
        self.current_file = None
        self.is_paused = False

    def play_music(self):
        if self.current_file:
            if self.is_paused:
                pygame.mixer.music.unpause()
                self.is_paused = False
            else:
                pygame.mixer.music.load(self.current_file)
                pygame.mixer.music.play()
        else:
            messagebox.showwarning("No file", "Please select a music file first.")

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_paused = False

    def open_file(self):
        self.current_file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3")])
        if self.current_file:
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()

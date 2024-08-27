import tkinter as tk
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Stopwatch")
        
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Label to display time
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
        self.time_label.pack()

        # Start button
        self.start_button = tk.Button(root, text="Start", command=self.start, font=("Helvetica", 24))
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Stop button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop, font=("Helvetica", 24))
        self.stop_button.pack(side=tk.LEFT, padx=10)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=("Helvetica", 24))
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.time_label.config(text="00:00:00")

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            time_str = self.format_time(self.elapsed_time)
            self.time_label.config(text=time_str)
            self.root.after(50, self.update_time)

    @staticmethod
    def format_time(elapsed_time):
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time % 1) * 100)
        return f"{minutes:02}:{seconds:02}:{milliseconds:02}"

if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()

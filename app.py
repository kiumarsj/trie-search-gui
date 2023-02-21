from trie import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

keys = [
    "apple", "apples",
    "book", "bookstore", "bookshelf", "bookworm", "books",
    "cat", "cating",
    "dog", "dogs",
    "hello", "hell", "hel", "help", "helps", "helping"
    "amazon", "amazon prime", "amazing", "amazing spiderman", "amazed"
]
t = Trie()
for key in keys:
    t.insert(key)

class App(customtkinter.CTk):
    width = 400
    height = 500
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        sv = customtkinter.StringVar()
        sv.trace_add("write", lambda name, index, mode, sv=sv: self.text_changed(sv))

        self.title("Trie Search")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Trie Search",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.login_label.grid(row=0, column=0, padx=30, pady=(10, 15))
        self.input = customtkinter.CTkEntry(self.login_frame, width=350, placeholder_text="input", textvariable=sv)
        self.input.grid(row=1, column=0, padx=10, pady=(0, 10))
        self.result = customtkinter.CTkTextbox(self.login_frame, width=350, height=300)
        self.result.grid(row=2, column=0, padx=10, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Exit", command=self.exit_event, width=350)
        self.login_button.grid(row=3, column=0, padx=10, pady=(0, 15))

    def exit_event(self):
        print("exit pressed")
        self.quit()

    def text_changed(self, sv):
        self.result.delete('1.0', customtkinter.END)
        #t.formTrie(keys)
        value = sv.get()
        #comp = t.printAutoSuggestions(value)
        comp = t.autocomplete(value)
        if comp == []:
            self.result.insert(customtkinter.END, "No strings found with this prefix\n")
        else:
            for i in comp:
                self.result.insert(customtkinter.END, f"{str(i)}\n")
        return True

if __name__ == "__main__":
    app = App()
    app.mainloop()

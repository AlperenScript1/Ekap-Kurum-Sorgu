#! Pencereyi ortalamak için kullanılan func CustomTkinter içinde pencere ortlama bulundurmuyor maalesef
def center_window(app, width, height):
    app.update_idletasks()  #? Ekran ölçülerini doğru almak için

    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    app.geometry(f"{width}x{height}+{x}+{y}")
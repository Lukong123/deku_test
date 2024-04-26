import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class HorizontalLine(Gtk.DrawingArea):
    def __init__(self):
        super().__init__()

        # Set the size of the drawing area
        self.set_size_request(-1, 1)

    def do_draw(self, cr):
        # Set the line color
        cr.set_source_rgb(0, 0, 0)  # Black color

        # Set the line width
        cr.set_line_width(1)

        # Draw the line
        cr.move_to(0, 0)
        cr.line_to(self.get_allocated_width(), 0)
        cr.stroke()

class MyApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="Horizontal Line Example")

        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(main_box)

        # Create and add the horizontal line
        line = HorizontalLine()
        main_box.pack_start(line, False, False, 0)

        self.show_all()

if __name__ == "__main__":
    app = MyApp()
    # app.run()
    Gtk.main
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class ModemWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Linux App")


        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        # Create the main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(main_box)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        nav_bar.set_border_width(10)
        main_box.pack_start(nav_bar, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        # Adjusting navbar
        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label")  # Set a custom CSS name for the label
        left_box.pack_start(title_label, False, False, 0)

        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)

        # icon
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 0)

       
        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)

        # widgets for container1
        label1 = Gtk.Label()
        label1.set_text("Container 1")
        container1.pack_start(label1, False, False, 0)

        main_box.pack_end(container1, True, True, 0)

        # Container 2
        container2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container2.set_vexpand(True)
        container2.set_homogeneous(False)
        container2.set_border_width(10)

        # widgets for container2
        label2 = Gtk.Label()
        label2.set_text("Container 1")
        container2.pack_start(label2, False, False, 0)

        main_box.pack_end(container2, True, True, 0)

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

    def apply_css(self):
        css_provider = Gtk.CssProvider()

        # Define the CSS rules
        css = """
            #title-label {
                font-weight: bold;
            }
            .nav-bar {
                background-color: green;
            }
        """

        # Load the CSS rules into the provider
        css_provider.load_from_data(css.encode())

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = MyApp()
    app.run()
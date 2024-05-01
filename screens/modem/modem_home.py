import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from utils.widgets.horizontal_line import HorizontalLine


class ModemWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Deku Linux App")

        self.connect("destroy", Gtk.main_quit)
        self.set_default_size(800, 600)

        # Create the main container
        main_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.add(main_box)

        # Create the sidebar
        sidebar = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.set_size_request(150, -1)
        sidebar.set_homogeneous(False)
        sidebar.set_border_width(0)
        sidebar.set_name("sidebar")
        main_box.pack_start(sidebar, False, False, 0)

        # Sidebar content
        sidebar_top = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        sidebar.pack_start(sidebar_top, False, False, 0)

        home_modem = Gtk.Label()
        home_modem.set_text("Home Modem")
        home_modem.set_name("side_label")
        home_modem.set_margin_bottom(8)
        home_modem.set_margin_top(60)
        sidebar_top.pack_start(home_modem, False, False, 0)

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # send
        send_label = Gtk.Label()
        send_label.set_text("Send")
        send_label.set_name("side_label")
        send_label.set_margin_bottom(8)
        send_label.set_margin_top(8)
        sidebar_top.pack_start(send_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # receive
        receive_label = Gtk.Label()
        receive_label.set_text("Incoming")
        receive_label.set_name("side_label")
        receive_label.set_margin_bottom(8)
        receive_label.set_margin_top(8)
        sidebar_top.pack_start(receive_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # Outgoing
        outgoing_label = Gtk.Label()
        outgoing_label.set_text("Outgoing ")
        outgoing_label.set_name("side_label")
        outgoing_label.set_margin_bottom(8)
        outgoing_label.set_margin_top(8)
        sidebar_top.pack_start(outgoing_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # Failed
        failed_label = Gtk.Label()
        failed_label.set_text("Failed ")
        failed_label.set_name("side_label")
        failed_label.set_margin_bottom(8)
        failed_label.set_margin_top(8)
        sidebar_top.pack_start(failed_label, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # encrypted
        encrypted_label = Gtk.Label()
        encrypted_label.set_text("Encrypted")
        encrypted_label.set_name("side_label")
        encrypted_label.set_margin_bottom(40)
        encrypted_label.set_margin_top(8)
        sidebar_top.pack_start(encrypted_label, False, False, 0)

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)
        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)


        # send
        message_forwarding = Gtk.Label()
        message_forwarding.set_text("Message Forwarding")
        message_forwarding.set_name("side_label")
        message_forwarding.set_margin_bottom(8)
        message_forwarding.set_margin_top(15)
        sidebar_top.pack_start(message_forwarding, False, False, 0)


        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # export
        export = Gtk.Label()
        export.set_text("Export")
        export.set_name("side_label")
        export.set_margin_bottom(8)
        export.set_margin_top(8)
        sidebar_top.pack_start(export, False, False, 0)
    

        line = HorizontalLine()
        sidebar_top.pack_start(line, False, False, 0)

        # About
        about = Gtk.Label()
        about.set_text("About ")
        about.set_name("side_label")
        about.set_margin_bottom(8)
        about.set_margin_top(8)
        sidebar_top.pack_start(about, False, False, 0)

        # sidebar_content = Gtk.Label()
        # sidebar_content.set_text("Sidebar")
        # sidebar.pack_start(sidebar_content, False, False, 0)

        # Create the main content area
        content_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        main_box.pack_start(content_area, True, True, 0)

        # Create the navigation bar
        nav_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        nav_bar.set_size_request(-1, 50)
        nav_bar.set_homogeneous(False)
        # nav_bar.set_border_width(10)
        nav_bar.set_name("nav-bar")
        content_area.pack_start(nav_bar, False, False, 0)

        # Create a box for the left side of the navigation bar
        left_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        left_box.set_homogeneous(True)
        nav_bar.pack_start(left_box, False, False, 0)

        # Adjusting navbar
        title_label = Gtk.Label()
        title_label.set_text("Deku Linux")
        title_label.set_name("title-label")
        left_box.pack_start(title_label, False, False, 0)

        # Create a box for the right side of the navigation bar
        right_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        right_box.set_homogeneous(True)
        nav_bar.pack_end(right_box, False, False, 0)

        # Icon
        nav_icon = Gtk.Image.new_from_icon_name("preferences-system-symbolic", Gtk.IconSize.SMALL_TOOLBAR)
        right_box.pack_end(nav_icon, False, False, 0)

        # Container 1
        container1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container1.set_vexpand(True)
        container1.set_homogeneous(False)
        container1.set_border_width(10)
        content_area.pack_start(container1, True, True, 0)

        # container1 main
        center_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        center_box.set_halign(Gtk.Align.CENTER)
        center_box.set_name("center-box-modem")
        container1.pack_start(center_box, False, False, 0)

        # Horizontal line widget
        line = HorizontalLine()
        container1.pack_start(line, False, False, 0)


        # device label
        device_label = Gtk.Label()
        device_label.set_text("MTN 4.2")
        center_box.pack_start(device_label, False, False, 30)


        # Container 2
        container2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        container2.set_vexpand(True)
        container2.set_homogeneous(False)
        container2.set_border_width(10)

        container2.set_valign(Gtk.Align.CENTER)
        container2.set_halign(Gtk.Align.CENTER)

        # grid for usb modem box information
        grid = Gtk.Grid()
        grid.set_column_spacing(80)
        grid.set_name("box-info")
        container2.pack_start(grid, True, True, 0)

        # dummy content
        labels = [
            "Manufacturer:",
            "Model:",
            "Serial Number:",
            "IMEI:",
            "ICCID:",
            "Firmware Version:",
            "Signal Strength:",
            "Connection Status:",
        ]
        values = [
            "Dummy Manufacturer",
            "Dummy Model",
            "Dummy Serial Number",
            "Dummy IMEI",
            "Dummy ICCID",
            "Dummy Firmware Version",
            "Dummy Signal Strength",
            "Dummy Connection Status",
        ]

        # Create column headers
        header_a = Gtk.Label()
        header_a.set_text("Box Info")
        header_a.set_name("box-info-header")
        grid.attach(header_a, 0, 0, 1, 1)

        header_b = Gtk.Label()
        header_b.set_text("Box Info")
        header_b.set_name("box-info-header")
        grid.attach(header_b, 1, 0, 1, 1)


        for i in range(len(labels)):
            label = Gtk.Label()
            label.set_text(labels[i])
            label.set_margin_top(10)
            value = Gtk.Label()

            value.set_text(values[i])

            grid.attach(label, 0, i+1, 1, 1)
            grid. attach(value, 1, i+1, 1, 1)

        content_area.pack_start(container2, True, True, 0)

        # floating action button
        fab_button = Gtk.Button()
        fab_button.set_tooltip_text("Compose")
        fab_button.get_style_context().add_class("fab-button")

        message_icon = Gtk.Image.new_from_icon_name("mail-send-symbolic", Gtk.IconSize.BUTTON)
        fab_button.add(message_icon)
        fab_button.set_size_request(50, 50)
        alignment = Gtk.Alignment.new(1, 0.8, 0, 0)
        alignment.set_padding(0, 50, 0, 50) 
        alignment.add(fab_button)
        content_area.pack_end(alignment, False, False, 0)

        # Apply custom CSS styling
        self.apply_css()

        self.show_all()

    def apply_css(self):
        css_provider = Gtk.CssProvider()
        css_path = "utils/styles/styles.css"
        # Load the CSS rules into the provider
        css_provider.load_from_path(css_path)

        # Apply the CSS provider to the window
        screen = Gdk.Screen.get_default()
        style_context = self.get_style_context()
        style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

    def run(self):
        Gtk.main()

if __name__ == "__main__":
    app = ModemWindow()
    app.run()
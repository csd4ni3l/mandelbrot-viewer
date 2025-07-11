import arcade.color
from arcade.types import Color
from arcade.gui.widgets.buttons import UITextureButtonStyle, UIFlatButtonStyle
from arcade.gui.widgets.slider import UISliderStyle

menu_background_color = (30, 30, 47)
log_dir = 'logs'
discord_presence_id = 1365949409254441000

initial_real_imag = {
    "mandelbrot": (-2.0, 1.0, -1.0, 1.0),
    "julia": (-2.0, 1.0, -1.0, 1.0),
    "mandelbar": (-2.0, 1.0, -1.0, 1.0),
    "phoenix_fractal": (-2.0, 1.0, -1.0, 1.0),
    "lambda_fractal": (-2.0, 1.0, -1.0, 1.0),
    "buffalo_fractal": (-2.0, 1.5, -2.0, 1.0),
    "burning_ship": (-2.0, 1.5, -2.0, 1.0),
    "newton_fractal": (-2.0, 2.0, -2.0, 2.0)
}

c_for_julia_type = {
    "Classic swirling": (-0.7, 0.27015),
    "Douady rabbit": (-0.123, 0.745),
    "Nebula-style": (0.285, 0),
    "Snowflake": (-0.8, 0.156)
}

iter_fractals = ["mandelbrot", "mandelbar", "phoenix_fractal", "lambda_fractal", "julia", "burning_ship", "buffalo_fractal", "newton_fractal"]

button_style = {'normal': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK), 'hover': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK),
                'press': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK), 'disabled': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK)}
big_button_style = {'normal': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26), 'hover': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26),
                'press': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26), 'disabled': UITextureButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, font_size=26)}

dropdown_style = {'normal': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(128, 128, 128)), 'hover': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(49, 154, 54)),
                  'press': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(128, 128, 128)), 'disabled': UIFlatButtonStyle(font_name="Roboto", font_color=arcade.color.BLACK, bg=Color(128, 128, 128))}

slider_default_style = UISliderStyle(bg=Color(128, 128, 128), unfilled_track=Color(128, 128, 128), filled_track=Color(49, 154, 54))
slider_hover_style = UISliderStyle(bg=Color(49, 154, 54), unfilled_track=Color(128, 128, 128), filled_track=Color(49, 154, 54))

slider_style = {'normal': slider_default_style, 'hover': slider_hover_style, 'press': slider_hover_style, 'disabled': slider_default_style}

settings = {
    "Mandelbrot": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "mandelbrot_precision", "default": "Single"},
        "N": {"type": "slider", "min": 1, "max": 10, "config_key": "mandelbrot_n", "default": 2, "step": 1},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "mandelbrot_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "mandelbrot_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "mandelbrot_max_iter", "default": 200, "step": 100}
    },
    "Mandelbar": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "mandelbar_precision", "default": "Single"},
        "N": {"type": "slider", "min": 1, "max": 10, "config_key": "mandelbar_n", "default": 2, "step": 1},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "mandelbar_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "mandelbar_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "mandelbar_max_iter", "default": 200, "step": 100}
    },
    "Burning Ship": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "burning_ship_precision", "default": "Single"},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "burning_ship_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "burning_ship_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "burning_ship_max_iter", "default": 200, "step": 100}
    },
    "Buffalo Fractal": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "buffalo_fractal_precision", "default": "Single"},
        "N": {"type": "slider", "min": 1, "max": 10, "config_key": "buffalo_fractal_n", "default": 2, "step": 1},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "buffalo_fractal_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "buffalo_fractal_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "buffalo_fractal_max_iter", "default": 200, "step": 100}
    },
    "Phoenix Fractal": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "phoenix_fractal_precision", "default": "Single"},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "phoenix_fractal_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "phoenix_fractal_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "phoenix_fractal_max_iter", "default": 200, "step": 100}
    },
    "Lambda Fractal": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "phoenix_fractal_precision", "default": "Single"},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "phoenix_fractal_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "phoenix_fractal_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "phoenix_fractal_max_iter", "default": 200, "step": 100}
    },
    "Sierpinsky Carpet": {
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "sierpinsky_precision", "default": "Single"},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "sierpinsky_zoom_increase", "default": 2},
        "Depth": {"type": "slider", "min": 100, "max": 10000, "config_key": "sierpinsky_depth", "default": 100, "step": 100}
    },
    "Julia": {
        "Type": {"type": "option", "options": ["Classic swirling", "Douady rabbit", "Nebula-style", "Snowflake"], "config_key": "julia_type", "default": "Classic swirling"},
        "Float Precision": {"type": "option", "options": ["Single", "Double"], "config_key": "julia_precision", "default": "Single"},
        "N": {"type": "slider", "min": 1, "max": 10, "config_key": "julia_n", "default": 2, "step": 1},
        "Escape Radius": {"type": "slider", "min": 1, "max": 10, "config_key": "julia_escape_radius", "default": 2, "step": 0.1},
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "julia_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 4000, "config_key": "julia_max_iter", "default": 200, "step": 100}
    },
    "Newton Fractal": {
        "Zoom Increase Per Click": {"type": "slider", "min": 2, "max": 100, "config_key": "newton_fractal_zoom_increase", "default": 2},
        "Max Iterations": {"type": "slider", "min": 100, "max": 10000, "config_key": "newton_fractal_max_iter", "default": 200, "step": 100}
    },
    "Graphics": {
        "Window Mode": {"type": "option", "options": ["Windowed", "Fullscreen", "Borderless"], "config_key": "window_mode", "default": "Windowed"},
        "Resolution": {"type": "option", "options": ["1366x768", "1440x900", "1600x900", "1920x1080", "2560x1440", "3840x2160"], "config_key": "resolution"},
        "Anti-Aliasing": {"type": "option", "options": ["None", "2x MSAA", "4x MSAA", "8x MSAA", "16x MSAA"], "config_key": "anti_aliasing", "default": "4x MSAA"},
        "VSync": {"type": "bool", "config_key": "vsync", "default": True},
        "FPS Limit": {"type": "slider", "min": 0, "max": 480, "config_key": "fps_limit", "default": 60, "step": 10},
    },
    "Miscellaneous": {
        "Discord RPC": {"type": "bool", "config_key": "discord_rpc", "default": True},
    },
    "Credits": {}
}
settings_start_category = "Mandelbrot"

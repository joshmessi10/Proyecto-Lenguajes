def create_canvas(width=80, height=20):
    return [[" " for _ in range(width + 6)] for _ in range(height + 3)]


def plot_point(canvas, x, y, char="*"):
    height = len(canvas) - 2  # espacio para ejes
    width = len(canvas[0]) - 6  # espacio para etiquetas
    canvas_y = height - int(round(y)) - 1
    canvas_x = int(round(x))
    if 0 <= canvas_x < width and 0 <= canvas_y < height:
        canvas[canvas_y][canvas_x + 6] = char  # desplazamiento para eje Y


def draw_axes(canvas, width=80, height=20, x_ticks=10, y_ticks=5):
    for y in range(height):
        canvas[y][5] = "|"
    for x in range(width):
        canvas[height][x + 6] = "-"

    # Etiquetas Y
    for i in range(y_ticks + 1):
        y_val = int(i * height / y_ticks)
        label = str(i * height // y_ticks).rjust(2)
        canvas[height - y_val - 1][0:3] = list(label)
        canvas[height - y_val - 1][4] = "-"

    # Etiquetas X
    for i in range(x_ticks + 1):
        x_val = int(i * width / x_ticks)
        label = str(x_val).rjust(3)
        for j, ch in enumerate(label):
            if x_val + 6 + j < len(canvas[0]) and height + 1 < len(canvas):
                canvas[height + 1][x_val + 6 + j] = ch

def draw_canvas(canvas):
    for row in canvas:
        print("".join(row))


def plot_line(canvas, x0, y0, x1, y1, char="*"):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = int(round(x0)), int(round(y0))
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    if dx > dy:
        err = dx / 2.0
        while x != int(round(x1)):
            plot_point(canvas, x, y, char)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != int(round(y1)):
            plot_point(canvas, x, y, char)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy
    plot_point(canvas, x, y, char)

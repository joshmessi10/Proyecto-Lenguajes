#graph.py

def create_canvas(width=80, height=20):
    return [[" " for _ in range(width + 6)] for _ in range(height + 3)]


def plot_point(canvas, x, y, char="*"):
    height = len(canvas) - 2  # espacio para ejes
    width = len(canvas[0]) - 6  # espacio para etiquetas
    canvas_y = height - int(round(y)) - 1
    canvas_x = int(round(x))
    if 0 <= canvas_x < width and 0 <= canvas_y < height:
        canvas[canvas_y][canvas_x + 6] = char  # desplazamiento para eje Y


def draw_axes(canvas, width=80, height=20, x_ticks=10, y_ticks=5, x_min=0, x_max=1, y_min=0, y_max=1):
    for y in range(height):
        canvas[y][5] = "|"
    for x in range(width):
        canvas[height][x + 6] = "-"

    # Etiquetas Y reales
    for i in range(y_ticks + 1):
        frac = i / y_ticks
        val = y_max - frac * (y_max - y_min)
        label = f"{val:.0f}".rjust(3)
        row = int(frac * (height - 1))
        canvas[row][0:3] = list(label)
        canvas[row][4] = "-"

    # Etiquetas X reales
    for i in range(x_ticks + 1):
        frac = i / x_ticks
        val = x_min + frac * (x_max - x_min)
        col = int(frac * (width - 1))
        label = f"{val:.0f}".rjust(3)
        for j, ch in enumerate(label):
            if col + 6 + j < len(canvas[0]):
                canvas[height + 1][col + 6 + j] = ch

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

def draw_title(canvas, title):
    # Dibuja el título centrado en la primera fila del canvas
    width = len(canvas[0])
    title_len = len(title)
    start_col = max((width - title_len) // 2, 0)
    for i, ch in enumerate(title):
        if 0 <= start_col + i < width:
            canvas[0][start_col + i] = ch

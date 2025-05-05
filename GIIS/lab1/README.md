
# Лабораторная работа №1. Разработка графического редактора для построения отрезков

## Цель работы

Разработать элементарный графический редактор, реализующий построение отрезков с использованием алгоритмов ЦДА, Брезенхема и Ву. Редактор должен предоставлять возможность выбора алгоритма через меню и панель инструментов, а также иметь отладочный режим с пошаговым отображением процесса построения на дискретной сетке.

## Задачи

1.  Реализовать алгоритм ЦДА для построения отрезков.
2.  Реализовать целочисленный алгоритм Брезенхема для построения отрезков.
3.  Реализовать алгоритм Ву для построения отрезков.
4.  Создать графический интерфейс с использованием библиотеки Tkinter.
5.  Предусмотреть выбор алгоритма построения отрезка через меню и панель инструментов.
6.  Реализовать отладочный режим с пошаговым отображением построения отрезка на дискретной сетке.
7.  Обеспечить возможность переключения между алгоритмами в отладочном режиме.

## Используемые алгоритмы

### 1. Алгоритм ЦДА (Digital Differential Analyzer)

Алгоритм ЦДА является простым алгоритмом построчного сканирования, который вычисляет координаты точек отрезка, используя дифференциальные уравнения.

#### Описание алгоритма

1.  Определяются начальные и конечные координаты отрезка: `(x1, y1)` и `(x2, y2)`.
2.  Вычисляются разности: `dx = x2 - x1` и `dy = y2 - y1`.
3.  Определяется количество шагов: `steps = max(abs(dx), abs(dy))`.
4.  Вычисляются инкременты: `x_increment = dx / steps` и `y_increment = dy / steps`.
5.  Для каждого шага, начиная с `(x1, y1)`:
    *   `x = x + x_increment`
    *   `y = y + y_increment`
    *   Рисуется пиксель с координатами `(round(x), round(y))`.



### 2.Алгоритм Брезенхема: Эффективное построение линий

## Описание

Алгоритм Брезенхема - это эффективный алгоритм построения линий на растровых устройствах (например, экранах мониторов), использующий только целочисленные вычисления. Он был разработан Джеком Э. Брезенхемом в 1962 году.  Алгоритм широко применяется в компьютерной графике, поскольку позволяет быстро и точно рисовать линии без использования дорогостоящих операций с плавающей точкой.

## Принцип работы

Основная идея алгоритма Брезенхема заключается в том, чтобы на каждом шаге выбирать ближайший пиксель к идеальной линии, используя только целочисленные операции.  Алгоритм избегает вычислений с плавающей точкой, что делает его значительно быстрее, чем другие алгоритмы построения линий, такие как алгоритм ЦДА (DDA).

Алгоритм работает следующим образом:

1.  **Определение начальных и конечных точек:** Задаются координаты начальной точки `(x1, y1)` и конечной точки `(x2, y2)` линии.

2.  **Вычисление разностей и приращений:**
    *   `dx = abs(x2 - x1)` - разность по оси X.
    *   `dy = abs(y2 - y1)` - разность по оси Y.
    *   `sx = 1 if x1 < x2 else -1` - знак приращения по оси X (определяет направление движения по X).
    *   `sy = 1 if y1 < y2 else -1` - знак приращения по оси Y (определяет направление движения по Y).

3.  **Определение "ведущей" оси:**  Определяется, какая ось имеет большую разность (dx или dy).  Если `dy > dx`, то ось Y является "ведущей", и происходит перестановка координат и знаков приращения (это позволяет упростить логику алгоритма).

4.  **Вычисление параметра ошибки:**  Вычисляется начальное значение параметра ошибки: `error = 2 * dy - dx`.  Этот параметр используется для принятия решения о том, какой пиксель выбрать на каждом шаге.

5.  **Итеративный процесс:**  Для каждой точки линии выполняется следующее:
    *   Рисуется пиксель с текущими координатами `(x, y)`.
    *   Если `error > 0`, то:
        *   `y = y + sy` (двигаемся по оси Y).
        *   `error = error - 2 * dx` (корректируем параметр ошибки).
    *   `x = x + sx` (двигаемся по оси X).
    *   `error = error + 2 * dy` (корректируем параметр ошибки).

6.  **Завершение:**  Процесс повторяется, пока не будет достигнута конечная точка линии.





#### Реализация

```python
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import math

class LineEditor:
    def __init__(self, master):
        self.master = master
        master.title("Графический редактор")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(expand=True, fill="both")

        self.cda_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.cda_tab, text="ЦДА")
        self.cda_canvas_width = 800
        self.cda_canvas_height = 600
        self.cda_canvas = tk.Canvas(self.cda_tab, width=self.cda_canvas_width, height=self.cda_canvas_height, bg='white')
        self.cda_canvas.pack()
        self.cda_start_x = None
        self.cda_start_y = None
        self.cda_canvas.bind("<Button-1>", self.on_cda_click)
        self.cda_canvas.bind("<B1-Motion>", self.on_cda_drag)
        self.cda_canvas.bind("<ButtonRelease-1>", self.on_cda_release)
        self.cda_status_label = tk.Label(self.cda_tab, text="Кликните для начала отрезка (ЦДА)")
        self.cda_status_label.pack()

        self.bresenham_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.bresenham_tab, text="Брезенхем")
        self.bresenham_canvas_width = 800
        self.bresenham_canvas_height = 600
        self.bresenham_canvas = tk.Canvas(self.bresenham_tab, width=self.bresenham_canvas_width, height=self.bresenham_canvas_height, bg='white')
        self.bresenham_canvas.pack()
        self.bresenham_start_x = None
        self.bresenham_start_y = None
        self.bresenham_canvas.bind("<Button-1>", self.on_bresenham_click)
        self.bresenham_canvas.bind("<B1-Motion>", self.on_bresenham_drag)
        self.bresenham_canvas.bind("<ButtonRelease-1>", self.on_bresenham_release)
        self.bresenham_status_label = tk.Label(self.bresenham_tab, text="Кликните для начала отрезка (Брезенхем)")
        self.bresenham_status_label.pack()

        self.wu_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.wu_tab, text="Ву")
        self.wu_canvas_width = 800
        self.wu_canvas_height = 600
        self.wu_canvas = tk.Canvas(self.wu_tab, width=self.wu_canvas_width, height=self.wu_canvas_height, bg='white')
        self.wu_canvas.pack()
        self.wu_start_x = None
        self.wu_start_y = None
        self.wu_canvas.bind("<Button-1>", self.on_wu_click)
        self.wu_canvas.bind("<B1-Motion>", self.on_wu_drag)
        self.wu_canvas.bind("<ButtonRelease-1>", self.on_wu_release)
        self.wu_status_label = tk.Label(self.wu_tab, text="Кликните для начала отрезка (Ву)")
        self.wu_status_label.pack()

        self.debug_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.debug_tab, text="Отладка")
        self.debug_canvas_width = 400
        self.debug_canvas_height = 300
        self.debug_canvas = tk.Canvas(self.debug_tab, width=self.debug_canvas_width, height=self.debug_canvas_height, bg='white')
        self.debug_canvas.pack()

        self.grid_spacing = 20
        self.draw_grid()

        self.debug_points = []
        self.debug_start_x = None
        self.debug_start_y = None
        self.debug_end_x = None
        self.debug_end_y = None
        self.debug_canvas.bind("<Button-1>", self.on_debug_click)
        self.debug_canvas.bind("<ButtonRelease-1>", self.on_debug_release)
        self.debug_status_label = tk.Label(self.debug_tab, text="Кликните для начала отрезка (Отладка)")
        self.debug_status_label.pack()

        self.algorithm_var = tk.StringVar(value="cda")
        self.cda_radio = tk.Radiobutton(self.debug_tab, text="ЦДА", variable=self.algorithm_var, value="cda")
        self.bresenham_radio = tk.Radiobutton(self.debug_tab, text="Брезенхем", variable=self.algorithm_var, value="bresenham")
        self.wu_radio = tk.Radiobutton(self.debug_tab, text="Ву", variable=self.algorithm_var, value="wu")
        self.cda_radio.pack()
        self.bresenham_radio.pack()
        self.wu_radio.pack()

    def draw_grid(self):
        """Рисует сетку на канве отладки."""
        width = self.debug_canvas_width
        height = self.debug_canvas_height
        spacing = self.grid_spacing

        for x in range(spacing, width, spacing):
            self.debug_canvas.create_line(x, 0, x, height, fill="lightgray", width=1)

        for y in range(spacing, height, spacing):
            self.debug_canvas.create_line(0, y, width, y, fill="lightgray", width=1)

        self.debug_canvas.create_line(0, self.debug_canvas_height / 2, self.debug_canvas_width, self.debug_canvas_height / 2, fill="gray", width=1.5)
        self.debug_canvas.create_line(self.debug_canvas_width / 2, 0, self.debug_canvas_width / 2, self.debug_canvas_height, fill="gray", width=1.5)

    def cda_line(self, x1, y1, x2, y2, debug=False):
        """Алгоритм ЦДА для построения отрезка."""
        dx = x2 - x1
        dy = y2 - y1
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        x = int(x1)
        y = int(y1)
        points = [(x, y)]

        if debug:
            self.debug_points = []
            self.debug_canvas.delete("all")
            self.draw_grid()
            self.debug_canvas.create_oval(self.scale_x(x1) - 5, self.scale_y(y1) - 5, self.scale_x(x1) + 5, self.scale_y(y1) + 5, fill="green")
            self.debug_canvas.create_oval(self.scale_x(x2) - 5, self.scale_y(y2) - 5, self.scale_x(x2) + 5, self.scale_y(y2) + 5, fill="red")

        if dx == 0 and dy == 0:
            return points

        if abs(dy) > abs(dx):
            dx, dy = abs(dy), abs(dx)
            steep = True
        else:
            dx, dy = abs(dx), abs(dy)
            steep = False

        error = dx / 2

        for i in range(dx):
            if steep:
                y += sy
            else:
                x += sx

            if error >= dy:
                if steep:
                    x += sx
                else:
                    y += sy
                error -= dx
            error += dy

            if debug:
                grid_x = round(x / self.grid_spacing) * self.grid_spacing
                grid_y = round(y / self.grid_spacing) * self.grid_spacing
                points.append((grid_x, grid_y))
                self.debug_points.append((grid_x, grid_y))
                self.update_debug_canvas(grid_x, grid_y, color="blue")
                self.master.after(50)
                self.master.update()
            else:
                points.append((x, y))

        return points

    def bresenham_line(self, x1, y1, x2, y2, debug=False):
        """Алгоритм Брезенхема для построения отрезка."""
        points = []
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        sx = 1 if x1 < x2 else -1
        sy = 1 if y1 < y2 else -1
        x = int(x1)
        y = int(y1)

        is_steep = dy > dx
        if is_steep:
            dx, dy = dy, dx
            x, y = y, x
            sx, sy = sy, sx

        error = 2 * dy - dx

        for i in range(dx + 1):
            if is_steep:
                if debug:
                    grid_x = round(y / self.grid_spacing) * self.grid_spacing
                    grid_y = round(x / self.grid_spacing) * self.grid_spacing
                    points.append((grid_x, grid_y))
                    self.debug_points.append((grid_x, grid_y))
                    self.update_debug_canvas(grid_x, grid_y, color="green")
                else:
                    points.append((y, x))
            else:
                if debug:
                    grid_x = round(x / self.grid_spacing) * self.grid_spacing
                    grid_y = round(y / self.grid_spacing) * self.grid_spacing
                    points.append((grid_x, grid_y))
                    self.debug_points.append((grid_x, grid_y))
                    self.update_debug_canvas(grid_x, grid_y, color="green")
                else:
                    points.append((x, y))

            if debug:
                self.master.after(50)
                self.master.update()

            if error > 0:
                y += sy
                error -= 2 * dx
            x += sx
            error += 2 * dy
        return points

    def wu_line(self, x1, y1, x2, y2, debug=False):
        """Алгоритм Ву для построения отрезка."""
        points = []
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)

        steep = abs(y2 - y1) > abs(x2 - x1)
        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0.0: 
            for y in range(int(min(y1, y2)), int(max(y1, y2)) + 1):
                points.append((x1, y, 1.0))  
        elif dy == 0.0: 
            for x in range(int(min(x1, x2)), int(max(x1, x2)) + 1):
                points.append((x, y1, 1.0))
        else:
            gradient = dy / dx

            xend = round(x1)
            yend = y1 + gradient * (xend - x1)
            xgap = self.rfpart(x1 + 0.5)
            xpxl1 = xend
            ypxl1 = int(yend)
            intensity1 = self.rfpart(yend) * xgap
            intensity2 = self.fpart(yend) * xgap
            if steep:
                points.append((ypxl1, xpxl1, intensity1))
                points.append((ypxl1 + 1, xpxl1, intensity2))
            else:
                points.append((xpxl1, ypxl1, intensity1))
                points.append((xpxl1, ypxl1 + 1, intensity2))

            intery = yend + gradient  

            xend = round(x2)
            yend = y2 + gradient * (xend - x2)
            xgap = self.fpart(x2 + 0.5)
            xpxl2 = xend
            ypxl2 = int(yend)
            intensity1 = self.rfpart(yend) * xgap
            intensity2 = self.fpart(yend) * xgap
            if steep:
                points.append((ypxl2, xpxl2, intensity1))
                points.append((ypxl2 + 1, xpxl2, intensity2))
            else:
                points.append((xpxl2, ypxl2, intensity1))
                points.append((xpxl2, ypxl2 + 1, intensity2))

            if steep:
                for x in range(xpxl1 + 1, xpxl2):
                    intensity1 = self.rfpart(intery)
                    intensity2 = self.fpart(intery)
                    points.append((int(intery), x, intensity1))
                    points.append((int(intery) + 1, x, intensity2))
                    intery += gradient
            else:
                for x in range(xpxl1 + 1, xpxl2):
                    intensity1 = self.rfpart(intery)
                    intensity2 = self.fpart(intery)
                    points.append((x, int(intery), intensity1))
                    points.append((x, int(intery) + 1, intensity2))
                    intery += gradient

        if debug:
            self.debug_points = []
            self.debug_canvas.delete("all")
            self.draw_grid()
            self.debug_canvas.create_oval(self.scale_x(x1) - 5, self.scale_y(y1) - 5, self.scale_x(x1) + 5, self.scale_y(y1) + 5, fill="green")
            self.debug_canvas.create_oval(self.scale_x(x2) - 5, self.scale_y(y2) - 5, self.scale_x(x2) + 5, self.scale_y(y2) - 5, fill="red")

            for point in points:
                x, y, intensity = point
                grid_x = round(x / self.grid_spacing) * self.grid_spacing
                grid_y = round(y / self.grid_spacing) * self.grid_spacing

                self.debug_points.append((grid_x, grid_y, intensity))
                self.update_debug_canvas(grid_x, grid_y, color=self.intensity_to_hex(intensity))
                self.master.after(1)
                self.master.update()

        return points

    def fpart(self, x):
        """Возвращает дробную часть числа."""
        return x - math.floor(x)

    def rfpart(self, x):
        """Возвращает 1 - дробная часть числа."""
        return 1 - self.fpart(x)

    def draw_line(self, x1, y1, x2, y2, canvas, algorithm="cda", debug=False):
        """Рисует отрезок на канве, используя выбранный алгоритм."""
        if algorithm == "cda":
            points = self.cda_line(x1, y1, x2, y2, debug)
        elif algorithm == "bresenham":
            points = self.bresenham_line(x1, y1, x2, y2, debug)
        elif algorithm == "wu":
            points = self.wu_line(x1, y1, x2, y2, debug)
            for point in points:
                x, y, intensity = point
                canvas.create_rectangle(x, y, x + 1, y + 1, fill=self.intensity_to_hex(intensity), outline='')
            return

        for x, y in points:
            canvas.create_rectangle(x, y, x + 1, y + 1, fill='black', outline='')

    def intensity_to_hex(self, intensity):
        """Преобразует интенсивность (от 0 до 1) в hex-цвет."""
        gray_scale = int(intensity * 255)
        hex_value = hex(gray_scale)[2:].zfill(2)
        return f'#{hex_value}{hex_value}{hex_value}'

    def on_cda_click(self, event):
        """Обработчик нажатия кнопки мыши (ЦДА)."""
        self.cda_start_x = event.x
        self.cda_start_y = event.y
        self.cda_status_label.config(text="Кликните для начала отрезка (ЦДА)")

    def on_cda_drag(self, event):
        """Обработчик движения мыши с нажатой кнопкой (ЦДА)."""
        pass

    def on_cda_release(self, event):
        """Обработчик отпускания кнопки мыши (ЦДА)."""
        if self.cda_start_x is not None and self.cda_start_y is not None:
            end_x = event.x
            end_y = event.y
            self.draw_line(self.cda_start_x, self.cda_start_y, end_x, end_y, self.cda_canvas, algorithm="cda")
            self.cda_start_x = None
            self.cda_start_y = None
            self.cda_status_label.config(text="Кликните для начала нового отрезка (ЦДА)")

    def on_bresenham_click(self, event):
        """Обработчик нажатия кнопки мыши (Брезенхем)."""
        self.bresenham_start_x = event.x
        self.bresenham_start_y = event.y
        self.bresenham_status_label.config(text="Кликните для начала отрезка (Брезенхем)")

    def on_bresenham_drag(self, event):
        """Обработчик движения мыши с нажатой кнопкой (Брезенхем)."""
        pass

    def on_bresenham_release(self, event):
        """Обработчик отпускания кнопки мыши (Брезенхем)."""
        if self.bresenham_start_x is not None and self.bresenham_start_y is not None:
            end_x = event.x
            end_y = event.y
            self.draw_line(self.bresenham_start_x, self.bresenham_start_y, end_x, end_y, self.bresenham_canvas, algorithm="bresenham")
            self.bresenham_start_x = None
            self.bresenham_start_y = None
            self.bresenham_status_label.config(text="Кликните для начала нового отрезка (Брезенхем)")

    def on_wu_click(self, event):
        """Обработчик нажатия кнопки мыши (Ву)."""
        self.wu_start_x = event.x
        self.wu_start_y = event.y
        self.wu_status_label.config(text="Кликните для начала отрезка (Ву)")

    def on_wu_drag(self, event):
        """Обработчик движения мыши с нажатой кнопкой (Ву)."""
        pass

    def on_wu_release(self, event):
        """Обработчик отпускания кнопки мыши (Ву)."""
        if self.wu_start_x is not None and self.wu_start_y is not None:
            end_x = event.x
            end_y = event.y
            self.draw_line(self.wu_start_x, self.wu_start_y, end_x, end_y, self.wu_canvas, algorithm="wu")
            self.wu_start_x = None
            self.wu_start_y = None
            self.wu_status_label.config(text="Кликните для начала нового отрезка (Ву)")

    def on_debug_click(self, event):
        """Обработчик нажатия кнопки мыши (Отладка)."""
        self.debug_start_x = round((event.x - self.debug_canvas_width / 2) / self.grid_spacing) * self.grid_spacing
        self.debug_start_y = round((self.debug_canvas_height / 2 - event.y) / self.grid_spacing) * self.grid_spacing
        self.debug_status_label.config(text="Кликните для конца отрезка (Отладка)")

    def on_debug_release(self, event):
        """Обработчик отпускания кнопки мыши (Отладка)."""
        if self.debug_start_x is not None and self.debug_start_y is not None:
            end_x = round((event.x - self.debug_canvas_width / 2) / self.grid_spacing) * self.grid_spacing
            end_y = round((self.debug_canvas_height / 2 - event.y) / self.grid_spacing) * self.grid_spacing
            algorithm = self.algorithm_var.get()
            self.draw_line(self.debug_start_x, self.debug_start_y, end_x, end_y, self.debug_canvas, algorithm=algorithm, debug=True)
            self.debug_start_x = None
            self.debug_start_y = None
            self.debug_status_label.config(text="Кликните для начала отрезка (Отладка)")

    def update_debug_canvas(self, x, y, color="blue"):
        """Отображает текущую точку на канве отладки."""
        self.debug_canvas.create_rectangle(self.scale_x(x) - 5, self.scale_y(y) - 5, self.scale_x(x) + 5, self.scale_y(y) + 5, fill=color, outline='')

    def scale_x(self, x):
        """Масштабирует координату X для отображения в окне отладки."""
        return x + self.debug_canvas_width / 2

    def scale_y(self, y):
        """Масштабирует координату Y для отображения в окне отладки."""
        return self.debug_canvas_height / 2 - y

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

debug_canvas_width = screen_width // 2
debug_canvas_height = screen_height // 2

root.geometry(f"{screen_width}x{screen_height}")

editor = LineEditor(root)

editor.debug_canvas_width = debug_canvas_width
editor.debug_canvas_height = debug_canvas_height
editor.debug_canvas.config(width=debug_canvas_width, height=debug_canvas_height)

editor.draw_grid()

root.mainloop()

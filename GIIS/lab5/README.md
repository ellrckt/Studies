<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Графический редактор</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f6f8;
        }

        header {
            background-color: #2c3e50;
            color: white;
            padding: 15px 20px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }

        #container {
            display: flex;
            padding: 20px;
            gap: 20px;
        }

        #canvasContainer {
            flex-grow: 1;
        }

        canvas {
            width: 100%;
            height: auto;
            max-height: 800px;
            border: 2px solid #ccc;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        #toolPanel {
            width: 300px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 20px;
        }

        .toolGroup {
            margin-bottom: 20px;
        }

        .toolGroup h3 {
            margin-top: 0;
            margin-bottom: 10px;
            font-size: 16px;
            color: #333;
        }

        .button {
            display: block;
            width: 100%;
            padding: 12px;
            font-size: 14px;
            font-weight: bold;
            color: white;
            background-color: #3498db;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            margin-bottom: 10px;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: #2980b9;
        }

        .button:active {
            background-color: #2573a6;
        }
    </style>
</head>
<body>

<header>Графический редактор — Лабораторная работа №5</header>

<div id="container">
    <div id="canvasContainer">
        <canvas id="cnv" width="1300" height="800"></canvas>
    </div>
    <div id="toolPanel">
        <div class="toolGroup">
            <h3>Проверка полигона</h3>
            <button class="button" onclick="checkConvexity()">Проверить на выпуклость</button>
            <button class="button" onclick="calculateNormals()">Рассчитать нормали</button>
        </div>
        <div class="toolGroup">
            <h3>Выпуклая оболочка</h3>
            <button class="button" onclick="computeConvexHullGraham()">Метод Грэхема</button>
            <button class="button" onclick="computeConvexHullJarvis()">Метод Джарвиса</button>
        </div>
        <div class="toolGroup">
            <h3>Дополнительно</h3>
            <button class="button" onclick="clearApp()">Очистить всё</button>
        </div>
    </div>
</div>

<script defer src="main.js"></script>

</body>
</html>

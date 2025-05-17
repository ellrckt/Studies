const canvas = document.getElementById("cnv");
const ctx = canvas.getContext("2d");
let points = [];

function drawCross(x, y) {
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x - 10, y);
    ctx.lineTo(x + 10, y);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x, y - 10);
    ctx.lineTo(x, y + 10);
    ctx.stroke();
}

function drawLine(x1, y1, x2, y2, color = "black") {
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}

function getOrientation(p1, p2, p3) {
    const val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1]);
    return val === 0 ? 0 : val > 0 ? 1 : -1;
}

function checkConvexity() {
    if (points.length < 3) {
        alert("Минимальное количество точек для проверки выпуклости: 3");
        return;
    }

    let orientation = null;
    for (let i = 0; i < points.length; i++) {
        const p1 = points[i];
        const p2 = points[(i + 1) % points.length];
        const p3 = points[(i + 2) % points.length];

        const currentOrientation = getOrientation(p1, p2, p3);

        if (currentOrientation === 0) continue;

        if (orientation === null) {
            orientation = currentOrientation;
        } else if (currentOrientation !== orientation) {
            alert("Полигон НЕ является выпуклым");
            return;
        }
    }

    if (orientation === null) {
        alert("Все точки коллинеарны");
    } else {
        alert("Полигон является выпуклым");
    }
}

function drawPolygon() {
    if (points.length === 0) return;

    for (const point of points) {
        drawCross(point[0], point[1]);
    }

    for (let i = 0; i < points.length; i++) {
        const curr = points[i];
        const next = points[(i + 1) % points.length];
        drawLine(curr[0], curr[1], next[0], next[1], "black");
    }
}

function computeConvexHullGraham() {
    if (points.length < 3) {
        alert("Минимальное количество точек для вычисления выпуклой оболочки: 3");
        return;
    }

    const sortedPoints = [...points].sort((a, b) => a[1] !== b[1] ? a[1] - b[1] : a[0] - b[0]);

    const hull = [];
    for (let i = 0; i < sortedPoints.length; i++) {
        while (hull.length >= 2 && getOrientation(hull[hull.length - 2], hull[hull.length - 1], sortedPoints[i]) !== -1) {
            hull.pop();
        }
        hull.push(sortedPoints[i]);
    }

    for (let i = 0; i < hull.length - 1; i++) {
        drawLine(hull[i][0], hull[i][1], hull[i + 1][0], hull[i + 1][1], "purple");
    }
    drawLine(hull[0][0], hull[0][1], hull[hull.length - 1][0], hull[hull.length - 1][1], "purple");
}

function computeConvexHullJarvis() {
    if (points.length < 3) {
        alert("Минимальное количество точек для вычисления выпуклой оболочки: 3");
        return;
    }

    let leftmost = points[0];
    for (let i = 1; i < points.length; i++) {
        if (points[i][0] < leftmost[0]) {
            leftmost = points[i];
        }
    }

    const hull = [];
    let p = leftmost;
    do {
        hull.push(p);
        let q = points[0];
        for (let j = 1; j < points.length; j++) {
            if (getOrientation(p, q, points[j]) === -1) {
                q = points[j];
            }
        }
        p = q;
    } while (p !== leftmost);

    for (let i = 0; i < hull.length - 1; i++) {
        drawLine(hull[i][0], hull[i][1], hull[i + 1][0], hull[i + 1][1], "DeepPink");
    }
    drawLine(hull[0][0], hull[0][1], hull[hull.length - 1][0], hull[hull.length - 1][1], "DeepPink");
}

function calculateNormals() {
    if (points.length < 3) {
        alert("Минимальное количество точек для расчета нормалей: 3");
        return;
    }

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPolygon();

    for (let i = 0; i < points.length; i++) {
        const curr = points[i];
        const next = points[(i + 1) % points.length];

        const dx = next[0] - curr[0];
        const dy = next[1] - curr[1];
        const length = Math.sqrt(dx * dx + dy * dy);
        const nx = -dy / length;
        const ny = dx / length;

        const normStartX = curr[0] + nx * 50;
        const normStartY = curr[1] + ny * 50;
        const normEndX = curr[0] - nx * 50;
        const normEndY = curr[1] - ny * 50;

        drawLine(normStartX, normStartY, normEndX, normEndY, "green");
    }
}

canvas.addEventListener("click", function(event) {
    const x = event.offsetX;
    const y = event.offsetY;

    points.push([x, y]);

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawPolygon();
});

function clearApp() {
    points = [];
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

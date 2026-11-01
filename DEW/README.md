<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Nginx + ngx_small_light</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f2f2;
            display: flex;
            justify-content: center;
            padding: 40px;
        }

        .container {
            width: 900px;
            background: white;
            border: 2px solid #ccc;
            padding: 20px;
            display: flex;
            gap: 20px;
        }

        .sidebar {
            width: 180px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .sidebar img {
            width: 100%;
            border: 4px solid #d58bf4;
            border-radius: 10px;
        }

        .main {
            flex: 1;
            text-align: center;
        }

        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }

        .form-group {
            margin: 10px 0;
        }

        label {
            display: block;
            text-align: left;
            font-weight: bold;
        }

        input {
            width: 100px;
            padding: 5px;
        }

        select {
            padding: 5px;
        }

        #btnGenerar {
            background: yellow;
            padding: 10px 20px;
            cursor: pointer;
            border: 1px solid black;
            font-weight: bold;
            margin-top: 10px;
        }

        #preview {
            margin-top: 20px;
            width: 280px;
            height: 280px;
            border: 4px solid black;
            object-fit: cover;
        }
    </style>

    <script>
        function generar() {
            const size = document.getElementById("size").value;
            const border = document.getElementById("border").value;
            const color = document.getElementById("color").value;
            const effect = document.getElementById("effect").value;
            const blur = document.getElementById("blur").value;
            const preview = document.getElementById("preview");

            // Construcción de URL small_light
            let url = `/images/image01.jpg?small_light=`;
            url += `w${size}`;
            url += `h${size}`;
            url += `bc${color}`;
            url += `bw${border}`;
            if (blur) url += `blur${blur}`;
            if (effect !== "none") url += `e${effect}`;

            preview.src = url;
        }
    </script>

</head>
<body>

<div class="container">

    <!-- Miniaturas -->
    <div class="sidebar">
        <img src="images/image01.jpg">
        <img src="images/image02.jpg">
        <img src="images/image03.jpg">
        <img src="images/image04.jpg">
        <img src="images/image05.jpg">
        <img src="images/image06.jpg">
        <img src="images/image07.jpg">
    </div>

    <!-- Panel principal -->
    <div class="main">
        <h1>Nginx + ngx_small_light</h1>

        <div class="form-group">
            <label>Tamaño</label>
            <input type="number" id="size" value="280">
        </div>

        <div class="form-group">
            <label>Ancho del borde</label>
            <input type="number" id="border" value="20">
        </div>

        <div class="form-group">
            <label>Color del borde</label>
            <input type="text" id="color" value="c04d4d">
        </div>

        <div class="form-group">
            <label>Efecto</label>
            <select id="effect">
                <option value="none">Ninguno</option>
                <option value="neg">Negativo</option>
                <option value="mono">Monocromo</option>
            </select>
        </div>

        <div class="form-group">
            <label>Desenfoque</label>
            <input type="number" id="blur" value="0">
        </div>

        <button id="btnGenerar" onclick="generar()">Generar</button>

        <img id="preview" src="images/image01.jpg">
    </div>

</div>

</body>
</html>

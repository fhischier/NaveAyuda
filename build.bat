@echo off
echo 🚀 Creando ejecutable para Windows...
echo.

REM Instalar PyInstaller si no está instalado
pip install pyinstaller

REM Crear el ejecutable
echo 📦 Creando TriviaClamers.exe...
pyinstaller --onefile --windowed --name "TriviaClamers" --add-data "assets;assets" main.py

echo.
echo ✅ ¡Listo! Tu archivo está en la carpeta dist/
echo 📁 Busca: dist\TriviaClamers.exe
echo.
echo 🎮 Puedes hacer doble clic para probarlo
echo 📤 Comparte el archivo .exe con quien quieras
echo.
pause

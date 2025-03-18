#!/bin/bash

# Variables
REPO_URL="https://github.com/LuisGrigore/SeekShell.git"  # Reemplázalo con tu repositorio real
INSTALL_DIR="$HOME/.seek_shell"
VENV_DIR="$INSTALL_DIR/venv"
EXECUTABLE_NAME="seek_shell"  # Reemplázalo con el nombre de tu herramienta

# Dependencias necesarias
echo "Instalando dependencias necesarias..."
sudo apt update && sudo apt install -y python3 python3-venv git

# Clonar el repositorio
echo "Descargando la herramienta..."
rm -rf "$INSTALL_DIR"
git clone "$REPO_URL" "$INSTALL_DIR"
mkdir "$INSTALL_DIR/persist"

# Crear entorno virtual e instalar dependencias
echo "Configurando el entorno virtual..."
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install -r "$INSTALL_DIR/requirements.txt"

# Crear un alias para ejecutar la herramienta desde cualquier lugar
echo "Creando acceso directo..."
echo "#!/bin/bash
source \"$VENV_DIR/bin/activate\"
python \"$INSTALL_DIR/src/main.py\" \"\$@\"" | sudo tee /usr/local/bin/$EXECUTABLE_NAME > /dev/null

# Dar permisos de ejecución
sudo chmod +x /usr/local/bin/$EXECUTABLE_NAME

echo "✅ Instalación completa. Usa '$EXECUTABLE_NAME' para ejecutar la herramienta."

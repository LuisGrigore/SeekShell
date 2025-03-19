#!/bin/bash

sudo apt install git

git clone https://github.com/LuisGrigore/SeekShell.git $HOME/SeekShell

# Definir variables
APP_NAME="seek-shell"
VENV_PATH="$HOME/.seek-shell-env"
BIN_PATH="$HOME/.local/bin/$APP_NAME"

# Crear entorno virtual si no existe
if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH"
fi

cp -r "$HOME/SeekShell"/* "$VENV_PATH"

# Instalar dependencias
"$VENV_PATH/bin/pip" install --upgrade pip
"$VENV_PATH/bin/pip" install -r $VENV_PATH/requirements.txt

# Crear el script ejecutable
mkdir -p "$HOME/.local/bin"
cat << EOF > "$BIN_PATH"
#!/bin/bash
$VENV_PATH/bin/python $VENV_PATH/seek_shell/main.py "\$@"
EOF

# Dar permisos de ejecución
chmod +x "$BIN_PATH"

# Agregar ~/.local/bin al PATH si no está
if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
    echo "export PATH=\"$HOME/.local/bin:\$PATH\"" >> "$HOME/.bashrc"
    echo "export PATH=\"$HOME/.local/bin:\$PATH\"" >> "$HOME/.zshrc"
fi

sudo rm -rf "$HOME/SeekShell"
echo "$APP_NAME instalado correctamente. Ejecuta 'seek-shell' desde cualquier parte."
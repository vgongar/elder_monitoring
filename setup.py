# HECHO POR GEMINI XD

import os
import sys
import subprocess
import platform
from pathlib import Path
import venv

# --- Configuración ---
ROOT_DIR = Path(__file__).parent.resolve()
VENV_NAME = ".venv"
VENV_PATH = ROOT_DIR / VENV_NAME
REQUIREMENTS_PATH = ROOT_DIR / "requirements.txt"

def get_pip_path():
    """Devuelve la ruta al ejecutable pip dentro del entorno virtual según el SO."""
    if platform.system() == "Windows":
        return VENV_PATH / "Scripts" / "pip.exe"
    else:
        # Mac / Linux
        return VENV_PATH / "bin" / "pip"

def run_command(command, description):
    """Ejecuta un comando en la terminal y maneja errores."""
    print(f"🔄 {description}...")
    try:
        subprocess.check_call(command)
        print("✅ Hecho.")
    except subprocess.CalledProcessError:
        print(f"❌ Error al ejecutar: {description}")
        sys.exit(1)

def main():
    print(f"🚀 Iniciando configuración del entorno en: {ROOT_DIR}")

    # 1. Crear entorno virtual
    if not VENV_PATH.exists():
        print(f"🔨 Creando entorno virtual '{VENV_NAME}'...")
        venv.create(VENV_PATH, with_pip=True)
        print("✅ Entorno creado.")
    else:
        print(f"ℹ️  El entorno '{VENV_NAME}' ya existe. Saltando creación.")

    # 2. Localizar el pip del entorno virtual
    pip_exe = str(get_pip_path())
    
    # 3. Actualizar pip (siempre es buena práctica)
    run_command([pip_exe, "install", "--upgrade", "pip"], "Actualizando pip")

    # 4. Instalar librerías
    if REQUIREMENTS_PATH.exists():
        run_command(
            [pip_exe, "install", "-r", str(REQUIREMENTS_PATH)], 
            "Instalando dependencias desde requirements.txt"
        )
    else:
        print("⚠️ No se encontró requirements.txt. Solo se ha creado el entorno vacío.")

    # 5. (Opcional) Instalar kernel para Jupyter
    # Esto ayuda a que VS Code detecte el entorno rápido
    print("🔄 Instalando soporte para Jupyter (ipykernel)...")
    try:
        subprocess.check_call([pip_exe, "install", "ipykernel"])
        print("✅ Kernel instalado.")
    except:
        print("⚠️ No se pudo instalar ipykernel (quizás no es necesario).")

    print("\n" + "="*40)
    print("🎉 ¡INSTALACIÓN COMPLETADA! 🎉")
    print("="*40)
    print("Para activar el entorno manualmente:")
    if platform.system() == "Windows":
        print(f"   {VENV_NAME}\\Scripts\\activate")
    else:
        print(f"   source {VENV_NAME}/bin/activate")

if __name__ == "__main__":
    main()

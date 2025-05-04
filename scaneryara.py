import yara
import os

# 1. Configurar las rutas
DESKTOP_PATH = os.path.expanduser("~/Desktop")  # Ruta al escritorio
MALWARE_FOLDER = os.path.join(DESKTOP_PATH, "malware")  # Carpeta con archivos sospechosos
RULES_PATH = os.path.join(DESKTOP_PATH, "rules-compiled")  # Archivo de reglas YARA compiladas

# 2. Cargar las reglas YARA compiladas
try:
    rules = yara.load(RULES_PATH)
    print(f"✅ Reglas YARA cargadas correctamente desde: {RULES_PATH}")
except Exception as e:
    print(f"❌ Error al cargar las reglas YARA: {e}")
    exit(1)

# 3. Escanear archivos en la carpeta 'malware'
print(f"\n🔍 Escaneando archivos en: {MALWARE_FOLDER}\n")

for filename in os.listdir(MALWARE_FOLDER):
    file_path = os.path.join(MALWARE_FOLDER, filename)
    
    if os.path.isfile(file_path):
        try:
            matches = rules.match(file_path)
            if matches:
                print(f"🚨 **Archivo sospechoso detectado**: {filename}")
                print(f"   🔗 Reglas que coinciden: {', '.join([match.rule for match in matches])}")
            else:
                print(f"✅ Archivo limpio: {filename}")
        except Exception as e:
            print(f"⚠️ Error al escanear {filename}: {e}")

print("\n✨ Escaneo completado.")
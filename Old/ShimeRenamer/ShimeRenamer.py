import os
import re

print("Starting ShimeRenamer...")  # Debug message

# Get the current directory where the script is running
folder = os.getcwd()
print(f"Current Directory: {folder}")  # Debug message

# Get all PNG files in the directory
files = [f for f in os.listdir(folder) if f.endswith(".png")]
print(f"Found files: {files}")  # Debug message

if not files:
    print("No PNG files found in the directory.")
else:
    # Rename each file
    for old_name in files:
        new_name = re.sub(r"(?<=shime)0+", "", old_name)  # Remove leading zeros after "shime"

        if old_name != new_name:
            old_path = os.path.join(folder, old_name)
            new_path = os.path.join(folder, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} -> {new_name}")
            except Exception as e:
                print(f"Failed to rename {old_name}: {e}")

print("Finished renaming files.")

# Pause before exiting
input("Press Enter to exit...")

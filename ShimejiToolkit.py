import os
import sys
import re
from PIL import Image

def image_sequence_renamer():
    """Rename PNG files in selected folder by removing leading zeros after 'shime', then rename 'shime.png' to 'shime47.png'"""
    # Get the directory of the script
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(__file__) or os.getcwd()

    while True:
        print("\n" + "="*60)
        print("IMAGE SEQUENCE RENAMER")
        print("="*60)

        # Get subfolders
        subfolders = get_subfolders(script_dir)

        if not subfolders:
            print("No folders found in the script directory.")
            break

        # Display folders
        print("\nAvailable folders:")
        for i, folder in enumerate(subfolders, 1):
            print(f"{i}. {folder}")

        print(f"{len(subfolders) + 1}. Exit")

        # Get user choice
        try:
            choice = input("\nSelect a folder (enter number): ").strip()
            choice_num = int(choice)

            if choice_num == len(subfolders) + 1:
                print("Exiting...")
                break

            if choice_num < 1 or choice_num > len(subfolders):
                print("Invalid choice. Please try again.")
                continue

            selected_folder = subfolders[choice_num - 1]
            folder = os.path.join(script_dir, selected_folder)

            print(f"Processing folder: {folder}")

            # Get all PNG files in the selected folder
            files = [f for f in os.listdir(folder) if f.endswith(".png")]
            print(f"Found files: {files}")

            if not files:
                print("No PNG files found in the selected folder.")
                input("\nPress Enter to continue...")
                continue

            # Rename each file by removing leading zeros after "shime"
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

            # After the renaming process, rename 'shime.png' to 'shime47.png' if it exists
            shime_path = os.path.join(folder, "shime.png")
            shime47_path = os.path.join(folder, "shime47.png")
            if os.path.exists(shime_path):
                try:
                    os.rename(shime_path, shime47_path)
                    print("Renamed: shime.png -> shime47.png")
                except Exception as e:
                    print(f"Failed to rename shime.png: {e}")

            print("Finished renaming files.")
            input("\nPress Enter to continue...")

        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")

def make_gif_from_sequence(folder_path, sequence, output_gif, fps=5):
    """Generate GIF from a sequence of images in the specified folder"""
    images = []
    for name in sequence:
        img_path = os.path.join(folder_path, f'{name}.png')
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image not found: {img_path}")
        img = Image.open(img_path).convert("RGBA")
        images.append(img)
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=int(1000/fps),
        loop=0,
        transparency=0,
        disposal=2
    )

def get_subfolders(path):
    """Get all subfolders in the given path"""
    try:
        subfolders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        return sorted(subfolders)
    except PermissionError:
        return []

def gif_thumbnail_maker():
    """Create GIF for individual shimeji folders"""
    # Get the directory of the script
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(__file__) or os.getcwd()

    sequence = ['shime2', 'shime47', 'shime3', 'shime47']
    fps = 5

    while True:
        print("\n" + "="*60)
        print("GIF THUMBNAIL MAKER")
        print("="*60)

        # Get subfolders
        subfolders = get_subfolders(script_dir)

        if not subfolders:
            print("No folders found in the script directory.")
            break

        # Display folders
        print("\nAvailable folders:")
        for i, folder in enumerate(subfolders, 1):
            print(f"{i}. {folder}")

        print(f"{len(subfolders) + 1}. Exit")

        # Get user choice
        try:
            choice = input("\nSelect a folder (enter number): ").strip()
            choice_num = int(choice)

            if choice_num == len(subfolders) + 1:
                print("Exiting...")
                break

            if choice_num < 1 or choice_num > len(subfolders):
                print("Invalid choice. Please try again.")
                continue

            selected_folder = subfolders[choice_num - 1]
            folder_path = os.path.join(script_dir, selected_folder)

            # Generate GIF
            output_gif = os.path.join(script_dir, f'{selected_folder}.gif')

            try:
                make_gif_from_sequence(folder_path, sequence, output_gif, fps)

                print("\n" + "="*60)
                print("✓ GIF SUCCESSFULLY CREATED!")
                print("="*60)
                print(f"Location: {output_gif}")
                print(f"File name: {selected_folder}.gif")
                print(f"FPS: {fps}")
                print("="*60)

            except FileNotFoundError as e:
                print(f"Error: {e}")

            input("\nPress Enter to continue...")

        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")

def group_gif_thumbnail_maker():
    """Create a combined GIF from multiple selected folders"""
    # Get the directory of the script
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(__file__) or os.getcwd()

    sequence = ['shime2', 'shime47', 'shime3', 'shime47']
    fps = 5

    print("\n" + "="*60)
    print("GROUP GIF THUMBNAIL MAKER")
    print("="*60)

    # Get subfolders
    subfolders = get_subfolders(script_dir)

    if not subfolders:
        print("No folders found in the script directory.")
        return

    # Display folders
    print("\nAvailable folders:")
    for i, folder in enumerate(subfolders, 1):
        print(f"{i}. {folder}")

    # Get user choices (multiple)
    try:
        choices = input("\nSelect folders (enter numbers separated by comma, e.g., 1,3,5): ").strip()
        choice_nums = [int(c.strip()) for c in choices.split(',') if c.strip()]

        selected_folders = []
        for num in choice_nums:
            if 1 <= num <= len(subfolders):
                selected_folders.append(subfolders[num - 1])
            else:
                print(f"Invalid choice: {num}")
                return

        if not selected_folders:
            print("No valid folders selected.")
            return

        print(f"Selected folders: {selected_folders}")

        # Collect all images from selected folders
        all_images = []
        for folder in selected_folders:
            folder_path = os.path.join(script_dir, folder)
            for name in sequence:
                img_path = os.path.join(folder_path, f'{name}.png')
                if os.path.exists(img_path):
                    img = Image.open(img_path).convert("RGBA")
                    all_images.append(img)
                else:
                    print(f"Warning: {img_path} not found, skipping.")

        if not all_images:
            print("No images found in selected folders.")
            return

        # Generate combined GIF
        output_gif = os.path.join(script_dir, 'group.gif')

        all_images[0].save(
            output_gif,
            save_all=True,
            append_images=all_images[1:],
            duration=int(1000/fps),
            loop=0,
            transparency=0,
            disposal=2
        )

        print("\n" + "="*60)
        print("✓ GROUP GIF SUCCESSFULLY CREATED!")
        print("="*60)
        print(f"Location: {output_gif}")
        print(f"File name: group.gif")
        print(f"FPS: {fps}")
        print(f"Combined from folders: {', '.join(selected_folders)}")
        print("="*60)

    except ValueError:
        print("Invalid input. Please enter numbers separated by comma.")

def main():
    while True:
        print("\n" + "="*60)
        print("SHIMEJI TOOLKIT")
        print("="*60)
        print("1. Image Sequence Renamer")
        print("2. GIF Thumbnail Maker")
        print("3. Group GIF Thumbnail Maker")
        print("4. Exit")

        choice = input("\nSelect an option (1-4): ").strip()

        if choice == '1':
            image_sequence_renamer()
        elif choice == '2':
            gif_thumbnail_maker()
        elif choice == '3':
            group_gif_thumbnail_maker()
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
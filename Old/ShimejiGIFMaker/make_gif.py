import os
import sys
from PIL import Image

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

def main():
    # Get the directory of the executable/script
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(__file__)
    
    sequence = ['shime2', 'shime47', 'shime3', 'shime47']
    fps = 5
    
    while True:
        print("\n" + "="*60)
        print("SHIMEJI GIF MAKER")
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

if __name__ == "__main__":
    main()

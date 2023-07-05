import os
import glob

# Path to the folder with the images

def change_all_labels_to_fish():

    labels = glob.glob("./*/labels/*.txt")
    for file in labels:
        with open(file, 'r') as f:
            lines = f.readlines()
            newlines = []
            for line in lines:
                class_id, rest = line.split(" ", 1)
                if class_id in ["1", "4"]:
                    newlines.append("0 " + rest)
            f.close()
        with open(file, 'w') as f:
            for line in newlines:
                f.write(line)
            f.close()

if __name__ == "__main__":
    change_all_labels_to_fish()
import os
import shutil

######################################################

# from CONSTANTS import
FRAMES_WITH_LABELS = os.path.join('.', 'frames')   # CHANGE ACCORDINGLY
TRAINING_DATA = os.path.join('.', 'training_data') # CHANGE ACCORDINGLY

######################################################
  

def main():
  # if './frames' does not exist, then exit (no data)
  if not os.path.isdir(FRAMES_WITH_LABELS):
    return

  # if './training_data' does not exist, make it
  # if it does, make sure it is empty
  os.makedirs(TRAINING_DATA, exist_ok = True)

  with os.scandir(TRAINING_DATA) as it:
    if not (next(it, None) is None):
      return

  os.makedirs(os.path.join(TRAINING_DATA, 'train'), exist_ok = True)
  os.makedirs(os.path.join(TRAINING_DATA, 'val'), exist_ok = True)

  directory = os.listdir(FRAMES_WITH_LABELS)
  filenames = [file[:-4] for file in directory if file.endswith(".jpg")]

  label_file = ""
  img_file = ""
  path_pref = ""
  copied_counter = 0

  for i in range(len(filenames)):
    item = filenames[i]
    img_file = item + ".jpg"
    label_file = item + ".txt"

    if i % 2 == 0:
      path_pref = os.path.join(TRAINING_DATA, 'train')
    else:
      path_pref = os.path.join(TRAINING_DATA, 'val')

    shutil.copy(os.path.join(FRAMES_WITH_LABELS, img_file), os.path.join(path_pref, img_file))

    if label_file in directory:
      shutil.copy(os.path.join(FRAMES_WITH_LABELS, label_file), os.path.join(path_pref, label_file))
      copied_counter += 1
    else:
      with open(os.path.join(path_pref, label_file), 'a'):
        pass

  print(f'There were {copied_counter} already existing label files, created {len(filenames) - copied_counter} empty ones')

if __name__ == '__main__':
  main()
from os import path

# path to dataset
BASE_PATH = path.sep.join(["dataset", "fer2013"])

# path to dataset csv
INPUT_PATH = path.sep.join([BASE_PATH, "fer2013/fer2013.csv"])

# define the number of classes (set to 6 if you are ignoring the
# "disgust" class)
# NUM_CLASSES = 7
NUM_CLASSES = 6

# define the path to the output HDF5 files
TRAIN_HDF5 = path.sep.join(["hdf5", "train.hdf5"])
VAL_HDF5 = path.sep.join(["hdf5", "val.hdf5"])
TEST_HDF5 = path.sep.join(["hdf5", "test.hdf5"])

# define the batch size
BATCH_SIZE = 128

# define the path to where output logs will be stored
OUTPUT_PATH = "outputs/"
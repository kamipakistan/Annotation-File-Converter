import os
import sys

# add the path to the COCO API to the system path
sys.path.append("coco/PythonAPI")
from pycocotools.coco import COCO


# define a function to convert COCO annotations to KITTI format
def coco2kitti(catNms, annFile, path):
    # initialize COCO api for instance annotations
    coco = COCO(annFile)

    # Create an index for the category names
    cats = coco.loadCats(coco.getCatIds())
    cat_idx = {}
    for c in cats:
        cat_idx[c['id']] = c['name']
    # print out the class names present in the dataset
    print(f'\nClass names present in the dataset:\n{cat_idx}')

    # iterate through each image in the dataset
    for img in coco.imgs:
        # Get all annotation IDs for the image
        catIds = coco.getCatIds(catNms=catNms)
        annIds = coco.getAnnIds(imgIds=[img], catIds=catIds)

        # If there are annotations, create a label file
        if len(annIds) > 0:
            # Get image filename
            img_fname = coco.imgs[img]['file_name']
            # Split the filename into its components and construct the label file name
            split = img_fname.split(".")
            filename = f"{split[0]}.{split[1]}.{split[2]}.txt"

            # Open the label file for writing
            with open(f"{path}/{filename}", 'w') as label_file:
                # load the annotations for the image
                anns = coco.loadAnns(annIds)
                # iterate through each annotation
                for a in anns:
                    bbox = a['bbox']
                    # Convert COCO bbox coords to Kitti ones
                    bbox = [bbox[0], bbox[1], bbox[2] + bbox[0], bbox[3] + bbox[1]]
                    bbox = [str(b) for b in bbox]
                    catname = cat_idx[a['category_id']]
                    # Format line in label file
                    # Note: all whitespace will be removed from class names
                    out_str = [catname.replace(" ", "")
                               + ' ' + ' '.join(['0'] * 3)
                               + ' ' + ' '.join([b for b in bbox])
                               + ' ' + ' '.join(['0'] * 7)
                               + '\n']
                    # write the label line to the label file
                    label_file.write(out_str[0])
    # print out the total number of files processed
    print(f'\n\nTotal files processed: {img}')


if __name__ == '__main__':
    """
    Note:
    If your are not converting roboflow annotations, change the code in line 33, 34
    """
    # json annotation file complete path
    annFile = r'datasets/Retail_Coolers/coco-annotation/_annotations.coco.json'

    # complete destination path, on which you want to place your annotations
    destPath = r"datasets/Retail_Coolers/kitti-annotations"

    # If this list is populated then label files will only be produced for images containing the listed classes
    # and only the listed classes will be in the label file
    # EXAMPLE:
    catNms = ['empty', 'product']

    # Check if a labels folder exists and, if not, make one
    # If it exists already, exit to avoid overwriting
    if os.path.isdir(destPath):
        print(f'\nWarning!. Labels folder already exists at path {destPath}\nHint: Delete it if you want to create new one')
    else:
        os.mkdir(destPath)
        # Call the function
        coco2kitti(catNms, annFile, destPath)

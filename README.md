# Annotation File Converter
Annotation File Converter is a GitHub repository that includes Python-based conversion scripts to convert annotations from one format to another. The repository provides conversion files for the following popular annotation formats:

> coco2kitti have been added to the repo, soon we will add the other files too.

* COCO 
* KITTI
* YOLO
* LISA
* VOC

Using the provided conversion scripts, you can quickly and easily convert your annotation files without any manual editing. 
The code is well-documented and easy to customize to suit your specific requirements.

To use Annotation File Converter, 
simply clone the repository, install the requirements and run the appropriate conversion script for your desired input and output formats.
For example, to convert a COCO annotation file to a KITTI annotation file, run the **coco2kitti.py** script.

This repository was built with the help of the [custom-object-detection-datasets](https://github.com/howl0893/custom-object-detection-datasets) and [cocoapi](https://github.com/cocodataset/cocoapi) repositories. 
We would like to express our gratitude to their creators for making these tools publicly available and for their contributions to the computer vision community.


>Note:
> 
> When you clone the main repository `Annotation-File-Converter`, you also need to clone the `coco` directory inside it.
> This directory is a submodule of `cocoapi`, which is a dependency required by the `Annotation-File-Converter` tool.
> So, make sure to clone both the main repository and its submodule to use the tool properly

To clone the submodule of coco api use the following command.
```commandline
git clone --recurse-submodules https://github.com/cocodataset/cocoapi.git coco
```

We believe that Annotation File Converter will be a valuable resource for anyone working with different annotation file formats and needing to convert them for various applications. Feel free to contribute to this repository by adding support for additional annotation file formats or improving the existing conversion scripts.

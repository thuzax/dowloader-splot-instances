# Download SPL instances
This objective of this project is to make the download of instances from SPLOT repository easier. The algorithm was implemented in Python3.

## Execution
To execute the program use the following command:

```
$ python3 downloader.py <keys-file> <destiny-folder>
```

**\<keys-file>** is a file containing the identifications of the files in SPLOT repository. The program will use each identification with the base link http://52.32.1.180:8080/SPLOT/models/ (for example: http://52.32.1.180:8080/SPLOT/models/model_01.xml).
**\<destiny-folder>** is the folder where all the downloaded models will be saved.

## Example

The file *xml-links* is an example of \<keys-file>. The identifications were collected on October 09 of 2019. 


## Authors

Arthur Henrique Sousa Cruz (github.com/thuzax)
Eduardo Fernando de Lima (github.com/limaeduardo)

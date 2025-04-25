Here is a space for donating data and data generation notebooks.

### Helper script: 

markdow_to_jsonl.py 

``` bash
python markdown_to_jsonl.py data/preview_pyconde_data_lanparty_1.md data/pyconde_data_lanparty_1.jsonl

```

In case you want to create a preview markdown file, to check your data for correctness..., you can then easily export it to a jsonl, the needed format.

The markdown should be a table. If you have an image column, name the column image, and the script will strip the image path of markdown syntax.



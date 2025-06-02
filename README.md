# Just Readme


**pip freeze without versions to import into .txt**

```
pip freeze | cut -d'=' -f1 > requirements.txt
```
# Generate Test MFT Files

This project is used to generate test files to simulate actual customer files in an MFT pipeline.

## Installing Dependencies

Make sure you have `python3` and `pip` installed, then run the following:

```
pip install -r requirements.txt
```

## Generating Files

Run the following command to generate 3 files of varying sizes for each available file type:

```
python main.py
```

The generated files will be in the `output` directory, and they will be of sizes 100MB, 3.7GB, and 5GB

## Supported File Types

As of now, the following file types can be generated:
   
- ASCII
- EBCDIC

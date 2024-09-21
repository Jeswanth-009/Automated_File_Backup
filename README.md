# Automated_File_Backup
Automated File Backup
# Automated File Backup Script

This Python script performs a one-time backup of a specified folder to a destination directory. It creates a new backup folder with the current date as its name, ensuring that you have a snapshot of your important files for the day it's run.

## Features

- Creates a date-stamped backup folder
- Copies entire directory structure and contents
- Simple configuration of source and destination directories
- Handles existing backup folders for the same date

## Requirements

To run this script, you need:
- Python 3.x
- No additional libraries required (all used libraries are part of Python's standard library)

## Configuration

Before running the script, set the source and destination directories:

```python
source_dir = "D:/New Back/Back from"
destination_dir = "D:/New Back/Back To"
```

Replace these paths with the appropriate directories on your system.

## Usage

To use the script:

1. Ensure you have set the correct `source_dir` and `destination_dir` in the script.
2. Run the script using Python:

   ```
   python Automated_File_Backup.py
   ```

The script will create a new folder in the destination directory with today's date as its name (format: YYYY-MM-DD), and copy all contents from the source directory into it.

## Current Limitations

- The script performs a one-time backup when executed. It does not continuously run or schedule backups.
- If a backup folder for the current date already exists, the script will print a message and not perform the backup.
- There's no progress indicator during the backup process.
- The script does not handle errors that might occur during the copy process (e.g., file permissions issues).

## Potential Future Improvements

- Implement scheduled backups using the `schedule` library
- Add error handling and logging
- Include options for incremental backups
- Add command-line arguments for easier configuration
- Implement a progress bar for large backups
- Add option to compress the backup folder

## License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

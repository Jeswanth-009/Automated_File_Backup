# Automated_File_Backup
Automated File Backup

# Automated Daily File Backup Script

This Python script performs automated daily backups of a specified folder to a destination directory. It creates a new backup folder with the current date as its name, ensuring that you have daily snapshots of your important files.

## Features

- Creates date-stamped backup folders
- Performs an initial backup upon script execution
- Schedules daily backups at a specified time
- Copies entire directory structure and contents
- Simple configuration of source and destination directories
- Handles existing backup folders for the same date

## Requirements

To run this script, you need:
- Python 3.x
- `schedule` library

You can install the required library using pip:

```
pip install schedule
```

## Configuration

Before running the script, set the source and destination directories:

```python
source_dir = "D:/New Back/Back from"
destination_dir = "D:/New Back/Back To"
```

Replace these paths with the appropriate directories on your system.

You can also adjust the scheduled backup time by modifying this line:

```python
schedule.every().day.at("18:40:00").do(l)
```

Change "18:40:00" to your desired backup time in 24-hour format.

## Usage

To use the script:

1. Ensure you have set the correct `source_dir` and `destination_dir` in the script.
2. Run the script using Python:

   ```
   python Automated_File_Backup.py
   ```

The script will:
1. Perform an initial backup immediately upon execution.
2. Schedule daily backups at the specified time (default is 18:40:00 or 6:40 PM).
3. Continue running in the background, performing backups at the scheduled time each day.

For each backup, the script creates a new folder in the destination directory with that day's date as its name (format: YYYY-MM-DD), and copies all contents from the source directory into it.

## Current Functionality

- Performs an immediate backup when the script is first run.
- Schedules and performs daily backups at a specified time.
- Creates a new dated folder for each day's backup.
- Prints a message if a backup folder for the current date already exists.
- Runs continuously to ensure scheduled backups occur.

## Limitations

- The script must be kept running continuously for scheduled backups to occur.
- If a backup folder for the current date already exists, the script will print a message and not perform another backup that day.
- There's no progress indicator during the backup process.
- The script does not handle errors that might occur during the copy process (e.g., file permissions issues).

## Potential Future Improvements

- Add error handling and logging
- Include options for incremental backups
- Add command-line arguments for easier configuration
- Implement a progress bar for large backups
- Add option to compress the backup folder
- Implement a more robust scheduling system that doesn't require the script to run continuously

## License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

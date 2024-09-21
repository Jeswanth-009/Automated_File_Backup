# Automated_File_Backup
Automated File Backup
# Automated File Backup Script

This Python script automates the process of backing up a specified folder to a destination directory. It creates a new backup folder with the current date as its name, ensuring that you have daily backups of your important files.

## Features

- Automatic daily backups
- Date-stamped backup folders
- Simple configuration of source and destination directories

## Requirements

To run this script, you need to have Python installed on your system along with the following libraries:
- `os` (built-in)
- `shutil` (built-in)
- `datetime` (built-in)
- `schedule` (needs to be installed)

You can install the `schedule` library using pip:

```
pip install schedule
```

## Configuration

Before running the script, you need to set the source and destination directories:

```python
source_dir = "D:/New Back/Back from"
destination_dir = "D:/New Back/Back To"
```

Replace these paths with the appropriate directories on your system.

## Usage

To use the script:

1. Ensure you have set the correct `source_dir` and `destination_dir`.
2. Run the script using Python:

   ```
   python Automated_File_Backup.py
   ```

The script will create a new folder in the destination directory with today's date as its name, and copy all contents from the source directory into it.

## Note

Currently, the script is set up to run the backup once when executed. To schedule regular backups, you would need to implement a scheduling mechanism using the `schedule` library or a system task scheduler.

## Future Improvements

- Implement scheduled backups using the `schedule` library
- Add error handling and logging
- Include options for incremental backups
- Add command-line arguments for easier configuration

## License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

import os
import pathlib
import datetime
import platform


def get_creation_date(path_to_file):
    """Get creation date for file

    Args:
        path_to_file (pathlib.Path): Path to file

    Returns:
        datetime.datetime: Creation date of file
    """
    if platform.system() == 'Windows':
        # Windows
        return datetime.datetime.fromtimestamp(os.path.getctime(path_to_file))
    else:
        # Unix-based systems (Linux, macOS)
        stat = os.stat(path_to_file)
        try:
            # macOS
            return datetime.datetime.fromtimestamp(stat.st_birthtime)
        except AttributeError:
            # Linux: fallback to last modification time
            return datetime.datetime.fromtimestamp(stat.st_mtime)


def sort_files_by_year(work_dir):
    """Sort files in a directory into subdirectories by year

    Args:
        work_dir (pathlib.Path): Path to directory to sort
    """
    for file in work_dir.iterdir():
        if file.is_file():
            creation_date = get_creation_date(file)
            year = creation_date.year

            if year in range(2000, 2100):
                folder = work_dir / str(year)
            else:
                folder = work_dir / "Autres"

            folder.mkdir(exist_ok=True)
            file.rename(folder / file.name)


if __name__ == "__main__":
    work_dir = pathlib.Path(input("Insert the path to the folder: "))
    sort_files_by_year(work_dir)

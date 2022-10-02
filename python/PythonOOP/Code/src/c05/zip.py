from __future__ import annotations
import fnmatch
from pathlib import Path
import re
import zipfile


class ZipReplace:
    def __init__(
        self,
        archive: Path,
        pattern: str,
        find: str,
        replace: str
    ) -> None:
        self.archive_path = archive
        self.pattern = pattern
        self.find = find
        self.replace = replace
    

    def find_and_replace(self) -> None:
        input_path, output_path = self.make_backup()

        with zipfile.ZipFile(output_path, "w") as output:
            with zipfile.ZipFile(input_path) as input:
                self.copy_and_transform(input, output)

    def make_backup(self) -> tuple[Path, Path]:
        input_path = self.archive_path.with_suffix(
            f"{self.archive_path.suffix}_old"
        )
        output_path = self.archive_path
        self.archive_path.rename(input_path)
        return input_path, output_path
    
    def copy_and_transform(
        self,
        input: zipfile.ZipFile,
        output: zipfile.ZipFile
    ) -> None:
        for item in input.infolist():
            extracted = Path(input.extract(item))
            if (not item.is_dir() and fnmatch.fnmatch(item.filename, self.pattern)):
                print(f"Transform {item}")
                input_text = extracted.read_text()
                output_text = re.sub(self.find, self.replace, input_text)
                extracted.write_text(output_text)
            else:
                print(f"Ignored {item}")
            output.write(extracted, item.filename)
            extracted.unlink()
            for parent in extracted.parents:
                if parent == Path.cwd():
                    break
                parent.rmdir()

if __name__ == "__main__":
    sample_size = Path("sample-zip-file.zip")
    print("running script")
    zr = ZipReplace(sample_size, "add", "REPLACED_0", "REPLACED")


from abc import ABC, abstractmethod

class ZipProcessor(ABC):
    def __init__(self, archive: Path) -> None:
        self.archive_path = archive
        self._pattern: str
    
    def process_files(self, pattern: str) -> None:
# Keep Note to Joplin
 Transfer data from Google KeepNote(html) to Joplin(md)

## Usage

1. Input your file path(where you put html files exported from google) to 'filePath' in Transform.py
2. Create a new folder called "md" in the same folder 
3. Run Transform.py

## Effect

Transform.py will transform the html files in the path to md files in "/md".

It can deal with the title, content and tags.

 If there's not title for your notes, the filename will be last edited time.

## Defect

It could not help with the pictures in Keep Note.

Though I've considered some special characters, there may be other special characters in your filename which will cause a fatal error.

